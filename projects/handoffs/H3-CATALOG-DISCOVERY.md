# Handoff H3: Catalog & Discovery — Auto-Update, Search, Metadata

> **Type:** Program→Project | **Priority:** P2 (after H1 + H2) | **Est. effort:** 6-10 hours

## Problem

The paper catalog at `deep.qwav.tech/papers/` is a static HTML file. Adding a new paper requires regenerating the catalog. There's no search index, no paper-level metadata display beyond title/date, no topic filtering, and no way to discover related papers from the catalog view. The catalog doesn't know about papers until manually rebuilt.

## Current State

```
papers/index.html (static) ← manually generated from md/*.md files
  - Lists all papers with title + date
  - Basic search (text filter, client-side)
  - No topic tags, no descriptions, no sorting options
  - Links to paper.html?p=[slug]
```

## Scope

### Included
- **Auto-updating catalog** — regenerates when new papers hit R2 (or on a schedule)
- **Rich metadata cards** — each paper shows title, date, topics, excerpt, author
- **Search index** — full-text search across all 497 papers (titles + abstracts)
- **Topic filtering** — tag cloud or sidebar filter by research domain
- **Sort options** — date (default), title, topic
- **Pagination** — if catalog grows beyond ~500 entries
- **Related paper links** — "If you liked X, see also Y" from shared topics
- **Analytics** — most-read papers, trending topics (via Cloudflare Analytics)

### Excluded
- R2 pipeline (H1)
- Paper rendering improvements (H2)
- User authentication
- Comment/discussion system

## Success Criteria

| # | Criterion | Verification |
|:--|:----------|:-------------|
| 1 | New paper in R2 → appears in catalog within 5 minutes | Upload test paper, verify catalog shows it |
| 2 | Search returns relevant results across titles + abstracts | Search "ultrametric", verify multiple papers found |
| 3 | Topic filter narrows catalog to matching papers | Click topic tag, verify only matching papers shown |
| 4 | Sort by date, title, or topic works | Click sort option, verify order changes |
| 5 | Paper cards show: title, date, topics, 2-line excerpt | Visual inspection of any 3 papers |
| 6 | Catalog loads < 1 second (or shows skeleton while loading) | Lighthouse performance audit |
| 7 | "Related papers" on each card shows 2-3 linked papers | Check any paper card |

## Architecture Options

### Option A: Static Regeneration (Simple)
- Python script watches R2 for changes
- Rebuilds `papers/index.html` automatically
- Client-side search via fuse.js or lunr.js
- **Pro:** Simple, no backend
- **Con:** Full rebuild on every change

### Option B: Pages Function + D1 (Recommended)
- Pages Function at `/api/catalog` reads R2 file listing
- D1 database stores paper metadata (synced from R2)
- `/api/search?q=` endpoint for full-text search
- `/api/related?slug=` for related paper discovery
- **Pro:** Incremental updates, real search, scales well
- **Con:** Requires D1 database setup

### Option C: Client-Side Everything
- Single JSON manifest in R2 (`qnfo/papers/manifest.json`)
- Client fetches manifest, does all filtering/searching locally
- **Pro:** Zero backend, works offline-ish
- **Con:** Full manifest download on every page load (~50KB for 500 papers)

## Recommendation: Option B (D1-backed)

D1 is already in the Cloudflare ecosystem (no new platform). The `d1-citation-graph` project already has D1 schema patterns. Metadata can be synced from R2 frontmatter via a Worker.

## Key Dependencies

| Dependency | Status |
|:-----------|:-------|
| H1 (R2 pipeline) | Must complete first — papers in R2 with metadata |
| D1 database | Needs creation (`qnfo-catalog`) |
| Cloudflare Analytics | Optional — for popularity tracking |

## Acceptance Gate

- [ ] New paper added to R2 → appears in catalog (verify timing)
- [ ] Search works (try 5 different queries)
- [ ] Topic filtering works (verify 3 different topics)
- [ ] Paper cards display all metadata fields
- [ ] Deployment: `wrangler pages deploy` deploys catalog + search
- [ ] Performance: catalog loads under 1s on slow 3G
