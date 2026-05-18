# QWAV PROJECT BACKLOG

> **Purpose:** Prioritized queue of future work. Updated whenever new ideas emerge or priorities shift. Items are ordered by priority — work top to bottom.

**Last updated:** 2026-05-18 | **Status:** Ultrametric_v2 (Tier 0.5) complete — 7 sprints. P17 outreach sent. Credential doc published. **Cross-project sync review complete** — Tree Distance Cophenetic + ultrametric_v2 reviewed for gaps; 14 new backlog items added (P31–P44).

**Key Reprioritization (2026-05-17):** Cross-project review identified CRITICAL gaps: (1) Companion paper exists but not on Zenodo — P31. (2) Best outreach targets are neutral atom labs, not NV centers — P32 supersedes P10. (3) Key results ($q$-ary 48×, correlated noise, hardware spec) not yet in QWAV narrative materials — P33. P26 (Tier 1 paper) is ESSENTIALLY COMPLETE — companion paper written; only needs Zenodo upload. P10 SUPERSEDED by P32. P28 scope updated to leverage ultrametric_v2 codebase.

---

## Priority Queue

| Priority | Item | Description | Estimated Sessions | Dependencies | Status |
|:---------|:-----|:------------|:-------------------|:-------------|:-------|
| **P6** | **Q-PNA / AI side** | Specify training mechanism on Bruhat-Tits trees (loss function, backpropagation in discrete space, token calculus verification). Currently the AI side is less developed than quantum. | 2–3 | None | NOT STARTED |
| **P7** | **Patent timeline** | Research and document: filing dates, conversion status, jurisdictions, key claims, expiration timeline. Current docs say "provisional" without specifics. | 1 | Access to patent records | ✅ DONE (2026-05-12) — `strategy/0.2.md` |
| **P8** | **Competitive landscape** | ✅ DONE — `strategy/0.5.md`. Zero direct competitors. Mapped adjacent communities: p-adic physics (Dragovich/Khrennikov/Zúñiga-Galindo — allies, not competitors), holographic codes (Pastawski/Yoshida/Harlow/Preskill — closest, but hyperbolic not ultrametric), neutral atom labs (Harvard/Caltech/PASQAL — hardware hosts, not competitors), topological QC (Kitaev — different math), MBQC (different use of trees). Documented structural reasons for null result: siloing between p-adic math and QC communities, assumption that space is continuous, credential barriers. | 1 | None | ✅ DONE (2026-05-18) |
| **P9** | **SBIR Phase I** | Federal small business grant. May require US entity formation. | 2–3 | US entity (possibly) | NOT STARTED |
| **P10** | **Cold outreach to labs** | ~~Send 10 emails to NV center labs.~~ **SUPERSEDED by P32.** Ultrametric_v2 platform scoping identified NEUTRAL ATOM labs as the primary target, not NV centers. See P32 for specific templates to Harvard/Lukin, Caltech/Endres, PASQAL, Innsbruck. | — | — | SUPERSEDED by P32 |
| **P16** | **MIT implosion carving — nanoscale 3D fabrication** | Investigate: Nature Photonics 2026 — 3D nanostructures via photopatterning + 2,000× isotropic shrinkage (800 nm → sub-100 nm). phys.org/news/2026-05-implosion-3d-photonic-devices-visible.html Potential relevance: (1) physical fabrication of Bruhat-Tits tree hierarchical lattice (patent Claim 4); (2) visible-light photonic quantum computing pathway; (3) vacancy engineering for ultrametric hardware substrate. | 1 | Read paper + assess | NOT STARTED |
| **P11** | **P11 formal verification collaboration** | Lean 4 formal verification of ultrametric QEC threshold theorem. ⚠️ Competitive dynamic identified: collaborator's commercial positioning (software QEC verification) conflicts with QWAV thesis (hardware passive fault tolerance). Collaboration unlikely unless next reply demonstrates good-faith engagement. | 3–5 (ongoing) | Resolution of competitive dynamic | ⚠️ Under review — likely walk |
| **P12** | **IP: Decide on High-Temp filing** | Decision: file the High-Temperature Topological Chiral provisional ($325) or wait for VSD/FRO/EWOR outcomes? Quantitative EV analysis done in `strategy/0.1.md` and `strategy/ip-strategic-plan.md`. Expected net value negative in all scenarios (-$453 to +$59). File only if $325 is disposable AND priority-date hedge is needed. | 0.5 | None | NOT STARTED |
| **P13** | **IP: Draft ultrametric encoding provisional** | Fill in the outline at `strategy/0.1.md` (DEFINITIONS, figures, computational validation data). 17 claims drafted. DO NOT FILE — hold for conversion plan. | 2–3 | P11 decision | NOT STARTED |
| **P14** | **IP: Quarterly review** | Review DEVELOP concepts, check 12-month deadlines for any filed provisionals, cross-reference with QWAV strategy updates. Add to calendar. | 0.5 (recurring) | None | NOT STARTED |
| **P15** | **IP: Pre-filing verification** | If filing High-Temp: verify micro-entity status, generate ADS sheet, prepare cover letter, confirm current USPTO fee ($325). | 0.5 | P11 = YES | NOT STARTED |
| **P16** | **MIT implosion carving — nanoscale 3D fabrication** | Investigate: Nature Photonics 2026 — 3D nanostructures via photopatterning + 2,000x isotropic shrinkage (800 nm to sub-100 nm). Potential relevance: (1) physical fabrication of Bruhat-Tits tree hierarchical lattice (patent Claim 4); (2) visible-light photonic quantum computing pathway; (3) vacancy engineering for ultrametric hardware substrate. | 1 | Read paper + assess | NOT STARTED |
| **P17** | **Outreach — Zúñiga-Galindo email** | ✅ SENT 2026-05-15. Two binary questions. Awaiting response (2-week window). | ✅ SENT |
| **P18** | **Outreach — Conference abstract prep** | IF Zuniga-Galindo responds positively: prepare a one-page abstract on structural connection between ultrametricity and quantum computation (Bruhat-Tits tree geometry, passive fault tolerance, computational validation results). Do NOT write until call-for-abstracts format is known. | 1-2 | P17 = positive response | NOT STARTED — contingent |
| **P19** | **Outreach — Dragovich email** | Branko Dragovich (Steklov Mathematical Institute): p-adic quantum cosmology, genetics, string theory. Same format as P17 — short, specific reference to his work, binary question about collaboration or events. | 0.5 | P17 sent first (learn from response) | NOT STARTED — contingent |
| **P20** | **Outreach — Khrennikov email** | Andrei Khrennikov (Linnaeus University): p-adic probability, cognitive modeling, quantum foundations. Same low-friction format. | 0.5 | P17 sent first | NOT STARTED — contingent |
| **P21** | **Outreach — David Wales email** | David Wales (Cambridge): energy landscape theory, ultrametric protein folding. Directly adjacent to hierarchical state space thesis. Accessible, responds to substance. Draft in progress. | 0.5 | P17 sent first | NOT STARTED |
| **P22** | **Outreach — Michel Planat email** | Michel Planat (FEMTO-ST): ultrametricity + Riemann zeta + Galois groups + quantum information. Bruhat-Tits tree / Galois connection would interest him. | 0.5 | P17 sent first | NOT STARTED |
| **P23** | **ArXiv submission** | Submit the Zenodo paper to arXiv (quant-ph or math-ph). Requires endorser for first submission OR moderator approval based on paper quality. Zenodo DOI + Tier 0 data should qualify. | 1 | Endorser or moderator review | NOT STARTED |
| **P24** | **"Why Ultrametricity" explainer** | Accessible 2,000-word document: what ultrametricity is, why the continuous manifold assumption matters, what changes if you switch to trees. No equations. This is the calling-card document people share. | ✅ PUBLISHED — `Ultrametric Quantum Computing Foundations.md` (DOI: 10.5281/zenodo.20154557) | 2026-05-15 |
| **P25** | **Pre-register falsifiable prediction** | Publicly state a specific, testable prediction: "If Bruhat-Tits tree encoding enables passive fault tolerance, then X should be observed under Y conditions." This is the nuclear credibility option — make a bet on reality that anyone can verify. | ✅ PUBLISHED — 5 predictions integrated into Section 6 of credential document (DOI: 10.5281/zenodo.20154557). | 2026-05-15 |
| **P26** | **Tier 1 computational paper** | ✅ DONE — Published on Zenodo: "Symmetric Extension of Ultrametric Error Confinement" (DOI: 10.5281/zenodo.20208437). 36K words. Covers: ternary ($p=3$) architecture, depths d=2-8, correlated noise, classical baseline, $q$-ary generalization, concatenation redundancy, hardware specs (40-atom neutral atom). | — | — | ✅ DONE (2026-05-16) |
| **P27** | **Cross-domain synthesis paper** | ✅ DONE — Published as "Cross-Domain Synthesis: Ultrametric Geometry as Common Mathematical Structure Across Quantum Error Correction, Spin Glasses, Protein Folding, Cosmology, and Cognition" on Zenodo (DOI: [10.5281/zenodo.20265907](https://doi.org/10.5281/zenodo.20265907), 2026-05-17, 6,366 words). Demonstrates ultrametricity as the unifying mathematical structure across six domains. | 2–3 | All outreach complete | ✅ DONE (2026-05-17) |
| **P28** | **Open-source simulation code** | ✅ DONE (2026-05-16) — GitHub repo enhanced: comprehensive README, MIT license, CITATION.cff, GitHub Pages config, v2 architecture guide. Internal QWAV docs removed. Ready for push + v2 code drop. | — | — | ✅ DONE |
| **P29** | **FQXi Essay Contest** | Check for open FQXi essay contest on foundational physics. "Continuous manifold is the wrong assumption" is exactly their kind of provocative thesis. | 0.5 + writing | Contest open | NOT STARTED |
| **P30** | **Entity formation assessment** | ⚠️ DEFERRED — requires exogenous information about existing corporate entities (Empowering Change 501c3, Data For Good LLC, planned Netherlands incorporation). Cannot execute autonomously. Must verify assumptions with founder first. | 0.5 | Founder input | DEFERRED |
| **P31** | **Publish ultrametric_v2 companion paper to Zenodo** | Published — DOI: [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437). **UNBLOCKS P32 (lab outreach) and P33 (credential doc refresh).** Verify: original paper [1] cross-referenced? | — | — | DONE (2026-05-16) |
| **P32** 🔴 | **Neutral atom lab outreach campaign** | Send templated emails to 4 labs: Harvard/Lukin-Greiner, Caltech/Endres, PASQAL/Browaeys, Innsbruck/Zoller-Blatt. Attach outreach whitepaper + hardware spec. Specific ask: 2-4 hours machine time for $d=3$ demonstration (40 atoms). Templates in ultrametric_v2 BACKLOG §B1-B2. **SUPERSEDES P10 — neutral atoms, not NV centers.** | 1 | P31 (DOI to cite), email access | NOT STARTED |
| **P33** 🔴 | **Refresh credential doc + narrative library with v2 findings** | ✅ P33a+P33b DONE — `Ultrametric Quantum Computing Foundations.md` updated with v2 section (ternary, 48× scatter, concatenation redundancy, 40-atom hardware pathway) + companion paper DOI. `QA - Narrative Modules` extended with M13-M16. Remaining strategy docs (P41) deferred. | 1-2 (remaining: P41) | P31 ✓ | ✅ P33a+P33b done (2026-05-16) |
| **P34** 🟠 | **$q$-ary scatter as standalone talking point** | ✅ DONE — `strategy/0.4.md`, ~500 words. "48× LER reduction at zero qubit cost via existing hyperfine levels." Most accessible "wow" for non-specialists. | 0.5 | None | ✅ DONE (2026-05-18) |
| **P35** | **arXiv submission** | ❌ CANCELLED — requires endorsement, which is gatekeeping incompatible with QWAV's substance-first strategy. Zenodo (DOI) → ResearchGate + QNFO.org provides complete pipeline. arXiv adds only category-browsing visibility, not worth the dependency on an endorser. | — | — | CANCELLED (2026-05-18) |
| **P36** 🟡 | **Cophenetic distance as philosophical bridge** | The Tree Distance Cophenetic paper establishes triadic rigidity theorem + resolution-dependence bridge. Integrated into cross-domain synthesis paper (P27). Once DOI is registered, add bidirectional references. | 0.25 | DOI registration | ✅ INTEGRATED into P27 (2026-05-17) |
| **P37** 🟡 | **Update competitive landscape with benchmarking methodology** | ✅ DONE — `strategy/0.5.1.md`. Documents ultrametric_v2 honest classical baseline comparison (tree loses at i.i.d., wins under correlation) as credibility differentiator. Maps who else benchmarks honestly (ETH Zürich, JQI, IBM, Google). Provides action items for integration. | 0.5 | None | ✅ DONE (2026-05-18) |
| **P38** 🟡 | **Open-source ultrametric_v2 codebase** | Same as P28 — polish 26-file codebase from 7 sprints. Includes general-$p$, $q$-ary, correlated noise, classical baseline. | 1 | None | Same as P28 |
| **P39** 🟢 | **Cross-reference Tree Distance Cophenetic publication** | Once both publications have DOIs, add bidirectional references in QWAV materials. | 0.25 | P31 + Tree Distance Cophenetic upload | NOT STARTED |
| **P40** 🟢 | **Cross-domain synthesis paper — updated scope (P27)** | ⚠️ SUPERSEDED by P27. The published "Cross-Domain Synthesis: Ultrametric Geometry as Common Structure" (DOI: 10.5281/zenodo.20265907, May 17) already incorporates Tree Distance Cophenetic framework and ultrametric_v2 findings. | — | — | SUPERSEDED (2026-05-17) |
| **P41** 🟡 | **Assumption-to-physical-realizability mapping** | ✅ DONE — `strategy/0.6.md` Section 2. All 12 assumptions (7 architectural + 5 mathematical) mapped to verification status, refutation experiments, and risk assessments. | 1–2 | Symmetric Extension paper | ✅ DONE (2026-05-18) |
| **P42** 🟡 | **Investigate Heydeman et al. (2018) holographic QEC** | ✅ DONE — `strategy/0.5.2.md` + `0.6.md` Section 3. Supporting prior art: Bruhat-Tits QEC codes exist. Positioned with generalized framing. | 1 | Access to arXiv | ✅ ANALYZED (2026-05-18) |
| **P43** 🟡 | **Investigate Boettcher (2020) quantum ultra-walk** | ✅ DONE — `strategy/0.5.2.md` + `0.6.md` Section 3. 5 reconciliation hypotheses. Generalized framing adds escape: Bruhat-Tits is one tree; ultrametric class may behave differently. | 1 | Access to PRR | ✅ ANALYZED (2026-05-18) |
| **P44** 🟠 | **Address AGP 2006 attribution + classical/quantum scope** | ✅ DONE — `strategy/0.6.md` Section 3. AGP (2006) positioned as the threshold theorem QWAV geometrically specializes. Citation language drafted for next revision. Classical simulation → quantum claim bridge specified. | 1–2 | P41, P42, P43 | ✅ DONE (2026-05-18) |

**Priority key:** 🔴 CRITICAL (immediately actionable, high leverage) | 🟠 HIGH | 🟡 MEDIUM | 🟢 LOW

**Recommended execution order:** P31 → P33 → P32 → P36 → P38 → P34 → P37 → P35 → P39 → P40

**Source projects referenced:**
- `ultrametric_v2`: `G:\My Drive\projects\ultrametric_v2\` — 7 sprints complete, 28 tasks, 26 files, 260K+ MC trials
- `Tree Distance Cophenetic`: `G:\My Drive\projects\Tree Distance Cophenetic\` — Sprint 3 nearly complete, 0.8.md publication-ready, DOI assigned
- `Can Math Prove Physics`: `G:\My Drive\projects\Can Math Prove Physics\` — CLOSED 2026-05-18. Essay published (DOI: 10.5281/zenodo.20266032). Residual items transferred here (P41-P44).

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
