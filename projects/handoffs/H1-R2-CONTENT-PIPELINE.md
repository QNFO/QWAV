# Handoff H1: R2 Content Pipeline — Markdown Ingestion & Storage Taxonomy

> **Type:** Program→Project | **Priority:** P0 (blocking) | **Est. effort:** 4-6 hours

## Problem

Papers exist as markdown files in `G:\My Drive\Obsidian\releases\` (650 files, clean UTF-8). They need to reach R2 (`qnfo/papers/[slug].md`) with proper metadata extracted, encoding validated, and a clear taxonomy separating active papers from archives. Currently this is done ad-hoc with Python scripts that handle encoding poorly and fail on subprocess output.

## Scope

### Included
- Python pipeline script that reads Obsidian markdown files
- UTF-8 encoding validation (reject or auto-fix non-UTF-8 files)
- Slug generation from YAML frontmatter `title:` field (fallback: first H1, fallback: filename)
- Metadata extraction: title, date, keywords, abstract from frontmatter
- R2 upload to `qnfo/papers/[slug].md` (all Cloudflare-native, no local directory in Pages)
- Archive taxonomy: `qnfo/papers/archive/YYYY/[slug].md` for older papers
- Content-Type `text/markdown; charset=utf-8` header (enforced at R2 level or proxy layer)

### Excluded
- Rendering/presentation (handled by Living Papers, H2)
- Catalog generation (handled by Catalog & Discovery, H3)
- Interactive AI features
- PDF generation

## Current Architecture (what exists)

```
Obsidian (650 .md files) → _pipeline.py → md/ (local) → npx wrangler → R2 qnfo/papers/
                                                    ↑
                                              SUBPROCESS ENCODING FAILS HERE
```

**The problem:** Python `subprocess.run` with `capture_output=True` fails when wrangler outputs non-ASCII characters. The `text=True` in subprocess uses system default encoding (CP1252 on Windows), which can't decode wrangler's UTF-8 output.

**Root cause:** `subprocess.run` needs `encoding='utf-8', errors='replace'` to handle mixed-encoding output from npx.

## Success Criteria

| # | Criterion | Verification |
|:--|:----------|:-------------|
| 1 | Pipeline processes all 650 files without crashing | Exit code 0, stats printed |
| 2 | Non-UTF-8 files detected and auto-converted (CP1252→UTF-8) | Log shows conversion count |
| 3 | Valid papers deduplicated (normalized title matching) | ~497 papers output (not 650) |
| 4 | All papers uploaded to R2 `qnfo/papers/` | `npx wrangler r2 object get qnfo/papers/autaxic-trilemma.md` succeeds |
| 5 | Paper renders at `https://deep.qwav.tech/papers/paper.html?p=[slug]` | Full markdown rendered with Living Papers |
| 6 | Archive taxonomy: `qnfo/papers/archive/2025/[slug].md` for older papers | Files organized by year |
| 7 | No `.md` files remain in Pages project (`G:\My Drive\QWAV\md\`) | Directory absent or gitignored |

## Key Files & Research Trail

| File | Purpose |
|:-----|:--------|
| `G:\My Drive\Obsidian\releases\` | Source: 650 markdown files (clean UTF-8, verified) |
| `G:\My Drive\QWAV\functions\api\paper\[slug].js` | R2 proxy — fetches from R2, adds charset=utf-8 |
| `G:\My Drive\QWAV\papers\paper.html` | Living Papers template — fetches from proxy |
| `G:\My Drive\QWAV\_pipeline.py` | Current pipeline attempt (broken — subprocess encoding) |
| `G:\My Drive\projects\research-pipeline\render-papers.py` | Legacy Pandoc approach (deprecated — replaced by markdown-first) |

## Technical Notes

### Subprocess Fix
```python
# WRONG (current approach):
result = subprocess.run([npx, 'wrangler', 'r2', 'object', 'put', ...],
    capture_output=True, text=True)  # text=True uses CP1252 on Windows!

# CORRECT:
result = subprocess.run([npx, 'wrangler', 'r2', 'object', 'put', ...],
    capture_output=True, encoding='utf-8', errors='replace')
```

### Encoding Detection
All 650 Obsidian files are clean UTF-8 (verified). The encoding issues only appear at the serving layer (R2 r2.dev doesn't set Content-Type headers). The Pages Function proxy (`/api/paper/[slug]`) adds `charset=utf-8`. No need for encoding conversion scripts — just validate and pass through.

### Archive Taxonomy
```
qnfo/papers/                          ← Active/latest papers
  autaxic-trilemma.md
  ultrametric-geometry-...
  
qnfo/papers/archive/2025/             ← Papers from 2025
  older-paper-slug.md
```

## Acceptance Gate

- [ ] Pipeline runs without crashing (no subprocess encoding errors)
- [ ] All ~497 papers in R2 (verified via `wrangler r2 object get`)
- [ ] Paper renders at `paper.html?p=[slug]` showing full markdown content
- [ ] Content-Type `charset=utf-8` present in proxy response
- [ ] Pipeline idempotent (re-running doesn't duplicate)
- [ ] Test plan: run pipeline, verify 3 random papers render
