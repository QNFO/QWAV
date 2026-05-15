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
| **P16** | **MIT implosion carving — nanoscale 3D fabrication** | Investigate: Nature Photonics 2026 — 3D nanostructures via photopatterning + 2,000× isotropic shrinkage (800 nm → sub-100 nm). phys.org/news/2026-05-implosion-3d-photonic-devices-visible.html Potential relevance: (1) physical fabrication of Bruhat-Tits tree hierarchical lattice (patent Claim 4); (2) visible-light photonic quantum computing pathway; (3) vacancy engineering for ultrametric hardware substrate. | 1 | Read paper + assess | NOT STARTED |
| **P11** | **P11 formal verification collaboration** | Lean 4 formal verification of ultrametric QEC threshold theorem. ⚠️ Competitive dynamic identified: collaborator's commercial positioning (software QEC verification) conflicts with QWAV thesis (hardware passive fault tolerance). Collaboration unlikely unless next reply demonstrates good-faith engagement. | 3–5 (ongoing) | Resolution of competitive dynamic | ⚠️ Under review — likely walk |
| **P12** | **IP: Decide on High-Temp filing** | Decision: file the High-Temperature Topological Chiral provisional ($325) or wait for VSD/FRO/EWOR outcomes? Quantitative EV analysis done in `strategy/0.1.md` and `strategy/ip-strategic-plan.md`. Expected net value negative in all scenarios (-$453 to +$59). File only if $325 is disposable AND priority-date hedge is needed. | 0.5 | None | NOT STARTED |
| **P13** | **IP: Draft ultrametric encoding provisional** | Fill in the outline at `strategy/0.1.md` (DEFINITIONS, figures, computational validation data). 17 claims drafted. DO NOT FILE — hold for conversion plan. | 2–3 | P11 decision | NOT STARTED |
| **P14** | **IP: Quarterly review** | Review DEVELOP concepts, check 12-month deadlines for any filed provisionals, cross-reference with QWAV strategy updates. Add to calendar. | 0.5 (recurring) | None | NOT STARTED |
| **P15** | **IP: Pre-filing verification** | If filing High-Temp: verify micro-entity status, generate ADS sheet, prepare cover letter, confirm current USPTO fee ($325). | 0.5 | P11 = YES | NOT STARTED |
| **P16** | **MIT implosion carving — nanoscale 3D fabrication** | Investigate: Nature Photonics 2026 — 3D nanostructures via photopatterning + 2,000x isotropic shrinkage (800 nm to sub-100 nm). Potential relevance: (1) physical fabrication of Bruhat-Tits tree hierarchical lattice (patent Claim 4); (2) visible-light photonic quantum computing pathway; (3) vacancy engineering for ultrametric hardware substrate. | 1 | Read paper + assess | NOT STARTED |
| **P17** | **Outreach — Zúñiga-Galindo email** | ✅ SENT 2026-05-15 — Version A to wazuniga@math.cinvestav.edu.mx. Two binary questions. Awaiting response (2-week window). | ✅ SENT |
| **P18** | **Outreach — Conference abstract prep** | IF Zuniga-Galindo responds positively: prepare a one-page abstract on structural connection between ultrametricity and quantum computation (Bruhat-Tits tree geometry, passive fault tolerance, computational validation results). Do NOT write until call-for-abstracts format is known. | 1-2 | P17 = positive response | NOT STARTED — contingent |
| **P19** | **Outreach — Dragovich email** | Branko Dragovich (Steklov Mathematical Institute): p-adic quantum cosmology, genetics, string theory. Same format as P17 — short, specific reference to his work, binary question about collaboration or events. | 0.5 | P17 sent first (learn from response) | NOT STARTED — contingent |
| **P20** | **Outreach — Khrennikov email** | Andrei Khrennikov (Linnaeus University): p-adic probability, cognitive modeling, quantum foundations. Same low-friction format. | 0.5 | P17 sent first | NOT STARTED — contingent |
| **P21** | **Outreach — David Wales email** | David Wales (Cambridge): energy landscape theory, ultrametric protein folding. Directly adjacent to hierarchical state space thesis. Accessible, responds to substance. Draft in progress. | 0.5 | P17 sent first | NOT STARTED |
| **P22** | **Outreach — Michel Planat email** | Michel Planat (FEMTO-ST): ultrametricity + Riemann zeta + Galois groups + quantum information. Bruhat-Tits tree / Galois connection would interest him. | 0.5 | P17 sent first | NOT STARTED |
| **P23** | **ArXiv submission** | Submit the Zenodo paper to arXiv (quant-ph or math-ph). Requires endorser for first submission OR moderator approval based on paper quality. Zenodo DOI + Tier 0 data should qualify. | 1 | Endorser or moderator review | NOT STARTED |
| **P24** | **"Why Ultrametricity" explainer** | Accessible 2,000-word document: what ultrametricity is, why the continuous manifold assumption matters, what changes if you switch to trees. No equations. This is the calling-card document people share. | ✅ DONE — see `0.3.md` | 2026-05-15 |
| **P25** | **Pre-register falsifiable prediction** | Publicly state a specific, testable prediction: "If Bruhat-Tits tree encoding enables passive fault tolerance, then X should be observed under Y conditions." This is the nuclear credibility option — make a bet on reality that anyone can verify. | ✅ DONE — 5 predictions integrated into `0.3.md` Section 6. | 2026-05-15 |
| **P26** | **Tier 1 computational paper** | Extend Tier 0: larger trees (depth 5–10), realistic noise models, comparison to surface code thresholds. Each paper is a brick in the evidence wall. | 2–3 | Tier 0 codebase | NOT STARTED |
| **P27** | **Cross-domain synthesis paper** | One paper showing ultrametricity as the unifying structure across: spin glasses (Parisi), protein folding (Wales), p-adic strings (Dragovich), cognitive models (Khrennikov), and quantum circuits (QWAV). This is the "pattern recognition" document. | 2–3 | All outreach complete (citations from community) | NOT STARTED |
| **P28** | **Open-source simulation code** | Polish the ultrametric-error-confinement repo: README, reproduction instructions, CI, license. Let people verify. | 1 | Tier 0 code exists | NOT STARTED |
| **P29** | **FQXi Essay Contest** | Check for open FQXi essay contest on foundational physics. "Continuous manifold is the wrong assumption" is exactly their kind of provocative thesis. | 0.5 + writing | Contest open | NOT STARTED |
| **P30** | **Entity formation assessment** | Evaluate: is a US entity (LLC or C-Corp) needed for SBIR/ARPA-E applications? Cost-benefit: entity cost vs. grant eligibility. | 0.5 | None | NOT STARTED |

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
