import requests

token = 'sJYUcifLTwaukCJEDAyTXRPnfNjWjE11XGLBelQAUNQ.P4u1eO-gMGG3IZiFv92fvfzKHdZ8M1H_lb_hyDxXeGo'
account_id = 'edb167b78c9fb901ea5bca3ce58ccc4b'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# Check qnfo-hub domain status
url = f'https://api.cloudflare.com/client/v4/accounts/{account_id}/pages/projects/qnfo-hub/domains'
r = requests.get(url, headers=headers, timeout=10)
print('=== qnfo-hub domains ===')
for d in r.json().get('result', []):
    name = d['name']
    status = d['status']
    verify = d.get('verification_data', {}).get('status', '?')
    cert = d.get('certificate_authority', '?')
    # Check for verification errors
    verr = d.get('verification_data', {}).get('error', '')
    if verr:
        print(f'  {name}: status={status} verify={verify} cert={cert} ERROR={verr}')
    else:
        print(f'  {name}: status={status} verify={verify} cert={cert}')
