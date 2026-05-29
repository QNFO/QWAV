# QWAV SEO & Discoverability — Setup Guide
## deep.qwav.tech + *.qnfo.org Research Papers Ecosystem

**Date:** 2026-05-29  
**Status:** Phase 1 deployed, Phase 2 pending manual steps

---

## 🔴 IMMEDIATE ACTION: CDN Cache Purge

The preview URL works perfectly but `deep.qwav.tech` root redirect is cached
from the old deployment.

**Fix:** Cloudflare Dashboard → `qwav.tech` zone → Caching → Purge Cache → Purge Everything

Or via API:
```bash
curl -X POST "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/purge_cache" \
  -H "Authorization: Bearer {API_TOKEN}" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything":true}'
```

---

## 🟠 TASK 1: Google Search Console

### Step 1: Add Property
1. Go to https://search.google.com/search-console
2. Click "Add property" → URL prefix
3. Enter: `https://deep.qwav.tech/`

### Step 2: Verify Ownership (DNS method — preferred)
1. Choose "DNS record" verification
2. Copy the TXT record value (e.g., `google-site-verification=XXXXXXX`)
3. Go to Cloudflare Dashboard → `qwav.tech` zone → DNS
4. Add TXT record:
   - Name: `deep` (or full: `deep.qwav.tech`)
   - Value: the TXT record from Google
   - TTL: Auto
5. Wait 1-2 minutes for DNS propagation
6. Click "Verify" in Search Console

### Step 3: Submit Sitemap
1. In Search Console, go to "Sitemaps"
2. Enter: `https://deep.qwav.tech/sitemap.xml`
3. Click "Submit"

### Step 4: Add *.qnfo.org Properties
Repeat for each paper domain:
- `https://quantum.qnfo.org/`
- `https://archive.qnfo.org/`
- `https://solo.qnfo.org/`
- etc.

---

## 🟠 TASK 2: Bing Webmaster Tools

### Step 1: Add Site
1. Go to https://www.bing.com/webmasters/
2. Sign in (Microsoft/Google account)
3. Click "Add a site" → `https://deep.qwav.tech/`

### Step 2: Verify Ownership
**Option A — DNS (easiest):**
- Add the TXT record Bing provides to Cloudflare DNS

**Option B — XML file:**
- The file `BingSiteAuth.xml` has been created in the deploy directory
- It will be included in the next deployment

### Step 3: Submit Sitemap
1. In Bing Webmaster Tools, go to "Sitemaps"
2. Enter: `https://deep.qwav.tech/sitemap.xml`
3. Click "Submit"

### Step 4: Enable IndexNow
IndexNow is auto-configured. The key file `7053de166d604835b7c151d0c43855a7.txt`
will be deployed to `https://deep.qwav.tech/7053de166d604835b7c151d0c43855a7.txt`.

Once deployed, run:
```bash
python G:\My Drive\QWAV\indexnow_submit.py --all
```

---

## 🟡 TASK 3: Cloudflare Web Analytics

### Setup
1. Cloudflare Dashboard → Analytics & Logs → Web Analytics
2. Click "Add a site"
3. Enter hostname: `deep.qwav.tech`
4. Copy the JavaScript snippet
5. Add it to `papers/read` (the paper template) before `</body>`

The snippet looks like:
```html
<script defer src='https://static.cloudflareinsights.com/beacon.min.js' 
  data-cf-beacon='{"token": "YOUR_TOKEN_HERE"}'></script>
```

### Benefits
- Free, no cookie banner needed (privacy-first)
- No sampling (unlike Google Analytics)
- Core Web Vitals monitoring
- Works even with ad blockers

---

## 🟡 TASK 4: Google Scholar Indexing

For each paper to appear in Google Scholar:
1. Ensure paper has Schema.org `ScholarlyArticle` structured data ✅ (already done)
2. Ensure paper is in PDF format (Scholar prefers PDFs)
3. Submit paper metadata to relevant repositories (arXiv, Zenodo, ResearchGate)
4. Get cited by other indexed papers

### PDF Generation
All papers should have PDF versions. Use the existing `pdf-builder` project:
```bash
cd G:\My Drive\projects\pdf-builder
python build_pdf.py --source papers/{slug}.html --output releases/{slug}.pdf
```

---

## 🟢 TASK 5: Ongoing Maintenance

### Monthly
- [ ] Check Google Search Console for coverage errors
- [ ] Check Bing Webmaster Tools for crawl errors  
- [ ] Run `python indexnow_submit.py` for any new papers
- [ ] Verify sitemap.xml includes all papers
- [ ] Check Cloudflare Web Analytics for traffic trends

### Quarterly
- [ ] Broken link scan across all 497 papers
- [ ] Update structured data if Schema.org changes
- [ ] Review crawl stats and optimize slow pages
- [ ] Check backlinks and citation counts

---

## 📁 Files Created/Updated

| File | Status | Purpose |
|:-----|:-------|:--------|
| `papers/index.html` | ✅ Updated | Catalog with Schema.org + Twitter Cards + "QWAV Home" → qwav.tech |
| `robots.txt` | ✅ Updated | deep.qwav.tech sitemap URL + AI crawler rules |
| `sitemap.xml` | ✅ Updated | All URLs → deep.qwav.tech |
| `_redirects` | ✅ Updated | Root → /papers/ redirect |
| `_headers` | ✅ Created | Security + caching |
| `404.html` | ✅ Created | Custom error page with search |
| `rss.xml` | ✅ Generated | 100 most recent papers |
| `feed.json` | ✅ Generated | JSON Feed format |
| `indexnow_submit.py` | ✅ Created | Auto-submit to Bing/Yandex |
| `{KEY}.txt` | ✅ Created | IndexNow verification |
| `BingSiteAuth.xml` | ✅ Created | Bing verification |
