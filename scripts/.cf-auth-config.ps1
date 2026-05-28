# Cloudflare Authentication — PERSISTENT
# Created: 2026-05-28 by Program Manager Agent
# 
# Wrangler OAuth is configured at:
#   C:\Users\LENOVO\AppData\Roaming\xdg.config\.wrangler\config\default.toml
#
# The config contains:
#   - oauth_token (access token, auto-refreshed by wrangler)
#   - refresh_token (used to get new access tokens)
#   - Full scopes: pages:write, workers:write, r2:write, dns:write, zone:read, etc.
#
# USAGE:
#   wrangler whoami  # Works without any env vars
#   All wrangler commands work without CLOUDFLARE_API_TOKEN set
#
# FOR NON-WRANGLER API ACCESS (curl, Python SDK):
#   Extract current token from config:
#   $token = (Get-Content "$env:APPDATA\xdg.config\.wrangler\config\default.toml" | Select-String "oauth_token").Line -replace 'oauth_token = "(.+)"','$1'
#   curl -H "Authorization: Bearer $token" https://api.cloudflare.com/client/v4/...
#
# TO CREATE A PERMANENT API TOKEN (optional, for non-expiring access):
#   Visit: https://dash.cloudflare.com/profile/api-tokens
#   Click "Create Token" → "Custom token"
#   Add ALL permissions (Pages, Workers, R2, DNS, Zone, SSL, D1, AI, Email, Containers)
#   Set resources to "All accounts"
#   No expiration (leave TTL empty)
#   Save the token value to this file:
#     CLOUDFLARE_API_TOKEN=<token-value>
#
# CURRENT STATUS: ✅ Authenticated (OAuth, auto-refreshing)
# Account: quniverse (edb167b78c9fb901ea5bca3ce58ccc4b)
# Email: rwnquni@outlook.com

# Path to wrangler config (canonical auth source)
$WRANGLER_CONFIG = "$env:APPDATA\xdg.config\.wrangler\config\default.toml"

# Account ID
$CF_ACCOUNT_ID = "edb167b78c9fb901ea5bca3ce58ccc4b"
