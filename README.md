# QWAV Technical Site

The hub site for QWAV — ultrametric quantum computing and AI. Serves as the bridge between the qwav.tech marquee page and the interactive artifact demos.

**Deploy:** Push to `QNFO/QWAV` repo as `index.html` (replaces README rendering)
**Live at:** https://qnfo.github.io/QWAV/

## Contents

- Hero section with thesis and call-to-action
- 4 evidence highlight cards (zero errors, 48x reduction, 40-atom spec, 6.6x AI)
- 5 interactive artifact cards (A1-A5) — links to GitHub Pages demos
- Full publication table (8 papers with DOIs + GitHub links)
- Research roadmap timeline (Q2 2026 → 2027)
- Footer with all cross-links (marquee, GitHub, Zenodo, ORCID, contact)

## Deploy

1. Push `index.html` and `.nojekyll` to `QNFO/QWAV` repo root (or `docs/` folder)
2. GitHub Pages auto-deploys
3. Verify at https://qnfo.github.io/QWAV/

## Update Cadence

- New publication → add row to pub-table
- New artifact deployed → update artifact card link
- New evidence result → add evidence-card
- Roadmap milestone met → update timeline-item class to "complete"
