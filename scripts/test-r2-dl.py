"""Test R2 object download API."""
import json, urllib.request

with open(r"C:\Users\LENOVO\AppData\Roaming\xdg.config\.wrangler\config\default.toml") as f:
    for line in f:
        if line.startswith("oauth_token"):
            TOKEN = line.split('"')[1]
            break

ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"
KEY = "Bridging the Gap.md"

# Try the R2 download API
req = urllib.request.Request(
    f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/r2/buckets/qnfo/objects/{urllib.request.quote(KEY)}",
    headers={"Authorization": f"Bearer {TOKEN}"}
)
resp = urllib.request.urlopen(req)
data = json.loads(resp.read())

if data.get("success"):
    result = data["result"]
    print(f"Keys: {list(result.keys())}")
    if "value" in result:
        import base64
        text = base64.b64decode(result["value"]).decode("utf-8")
        print(f"Text: {text[:200]}...")
    else:
        print(f"No value field")
        print(str(result)[:500])
else:
    print(f"FAIL: {data['errors']}")
