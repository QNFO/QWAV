"""Fix long Vectorize IDs in NDJSON batches by truncating to 64 chars."""
import json, hashlib, os

d = os.environ["TEMP"] + r"\qwav-ingest"
for b in range(15, 19):
    fpath = os.path.join(d, f"batch-{b:04d}.ndjson")
    if not os.path.exists(fpath):
        print(f"batch-{b:04d}: MISSING")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]
    
    out = []
    fixed = 0
    for line in lines:
        obj = json.loads(line)
        oid = obj.get("id", "")
        if len(oid) > 64:
            src = obj.get("metadata", {}).get("source", "unknown")
            chk = obj.get("metadata", {}).get("chunk", 0)
            h = hashlib.md5(oid.encode()).hexdigest()[:12]
            new_id = f"{src}::{h}::{chk}"
            if len(new_id) > 64:
                new_id = new_id[:64]
            obj["id"] = new_id
            fixed += 1
        out.append(json.dumps(obj))
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    
    print(f"batch-{b:04d}: {len(out)} lines, {fixed} fixed")

print("DONE - re-insert batches 15-18 now")
