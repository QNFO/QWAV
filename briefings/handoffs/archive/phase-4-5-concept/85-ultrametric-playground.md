# PROJECT HANDOFF: Ultrametric Playground — Interactive Tree Geometry (#85)

**Parent Program:** QWAV Phase 3
**Priority:** MEDIUM
**Status:** Ready
**Estimated Effort:** 1-2 sessions

## Vision

An interactive visualization of ultrametric tree geometry. Users select a prime $p$, see the Bruhat-Tits tree, explore p-adic distances, and understand how "balls within balls" structure emerges from the ultrametric inequality.

## Key Features
- [ ] Select prime $p$ (2, 3, 5, 7, 11...)
- [ ] Visualize Bruhat-Tits tree $T_p$ (infinite regular tree, degree $p+1$)
- [ ] Click nodes to see p-adic valuation
- [ ] Animate: "measure distance between two p-adic numbers"
- [ ] Overlay: quantum gate operations on the tree

## Infrastructure
| Resource | Detail |
|:---------|:-------|
| Pages | Deploy as standalone app at playground.qwav.tech |
| Workers AI | LLM explanations of tree concepts |
| R2 | Store pre-rendered assets |

## Success Criteria
- [ ] Interactive tree visualization deployed
- [ ] Users can select prime and see tree update
- [ ] Distance measurement between selected nodes
