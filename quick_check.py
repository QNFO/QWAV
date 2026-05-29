import requests
token = 'sJYUcifLTwaukCJEDAyTXRPnfNjWjE11XGLBelQAUNQ.P4u1eO-gMGG3IZiFv92fvfzKHdZ8M1H_lb_hyDxXeGo'
account_id = 'edb167b78c9fb901ea5bca3ce58ccc4b'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
for project in ['qnfo-hub', 'qwav', 'ultrametric-quantum']:
    url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project}/domains'
    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code == 200:
        for d in r.json().get('result', []):
            v = d.get('verification_data',{}).get('status','?')
            print(f'{project}: {d["name"]} status={d["status"]} verify={v}')
    else:
        print(f'{project}: Error {r.status_code} {r.text[:100]}')
