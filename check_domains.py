import requests, time, socket

token = 'sJYUcifLTwaukCJEDAyTXRPnfNjWjE11XGLBelQAUNQ.P4u1eO-gMGG3IZiFv92fvfzKHdZ8M1H_lb_hyDxXeGo'
account_id = 'edb167b78c9fb901ea5bca3ce58ccc4b'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# Check verification status for all projects with domains
projects = ['qnfo-hub', 'ultrametric-quantum', 'qwav', 'solo-scientist', 'knowing-patterns', 'quantum-laws-of-form', 'qnfo-archive']
for project in projects:
    url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/{project}/domains'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        domains = r.json().get('result', [])
        print(f'{project}: {len(domains)} domain(s)')
        for d in domains:
            verif = d.get('verification_data', {}).get('status', '?')
            valid = d.get('validation_data', {}).get('status', '?')
            ca = d.get('certificate_authority', '?')
            print(f'  {d["name"]}: status={d["status"]}, verif={verif}, valid={valid}, CA={ca}')
    else:
        print(f'{project}: Error {r.status_code}')
    print()

# DNS resolution check
print('=== DNS Resolution ===')
for host in ['hub.qnfo.org', 'qnfo.org', 'deep.qwav.tech', 'quantum.qnfo.org']:
    try:
        ip = socket.gethostbyname(host)
        print(f'{host} -> {ip}')
    except:
        print(f'{host} -> NOT RESOLVING')
