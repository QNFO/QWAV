import requests, json

token = 'sJYUcifLTwaukCJEDAyTXRPnfNjWjE11XGLBelQAUNQ.P4u1eO-gMGG3IZiFv92fvfzKHdZ8M1H_lb_hyDxXeGo'
account_id = 'edb167b78c9fb901ea5bca3ce58ccc4b'
zone_qnfo = '84e9dc1d7fb72629ccdbe3174ed24420'
zone_qwav = '331e4363fd05e8e4fc123ea7d2775411'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# 1. Add qnfo.org apex to qnfo-hub
print('=== 1: Add qnfo.org apex to qnfo-hub ===')
url1 = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/qnfo-hub/domains'
r1 = requests.post(url1, headers=headers, json={'name': 'qnfo.org'})
print(f'Status: {r1.status_code}')
print(f'Response: {r1.text[:400]}')

# 2. Read qnfo.org DNS records
print('\n=== 2: Read qnfo.org DNS records ===')
url2 = f'https://api.cloudflare.com/client/v4/zones/{zone_qnfo}/dns_records'
r2 = requests.get(url2, headers=headers)
print(f'Status: {r2.status_code}')
if r2.status_code == 200:
    data = r2.json()
    records = data.get('result', [])
    print(f'Found {len(records)} records')
    for rec in records[:15]:
        print(f'  {rec["type"]} {rec["name"]} -> {rec["content"]} (id={rec["id"]}, proxied={rec.get("proxied",False)})')
else:
    print(f'Error: {r2.text[:300]}')

# 3. Purge cache for qwav.tech
print('\n=== 3: Purge cache for qwav.tech ===')
url3 = f'https://api.cloudflare.com/client/v4/zones/{zone_qwav}/purge_cache'
r3 = requests.post(url3, headers=headers, json={'purge_everything': True})
print(f'Status: {r3.status_code}')
print(f'Response: {r3.text[:300]}')

# 4. Create CNAME for hub.qnfo.org → qnfo-hub.pages.dev
print('\n=== 4: Create CNAME hub.qnfo.org -> qnfo-hub.pages.dev ===')
url4 = f'https://api.cloudflare.com/client/v4/zones/{zone_qnfo}/dns_records'
body4 = {'type': 'CNAME', 'name': 'hub.qnfo.org', 'content': 'qnfo-hub.pages.dev', 'proxied': True, 'ttl': 1}
r4 = requests.post(url4, headers=headers, json=body4)
print(f'Status: {r4.status_code}')
print(f'Response: {r4.text[:300]}')

# 5. Create CNAME for qnfo.org → qnfo-hub.pages.dev (apex)
print('\n=== 5: Create CNAME qnfo.org -> qnfo-hub.pages.dev (apex) ===')
body5 = {'type': 'CNAME', 'name': 'qnfo.org', 'content': 'qnfo-hub.pages.dev', 'proxied': True, 'ttl': 1}
r5 = requests.post(url4, headers=headers, json=body5)
print(f'Status: {r5.status_code}')
print(f'Response: {r5.text[:300]}')

print('\n=== DONE ===')
