"""Generate embedding and insert into Vectorize for pipeline validation."""
import json, os, subprocess, urllib.request

with open(r'C:\Users\LENOVO\AppData\Roaming\xdg.config\.wrangler\config\default.toml') as f:
    for line in f:
        if line.startswith('oauth_token'):
            TOKEN = line.split('"')[1]
            break

# 1. Generate embedding via Workers AI
req = urllib.request.Request(
    'https://api.cloudflare.com/client/v4/accounts/edb167b78c9fb901ea5bca3ce58ccc4b/ai/run/@cf/baai/bge-base-en-v1.5',
    data=json.dumps({'text': ['Ultrametric geometry is a non-Archimedean geometry where the strong triangle inequality holds for all points.']}).encode(),
    method='POST',
    headers={'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'}
)
resp = urllib.request.urlopen(req)
d = json.loads(resp.read())
vector = d['result']['data'][0]
print(f'[OK] Embedding generated: {len(vector)} dimensions')

# 2. Write NDJSON for Vectorize
ndjson = json.dumps({
    'id': 'test-1',
    'values': vector,
    'metadata': {'text': 'Ultrametric geometry definition', 'source': 'test'}
})
path = os.environ['TEMP'] + r'\test-vector.ndjson'
with open(path, 'w') as f:
    f.write(ndjson)
print(f'[OK] NDJSON written: {path}')

# 3. Insert via wrangler
print('[..] Inserting into qwav-research...')
result = subprocess.run(
    ['wrangler', 'vectorize', 'insert', 'qwav-research', '--file', path],
    capture_output=True, text=True
)
print(result.stdout)
if result.returncode != 0:
    print(f'STDERR: {result.stderr}')

# 4. Verify
print('[..] Verifying...')
result2 = subprocess.run(
    ['wrangler', 'vectorize', 'get', 'qwav-research', 'test-1'],
    capture_output=True, text=True
)
print(result2.stdout)
