"""Full QWAV corpus ingestion: 13 repos / 163+ markdown files -> Vectorize.

Scans all paper repos in temp, extracts text from markdown files,
chunks them, generates 768-dim embeddings via Workers AI (bge-base-en-v1.5),
and writes NDJSON files ready for Vectorize insert.
"""
import json, os, re, time, urllib.request, glob, sys

# Force UTF-8 output
# Output will use default encoding

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
TEMP = os.environ["TEMP"]
OUT_DIR = os.path.join(TEMP, "qwav-ingest")
os.makedirs(OUT_DIR, exist_ok=True)

# ===================== STEP 1: SCAN + CHUNK =====================
print("=== STEP 1: Scanning paper repos ===")
all_chunks = []
repos_found = 0

for dname in sorted(os.listdir(TEMP)):
    dpath = os.path.join(TEMP, dname)
    if not os.path.isdir(dpath) or not dname.endswith("-deploy"):
        continue
    
    repo_name = dname.replace("-deploy", "")
    md_files = glob.glob(dpath + "/**/*.md", recursive=True)
    
    if not md_files:
        continue
    
    repos_found += 1
    repo_chunks = 0
    for md_path in sorted(md_files):
        rel = os.path.relpath(md_path, dpath)
        try:
            with open(md_path, "r", encoding="utf-8", errors="replace") as f:
                text = f.read()
        except:
            continue
        
        if len(text) < 100:
            continue
        
        words = text.split()
        step = max(CHUNK_SIZE - CHUNK_OVERLAP, 1)
        for i in range(0, len(words), step):
            chunk_words = words[i:i + CHUNK_SIZE]
            if len(chunk_words) < 20:
                continue
            chunk_text = " ".join(chunk_words)
            fid = f"{repo_name}/{rel}".replace("\\", "/").replace(".md", "")
            all_chunks.append({
                "id": f"{fid}::{repo_chunks:04d}",
                "text": chunk_text,
                "source": repo_name,
                "file": rel,
                "chunk_index": repo_chunks
            })
            repo_chunks += 1
    print(f"  [{repos_found}] {repo_name}: {len(md_files)} md -> {repo_chunks} chunks")

print(f"\nTotal: {len(all_chunks)} chunks from {repos_found} repos")

# ===================== STEP 2: EMBED =====================
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
failed_batches = 0
for i in range(0, len(all_chunks), EMBED_BATCH):
    batch = all_chunks[i:i + EMBED_BATCH]
    texts = [c["text"] for c in batch]
    try:
        vectors = embed_batch(texts)
        for j, vec in enumerate(vectors):
            batch[j]["values"] = vec
        embedded += len(batch)
        if embedded % 100 == 0 or embedded == len(all_chunks):
            print(f"  [{embedded}/{len(all_chunks)}]")
        time.sleep(0.1)
    except Exception as e:
        failed_batches += 1
        # Skip failed batch
        continue

print(f"  Embedded: {embedded}/{len(all_chunks)} (failed batches: {failed_batches})")

# ===================== STEP 3: WRITE NDJSON =====================
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
                "file": c["file"],
                "chunk": c["chunk_index"]
            }
        }))
    
    if lines:
        filepath = os.path.join(OUT_DIR, f"batch-{files_written:04d}.ndjson")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        files_written += 1
        total_vectors += len(lines)

print(f"  Files: {files_written}")
print(f"  Vectors: {total_vectors}")
print(f"  Directory: {OUT_DIR}")

# ===================== SUMMARY =====================
print(f"\n{'='*50}")
print(f"INGESTION COMPLETE")
print(f"Repos: {repos_found}")
print(f"Chunks: {len(all_chunks)}")
print(f"Embedded: {embedded}")
print(f"NDJSON files: {files_written} ({total_vectors} vectors)")
print(f"\nInsert commands (run sequentially):")
for j in range(files_written):
    print(f'wrangler vectorize insert qwav-research --file "{os.path.join(OUT_DIR, f"batch-{j:04d}.ndjson")}"')
