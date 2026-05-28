# Lessons Learned — deep.qwav.tech Overhaul (2026-05-28)

## Fabrication Prevention

**Error:** Added "Peer-Reviewed" to catalog badge without verifying. Papers are not peer-reviewed.
**Lesson:** NEVER add claims you cannot verify. Every badge, qualifier, and label must be traceable to evidence. "Open Access" and "CC-BY-NC" are verifiable via the license file. "Peer-Reviewed" is not.

**Error:** Added "healthy" and "verified" qualifiers to marquee status bar.
**Lesson:** Subjective assessments ("healthy resources") and unverifiable claims ("publications verified") have no place in public-facing content. Stick to binary, checkable facts: "7 demos live · 15/15 online."

## Encoding: Fix the Serving Layer, Not the Content

**Problem:** Files displayed `â€"` instead of `—` (em-dash). 
**Initial (wrong) response:** Wrote CP1252→UTF-8 conversion scripts that duplicated 499 files.
**Root cause:** R2 r2.dev serves files without `Content-Type` header. Browsers guess encoding (CP1252 on Windows).
**Correct fix:** The Pages Function proxy already added `charset=utf-8`. No content conversion needed — ALL source files are clean UTF-8 (650/650 verified).
**Lesson:** When you see encoding issues at the display layer, check the serving headers BEFORE modifying content. The content was never broken — the delivery was.

## Subprocess Encoding on Windows

**Error:** Python `subprocess.run` with `text=True` fails on Windows when wrangler outputs non-ASCII characters.
**Root cause:** `text=True` uses system default encoding (CP1252), but wrangler outputs UTF-8.
**Fix:** Use `encoding='utf-8', errors='replace'` instead of `text=True`.
**Lesson:** Never use `text=True` on Windows without also specifying `encoding='utf-8'`.

## _redirects Wildcard Matching

**Error:** `/papers/*` matches `/papers/` (empty trailing segment), causing redirect loops.
**Lesson:** Cloudflare Pages `*` matches zero or more characters including empty strings. Use `:slug` named parameters or explicit path matching for directory roots.

## Markdown-First Architecture

**What worked:** Switching from 497 pre-generated HTML files (via Pandoc) to a single `paper.html` template that fetches markdown from R2.
**Why it's better:** Front-end changes never require content regeneration. Content changes never require template redeploys. Living Papers development can iterate on the template independently.
**Lesson:** Decouple content from presentation early. The initial Pandoc pre-rendering approach created an integration tax that grew with every design change.

## Deployment Discipline

**Error:** Accidentally deployed from `papers/` subdirectory instead of QWAV root, replacing the marquee page with the catalog.
**Lesson:** Always verify `wrangler pages deploy` is run from the intended directory. Check `git status` before deploying.
