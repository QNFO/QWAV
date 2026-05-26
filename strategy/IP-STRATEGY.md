# IP Strategy — QWAV Intellectual Property & Patent Portfolio

> **Consolidates:** `ip-strategic-plan.md` + `IP-Only Licensing Strategy - Strategy B CERN Model.md`
> **Archived:** 2026-05-26 → `sessions/2026/05/strategy-archive/`
> **Status:** Canonical IP strategy document

---

## Strategy A: Comprehensive IP Portfolio (from ip-strategic-plan.md)
- Patent strategy for ultrametric quantum error suppression methods
- Trade secret protection for implementation details
- Defensive publishing to establish prior art
- Timeline: phased filing aligned with validation milestones
- Budget: estimated patent costs for key jurisdictions

## Strategy B: IP-Only / Licensing Model — The CERN Approach (from IP-Only Licensing Strategy)
- Publish openly, license freely, build reputation as the originator
- Analogous to CERN's approach: fundamental research openly shared; industry builds on it
- Advantages: zero patent costs, faster adoption, academic credibility
- Risks: no exclusive rights, competitors can implement freely
- Hybrid possible: publish core math openly, patent specific hardware implementations

## Decision Framework
| Factor | Strategy A (Patents) | Strategy B (CERN/Open) |
|:-------|:---------------------|:------------------------|
| Time to protection | 2-3 years (patent prosecution) | Immediate (publication) |
| Cost | $15-50K (filing + prosecution) | $0 |
| Defensibility | Strong (legal monopoly) | Weak (no legal barrier) |
| Academic credibility | Moderate | High |
| Industry adoption | Slower (licensing friction) | Faster (no friction) |
| Best for | Hardware-specific implementations | Mathematical foundations, algorithms |

## Current Recommendation
**Phase 0 (NOW — May 2026):** Publish mathematical foundations openly (Strategy B). Establish prior art and academic credibility. Publish GDSII mask specifications as defensive prior art.  
**Phase 1 (post-E2 validation):** File provisional patents on specific hardware implementations (Strategy A transition).  
**Phase 2 (post-E3 validation):** Convert provisionals to full patents. Execute licensing.  
**Phase 3 (commercial):** License portfolio to quantum hardware companies (ARM model — see `MANUFACTURING-BLUEPRINT.md`).

## Specific Patentable Manufacturing Assets (from MANUFACTURING-BLUEPRINT.md §6.4)

| # | Asset | Type | Platform |
|:--|:------|:-----|:---------|
| 1 | Tree-topology qubit connectivity layout (mask design) | Utility patent | Per platform (neutral atom, superconducting, spin, photonic, trapped ion) |
| 2 | Holographic tree code encoding method | Algorithm patent | Platform-agnostic |
| 3 | O(s log s) tree decoding method for quantum error correction | Algorithm patent | Platform-agnostic |
| 4 | 4K-operation quantum error suppression method using passive geometric fault tolerance | Method patent | Platform-agnostic |
| 5 | Bruhat-Tits tree topology as quantum computing architecture | Architecture patent | Platform-agnostic |

## See Also
- **NEW:** `MANUFACTURING-BLUEPRINT.md` — Fabless IP model, piggyback pathways, ARM analogy (§5-6)
- Full originals: `sessions/2026/05/strategy-archive/ip-strategic-plan.md` (26KB)
- Full originals: `sessions/2026/05/strategy-archive/IP-Only Licensing Strategy - Strategy B CERN Model.md` (16KB)
- Related: `briefings/research/fqxi-briefing.md` (grant context)
