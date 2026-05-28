"""Create CNAME records and bind custom domains for all 13 Pages sites."""
import urllib.request, json, sys

# Read token from wrangler config
with open(r"C:\Users\LENOVO\AppData\Roaming\xdg.config\.wrangler\config\default.toml") as f:
    for line in f:
        if line.startswith("oauth_token"):
            TOKEN = line.split('"')[1]
            break

ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"
ZONE_ID = "84e9dc1d7fb72629ccdbe3174ed24420"

def api(method, path, body=None):
    url = f"https://api.cloudflare.com/client/v4{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {TOKEN}")
    req.add_header("Content-Type", "application/json")
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())

# Step 1: List existing CNAME records
print("=== EXISTING CNAME RECORDS ===")
result = api("GET", f"/zones/{ZONE_ID}/dns_records?type=CNAME&per_page=100")
existing_names = set()
for r in result["result"]:
    print(f"  {r['name']} -> {r['content']} (proxied={r.get('proxied', False)})")
    existing_names.add(r["name"])
print(f"  Total: {len(result['result'])} CNAME records")

# Step 2: CNAME records to create
SITES = [
    ("laws.qnfo.org", "quantum-laws-of-form.pages.dev"),
    ("paradigm.qnfo.org", "ultrametric-paradigm.pages.dev"),
    ("hierarchy.qnfo.org", "hierarchical-universe.pages.dev"),
    ("different.qnfo.org", "different-physics.pages.dev"),
    ("measure.qnfo.org", "two-ways-of-measuring.pages.dev"),
    ("unity.qnfo.org", "unity-of-ultrametric-physics.pages.dev"),
    ("quantum.qnfo.org", "ultrametric-quantum.pages.dev"),
    ("ai-poc.qnfo.org", "ultrametric-ai-poc.pages.dev"),
    ("adelic.qnfo.org", "adelic-qft.pages.dev"),
    ("cocyle.qnfo.org", "cocyle.pages.dev"),
    ("knowing.qnfo.org", "knowing-patterns.pages.dev"),
    ("solo.qnfo.org", "solo-scientist.pages.dev"),
    ("lexicon.qnfo.org", "verb-lexicon.pages.dev"),
]

print("\n=== CREATING CNAME RECORDS ===")
created = []
for name, target in SITES:
    if name in existing_names:
        print(f"  SKIP {name} (already exists)")
        continue
    
    body = {
        "type": "CNAME",
        "name": name,
        "content": target,
        "proxied": True,
        "ttl": 1  # Auto
    }
    result = api("POST", f"/zones/{ZONE_ID}/dns_records", body)
    if result["success"]:
        print(f"  OK   {name} -> {target} [{result['result']['id']}]")
        created.append((name, target))
    else:
        print(f"  FAIL {name}: {result['errors']}")

# Step 3: Add custom domains to Pages projects
print(f"\n=== ADDING CUSTOM DOMAINS TO PAGES ({len(created)} domains) ===")
PROJECT_MAP = {
    "laws.qnfo.org": "quantum-laws-of-form",
    "paradigm.qnfo.org": "ultrametric-paradigm",
    "hierarchy.qnfo.org": "hierarchical-universe",
    "different.qnfo.org": "different-physics",
    "measure.qnfo.org": "two-ways-of-measuring",
    "unity.qnfo.org": "unity-of-ultrametric-physics",
    "quantum.qnfo.org": "ultrametric-quantum",
    "ai-poc.qnfo.org": "ultrametric-ai-poc",
    "adelic.qnfo.org": "adelic-qft",
    "cocyle.qnfo.org": "cocyle",
    "knowing.qnfo.org": "knowing-patterns",
    "solo.qnfo.org": "solo-scientist",
    "lexicon.qnfo.org": "verb-lexicon",
}

for name, target in created:
    project = PROJECT_MAP.get(name)
    if not project:
        print(f"  SKIP {name} (no project mapping)")
        continue
    
    body = {"name": name}
    try:
        result = api("POST", f"/accounts/{ACCOUNT_ID}/pages/projects/{project}/domains", body)
        if result["success"]:
            status = result["result"].get("status", "?")
            print(f"  OK   {name} -> {project} [{status}]")
        else:
            print(f"  FAIL {name}: {result['errors']}")
    except Exception as e:
        print(f"  ERR  {name}: {e}")

# Step 4: Also fix www.qwav.tech
print("\n=== FIX: www.qwav.tech ===")
body = {
    "type": "CNAME",
    "name": "www.qwav.tech",
    "content": "qwav.tech",
    "proxied": True,
    "ttl": 1
}
# Need qwav.tech zone ID
qwav_zones = api("GET", "/zones?name=qwav.tech")
if qwav_zones["success"] and qwav_zones["result"]:
    qwav_zone = qwav_zones["result"][0]["id"]
    result = api("POST", f"/zones/{qwav_zone}/dns_records", body)
    if result["success"]:
        print(f"  OK   www.qwav.tech -> qwav.tech [{result['result']['id']}]")
    else:
        print(f"  FAIL: {result['errors']}")

print("\n=== DONE ===")
