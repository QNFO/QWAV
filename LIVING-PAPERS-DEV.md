# Living Papers — Development Roadmap & Lessons Learned

## Architecture

```
User → paper.html?p=[slug]
         │
         ├── /api/paper/[slug] → R2 content (Functions proxy, adds charset=utf-8)
         ├── marked.js → markdown → HTML
         ├── MathJax → LaTeX rendering
         ├── overlay.js → equation click → AI explanation
         └── sidebar.js → concept sidebar
```

## What Works

- Markdown rendering with YAML frontmatter extraction
- MathJax for all LaTeX equations
- R2 proxy with proper charset headers
- overlay.js and sidebar.js deployed (inactive — needs H2 activation)
- Single template for all papers (no regeneration needed)

## What Needs Work (H2)

- **Equation overlay AI**: overlay.js deployed but API calls fail (Vectorize index not populated)
- **Concept sidebar**: sidebar.js deployed but needs concept graph wiring
- **In-paper search**: Ctrl+F with highlights
- **Table of contents**: Auto-generated from H2/H3 headings
- **Theme toggle**: Light/dark with localStorage persistence
- **Mobile**: Sidebar collapses, better touch targets

## Critical Errors Fixed

| Error | Root Cause | Fix |
|:------|:-----------|:----|
| `â€"` in paper text | R2 r2.dev serves without `charset=utf-8`. Browser defaults to CP1252 on Windows. | Proxy function adds `Content-Type: text/markdown; charset=utf-8` |
| "Paper not found" | Markdown files not in R2 (only 1/498 uploaded) | H1 pipeline needed |
| Subprocess encoding crash | Python `subprocess.run(text=True)` uses CP1252 on Windows, wrangler outputs UTF-8 | Use `encoding='utf-8', errors='replace'` |
| `_redirects` loop | `*` wildcard matches empty path `/papers/` | Use `:slug` named parameter or query-parameter routing |

## Dependencies

| Component | Location | Status |
|:----------|:---------|:-------|
| overlay.js | `G:\My Drive\QWAV\overlay.js` | Deployed (inactive) |
| sidebar.js | `G:\My Drive\QWAV\sidebar.js` | Deployed (inactive) |
| Workers AI | living-paper project | Configured |
| Vectorize index | living-paper project | Needs population |
| EQUATION_CACHE KV | living-paper project | Configured |
| Reference implementation | `G:\My Drive\projects\living-paper\` | Test page at living-paper.pages.dev |
