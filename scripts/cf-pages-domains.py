"""Add custom domains to Cloudflare Pages projects (no DNS changes)."""
import urllib.request, json

with open(r"C:\Users\LENOVO\AppData\Roaming\xdg.config\.wrangler\config\default.toml") as f:
    for line in f:
        if line.startswith("oauth_token"):
            TOKEN = line.split('"')[1]
            break

ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"

DOMAIN_MAP = [
    ("quantum-laws-of-form", "laws.qnfo.org"),
    ("ultrametric-paradigm", "paradigm.qnfo.org"),
    ("hierarchical-universe", "hierarchy.qnfo.org"),
    ("different-physics", "different.qnfo.org"),
    ("two-ways-of-measuring", "measure.qnfo.org"),
    ("unity-of-ultrametric-physics", "unity.qnfo.org"),
    ("ultrametric-quantum", "quantum.qnfo.org"),
    ("ultrametric-ai-poc", "ai-poc.qnfo.org"),
    ("adelic-qft", "adelic.qnfo.org"),
    ("cocyle", "cocyle.qnfo.org"),
    ("knowing-patterns", "knowing.qnfo.org"),
    ("solo-scientist", "solo.qnfo.org"),
    ("verb-lexicon", "lexicon.qnfo.org"),
]

ok = 0
fail = 0
for project, domain in DOMAIN_MAP:
    body = {"name": domain}
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/pages/projects/{project}/domains",
        data=json.dumps(body).encode(),
        method="POST",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    )
    try:
        resp = urllib.request.urlopen(req)
        result = json.loads(resp.read())
        if result["success"]:
            status = result["result"].get("status", "?")
            print(f"  OK   {project} <- {domain}  [{status}]")
            ok += 1
        else:
            print(f"  FAIL {project} <- {domain}: {result['errors']}")
            fail += 1
    except Exception as e:
        print(f"  ERR  {project} <- {domain}: {e}")
        fail += 1

print(f"\n=== {ok} OK / {fail} FAIL / {len(DOMAIN_MAP)} TOTAL ===")
