# HANDOFF: Queues + Browser Run Prototype — Research Pipeline v0.1

> **Type:** Program → Project  
> **Date:** 2026-05-28  
> **Priority:** 🟡 P1 — Async research pipeline backbone. Foundation for Autonomous Research Pipeline (Phase 5).  
> **Sessions:** 2  
> **Phase:** 3 (Enhancement) — P3.5  
> **Cross-Reference:** Cloudflare Audit §1.2 (S4: Queues), §1.1 (C10: Browser Run), §7 Action #4; Blue-Sky Blueprint §3

---

## SCOPE

QWAV has no automated system for discovering new research. This handoff creates a prototype pipeline that scrapes arXiv daily feeds, classifies papers by relevance, and stores results — using Cloudflare Queues (message routing) and Browser Run (headless Chrome for scraping/rendering).

**What the Projects Agent should produce:**

1. **A Cloudflare Queue** named `scrape-queue` with:
   - Messages containing arXiv feed URLs or paper URLs
   - Dead-letter queue for failed processing
   - Consumer Worker that processes each message

2. **A Consumer Worker** that:
   - Receives messages from `scrape-queue`
   - Uses Browser Run to render arXiv listing pages or individual paper pages
   - Extracts: title, authors, abstract, categories, arXiv ID, submission date
   - Classifies paper relevance using Workers AI: RELEVANT / BACKGROUND / IGNORE
   - Stores results (optionally to D1 if handoff #2 is complete, otherwise to KV or R2 as JSON)
   - Reports processing stats (papers found, classified, errors)

3. **A Producer Worker** (or manual trigger) that:
   - Fetches the arXiv daily feed for selected categories: `quant-ph`, `cs.AI`, `math-ph`, `hep-th`, `cond-mat`
   - Queues each paper URL into `scrape-queue`
   - Can be triggered via cron or HTTP endpoint

4. **Documentation:** README.md in the pipeline repo explaining:
   - Architecture diagram (Queue → Worker → Browser Run → Classification → Storage)
   - How to trigger a scrape
   - How to add new arXiv categories
   - How to view results
   - Known limitations (Browser Run timeout, rate limits)

## SUCCESS CRITERIA

- [ ] Queue `scrape-queue` created and visible via `wrangler queues list`
- [ ] Consumer Worker processes at least one arXiv paper URL through Browser Run
- [ ] Title, authors, abstract successfully extracted from rendered page
- [ ] Workers AI classifies at least one paper (RELEVANT/BACKGROUND/IGNORE)
- [ ] Results stored in accessible location (D1, KV, or R2)
- [ ] Pipeline completes end-to-end without manual intervention
- [ ] Error handling: malformed URL → DLQ (dead letter queue), Browser Run timeout → retry

## CONSTRAINTS

- **Free tier:** Queues (1M ops/mo), Browser Run (included renders), Workers AI (included Neurons). Stay within limits.
- **No external APIs:** Use Cloudflare Browser Run for rendering. Do NOT use external scraping services.
- **arXiv rate limits:** Be respectful. Space requests. Add delays between scrapes.
- **Browser Run timeout:** Browser Run has execution time limits (~30s). Handle gracefully. If page render exceeds limit, log and skip.
- **If D1 exists (handoff #2):** Use D1 for storage. If not, fall back to KV or R2 JSON files and note in code where D1 integration would go.

## RESEARCH TRAIL

| File / Resource | Purpose |
|:----------------|:--------|
| `G:\My Drive\QWAV\briefings\platform\cloudflare-comprehensive-audit-2026-05-28.md` §1.2 S4, §1.1 C10 | Queues + Browser Run details |
| `G:\My Drive\QWAV\archive\cloudflare-blue-sky-blueprint-2026-05-27.md` §3 | Autonomous Research Pipeline design |
| `G:\My Drive\QWAV\archive\cloudflare-master-strategy-2026-05-27.md` P3.6 | Original spec |
| Cloudflare Docs: [Queues](https://developers.cloudflare.com/queues/), [Browser Run](https://developers.cloudflare.com/browser-rendering/) | API reference |
| arXiv API docs: https://info.arxiv.org/help/api/ | Feed format, categories |

### Key wrangler Commands

```bash
# Create queue
npx wrangler queues create scrape-queue

# List queues
npx wrangler queues list

# Deploy consumer worker
npx wrangler deploy --name scrape-consumer

# Deploy producer worker
npx wrangler deploy --name scrape-producer
```

## RETURN PROTOCOL

1. Queue created → `wrangler queues list` evidence
2. Consumer Worker deployed and tested → processes at least one message
3. Browser Run extracts paper metadata → example output provided
4. Workers AI classification demonstrated → 3-5 example classifications
5. End-to-end test: trigger producer → message in queue → consumer processes → result stored
6. Pipeline code committed to git repo
7. Report back to Program Agent with: Queue name, Worker names, test results, storage location
8. Update PROGRAM-STATE.md Queues row: `scrape-queue: ⬜ → ✅`

---

*Projects Agent: This is the prototype for QWAV-SCAN — the always-on research discovery system. Get the pipeline working end-to-end with one arXiv category first, then scaling is just adding more categories to the producer.*
