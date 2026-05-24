# QWAV Spinoff Registry -- Interactive Artifacts (A1-A5)

**Date:** 2026-05-22
**Type:** Program→Project -- 5 interactive artifact deployments

---

## Project Inventory

| # | Project | Directory | Status | Deploy Target |
|:--|:--------|:----------|:-------|:--------------|
| A1 | Error Confinement Live Demo | `projects/2026/05/ultrametric-error-confinement-demo/` | ✅ Built, committed | `QNFO.github.io/ultrametric-error-confinement/` |
| A2 | Q-PNA Classifier Playground | `projects/2026/05/qpna-classifier-playground/` | ✅ Built, committed | `QNFO.github.io/q-pna/` |
| A3 | Ultrametric Convergence Explorer | `projects/2026/05/ultrametric-convergence-explorer/` | ✅ Built, committed | `QNFO.github.io/ultrametric-convergence/` |
| A4 | Tree Distance Sandbox | `projects/2026/05/tree-distance-sandbox/` | ✅ Built, committed | `QNFO.github.io/tree-distance/` |
| A5 | Hardware Pathway Visualizer | `projects/2026/05/hardware-pathway-visualizer/` | ✅ Built, committed | `QNFO.github.io/hardware-pathway/` |

## What's In Each Project

- `index.html` -- Complete interactive artifact (single file, vanilla JS)
- `.nojekyll` -- GitHub Pages requirement
- `README.md` -- Project overview and deploy instructions
- `PROJECT STATE.md` -- Current status
- `SPRINT.md` -- Task tracker
- `.gitignore` -- Standard ignores
- Initial git commit on `master`

## Next Action (Projects Agent)

For each project:
1. Create GitHub repo under `QNFO/` organization
2. Push the project directory
3. Enable GitHub Pages in repo Settings
4. Verify live URL
5. Report back to QWAV agent with URLs

## Return Protocol

When all 5 are deployed, QWAV agent will:
1. Verify each URL is live
2. Update qwav.tech marquee page (replace "Coming Soon" badges with live links)
3. Update qnfo.github.io/QWAV/ technical site (same)
4. Create Buffer social campaign
5. Update VENUE-REGISTRY.md
6. Mark A1-A5 complete in BACKLOG.md
