# PROJECT HANDOFF: QWAV Compute Cloud — On-Demand Embedding/Valuation (#89)

**Parent Program:** QWAV Phase 3
**Priority:** LOW
**Status:** Ready
**Estimated Effort:** 1 session

## Vision

A simple API for on-demand mathematical computation: p-adic valuations, ultrametric distances, tree operations, and embedding visualizations. Researchers can POST a computation request and get results back.

## MVP API
- `POST /compute/p-adic-distance` — $d_p(x, y)$ for given $p$, $x$, $y$
- `POST /compute/tree-path` — path between two nodes in Bruhat-Tits tree
- `POST /embed` — generate embedding vector for text
- `GET /compute/status` — service health

## Infrastructure
| Resource | Detail |
|:---------|:-------|
| Workers | API endpoints |
| Workers Containers | Mathematical computation (Python/Sage) |
| R2 | Cache results |

## Success Criteria
- [ ] 3+ compute endpoints operational
- [ ] Results returned within 5s
- [ ] API documentation at compute.qwav.tech
