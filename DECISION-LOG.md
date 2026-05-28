

## 2026-05-28 -- deep.qwav.tech Overhaul Session

### ADR-003: Markdown-First Architecture
**Decision:** Papers render from .md files via single paper.html template (marked.js + MathJax). No Pandoc pre-generation.
**Rationale:** User directive: separate content from presentation. Front-end changes never require content regeneration.
**Impact:** 497 HTML files removed. 1 template file. 498 .md files in R2. Content/presentation fully decoupled.

### ADR-004: R2 Content + Pages Template + Function Proxy
**Decision:** Three-layer decoupled architecture: R2 (qnfo/papers/), Pages (paper.html), Function (/api/paper/[slug]) as proxy adding charset=utf-8.
**Rationale:** r2.dev serves without Content-Type header, causing browser encoding guessing (CP1252 on Windows). Proxy fixes.
**Impact:** New functions/api/paper/[slug].js. Content must be in R2 (blocker: only 1/498 uploaded -- H1).

### ADR-005: Query-Parameter Routing
**Decision:** Paper URLs use ?p=slug query parameter instead of /papers/slug path-based routing.
**Rationale:** Cloudflare Pages _redirects wildcard (*) matches empty path segments, causing redirect loops.
**Impact:** Catalog links changed. _redirects simplified to only handle catalog routing.

### ADR-006: No Subjective/Unverifiable Claims
**Decision:** All public-facing content must contain only verifiable claims. Scrubbed: Peer-Reviewed, healthy, verified.
**Rationale:** Fabricated claims damage credibility. User directive.
**Impact:** Marquee status bar changed to "7 demos live - 15/15 online".

### ADR-007: Deprecated Platform Removal
**Decision:** GitHub, Zenodo, ResearchGate references removed from all templates.
**Rationale:** All research hosted on Cloudflare. Cross-references misleading.
**Impact:** Nav: Home | Papers only. License references retained (github.com/QNFO/license is a license URL, not a platform).

### ADR-008: Encoding Prevention
**Decision:** No CP1252 conversion scripts. Source files verified clean (650/650 UTF-8). Corruption from r2.dev missing charset header.
**Rationale:** Fix the serving layer, not the content. Content was never broken.
**Impact:** 35MB md/ directory removed from git. Proxy function adds Content-Type: text/markdown; charset=utf-8.

### ADR-009: Theme Toggle
**Decision:** Paper template includes light/dark theme toggle with localStorage persistence. Respects prefers-color-scheme.
**Rationale:** User preference -- dark theme hard to read. Toggle gives reader choice.
**Impact:** CSS variables for light/dark. Button in nav. JS for toggle + persistence.

