# QWAV PROJECT BACKLOG

> **Purpose:** Prioritized queue of future work. Updated whenever new ideas emerge or priorities shift. Items are ordered by priority — work top to bottom.

**Last updated:** 2026-05-12 | **Status:** Paper published (P4 complete)

---

## Priority Queue

| Priority | Item | Description | Estimated Sessions | Dependencies | Status |
|:---------|:-----|:------------|:-------------------|:-------------|:-------|
| **P6** | **Q-PNA / AI side** | Specify training mechanism on Bruhat-Tits trees (loss function, backpropagation in discrete space, token calculus verification). Currently the AI side is less developed than quantum. | 2–3 | None | NOT STARTED |
| **P7** | **Patent timeline** | Research and document: filing dates, conversion status, jurisdictions, key claims, expiration timeline. Current docs say "provisional" without specifics. | 1 | Access to patent records | ✅ DONE (2026-05-12) — `strategy/0.2.md` |
| **P8** | **Competitive landscape** | Research: who else works on $p$-adic/ultrametric quantum computing? If none, document why. If some, differentiate. | 1 | None | NOT STARTED |
| **P9** | **SBIR Phase I** | Federal small business grant. May require US entity formation. | 2–3 | US entity (possibly) | NOT STARTED |
| **P10** | **Cold outreach to labs** | Send 10 emails to NV center labs using template from Validation Roadmap. Track responses. This is optional — computational validation may be sufficient. | 1–2 | Email access | NOT STARTED |
| **P11** | **P11 formal verification collaboration** | Lean 4 formal verification of ultrametric QEC threshold theorem. ⚠️ Competitive dynamic identified: collaborator's commercial positioning (software QEC verification) conflicts with QWAV thesis (hardware passive fault tolerance). Collaboration unlikely unless next reply demonstrates good-faith engagement. | 3–5 (ongoing) | Resolution of competitive dynamic | ⚠️ Under review — likely walk |
| **P12** | **IP: Decide on High-Temp filing** | Decision: file the High-Temperature Topological Chiral provisional ($325) or wait for VSD/FRO/EWOR outcomes? Quantitative EV analysis done in `strategy/0.1.md` and `strategy/ip-strategic-plan.md`. Expected net value negative in all scenarios (-$453 to +$59). File only if $325 is disposable AND priority-date hedge is needed. | 0.5 | None | NOT STARTED |
| **P13** | **IP: Draft ultrametric encoding provisional** | Fill in the outline at `strategy/0.1.md` (DEFINITIONS, figures, computational validation data). 17 claims drafted. DO NOT FILE — hold for conversion plan. | 2–3 | P11 decision | NOT STARTED |
| **P14** | **IP: Quarterly review** | Review DEVELOP concepts, check 12-month deadlines for any filed provisionals, cross-reference with QWAV strategy updates. Add to calendar. | 0.5 (recurring) | None | NOT STARTED |
| **P15** | **IP: Pre-filing verification** | If filing High-Temp: verify micro-entity status, generate ADS sheet, prepare cover letter, confirm current USPTO fee ($325). | 0.5 | P11 = YES | NOT STARTED |

---

## Application Tracker

| # | Application | Organization | Type | Status | Submitted | Decision Expected | Notes |
|:--|:------------|:-------------|:-----|:-------|:----------|:------------------|:------|
| 1 | VSD | Deep Science Ventures College | Venture-creation PhD | ❌ REJECTED | May 2026 | — | Bans LLM use, prohibits existing IP. |
| 2 | FRO Abstract | Convergent Research | Focused Research Org ($20–50M) | ⏳ Pending | May 2026 | Unknown | Abstract stage only |
| 3 | EWOR Fellowship | EWOR | Fellowship for outlier founders | ⏳ Pending | May 2026 | Unknown | Written application |
| 4 | Emergent Ventures | Mercatus Center | Moonshot grant | ⏳ Pending | May 2026 | Unknown | Tyler Cowen's program |
| 5 | Harmonic.ai | Harmonic | Startup database | ⏳ Pending | May 2026 | Rolling | VC discovery platform |
| 6 | LinkedIn Co-Founder & Head of AI | Stealth Startup (LinkedIn Jobs) | Co-founder position | ⏳ Pending | May 2026 | Rolling | Physics-informed AI SaaS for semiconductors. On-site San Jose. Equity-only until funding. ⚠️ Conflicts with D4 (solo founder) + D6 (written-only) if accepted. |

---

## Completed & Archived

| Priority | Item | Outcome | Date |
|:---------|:-----|:--------|:-----|
| P1 | Tier 0 Simulation | btree.py, encoding.py, noise.py, metrics.py, experiments 0A+0B, plots | 2026-05-11 |
| P2 | Emergent Ventures application | Submitted | 2026-05-11 |
| P3 | Foresight Institute application | Submitted | 2026-05-11 |
| P4 | arXiv/Zenodo paper | Published on Zenodo — "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits." DOI: 10.5281/zenodo.20134944. Repo: github.com/QNFO/ultrametric-error-confinement. | 2026-05-12 |
| P5 | Mathematical foundations | Formal definitions, 4 theorems, lemma chain, Lean formalization priority table | 2026-05-11 |
| P7 | Patent timeline | `strategy/0.2.md` — Full timeline + comprehensive provisional design (25 claims, 3 domains). Filing held per D7. | 2026-05-12 |
