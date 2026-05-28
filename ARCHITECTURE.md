# Architecture Reference — deep.qwav.tech

> **Last updated:** 2026-05-28 | **Version:** 2.0 (markdown-first)
> **Principle:** Content (R2) and Presentation (Pages) are completely decoupled.

## System Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        deep.qwav.tech                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  /                    → index.html (marquee)                    │
│  /papers/             → papers/index.html (catalog)             │
│  /papers/paper.html   → papers/paper.html (template)            │
│  /api/paper/[slug]    → functions/api/paper/[slug].js (proxy)   │
│  /overlay.js          → overlay.js (Living Papers equation)     │
│  /sidebar.js          → sidebar.js (Living Papers concepts)     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                        DATA FLOW                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  User clicks paper in catalog                                   │
│       │                                                         │
│       ▼                                                         │
│  /papers/paper.html?p=[slug]                                    │
│       │                                                         │
│       ├── fetch('/api/paper/' + slug)                           │
│       │         │                                                │
│       │         ▼                                                │
│       │   functions/api/paper/[slug].js                         │
│       │         │                                                │
│       │         ├── fetch('pub-...r2.dev/papers/[slug].md')    │
│       │         │         │                                      │
│       │         │         ▼                                      │
│       │         │   R2: qnfo/papers/[slug].md                  │
│       │         │                                                │
│       │         └── adds Content-Type: text/markdown; utf-8    │
│       │                                                         │
│       ├── marked.js → markdown → HTML                           │
│       ├── MathJax → LaTeX → SVG                                 │
│       ├── overlay.js → equation click → AI explain              │
│       └── sidebar.js → concept sidebar                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Component Map

| Layer | Component | Location | Deployed |
|:------|:----------|:---------|:---------|
| **Routing** | `_redirects` | `G:\My Drive\QWAV\_redirects` | ✅ |
| **Landing** | `index.html` (marquee) | `G:\My Drive\QWAV\index.html` | ✅ |
| **Catalog** | `papers/index.html` | Generated from `md/*.md` | ✅ |
| **Template** | `papers/paper.html` | Single template for all papers | ✅ |
| **Proxy** | `functions/api/paper/[slug].js` | R2 proxy with charset header | ✅ |
| **Content** | `qnfo/papers/*.md` | R2 bucket `qnfo` | ⚠️ 1/498 uploaded |
| **Overlay** | `overlay.js` | Equation click-to-explain | ✅ deployed (inactive) |
| **Sidebar** | `sidebar.js` | Concept sidebar | ✅ deployed (inactive) |
| **AI API** | living-paper.pages.dev/api | Workers AI + Vectorize | ✅ cross-origin |

## File Structure (QWAV root)

```
G:\My Drive\QWAV\
├── index.html                    ← Marquee landing page
├── _redirects                    ← Cloudflare Pages routing
├── overlay.js                    ← Living Papers equation overlay
├── sidebar.js                    ← Living Papers concept sidebar
├── SESSION-CLOSEOUT-2026-05-28.md
├── LIVING-PAPERS-DEV.md
├── LESSONS-LEARNED.md
├── ARCHITECTURE.md (this file)
├── papers/
│   ├── index.html                ← Catalog (498 papers)
│   └── paper.html                ← Single rendering template
├── functions/
│   └── api/
│       └── paper/
│           └── [slug].js          ← R2 content proxy
├── projects/
│   └── handoffs/
│       ├── H1-R2-CONTENT-PIPELINE.md
│       ├── H2-LIVING-PAPERS-V2.md
│       ├── H3-CATALOG-DISCOVERY.md
│       └── H4-AI-PAPER-REVIEW.md
├── md/                           ← Temporary local copy (gitignored)
└── (content in R2)               ← qnfo/papers/*.md (498 files)
```

## Key Principles

1. **Content/Presentation decoupled** — R2 stores markdown, Pages stores template. Never co-mingled.
2. **Single template** — `paper.html` renders ALL papers. Front-end changes never require content regeneration.
3. **No Pandoc** — Markdown rendered client-side via marked.js. No pre-generation step.
4. **No deprecated platforms** — GitHub, Zenodo, ResearchGate references removed.
5. **No unverifiable claims** — "Peer-Reviewed", "healthy", "verified" removed. Only factual/verifiable content.
6. **Proxy for headers** — R2 r2.dev lacks charset header. Function proxy adds it.
7. **Query-parameter routing** — `?p=slug` avoids `_redirects` wildcard complexity.
