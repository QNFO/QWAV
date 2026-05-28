"""QVAV Ask QWAV — Ingestion Pipeline: R2 papers → Vectorize embeddings.

Downloads markdown papers from R2, chunks them, generates 768-dim embeddings
via Workers AI (bge-base-en-v1.5), and inserts into Vectorize index qwav-research.
"""
import json, os, re, time, urllib.request

# ===================== CONFIG =====================
with open(r"C:\Users\LENOVO\AppData\Roaming\xdg.config\.wrangler\config\default.toml") as f:
    for line in f:
        if line.startswith("oauth_token"):
            TOKEN = line.split('"')[1]
            break

ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"
R2_BUCKET = "qnfo"
VECTORIZE_INDEX = "qwav-research"
EMBED_MODEL = "@cf/baai/bge-base-en-v1.5"
CHUNK_SIZE = 500   # tokens (approximate: ~4 chars per token)
CHUNK_OVERLAP = 50
EMBED_BATCH = 20   # texts per API call (max 100 for bge)
INSERT_BATCH = 50  # vectors per NDJSON file

HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

# ===================== STEP 1: LIST R2 PAPERS =====================
print("=== STEP 1: Listing R2 papers ===")
cursor = None
all_keys = []
while True:
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/r2/buckets/{R2_BUCKET}/objects?per_page=100"
    if cursor:
        url += f"&cursor={cursor}"
    resp = urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS))
    data = json.loads(resp.read())
    if not data.get("success"):
        print(f"FAIL: {data.get('errors')}")
        break
    all_keys.extend(data["result"])
    if data.get("result_info", {}).get("is_truncated"):
        cursor = data["result_info"]["cursor"]
    else:
        break

PAPERS = [obj for obj in all_keys if obj["key"].endswith(".md") and not obj["key"].startswith("audit/")]
print(f"Found {len(PAPERS)} papers in R2 (total {len(all_keys)} objects)")
for p in PAPERS:
    print(f"  {p['key']} ({p['size']:,} bytes)")

# ===================== STEP 2: DOWNLOAD + CHUNK =====================
print(f"\n=== STEP 2: Downloading and chunking {len(PAPERS)} papers ===")

def download_r2(key):
    """Download a file from R2 and return text content."""
    url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/r2/buckets/{R2_BUCKET}/objects/{urllib.request.quote(key, safe='')}"
    resp = urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS))
    data = json.loads(resp.read())
    if not data.get("success"):
        return None
    return data["result"]["value"]  # base64-encoded? Let's check

# Actually, R2 objects need a different approach. Let's use the direct download URL.
def download_r2_direct(key):
    """Download via R2 direct access URL."""
    url = f"https://pub-edb167b78c9fb901ea5bca3ce58ccc4b.r2.dev/{urllib.request.quote(key, safe='')}"
    resp = urllib.request.urlopen(urllib.request.Request(url))
    return resp.read().decode("utf-8", errors="replace")

def chunk_text(text, source, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks of ~chunk_size words."""
    # Use word-based chunking for simplicity (~4 chars = 1 token)
    words = text.split()
    chunks = []
    step = max(chunk_size - overlap, 1)
    for i in range(0, len(words), step):
        chunk_words = words[i:i + chunk_size]
        if len(chunk_words) < 20:  # Skip tiny chunks
            continue
        chunk_text = " ".join(chunk_words)
        chunks.append({
            "id": f"{source}::{i // step:04d}",
            "text": chunk_text,
            "source": source,
            "chunk_index": i // step
        })
    return chunks

all_chunks = []
for paper in PAPERS:
    key = paper["key"]
    print(f"  Downloading: {key}...")
    try:
        text = download_r2_direct(key)
        chunks = chunk_text(text, source=key.replace(".md", ""))
        all_chunks.extend(chunks)
        print(f"    → {len(chunks)} chunks")
    except Exception as e:
        print(f"    → FAILED: {e}")

print(f"\nTotal chunks: {len(all_chunks)}")

# ===================== STEP 3: GENERATE EMBEDDINGS =====================
print(f"\n=== STEP 3: Generating embeddings (batch size {EMBED_BATCH}) ===")

def embed_batch(texts):
    """Generate embeddings for a batch of texts."""
    body = json.dumps({"text": texts}).encode()
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/ai/run/{EMBED_MODEL}",
        data=body, method="POST", headers=HEADERS
    )
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    if data.get("success"):
        return data["result"]["data"]
    else:
        raise Exception(f"Embed failed: {data.get('errors')}")

embedded = 0
for i in range(0, len(all_chunks), EMBED_BATCH):
    batch = all_chunks[i:i + EMBED_BATCH]
    texts = [c["text"] for c in batch]
    try:
        vectors = embed_batch(texts)
        for j, vec in enumerate(vectors):
            batch[j]["values"] = vec
        embedded += len(batch)
        print(f"  Embedded {embedded}/{len(all_chunks)} chunks...")
        time.sleep(0.1)  # Rate limit courtesy
    except Exception as e:
        print(f"  Batch {i}-{i+EMBED_BATCH} FAILED: {e}")

# ===================== STEP 4: INSERT INTO VECTORIZE =====================
print(f"\n=== STEP 4: Inserting into Vectorize ===")

INSERT_DIR = os.environ["TEMP"] + r"\qwav-ingest"
os.makedirs(INSERT_DIR, exist_ok=True)

inserted = 0
files_created = 0
for i in range(0, len(all_chunks), INSERT_BATCH):
    batch = all_chunks[i:i + INSERT_BATCH]
    ndjson_lines = []
    for c in batch:
        if "values" not in c:
            continue
        ndjson_lines.append(json.dumps({
            "id": c["id"],
            "values": c["values"],
            "metadata": {
                "text": c["text"][:200],  # Truncate in metadata
                "source": c["source"],
                "chunk_index": c["chunk_index"]
            }
        }))
    
    if not ndjson_lines:
        continue
    
    ndjson = "\n".join(ndjson_lines)
    filepath = os.path.join(INSERT_DIR, f"batch-{files_created:04d}.ndjson")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(ndjson)
    
    files_created += 1
    inserted += len(ndjson_lines)
    print(f"  Wrote batch {files_created}: {len(ndjson_lines)} vectors → {filepath}")

print(f"\n=== INGESTION COMPLETE ===")
print(f"Papers: {len(PAPERS)}")
print(f"Chunks: {len(all_chunks)}")
print(f"Embedded: {embedded}")
print(f"Insert files: {files_created} ({inserted} vectors total)")
print(f"Insert directory: {INSERT_DIR}")
print(f"\nRun these commands to insert into Vectorize:")
for j in range(files_created):
    filepath = os.path.join(INSERT_DIR, f"batch-{j:04d}.ndjson")
    print(f'wrangler vectorize insert qwav-research --file "{filepath}"')
