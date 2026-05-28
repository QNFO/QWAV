# PROJECT HANDOFF: QWAV-SCAN — arXiv Discovery Engine (#83)

**Parent Program:** QWAV Phase 3
**Priority:** HIGH  
**Status:** Ready — all infrastructure provisioned
**Estimated Effort:** 2 sessions

## Vision

Autonomous arXiv scraper that discovers new papers relevant to QWAV's research domains (ultrametric geometry, p-adic physics, quantum computing), classifies them, and enriches the corpus.

## Infrastructure Available

| Resource | Detail |
|:---------|:-------|
| Browser Rendering | Headless Chromium in Workers — scrape arXiv |
| Workers AI | LLM for paper classification and summarization |
| D1 | Store paper metadata (title, authors, abstract, classification, tags) |
| R2 | Archive paper PDFs |
| Vectorize | Embed new papers into qwav-research index |
| Queues | Batch processing pipeline |

## MVP (Session 1)
- [ ] Worker: scrape arXiv daily for new papers in relevant categories (math.CO, math.QA, quant-ph, hep-th)
- [ ] LLM classifier: is this paper relevant to QWAV? (ultrametric, p-adic, tree geometry, distinction, etc.)
- [ ] Store metadata in D1 database
- [ ] Dashboard (simple HTML page): new papers found today, classification results

## Enhancement (Session 2)
- [ ] Auto-generate TL;DR summary via Workers AI
- [ ] Auto-embed and insert into Vectorize (growing the corpus)
- [ ] Email/webhook notification for high-relevance papers
- [ ] Paper similarity graph: "If you read X, you'll want Y"

## Key References
- arXiv API: https://arxiv.org/help/api/
- Browser Rendering docs: https://developers.cloudflare.com/browser-rendering/
- D1 database: `qwav-scan` (to be created)

## Success Criteria
- [ ] Daily arXiv scrape runs autonomously
- [ ] >80% classification accuracy (validated against 10 known-relevant papers)
- [ ] New papers appear in dashboard within 1 hour of arXiv posting
