# LEARNINGS — QWAV Technical Site Hub

## L1: IIFE semicolons are NOT optional in multi-chart scripts
- **Category:** JAVASCRIPT
- **Issue:** Three chart functions wrapped in IIFEs inside one <script> tag. Charts 2 and 3 rendered blank (0 non-zero pixels). No console error on page load — only visible on Runtime.evaluate().
- **Root cause:** `})()(function(){` was parsed as calling the return value (undefined) of the first IIFE with the second function as argument → "is not a function."
- **Solution:** Add semicolons between IIFEs: `})(); (function(){`.
- **Prevention:** Always put `;` after IIFE closing `})()`. Better: use named functions, not anonymous IIFEs.
- **Cross-Project:** YES — applies to any multi-chart Canvas visualization.

## L2: Non-zero pixel check is the only reliable Canvas test
- **Category:** TESTING
- **Issue:** Canvas elements exist in DOM and have dimensions, but may be blank. `canvas.toDataURL()` and `canvas.getContext()` succeed even when nothing is drawn.
- **Solution:** After render, check `ctx.getImageData()` for pixels with R+G+B > threshold.
- **Prevention:** Add to every canvas-based demo's deploy checklist.
- **Cross-Project:** YES.

## L3: Single-file HTML with inline data scales to ~30 KB before needing split
- **Category:** ARCHITECTURE
- **Issue:** How large can a single HTML file get before it needs to be split?
- **Solution:** 13 KB (v1.0) expanded to 31 KB (v1.1 with charts + genealogy). Still manageable. Files over 50 KB should consider splitting.
- **Prevention:** Monitor file size. Split at 50 KB threshold.
- **Cross-Project:** YES.

## L4: Publication links need periodic DOI verification
- **Category:** MAINTENANCE
- **Issue:** 30+ publication DOIs embedded in the page. One broken DOI undermines credibility.
- **Solution:** Write a script that checks all href values matching `doi.org/10.5281/zenodo.` and verifies they resolve (HTTP 200).
- **Prevention:** Run DOI audit before any site update that touches publications.
- **Cross-Project:** PARTIAL — applies to all sites with publication links.

---

*Learned during qwav-technical-site development.*
