"""Ingest QWAV papers: chunk + embed + prepare NDJSON for Vectorize insert."""
import json, os, re, time, urllib.request, glob

# ===================== CONFIG =====================
with open(r"C:\Users\LENOVO\AppData\Roaming\xdg.config\.wrangler\config\default.toml") as f:
    for line in f:
        if line.startswith("oauth_token"):
            TOKEN = line.split('"')[1]
            break

ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"
EMBED_MODEL = "@cf/baai/bge-base-en-v1.5"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
EMBED_BATCH = 20
INSERT_BATCH = 50
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
PAPERS_DIR = os.environ["TEMP"] + r"\qwav-papers"
OUT_DIR = os.environ["TEMP"] + r"\qwav-ingest"
os.makedirs(OUT_DIR, exist_ok=True)

# ===================== STEP 1: READ + CHUNK PAPERS =====================
print("=== STEP 1: Reading and chunking papers ===")
all_chunks = []

for fpath in sorted(glob.glob(PAPERS_DIR + r"\*-*.md")):
    fname = os.path.basename(fpath)
    source = fname.replace(".md", "").replace("-", " ")
    with open(fpath, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    
    words = text.split()
    step = max(CHUNK_SIZE - CHUNK_OVERLAP, 1)
    nchunks = 0
    for i in range(0, len(words), step):
        chunk_words = words[i:i + CHUNK_SIZE]
        if len(chunk_words) < 20:
            continue
        chunk_text = " ".join(chunk_words)
        all_chunks.append({
            "id": f"{source}::{nchunks:04d}",
            "text": chunk_text,
            "source": source,
            "chunk_index": nchunks
        })
        nchunks += 1
    print(f"  {fname}: {nchunks} chunks ({len(words)} words)")

print(f"\nTotal: {len(all_chunks)} chunks from {len(glob.glob(PAPERS_DIR + '/*-*.md'))} papers")

# ===================== STEP 2: GENERATE EMBEDDINGS =====================
print(f"\n=== STEP 2: Generating embeddings (Workers AI, batch={EMBED_BATCH}) ===")

def embed_batch(texts):
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
        print(f"  [{embedded}/{len(all_chunks)}] embedded")
        time.sleep(0.15)
    except Exception as e:
        print(f"  BATCH {i}-{i+EMBED_BATCH} FAILED: {e}")

# ===================== STEP 3: WRITE NDJSON FILES =====================
print(f"\n=== STEP 3: Writing NDJSON insert files ===")
files_written = 0
total_vectors = 0

for i in range(0, len(all_chunks), INSERT_BATCH):
    batch = all_chunks[i:i + INSERT_BATCH]
    lines = []
    for c in batch:
        if "values" not in c:
            continue
        lines.append(json.dumps({
            "id": c["id"],
            "values": c["values"],
            "metadata": {
                "text": c["text"][:300],
                "source": c["source"],
                "chunk": c["chunk_index"]
            }
        }))
    
    if lines:
        filepath = os.path.join(OUT_DIR, f"batch-{files_written:04d}.ndjson")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        files_written += 1
        total_vectors += len(lines)
        print(f"  {filepath}: {len(lines)} vectors")

print(f"\n=== INGESTION READY ===")
print(f"Papers: 6")
print(f"Chunks: {len(all_chunks)}")
print(f"Embedded: {embedded}")
print(f"NDJSON files: {files_written} ({total_vectors} vectors)")
print(f"Directory: {OUT_DIR}")
print(f"\nInsert command:")
for j in range(files_written):
    print(f'  wrangler vectorize insert qwav-research --file "{os.path.join(OUT_DIR, f"batch-{j:04d}.ndjson")}"')
