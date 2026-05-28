# HANDOFF: Secrets Store Setup — API Key Management

> **Type:** Program → Project  
> **Date:** 2026-05-28  
> **Priority:** 🟡 P1 — Security foundation. All autonomous pipelines need API keys stored securely.  
> **Sessions:** 0.5  
> **Phase:** 3 (Enhancement) — P3.8  
> **Cross-Reference:** Cloudflare Audit §1.5 (SE8: Secrets Store), §7 Action #7

---

## SCOPE

QWAV's autonomous pipelines — Zenodo DOI registration, arXiv API access, Buffer social media posting, Email Service — all need API keys. Currently, these are either stored in local environment variables or hardcoded in scripts (security risk). Cloudflare Secrets Store provides a secure, Cloudflare-native way to manage API keys — encrypted at rest, never in code, accessible from Workers.

**What the Projects Agent should produce:**

1. **Secrets Store configured** with the following secrets:

| Secret Name | Purpose | Service |
|:------------|:--------|:--------|
| `ZENODO_API_TOKEN` | Zenodo DOI registration | Zenodo REST API |
| `BUFFER_ACCESS_TOKEN` | Buffer social media posting | Buffer API |
| `ARXIV_API_KEY` | arXiv API (if needed for higher rate limits) | arXiv |
| `QNFO_DOMAINS_API_KEY` | Future: domain management | Registrar API |

2. **A test Worker** (`secrets-test`) that:
   - Reads a secret from Secrets Store
   - Uses it to make a test API call (e.g., Zenodo API status check)
   - Returns success/failure (without exposing the secret value)
   - Demonstrates the pattern: secret → Worker → API

3. **Integration notes** for existing and planned Workers:
   - How `zenodo-automation` Worker should use `ZENODO_API_TOKEN`
   - How future Buffer-posting Worker should use `BUFFER_ACCESS_TOKEN`
   - Code snippet for reading secrets in Workers

4. **Documentation:** SECRETS.md or section in PROGRAM-STATE.md documenting:
   - What secrets exist (names only, not values)
   - Which Workers use which secrets
   - How to add a new secret
   - How to rotate a secret

## SUCCESS CRITERIA

- [ ] Secrets Store contains at least 2 secrets (ZENODO_API_TOKEN, BUFFER_ACCESS_TOKEN)
- [ ] Test Worker reads a secret successfully
- [ ] Test Worker makes an API call using the secret
- [ ] Secret value is NEVER exposed in logs, responses, or git
- [ ] Secret names documented (values remain private)
- [ ] Integration pattern documented for other Workers

## CONSTRAINTS

- **Never in code:** Secrets must be accessed via `env.SECRET_NAME` in Workers or `wrangler secret put`. Never hardcoded.
- **Never in git:** Secret values must never appear in committed files. Git hygiene: verify before commit.
- **Scoped tokens:** Use least-privilege tokens. Zenodo token has deposit scope only. Buffer token has post scope only.
- **Existing tokens:** Use existing API keys where available (check with user for current Zenodo/Buffer credentials). Do NOT generate new keys unless existing ones are unavailable.

## RESEARCH TRAIL

| File / Resource | Purpose |
|:----------------|:--------|
| `G:\My Drive\QWAV\briefings\platform\cloudflare-comprehensive-audit-2026-05-28.md` §1.5 SE8 | Secrets Store capability |
| Cloudflare Docs: [Secrets Store](https://developers.cloudflare.com/workers/configuration/secrets/) | API reference |
| `npx wrangler secret list` | Check existing secrets |
| `G:\My Drive\QWAV\briefings\platform\zenodo-crosslink-audit.md` | Zenodo integration details |
| Buffer Dashboard | Existing Buffer API tokens |

### Key wrangler Commands

```bash
# Put a secret
npx wrangler secret put ZENODO_API_TOKEN

# List secrets (names only, values hidden)
npx wrangler secret list

# Worker code pattern:
# const token = env.ZENODO_API_TOKEN; // Read from environment
# fetch('https://zenodo.org/api/...', { headers: { 'Authorization': `Bearer ${token}` } })
```

## RETURN PROTOCOL

1. Secrets Store configured → `wrangler secret list` shows all secrets (names only)
2. Test Worker deployed → reads secret, makes API call, returns success
3. Integration notes provided for zenodo-automation and Buffer Workers
4. Documentation committed: secret names, which Workers use which secrets, rotation procedure
5. Git audit: verify no secrets in committed files
6. Report back to Program Agent with: number of secrets configured, test Worker URL, integration notes
7. Update PROGRAM-STATE.md Secrets Store row: `⬜ → ✅`

---

*Projects Agent: This is the security foundation. Every autonomous pipeline — Zenodo DOI registration, arXiv scraping, Buffer posting — needs API keys. Secrets Store keeps them encrypted and never in code. 30-minute task with outsized security impact.*
