import urllib.request, json, os

oauth_token = "65agVR_zNs2NIvxLFchCWomDahbVANGGC93Zh8iuEEs.zF74zQnKHBAF4TUbqfjVFWmI6dWhvmeTC-TS_oUxpMU"
ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"

def api(method, path, body=None):
    url = f"https://api.cloudflare.com/client/v4{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {oauth_token}")
    req.add_header("Content-Type", "application/json")
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())

# Step 1: Get all permission groups
print("=== Permission Groups ===")
groups = api("GET", "/user/tokens/permission_groups")["result"]
for g in groups:
    name = g["name"]
    if any(k in name.lower() for k in ["pages", "workers", "dns", "zone", "r2", "d1", "ssl", "account", "ai", "email", "browser", "containers", "workers kv", "workers routes"]):
        print(f"  {g['id']} | {name} | scopes: {g.get('scopes', '')}")

# Step 2: Create token with ALL read+write permissions we need
all_group_ids = [g["id"] for g in groups if any(
    k in g["name"].lower() for k in [
        "pages", "workers scripts", "workers kv", "workers routes",
        "workers r2", "dns", "zone", "ssl", "account",
        "d1", "ai", "email", "browser", "containers", "workers tail"
    ]
)]

token_body = {
    "name": "qwav-program-manager-persistent",
    "policies": [
        {
            "effect": "allow",
            "resources": {
                f"com.cloudflare.api.account.{ACCOUNT_ID}": ["*"],
                f"com.cloudflare.api.account.zone.*": ["*"]
            },
            "permission_groups": [
                {"id": gid} for gid in all_group_ids
            ]
        }
    ]
}

print(f"\n=== Creating token with {len(all_group_ids)} permissions ===")
result = api("POST", "/user/tokens", token_body)
if result["success"]:
    token_value = result["result"]["value"]
    token_id = result["result"]["id"]
    print(f"SUCCESS! Token ID: {token_id}")
    print(f"Token value: {token_value}")
    
    # Save to file
    with open(r"G:\My Drive\QWAV\cf-token-value.txt", "w") as f:
        f.write(token_value)
    print("Token saved to G:\\My Drive\\QWAV\\cf-token-value.txt")
else:
    print(f"FAILED: {json.dumps(result['errors'], indent=2)}")
