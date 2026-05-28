# HANDOFF: Cloudflare Email Service — Replace Outlook COM

> **Type:** Program → Project  
> **Date:** 2026-05-28  
> **Priority:** 🟡 P1 — Replaces deprecated Outlook COM. Enables native email processing.  
> **Sessions:** 1  
> **Phase:** 3 (Enhancement) — P3.6  
> **Cross-Reference:** Cloudflare Audit §1.6 (N4: Email Service), §7 Action #5; Master Strategy P3.3

---

## SCOPE

QWAV currently relies on Outlook COM (Windows-only, requires Desktop session) for email operations. Cloudflare Email Service provides native programmatic email sending and receiving — accessible from Workers, Queues, and the entire Cloudflare ecosystem. This handoff deploys Email Service as the replacement for Outlook COM in QWAV's workflow.

**What the Projects Agent should produce:**

1. **Email Service configured** with:
   - Verified sending domain (qnfo.org is already on Cloudflare DNS — use existing)
   - Verified sending email addresses: `papers@qnfo.org`, `collab@qnfo.org`
   - SPF/DKIM/DMARC records verified (Cloudflare DNS auto-configures)

2. **A Worker** (`email-processor`) that:
   - Receives inbound emails via Email Service routing
   - Classifies email using Workers AI: COLLABORATION / PAPER_COMMENT / MEDIA / SPAM / OTHER
   - Stores email metadata (from, subject, classification, timestamp) to D1 (if available) or KV
   - Forwards important emails to `rwnquni@outlook.com` (the human inbox)
   - Auto-responds to SPAM with polite decline

3. **An outbound email sender** (`email-sender`) Worker that:
   - Accepts HTTP POST with `{to, subject, body}`
   - Sends email via Email Service
   - Logs sent emails to KV or D1

4. **Documentation:** README.md explaining:
   - How Email Service is configured
   - How to send email programmatically (curl example)
   - How inbound routing works
   - SPF/DKIM/DMARC verification status
   - Migration checklist from Outlook COM

## SUCCESS CRITERIA

- [ ] Email Service domain verified (qnfo.org)
- [ ] `papers@qnfo.org` and `collab@qnfo.org` configured as sending addresses
- [ ] Inbound Worker deployed — receives test email, classifies it, forwards to human inbox
- [ ] Outbound Worker deployed — sends test email successfully
- [ ] SPF/DKIM/DMARC passing (check with `dig` or MXToolbox)
- [ ] Workers AI classification tested: at least 3 categories demonstrated
- [ ] Email metadata logged (KV or D1)

## CONSTRAINTS

- **Use existing domain:** qnfo.org is already on Cloudflare DNS. Do NOT register new domains.
- **Email Service limits:** Free tier has sending/receiving limits. Stay within.
- **No external email APIs:** Use Cloudflare Email Service natively. Do NOT integrate SendGrid/Mailgun/etc.
- **Security:** Do NOT store email contents in plain text in publicly accessible storage. Use Workers secrets or internal-only KV.
- **Gradual replacement:** Outlook COM remains available as fallback during transition. Email Service is additive, not a hard cutover.

## RESEARCH TRAIL

| File / Resource | Purpose |
|:----------------|:--------|
| `G:\My Drive\QWAV\briefings\platform\cloudflare-comprehensive-audit-2026-05-28.md` §1.6 N4 | Email Service capability, pricing |
| `G:\My Drive\QWAV\archive\cloudflare-master-strategy-2026-05-27.md` P3.3, #65 | Original Email Workers investigation |
| `G:\My Drive\QWAV\PROGRAM-STATE.md` D1/Queues sections | Storage targets for email metadata |
| Cloudflare Docs: [Email Service](https://developers.cloudflare.com/email-service/) | API reference, setup guide |
| Cloudflare Dashboard → Email → Email Routing | Verify existing routing config |

### Key wrangler Commands

```bash
# Verify email routing zones
npx wrangler email-routing zones list

# Deploy email worker
npx wrangler deploy --name email-processor

# Test outbound
curl -X POST https://email-sender.<worker>.workers.dev/send \
  -H "Content-Type: application/json" \
  -d '{"to":"rwnquni@outlook.com","subject":"Test from Email Service","body":"Hello from Cloudflare!"}'
```

## RETURN PROTOCOL

1. Email Service configured → domain verified, addresses active
2. Inbound Worker deployed → test email received and classified
3. Outbound Worker deployed → test email sent and received
4. SPF/DKIM/DMARC verification → evidence of passing records
5. Classification demo: 3 example emails classified
6. Email processor code committed to git repo
7. Report back to Program Agent with: Worker names, test results, DMARC status
8. Update PROGRAM-STATE.md Email Service row: `⬜ → ✅`

---

*Projects Agent: This replaces the Outlook COM dependency that requires a Windows Desktop session. Once deployed, email becomes a first-class Cloudflare primitive — triggerable from Workers, Queues, and the Agent Swarm.*
