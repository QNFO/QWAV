import requests, time

token = 'sJYUcifLTwaukCJEDAyTXRPnfNjWjE11XGLBelQAUNQ.P4u1eO-gMGG3IZiFv92fvfzKHdZ8M1H_lb_hyDxXeGo'
account_id = 'edb167b78c9fb901ea5bca3ce58ccc4b'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
base = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects'

# 1. Get deep.qwav.tech domain ID from qwav project
print('=== 1: Find deep.qwav.tech domain ID ===')
r = requests.get(f'{base}/qwav/domains', headers=headers, timeout=10)
domains = r.json().get('result', [])
domain_id = None
for d in domains:
    if d['name'] == 'deep.qwav.tech':
        domain_id = d['id']
        print(f'Found: {d["name"]} id={domain_id}')
        break

if not domain_id:
    print('ERROR: deep.qwav.tech not found on qwav project')
    exit(1)

# 2. DELETE the custom domain
print('\n=== 2: Delete deep.qwav.tech from qwav ===')
r2 = requests.delete(f'{base}/qwav/domains/{domain_id}', headers=headers, timeout=10)
print(f'Delete status: {r2.status_code} {r2.text[:200]}')

# 3. Wait 3 seconds for CDN to register the deletion
print('\n=== 3: Waiting 5s... ===')
time.sleep(5)

# 4. Re-add deep.qwav.tech
print('\n=== 4: Re-add deep.qwav.tech to qwav ===')
r3 = requests.post(f'{base}/qwav/domains', headers=headers, json={'name': 'deep.qwav.tech'}, timeout=10)
print(f'Add status: {r3.status_code}')
resp = r3.json()
if resp.get('success'):
    d = resp['result']
    print(f'  name={d["name"]} status={d["status"]} verify={d.get("verification_data",{}).get("status","?")}')
else:
    print(f'  Errors: {resp.get("errors",[])}')

# 5. Check status
print('\n=== 5: Current domains on qwav ===')
r4 = requests.get(f'{base}/qwav/domains', headers=headers, timeout=10)
for d in r4.json().get('result', []):
    print(f'  {d["name"]}: status={d["status"]}')

print('\n=== DONE ===')
