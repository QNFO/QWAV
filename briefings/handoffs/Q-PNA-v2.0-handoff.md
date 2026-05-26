# Handoff: Q-PNA v2.0 — Tree Embedding Integration

**Type:** Program→Project
**Date:** 2026-05-26
**Issuing Authority:** Program Agent v2.0
**Accepting Authority:** Projects Agent
**GitHub Issue:** [#52](https://github.com/QNFO/QWAV/issues/52)

## Scope

### Included
- Upgrade Q-PNA Playground to v2.0 with tree embedding visualization
- Integrate ultrametric tree structure from tree-distance sandbox
- Show how p-adic metric space embeds naturally into tree geometry
- Interactive visualization with tree structure superimposed on Q-PNA lattice
- All A2 smoke tests passing from new implementation

### Excluded
- New mathematical formalism (use existing strategy/mathematical-foundations.md)
- Server-side computation (browser-only)
- Changes to other artifacts (A1, A3, A4, A5)

## Success Criteria

| # | Criterion | How Measured |
|:--|:----------|:-------------|
| 1 | Tree embedding integrated into Q-PNA visualization | Visual inspection + code review |
| 2 | Interactive controls for tree structure exploration | Manual browser testing |
| 3 | All A2 smoke tests pass | `python tests/test_smoke.py` — A2 section |
| 4 | Published via GitHub Release + GitHub Pages | URL returns HTTP 200 |

## Constraints

| Constraint | Value |
|:-----------|:------|
| Budget | $0 (human attention hours only) |
| Technology | Browser-based (HTML/JS/Three.js) |
| Compatibility | Must work alongside existing QWAV artifacts |
| Deadline | Sprint 25 (2 weeks) |

## Dependencies

| Dependency | Status | Blocking? |
|:-----------|:-------|:----------|
| tree-distance sandbox (artifacts/tree-distance/) | ✅ Complete | No |
| hardware-visualizer (artifacts/hardware-visualizer/) | ✅ Complete (reference patterns) | No |
| mathematical-foundations.md | ✅ Complete | No |

## Research Trail

1. `artifacts/qpna-playground/index.html` — Current Q-PNA implementation
2. `artifacts/tree-distance/index.html` — Tree distance sandbox
3. `artifacts/hardware-visualizer/index.html` — Three.js patterns (OrbitControls, etc.)
4. `strategy/mathematical-foundations.md` — Theoretical basis

## Acceptance Gate

- [ ] Re-read original handoff spec — each Success Criterion verified against deliverable
- [ ] Test plan executed — output committed, pass/fail honest
- [ ] A2 smoke test output showing all PASS
- [ ] GitHub Release published with version tag
- [ ] Issue #52 closed with deliverable reference

## Return Protocol

1. Publish to GitHub Release in QNFO/QWAV repository
2. Update GitHub Pages artifact at artifacts/qpna-playground/
3. Close GitHub Issue #52 with comment: deliverable URL + test results
4. Update roadmap #43 QEC Tiers status

---
*Program Agent → Projects Agent. Discover on startup by scanning for issues labeled `handoff`.*
