# Handoff H2: Living Papers v2 — Full Interactive Rendering & AI Features

> **Type:** Program→Project | **Priority:** P1 (after H1 completes) | **Est. effort:** 8-12 hours

## Problem

Clicking a paper title shows full markdown text rendered via `marked.js` + MathJax — but the Living Papers experience is incomplete. The overlay.js and sidebar.js scripts are deployed but the equation-overlay AI explanations don't work because the Vectorize index and Workers AI backend aren't fully wired for all papers. The rendering is functional but basic — no concept sidebar, no related-equation discovery, no search within papers.

## Current State

```
paper.html loads → fetches /api/paper/[slug] (R2 proxy) → renders with marked.js
                                                              ├── MathJax (LaTeX)
                                                              ├── overlay.js (deployed, inactive)
                                                              └── sidebar.js (deployed, inactive)
```

**What works:** Markdown→HTML rendering, YAML frontmatter extraction, MathJax for LaTeX, basic metadata display.

**What doesn't:** AI equation explanations, concept sidebar, related paper discovery, in-paper search, table of contents generation.

## Scope

### Included
- **Equation overlay AI** — click any equation → Workers AI explains it (uses `living-paper.pages.dev/api/explain`)
- **Concept sidebar** — shows related concepts from QWAV corpus as user reads
- **In-paper search** — Ctrl+F style search with highlights
- **Table of contents** — auto-generated from H2/H3 headings
- **Dark/light theme toggle** — persist user preference
- **Mobile-responsive improvements** — sidebar collapses, better touch targets
- **Reading progress bar** — thin bar at top showing scroll position
- **Copy equation as LaTeX** — right-click or button to copy equation source

### Excluded
- R2 content pipeline (H1)
- Catalog & search index (H3)
- PDF generation
- New paper submission workflow

## Success Criteria

| # | Criterion | Verification |
|:--|:----------|:-------------|
| 1 | Click any equation → AI explanation appears within 3 seconds | Test on 5 equations across 3 papers |
| 2 | Concept sidebar shows related concepts while reading | Open paper, scroll, sidebar updates |
| 3 | In-paper search finds and highlights all matches | Ctrl+F, search term, count matches |
| 4 | TOC generates from headings, click navigates to section | Multi-section paper, TOC renders, click scrolls |
| 5 | Mobile: sidebar collapses, paper fills screen | Chrome DevTools mobile viewport test |
| 6 | Reading progress bar updates on scroll | Open long paper, scroll, bar fills |
| 7 | Theme toggle persists across page loads | localStorage check |
| 8 | Copy LaTeX button works on all MathJax equations | Right-click equation, copy, paste in editor |

## Key Files

| File | Purpose |
|:-----|:--------|
| `G:\My Drive\QWAV\papers\paper.html` | Main template — ALL rendering logic lives here |
| `G:\My Drive\QWAV\overlay.js` | Equation click overlay (deployed, needs activation) |
| `G:\My Drive\QWAV\sidebar.js` | Concept sidebar (deployed, needs activation) |
| `G:\My Drive\projects\living-paper\` | Reference implementation (test page) |
| `G:\My Drive\projects\living-paper\functions\api\explain.js` | AI explanation endpoint |
| `G:\My Drive\projects\living-paper\functions\api\related.js` | Related concepts endpoint |

## Dependencies

| Dependency | Status |
|:-----------|:-------|
| H1 (R2 Content Pipeline) | Must complete first — papers must be in R2 |
| Workers AI binding on living-paper project | Already configured |
| Vectorize index | Needs verification |
| EQUATION_CACHE KV namespace | Already configured on living-paper |

## Architecture Principle

**Content vs Presentation decoupling (per user directive):**
- Content: R2 markdown files (H1)
- Presentation: `paper.html` template (THIS project)
- Interactive AI: `living-paper.pages.dev/api/*` (already deployed)

No content changes for any rendering update. Template changes never touch R2 files. Living Paper API changes never touch either.

## Acceptance Gate

- [ ] 8 success criteria verified on preview URL
- [ ] No 497-paper regeneration required for template changes
- [ ] Works on production `deep.qwav.tech`
- [ ] Mobile-responsive verified (iPhone SE, iPad viewport)
- [ ] Performance: First Contentful Paint < 2s, Time to Interactive < 5s
