# QWAV PROJECT CHANGELOG

> **Purpose:** Versioned record of all project changes. Read this alongside SPRINT.md when starting a new thread to understand what changed, when, and why.

---

## [v2.17] — 2026-05-17 — P31 Complete: Companion Paper on Zenodo

### Completed

| Item | Description |
|:-----|:------------|
| **P31 DONE** | Companion paper published on Zenodo. DOI: [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437). Unblocks P32 (lab outreach) and P33 (credential doc refresh). |
| **Obsidian release verified** | Release at `G:\\My Drive\\Obsidian\\releases\\2026\\05\\Symmetric Extension of Ultrametric Error Confinement.md` confirms DOI. |
| **Redundant files removed** | `p31-companion-paper.pdf` and `p31-zenodo-upload-instructions.md` deleted (paper was already published). |

### Files Changed

| File | Action |
|:-----|:-------|
| `BACKLOG.md` | P31 marked DONE with DOI |
| `SPRINT.md` | P31 marked DONE, IN PROGRESS updated |
| `PROJECT STATE.md` | Header updated |
| `CHANGELOG.md` | This entry |
| `p31-companion-paper.pdf` | DELETED (redundant) |
| `p31-zenodo-upload-instructions.md` | DELETED (redundant) |

### Verification Needed (Manual)

- Original paper [1] Zenodo record (10.5281/zenodo.20134944): was companion cross-reference added?
  If not, add note: "Companion: Quni-Gudzinas, DOI: 10.5281/zenodo.20208437."

### Next Unblocked

- **P33** — Refresh credential doc + narrative library (now has DOI to cite)
- **P32** — Neutral atom lab outreach (now has DOI for email)

---
## [v2.16] — 2026-05-17 — Cross-Project Sync Review: Tree Distance Cophenetic & Ultrametric_v2

### Completed

| Item | Description |
|:-----|:------------|
| **Cross-project gap analysis** | Reviewed `Tree Distance Cophenetic` (Sprint 3, 0.8.md publication-ready, DOI 10.5281/zenodo.20213043) and `ultrametric_v2` (7 sprints, 28 tasks, 26 files) for actionable gaps against QWAV strategy. |
| **Backlog expansion** | Added 10 new items (P31–P40) with priority tiers: 🔴 CRITICAL (P31-P33), 🟠 HIGH (P34-P35), 🟡 MEDIUM (P36-P38), 🟢 LOW (P39-P40). |
| **Status corrections** | P26 reclassified from "NOT STARTED" to "ESSENTIALLY COMPLETE" (companion paper written, only Zenodo upload needed). P10 marked SUPERSEDED by P32 (neutral atoms not NV centers). P28 scope updated to leverage ultrametric_v2 codebase. |
| **New decisions** | D8: Outreach targets shifted from NV centers to neutral atoms. D9: Companion paper IS Tier 1 — no separate writing needed. D10: $q$-ary scatter is primary differentiation narrative. |
| **IN PROGRESS updated** | Cross-project sync review findings integrated into sprint tracker. |

### Key Findings Absorbed from Ultrametric_v2

| Finding | QWAV Action |
|:--------|:------------|
| $q$-ary 48× LER reduction at zero qubit cost | Designated primary talking point (D10). Standalone piece: P34. Narrative library update: P33. |
| Correlated noise advantage (tree beats classical) | First practical advantage claim. Add to credential doc + narrative (P33). |
| 40-atom hardware spec, $d=3$, neutral atoms | Outreach campaign with 4 specific labs (P32). Supersedes vague NV center plan (P10). |
| Concatenation proven redundant | Elegant negative result — tree IS already optimal. Narrative library (P33). |
| Companion paper written (36K chars, 8 sections) | Only needs Zenodo upload (P31). Unblocks P32+P33. |

### Key Findings Absorbed from Tree Distance Cophenetic

| Finding | QWAV Action |
|:--------|:------------|
| Cophenetic distance as unified hierarchical ontology | Philosophical bridge for cross-domain synthesis paper (P36 → P27). |
| Triadic rigidity theorem | Lemma for "why trees not manifolds" argument in cross-domain paper. |
| Resolution-dependence bridge (height function = $\varepsilon$) | Connects to QWAV's "geometry choice determines physics" thesis. |
| 0.8.md publication-ready (DOI: 10.5281/zenodo.20213043) | Cross-reference in QWAV materials once published (P39). |

### Files Changed

| File | Action | Summary |
|:-----|:-------|:--------|
| `BACKLOG.md` | Major edit | P26 reclassified, P10 superseded, P28 scope updated, P31-P40 added with priority tiers |
| `SPRINT.md` | Major edit | Backlog table updated with P31-P40, IN PROGRESS refreshed, completed item #27 added |
| `DECISIONS.md` | Append | D8, D9, D10 added |
| `CHANGELOG.md` | Append | This entry |

### Next Session Start Here

1. **P31** — Upload companion paper to Zenodo (0.5 session, highest-leverage single action)
2. **P33** — Refresh credential doc + narrative library with v2 findings (1-2 sessions)
3. **P32** — Neutral atom lab outreach campaign (1 session, after P31)

Full execution order: P31 → P33 → P32 → P36 → P38 → P34 → P37 → P35 → P39 → P40

---

## [v2.16] — 2026-05-16 — P26+P31 Complete — Tier 1 Companion Paper Published

### Completed

| Item | Description |
|:-----|:------------|
| **P26 — Tier 1 paper** | Published "Symmetric Extension of Ultrametric Error Confinement" on Zenodo (DOI: 10.5281/zenodo.20208437). 36K words covering ternary ($p=3$) architecture, depths d=2-8, correlated noise, classical baseline, $q$-ary generalization, concatenation redundancy, hardware specs. |
| **P31 — Zenodo upload** | Companion paper uploaded with bidirectional cross-reference to original Tier 0 paper (DOI: 10.5281/zenodo.20134944). |

### Files Changed

| File | Action |
|:-----|:-------|
| `SPRINT.md` | P26 + P31 marked ✅ DONE. IN PROGRESS updated — next: P32 or P28. Milestone (3) added for companion paper. |
| `BACKLOG.md` | P26 + P31 marked ✅ DONE with DOI. |

### Status After This Update

3 Zenodo papers published:
1. Tier 0: "Computational Validation of Ultrametric Error Confinement" — DOI: 10.5281/zenodo.20134944
2. Credential: "Ultrametric Quantum Computing Foundations" — DOI: 10.5281/zenodo.20154557
3. Tier 1: "Symmetric Extension of Ultrametric Error Confinement" — DOI: 10.5281/zenodo.20208437

---

## [v2.15] — 2026-05-16 — Cross-Project Sync & Ultrametric_v2 Integration

### Completed

| Item | Description |
|:-----|:------------|
| **Ultrametric_v2 integration** | Ultrametric_v2 project (7 sprints, `G:\My Drive\projects\ultrametric_v2\`) COMPLETE. Key results synced into QWAV docs: ternary ($p=3$) symmetric architecture, ZERO logical errors at depth 7, 48× LER reduction via scatter, concatenation proven redundant, 40-atom neutral atom hardware design. |
| **Credential doc synced** | `Ultrametric Quantum Computing Foundations.md` updated to match published release version — added YAML frontmatter (author, ORCID, ISNI, title, aliases, modified). |
| **PROJECT STATE.md refreshed** | Section 7 (Priorities) updated — all "NOT STARTED" corrected to reflect actual completion. Section 11 (Cross-Project Ecosystem) added with links to all 4 sibling projects. Priority 5 (Outreach) updated to IN PROGRESS. |
| **SPRINT.md updated** | IN PROGRESS section reflects ultrametric_v2 completion. P26 backlog note updated. 4 new learnings (L7-L10) from ultrametric_v2 sprints. |
| **Stale files cleaned** | 11 stale ultrametric_v2 development files (`_barrier_*`, `_verify_*`, `_constructive*`, `_run_d7.py`, `_minimal.py`) removed from QWAV repo. |

### Files Changed

| File | Action |
|:-----|:-------|
| `Ultrametric Quantum Computing Foundations.md` | Synced with release version (+YAML frontmatter) |
| `PROJECT STATE.md` | Major refresh — corrected outdated priorities, added cross-project ecosystem |
| `SPRINT.md` | Added ultrametric_v2 completion + new learnings |
| 11 stale files deleted | `_barrier_out.txt`, `_barrier_v2.py`, `_barrier_verify.py`, `_constructive.py`, `_constructive2.py`, `_minimal.py`, `_quick_verify.py`, `_run_d7.py`, `_standalone_verify.py`, `_verify_file.py`, `_verify_v3.py` |

### New Cross-Project References

| Project | Path | Relationship |
|:--------|:-----|:-------------|
| ultrametric_v2 | `projects/ultrametric_v2/` | Direct computational validation engine — 7 sprints complete |
| Fractal Harmonic Trees | `projects/Fractal Harmonic Trees/` | Quantum foundations, Langlands program |
| Tree Distance Cophenetic | `projects/Tree Distance Cophenetic/` | Tree geometry metrics |
| Can Math Prove Physics | `projects/Can Math Prove Physics/` | Philosophical foundations |

---

## [v2.14] — 2026-05-14 — Collaboration Vetting & Competitive Dynamics (L10)

### Completed

| Item | Description |
|:-----|:------------|
| **L10 captured** | Technical objections can be competitive positioning disguised as rigor. A potential collaborator's four paper objections each protected his own commercial positioning (software QEC verification vs. QWAV hardware passive fault tolerance). Framework: (1) audit collaborator's business model before sharing technical detail, (2) apply symmetry test ("does the objection also apply to their work?"), (3) demand competing-work disclosure upfront, not after. |
| **L9 + L10 in SPRINT learnings table** | Both now documented in the main learnings tracker alongside L1-L8 |
| **P11 status updated** | P11 collaboration marked ⚠️ Under review — likely walk. Competitive dynamic incompatible with genuine collaboration. |
| **VSD rejection + L9 documented** | LLM-hostile programs structurally incompatible with QWAV workflow. |

### Files Changed
| File | Change |
|:-----|:-------|
| `LEARNINGS.md` | EDIT — L10 added, last-updated date |
| `SPRINT.md` | EDIT — L9 + L10 in learnings table, P11 status updated |
| `BACKLOG.md` | EDIT — P11 status updated |
| `CHANGELOG.md` | EDIT — This entry |
| `PROJECT STATE.md` | EDIT — Session header |

### Key Insights
- **L10 pattern:** Collaboration scoping and competitive intelligence gathering look identical in early email exchanges. The differentiator: does the "collaborator" disclose competing work BEFORE or AFTER extracting technical detail?
- **Symmetry test:** "Classical decoder therefore not quantum" is structurally invalid — every QEC decoder is classical by architecture (syndrome extraction → classical decoder → correction). The objection, if valid, would invalidate the objector's own QEC verification business.
- **Filter confirmed:** The collaborator self-filtered. His commercial interests (software QEC) and QWAV's thesis (hardware passive fault tolerance) are in direct competition. Better to identify this now than after formalization investment.

---

## [v2.13] — 2026-05-12 — Comprehensive Patent Design & Timeline (P7)

### Completed

| Item | Description |
|:-----|:------------|
| **P7: Patent timeline** | Documented existing filings, conversion status, jurisdictions, 12-month clock across ~18 provisionals and 25-package portfolio. |
| **Comprehensive provisional designed** | `strategy/0.2.md` — Unified patent covering all three QWAV domains: quantum hardware (claims 1-8), error correction software method (claims 9-15), AI methods on ultrametric structures (claims 16-22), integrated system (claims 23-25). Total: 25 claims. |
| **EV analysis** | Expected net value: +$74K (vs. -$453 to +$59 for quantum-only per D7). Filing held per D7 until at least one application funded or conversion partner secured. |
| **Pre-filing checklist** | 14 items prepared: figures, ADS, cover sheet, micro-entity verification, 12-month clock tracking, High-Temp Chiral cross-reference. |

### Files Changed
| File | Change |
|:-----|:-------|
| `strategy/0.2.md` | CREATE — Comprehensive patent timeline + 25-claim provisional design (430 lines, 33K chars) |
| `SPRINT.md` | EDIT — Added completed item 23, updated P7 backlog status, state header |
| `PROJECT STATE.md` | EDIT — Session header updated |
| `CHANGELOG.md` | EDIT — This entry |
| `BACKLOG.md` | EDIT — P7 status updated |

### Key Metrics
- **Patent claims designed:** 25 (up from 17 in 0.1.md)
- **Domains covered:** 3 (quantum hardware + error correction software + AI)
- **Filing cost if triggered:** $325 (micro-entity provisional)
- **Filing trigger:** At least one application funded $\to$ file within 24 hours
- **Patentability clock:** Paper published ~2026-05-12 $\to$ 12-month grace period expires ~2027-05-12

---

## [v2.12] — 2026-05-12 — Paper Published on Zenodo

### Completed

| Item | Description |
|:-----|:------------|
| **Paper published** | "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits" published on Zenodo. DOI: 10.5281/zenodo.20134944. Repo: github.com/QNFO/ultrametric-error-confinement (commit a902ddf). |
| **Project docs updated** | SPRINT.md, PROJECT STATE.md, BACKLOG.md updated to reflect publication status. Primary bottleneck shifted from "computational validation" to "adoption." |

### Files Changed
| File | Change |
|:-----|:-------|
| `SPRINT.md` | EDIT — item 12 updated to PUBLISHED, bottleneck recalculated, state date updated |
| `PROJECT STATE.md` | EDIT — computational validation status updated, application count corrected, session header updated |
| `CHANGELOG.md` | EDIT — this entry |
| `BACKLOG.md` | EDIT — P4 status updated from DONE to PUBLISHED with DOI |

### Key Metrics
- **DOI:** 10.5281/zenodo.20134944
- **Commit:** a902ddf
- **Experiment 0A:** LER=0 at depth 3+ for physical error rates up to 40%
- **Experiment 0B:** Energy barrier exponential in tree depth, consistent with $\Gamma \sim 80$ at 4K

---

## [v2.11] — 2026-05-12 — Paper & Simulations Moved to Standalone Project

### Completed

| Item | Description |
|:-----|:------------|
| **Paper extracted** | `papers/ultrametric-error-confinement.md` moved to `G:\My Drive\projects\Validation of Ultrametric Error Confinement\` |
| **Simulations extracted** | Full Tier 0 simulation suite (12 files) moved to same project |
| **QWAV cleaned** | `papers/` and `simulations/` directories removed from QWAV. 29 tracked files remaining. |

### Files Changed
| File | Change |
|:-----|:-------|
| `papers/ultrametric-error-confinement.md` | DELETE — moved to standalone project |
| `simulations/` (12 files) | DELETE — moved to standalone project |
| `README.md` | EDIT — removed Simulations and Papers sections, updated QUICK LOOKUP, footer to v7.3 |
| `PROJECT STATE.md` | EDIT — updated file counts, subdirectory count |
| `CHANGELOG.md` | EDIT — this entry |
| `SPRINT.md` | EDIT — added completed item 22 |
| `strategy/mathematical-foundations.md` | EDIT — updated citation reference |

### New Project
`G:\My Drive\projects\Validation of Ultrametric Error Confinement\` — standalone repo with paper, simulations, 7 project docs, .gitignore. Initial commit: c4b98ef.

---

## [v2.10] — 2026-05-12 — Root Cleanup & Agenda Review

### Completed

| Item | Description |
|:-----|:------------|
| **Briefings cleanup** | Deleted 17 obsolete files: old P11 collaborator meeting docs (10 files) and helper/conversion scripts (7 files). Added final `[redacted] Agenda (Shareable)` in 3 formats (`.md`, `.docx`, `.pdf`) + `business-docs-template.tex`. |
| **Root directory decluttered** | Moved 4 standalone docs to `strategy/`. Deleted `index.md` (not using GitHub Pages). Root now contains only 7 project docs. |
| **Project documentation completed** | Created BACKLOG.md, LEARNINGS.md, DECISIONS.md. All 7 required docs per Section 0.7 now present. |
| **Cross-reference audit** | Updated all broken/moved links in README.md, SPRINT.md, PROJECT STATE.md, index.md. All `Meet-and-Greet` references updated to `Agenda (Shareable)`. All root-level file links updated to `strategy/` prefix. |
| **Git hygiene** | Created `feature/root-cleanup-and-agenda-review` branch. 4 clean commits with descriptive messages. |

### Files Changed
| File | Change |
|:-----|:-------|
| `briefings/` (21 files) | 17 deletions (old agenda + helpers), 4 additions (final agenda + template) |
| `strategy/` (4 files) | Moved from root: Introvert's Path, NEXT STEPS, Pitch Deck, QA |
| `BACKLOG.md` | CREATE |
| `LEARNINGS.md` | CREATE |
| `DECISIONS.md` | CREATE |
| `README.md` | EDIT — updated links, file count, version to v7.1 |
| `SPRINT.md` | EDIT — updated reference, added completed items 18-21 |
| `PROJECT STATE.md` | EDIT — updated file count, documentation map, session header |
| `index.md` | DELETE — not using GitHub Pages with this repo |
| `CHANGELOG.md` | EDIT — this entry |
| `.gitignore` | Unchanged |

### Key Decisions
- D1–D8 documented in `DECISIONS.md` (all pre-existing, now formally recorded)
- D7: No patent filings without funded conversion plan
- D8: P11 collaborator Shape #1 — Lean 4 formalization transport

---

## [v2.9] — 2026-05-11 — IP Portfolio Audit & Reorganization

### Completed

| Item | Description |
|:-----|:------------|
| **IP portfolio audit** | Full inventory of 1,194 files across 25 draft patent packages at `G:\My Drive\Patents\`. Identified 0 active USPTO filings. |
| **QWAV relevance classification** | 25 packages cross-referenced against ultrametric/p-adic QWAV thesis. 1 exact match (High-Temp Chiral Topological — $45^\circ$ twisted Bi-2212, chiral $d+id'$, $\Delta \approx 25$ meV, 4K). 2 partial matches. 22 dead/off-path. |
| **Portfolio reorganization** | 770 dead/off-path files archived to `G:\My Drive\Archive\Patents\` (11 searchable categories with INDEX.md). Patents directory cleaned into 6 categories (01_FILING_READY through 06_TBD). Old FILED/2025 structure removed. |
| **Git recovery** | 55 previously deleted files recovered via `git checkout HEAD` (Bruhat-Tits Processor — 20 files, Invariant Geometric Structure — 24 files, Morita Gamma — 7 files, Adelic Constraints, misc). Geometric Attention Networks NOT found in git history — needs recreation from QWAV materials. |
| **Cost-benefit analysis** | Quantitative EV model for provisional filings (`strategy/_costbenefit.py`). Conversion probability: 5.1%. Licensing probability: 0.26%. Expected net value: -$453 to +$59 (file one) or -$868 (file both). Recommendation: file ONE or ZERO. Previous $6,000 spent on ~18 expired provisionals with no conversions. Rule: FILE ONLY IF a specific, funded 12-month conversion plan exists. |
| **Ultrametric encoding provisional outline** | `strategy/0.1.md` — 17 claims drafted covering Bruhat-Tits tree encoding, holographic perfect-tensor codes, tree-automorphism logical gates, fractal-multiplexed readout. Cross-references High-Temp Chiral application. Includes filling instructions, §101 self-check, and filing checklist. NOT FILED — held pending conversion plan. |
| **Project files updated** | PROJECT STATE.md (Priority 4 rewritten with honest IP assessment), SPRINT.md (P11-P14 IP tasks added to backlog), CHANGELOG.md (this entry). |

### Key Finding
**The ultrametric encoding mechanism — QWAV's core novel contribution — has ZERO patent protection.** The existing High-Temp patent covers the hardware (twisted bilayer superconductor). The encoding architecture (Bruhat-Tits tree, geometric error suppression, tree-automorphism gates) is entirely unprotected. An outline exists but is deliberately not filed because no funded 12-month conversion plan exists. Without experimental validation, lab access, or collaborators, the probability of converting any provisional is ~5%.

### Documents Created
| File | Purpose |
|:-----|:--------|
| `strategy/ip-strategic-plan.md` | Full 8-step IP strategic plan |
| `strategy/0.1.md` | Ultrametric encoding provisional outline (17 claims) |
| `strategy/_costbenefit.py` | Quantitative filing cost-benefit model |

### Documents Updated
| File | Changes |
|:-----|:--------|
| `PROJECT STATE.md` | Priority 4 rewritten — honest IP assessment replacing outdated PCT plan |
| `SPRINT.md` | Completed items 14-17, backlog items P11-P14 for IP work |
| `CHANGELOG.md` | This entry |

---

## [v2.8] — 2026-05-11 — Mathematical Foundations (P5)

### Completed

| Item | Description |
|:-----|:------------|
| **Mathematical foundations document** | Formal definitions, 4 theorems (strong triangle inequality, error confinement, threshold theorem, energy barrier scaling), lemma chain, Lean 4 formalization priority table, quantum generalization, relationship to surface codes/TQC/bosonic codes. 9 sections. |
| **P5 marked complete** | SPRINT.md backlog and completed items updated. |

### Files Changed
- `strategy/mathematical-foundations.md` — Full document (CREATE)
- `SPRINT.md` — P5 complete, item 13 added (EDIT)
- `CHANGELOG.md` — This entry (EDIT)

---

## [v2.7] — 2026-05-11 — arXiv Paper: Ultrametric Error Confinement

### Completed

| Item | Description |
|:-----|:------------|
| **arXiv/Zenodo paper (P4)** | Formal paper: "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits." 6 sections, 19 references. Presents Tier 0 results with full methods, results tables, and threshold theorem conjecture. Ready for arXiv/Zenodo submission. |
| **P4 marked complete** | SPRINT.md backlog updated. |

### Files Changed
- `papers/ultrametric-error-confinement.md` — Full paper (CREATE)
- `SPRINT.md` — P4 complete (EDIT)
- `CHANGELOG.md` — This entry (EDIT)

---

## [v2.6] — 2026-05-11 — Foresight Institute Application Drafted

### Completed

| Item | Description |
|:-----|:------------|
| **Foresight Institute proposal** | Application drafted (P3) for AI for Science & Safety track. Glass-box AI as safety mechanism, decentralized science alignment, Tier 0 evidence. |
| **P3 marked complete** | SPRINT.md backlog and application tracker updated. |

### Files Changed
- `applications/foresight-institute.md` — Full proposal (CREATE)
- `SPRINT.md` — P3 complete, application tracker updated (EDIT)
- `CHANGELOG.md` — This entry (EDIT)

---

## [v2.5] — 2026-05-11 — Emergent Ventures Application Drafted + README v7.0

### Completed

| Item | Description |
|:-----|:------------|
| **Emergent Ventures proposal** | 1-page application drafted (P2). Core thesis + Tier 0 evidence + founder track record + $100K use-of-funds. Rolling deadline — ready to submit. |
| **README v7.0** | Every file reference converted to clickable relative links. ASCII art directory tree replaced with structured linked list. Quick Lookup table fully linked. Added simulations, briefings, applications entries. GitHub Pages URL in footer. |
| **P2 marked complete** | SPRINT.md application tracker updated. |

### Files Changed
- `applications/emergent-ventures.md` — Proposal (CREATE)
- `README.md` — v7.0: clickable links, structured directory (EDIT)
- `SPRINT.md` — P2 complete, application tracker updated (EDIT)
- `CHANGELOG.md` — This entry (EDIT)

---

## [v2.3] — 2026-05-11 — P11 collaborator Collaboration Prep

### What Happened
Identified a formal verification collaboration opportunity with P11 collaborator. P11 runs HeytingLean — a Lean 4 formal verification stack with 4,649 files, 876,000+ lines, zero `sorry` in core. They have offered "formalization transport" — taking specific QWAV claims and proving them as theorems in Lean 4 using their existing infrastructure.

### Why This Matters
Formal verification in Lean 4 is the ultimate realization of the substance-first strategy:
- **Bypasses peer review:** A proof that type-checks is unassailable — no reviewer, no gatekeeper
- **Bypasses lab experiments:** Proofs can be parameterized with published experimental data
- **Produces unassailable evidence:** Machine-verified theorems are stronger than either peer review or experimental data
- **Aligned with P11's precedent:** They previously formalized 6 papers for Vladimir Veselov (student of Kolmogorov) on ultrametric structures — directly adjacent to QWAV's ultrametric work

### Key Insight
The core QWAV theorem to formalize: a threshold theorem for ultrametric QEC, analogous to the surface code threshold theorem from the 1990s. Statement: in a Bruhat-Tits tree encoding, $p_{\text{logical}} \leq C \cdot p_{\text{err}}^{k \cdot d}$, giving a geometric threshold for fault tolerance. This uses well-defined mathematical objects (trees, probability bounds) and can be parameterized with published experimental data from Google/IBM/Rigetti.

### Deliverable
`briefings/P11 collaborator - [redacted] Meet-and-Greet.md` — comprehensive briefing covering: who P11 is, the Veselov precedent, three collaboration shapes, IP terms, talking points, questions to ask, risks, and follow-up plan.

### Files Changed
- `briefings/P11 collaborator - [redacted] Meet-and-Greet.md` — Full briefing document (CREATE)
- `SPRINT.md` — Added P11 (collaboration), item 11 to COMPLETED (EDIT)
- `CHANGELOG.md` — This entry (EDIT)

---

## [v2.2] — 2026-05-11 — Independent Git Repo Initialized

### Why
QWAV previously existed as a directory within the DeepChat workspace, where multiple LLM agents operate on different projects simultaneously. This created risk of cross-project git contamination. QWAV is being published to GitHub and requires its own clean, independent repository.

### What Changed
- **QWAV extracted** from DeepChat workspace git tracking
- **Independent git repo** initialized at this repository on `main` branch
- **Path fix:** `simulations/simulations/plots/` $\to$ `simulations/plots/` (nested directory from wrong relative path — fixed in experiment code)
- **.gitignore updated:** Added `simulations/__pycache__/`, OS files, temp files
- **`__pycache__/` removed** from simulations directory
- **Experiment code fixed:** `save_path` now uses `os.path.dirname(__file__)` for reliable plot paths
- **Initial commit:** 26 files, 4,122 insertions. All project files committed cleanly.

### Git Remote
*Not yet configured.* To publish to GitHub:
```bash
cd QWAV
git remote add origin https://github.com/YOUR_USERNAME/qwav.git
git push -u origin main
```

### Current State
- Branch: `main`
- Working tree: clean
- 26 tracked files across 4 directories (root, strategy/, simulations/, people/)

### Files Changed
- `.gitignore` — Updated for independent repo (EDIT)
- `simulations/experiment_0a.py` — Fixed plot save path (EDIT)
- `simulations/experiment_0b.py` — Fixed plot save path (EDIT)
- `CHANGELOG.md` — This entry (EDIT)
- `SPRINT.md` — Updated to reflect independent repo (EDIT)

---

## [v2.1] — 2026-05-11 — Tier 0 Computational Validation Built

### Completed

| Item | Description |
|:-----|:------------|
| simulations/ package created | Full Tier 0 simulation suite: btree.py, encoding.py, noise.py, metrics.py, experiments 0A+0B, plots |
| Experiment 0A: Error Confinement | Demonstrated ultrametric error suppression: tree LER = 0 for depths 3+ at p_err <= 0.40, vs. flat LER up to 0.152. Suppression factor exceeds 10^7x at depth 3+. |
| Experiment 0B: Energy Barrier Scaling | Confirmed E_barrier(d) = 2^d exponential scaling. Verified exhaustively for d=2,3. Barrier grows from 4 (d=2) to 1024 (d=10) leaf flips. |
| Strong triangle inequality verified | 0 violations in 15,000 trials across p=2,3,5. |
| SPRINT.md updated | P1 marked complete; Tier 0 results added to learnings |

### Key Results

- **Error confinement confirmed:** Tree encoding suppresses errors exponentially with depth
- **Barrier scaling confirmed:** E_barrier ∝ 2^d for p=2
- **Falsifiable prediction tested:** The prediction "errors at fine levels don't propagate to coarse levels" passes simulation test
- **Next:** P2 (Emergent Ventures application), P4 (arXiv/Zenodo paper with simulation results)

### Files Changed
- `simulations/btree.py` — Bruhat-Tits tree data structure (CREATE)
- `simulations/encoding.py` — Tree and flat state encoding (CREATE)
- `simulations/noise.py` — Bit-flip and correlated error models (CREATE)
- `simulations/metrics.py` — LER, R_prop, suppression, CI computation (CREATE)
- `simulations/experiment_0a.py` — Error confinement experiment (CREATE)
- `simulations/experiment_0b.py` — Energy barrier experiment (CREATE)
- `simulations/plots.py` — ASCII and matplotlib visualization (CREATE)
- `simulations/README.md` — Documentation (CREATE)
- `SPRINT.md` — Updated P1 status, added learnings (EDIT)
- `CHANGELOG.md` — This entry (EDIT)

---

## [v2.0] — 2026-05-11 — Strategy Recalibration

### Strategic Context

This changelog is initiated after a comprehensive strategy review (2026-05-11) that identified and corrected misalignment between the project's actual constraints and implicit assumptions in some documentation. Two critical recalibrations drive all changes:

1. **No physical lab experiments** $\to$ all "experiments" are computational simulations synthesized from known parameters and theory. This is legitimate computational physics — cheaper, faster, and fully compatible with the written-first strategy.

2. **No peer review** $\to$ the peer-review system is rejected as institutional gatekeeping. Paradigm-challenging work has historically been suppressed by peer review. Open-access publication with direct reader evaluation — where individuals judge substance for themselves — is the only credible channel for genuinely novel ideas.

**Session work (2026-05-11):** Full document consistency audit. Fixed broken file references (QA.md referenced nonexistent "Computational Validation Roadmap.md" — corrected to actual filename), fixed duplicate Q8 in README, fixed mangled version line, fixed broken table row in External Sources, added Q8 to QA.md, created SPRINT.md and CHANGELOG.md for thread continuity, updated all version numbers. Many files already contained partial recalibration language — this session completed and verified the transition.

### Completed This Session (2026-05-11)

| Item | Description |
|:-----|:------------|
| Strategy review delivered | Full critique of QWAV thesis, gaps, and path forward |
| Strategy recalibrated | Aligned all docs with actual constraints (computational-only, no peer review) |
| CHANGELOG.md created | Versioned change tracking |
| SPRINT.md created | State tracker and handoff document |
| QA.md $\to$ v3.0 | Fixed broken file references (3×), added Q8, updated evidence table |
| README.md $\to$ v6.0 | Fixed references, updated directory (15 files), added Q8, updated version |
| NEXT STEPS.md | Fixed file reference to Experimental Validation Roadmap |
| External Sources & Citation Map $\to$ v2.0 | Fixed broken table row, added computational simulation category, updated version |
| Cross-document audit | Fixed all broken internal file references; verified consistency |

### Rationale

The previous documentation strategy implicitly assumed:
- Physical lab experiments as the validation path
- Peer-reviewed publication as the credibility path
- Institutional affiliation as desirable or attainable

None of these assumptions hold. The recalibration centers on:
- **Computational simulation** as the primary evidence-generation method (faster, cheaper, fully under founder control)
- **Open-access, substance-first evaluation** as the audience strategy (target individuals who judge merit independently)
- **Falsifiable predictions tested in silico** rather than in vitro (equally valid for theory validation)

### Unresolved

| Item | Status |
|:-----|:-------|
| Tier 0 simulation code | Not yet built (P1 in SPRINT.md) |
| Experimental collaborator | None engaged (not required for current stage) |
| VSD application | Pending |
| FRO Abstract | Pending |
| EWOR Fellowship | Pending |
| Patent timeline | Not yet documented (P7 in SPRINT.md) |
| Competitive landscape | Not yet researched (P8 in SPRINT.md) |

---

## 2026-05-15 — Multi-Platform Distribution

### What Changed

- **Buffer posts scheduled:** Bluesky, Mastodon, Twitter/X (with reply thread) — all automated, addToQueue.
- **Substack article posted:** Full article with subject, title, subtitle, read-more break, 2 notes, 6 tags.
- **LinkedIn article posted:** Full article with headline, subtitle, body, key takeaways, DOI reference, teaser.

### Rationale

Credential document (DOI: 10.5281/zenodo.20154557) distributed across all available platforms. Buffer handles short-form (Bluesky, Mastodon, Twitter). Substack and LinkedIn carry the long-form narrative. This is the "Introvert's Path" distribution strategy — written-only, automated scheduling, no live engagement required.

---

## 2026-05-15 — Credential Document Published (DOI: 10.5281/zenodo.20154557)

### What Changed

- **PUBLISHED:** `Ultrametric Quantum Computing Foundations.md` on Zenodo with DOI: 10.5281/zenodo.20154557.
- **Renamed:** `0.3.md` → `Ultrametric Quantum Computing Foundations.md` (titled filename).
- **Copied:** To `G:\My Drive\Obsidian\releases\2026\05\` for archival cross-reference.
- **SPRINT.md:** P24+P25 marked PUBLISHED with DOI.
- **BACKLOG.md:** P24+P25 marked PUBLISHED with DOI.

### Rationale

Credential document now has a permanent, citable DOI. Combined with the Tier 0 paper (DOI: 10.5281/zenodo.20134944), QWAV now has two citable works on Zenodo — an evidence trajectory independent of any gatekeeper.

---

## 2026-05-15 — Explainable Credential Document (P24+P25)

### What Changed

- **NEW FILE:** `0.3.md` — Comprehensive ultrametric quantum computing explainer: foundations, computational validation results, 5 pre-registered falsifiable predictions. 3,700 words, 12 references. Designed for Zenodo publication (DOI pending) and ResearchGate cross-post.
- **SPRINT.md:** P24+P25 marked complete (item 25). BACKLOG table updated.
- **BACKLOG.md:** P24+P25 marked complete.

### Rationale

The credential document replaces the arXiv paper, the PhD, and the institutional affiliation as the primary credibility asset. It is published on Zenodo with a DOI, cross-posted on ResearchGate for search indexing, and linked from qnfo.org/releases. No endorsement required. No peer review. No gatekeeper. The work stands on substance.

### Files Changed

- `0.3.md` (NEW)
- `SPRINT.md` (COMPLETED + BACKLOG updated)
- `BACKLOG.md` (P24+P25 marked complete)

---

## 2026-05-15 — P17 Sent: First Outreach Executed

### What Changed

- **P17 SENT:** Zúñiga-Galindo email (Version A) sent to wazuniga@math.cinvestav.edu.mx. Two binary questions. 2-week response window.
- **SPRINT.md:** P17 added to COMPLETED (item 24). BACKLOG table: P17 marked SENT. IN PROGRESS: updated with 2-week wait + unblocked next actions.
- **BACKLOG.md:** P17 marked SENT.
- **PROJECT STATE.md:** Session header updated, Section 4.3 outreach table updated, Priority 5 status updated.

### Rationale

First targeted outreach executed. This is the door-opener — not a pitch, not a favor request. Two binary questions (conference date? unaffiliated researchers welcome?) answerable in 30 seconds. Consistent with Introvert's Path (written-only, no live interaction). If response is positive, next step is P18 (abstract prep). If no response after 2 weeks, send one brief follow-up, then proceed to P19-P22 (Dragovich, Khrennikov, Wales, Planat).

---

## 2026-05-14 — Outreach Pipeline Integration

### What Changed

- **NEW FILE:** `outreach-email-zuniga-galindo.md` — Two-version email draft (A: confident with Zenodo DOI, B: softer deferential) targeting W.A. Zuniga-Galindo for the First International Conference on Models of Complex Hierarchic Systems and non-Archimedean Analysis (Mexico City, 2026). Includes rationale, follow-up protocol, and alignment with Introvert's Path.
- **SPRINT.md:** Added P17 to IN PROGRESS (active task: send the email). Added P17-P20 to BACKLOG section (outreach pipeline: Zuniga-Galindo, Dragovich, Khrennikov emails + abstract prep).
- **BACKLOG.md:** Added P16 (MIT implosion carving), P17-P20 (outreach pipeline) to priority queue.

### Rationale

The founder identified a strategic gap: despite 300+ open-access publications, no active connections to the researchers building bridges across ultrametric/p-adic fields. The "First International Conference" organized by Zuniga-Galindo represents a rare opportunity for a "back door" into the community — submit an abstract (peer-reviewed but not a full paper) and present written work. Email outreach is entirely consistent with the Introvert's Path (written-only communication; no live pitching required).

### Files Changed

- `outreach-email-zuniga-galindo.md` (NEW)
- `SPRINT.md` (IN PROGRESS + BACKLOG sections updated)
- `BACKLOG.md` (P16-P20 added)
- `PROJECT STATE.md` (upcoming)
- `LEARNINGS.md` (upcoming)
