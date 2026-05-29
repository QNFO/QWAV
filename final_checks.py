import requests

token = 'sJYUcifLTwaukCJEDAyTXRPnfNjWjE11XGLBelQAUNQ.P4u1eO-gMGG3IZiFv92fvfzKHdZ8M1H_lb_hyDxXeGo'
account_id = 'edb167b78c9fb901ea5bca3ce58ccc4b'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# 1. Check qnfo-hub domain verification status
print('=== qnfo-hub domains ===')
url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/qnfo-hub/domains'
r = requests.get(url, headers=headers, timeout=10)
for d in r.json().get('result', []):
    name = d['name']
    status = d['status']
    verify = d.get('verification_data', {}).get('status', '?')
    print(f'  {name}: status={status} verify={verify}')

# 2. Try Pages-specific cache purge for qwav
print('\n=== Pages cache purge (qwav) ===')
url2 = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/qwav/purge_cache'
try:
    r2 = requests.post(url2, headers=headers, json={'purge_everything': True}, timeout=10)
    print(f'Status: {r2.status_code} Response: {r2.text[:300]}')
except Exception as e:
    print(f'Error: {e}')

# 3. Try deleting project cache  
print('\n=== Project cache delete ===')
url3 = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/qwav/cache'
try:
    r3 = requests.delete(url3, headers=headers, timeout=10)
    print(f'Status: {r3.status_code} Response: {r3.text[:200]}')
except Exception as e:
    print(f'Error: {e}')

# 4. Force a new deployment to invalidate CDN (trivial change)
print('\n=== Force redeploy qwav (just _headers) ===')
# Check latest deployment
url4 = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/qwav/deployments'
r4 = requests.get(url4, headers=headers, timeout=10)
if r4.status_code == 200:
    deps = r4.json().get('result', [])
    if deps:
        latest = deps[0]
        print(f'Latest deployment: {latest["id"][:8]}... status={latest.get("latest_stage",{}).get("status","?")}')
        print(f'Preview URL: {latest.get("url","?")}')
    else:
        print('No deployments found')
