# QWAV PROGRAM BACKLOG

> **Purpose:** Prioritized queue of future work. Items ordered by priority — work top to bottom. 
> **Update rule:** When an item is completed, move it to Completed & Archived. When new ideas emerge, add them.
> **Task markers:** `[ ]` incomplete | `[~]` in-progress | `[!]` blocked | `[x]` complete | `[-]` cancelled

**Last updated:** 2026-05-23 | **Status:** Post-Sprint-12. Audit complete (FINAL_AUDIT_REPORT.md). Smoke tests 64/64. 5 artifacts deployed. K1 live. Buffer autonomous through Jun 11. **Branch:** feature/audit-export-conversation

---

## Priority Queue — Active Items

### P0 — Critical / Blocking

| # | Item | Description | Effort | Depends On |
|:--|:-----|:------------|:-------|:-----------|
| [~] | **S9.1 Git branch hygiene** | Switch all 5 artifact repos + QWAV to feature/ branches. GitHub Pages requires main/master for deployment — reconcile. | 0.5h | — |
| [!] | **S8.3 Buffer campaign** | Complete A4, A5, K1 social posts. Buffer session expired — needs reconnection. | 0.5h | Buffer re-auth |

### P1 — High Priority

| # | Item | Description | Effort | Depends On |
|:--|:-----|:------------|:-------|:-----------|
| [ ] | **Sprint 13 planning** | Plan next sprint: backlog triage, remaining audit recommendations, test suite refactoring. | 0.5h | — |
| [ ] | **QNFO org README deploy** | Content written (`briefings/QNFO-org-README.md`). Push to `QNFO/.github` repo as `profile/README.md`. | 0.25h | GitHub push |
| [ ] | **qwav.tech domain site** | K1 hub is live but at `qnfo.github.io/QWAV/`. Build or redirect `qwav.tech` → K1. | 0.5h | Domain DNS |
| [ ] | **Test suite refactoring** | Convert `test_all_artifacts.py` to pytest-style with individual `def test_*` functions. From audit recommendation #2. | 2-3h | — |
| [ ] | **JS error detection in tests** | Add browser-console error capture to smoke tests. From audit recommendation #3. | 1-2h | YoBrowser/CDP |

### P2 — Medium Priority

| # | Item | Description | Effort | Depends On |
|:--|:-----|:------------|:-------|:-----------|
| [ ] | **SBIR Phase I** | Federal small business grant. May require US entity formation. Research eligibility and requirements. | 2-3h | Entity status |
| [ ] | **FQXi Essay Contest** | Check for open FQXi essay contest. "Continuous manifold is the wrong assumption" is their kind of thesis. | 0.5h + writing | Contest open |
| [ ] | **Curate Prior Work catalog** | Select 20-30 most QWAV-relevant publications from 673-release corpus. One-line relevance statements for qwav.tech. | 1-2h | qwav.tech live |
| [ ] | **Smoke test maintenance** | Schedule periodic smoke test runs (weekly). Monitor for regressions as artifacts evolve. | 0.25h/run | — |
| [ ] | **BACKLOG.md P-number cleanup** | Renumber items sequentially. Remove gaps/duplicates from legacy P1-P60 era. | 0.25h | — |

### P3 — Nice to Have / Deferred

| # | Item | Description | Effort | Depends On |
|:--|:-----|:------------|:-------|:-----------|
| [ ] | **Entity formation assessment** | Requires exogenous info: existing corporate entities (Empowering Change 501c3, Data For Good LLC, planned Netherlands incorporation). Cannot execute autonomously. | 0.5h | Founder input |
| [ ] | **ResearchGate cross-posting verify** | Documented in `briefings/zenodo-crosslink-audit.md`. ResearchGate blocks automated access — founder must verify manually. | 0.25h | Founder login |
| [ ] | **Domain redirects** | qwav.org confirmed registered. QNFO.org needs founder DNS verification. | 0.25h | Founder DNS |
| [ ] | **LinkedIn profile alignment** | Bio text ready. Update LinkedIn About + add Zenodo link. | 0.5h | Founder login |
| [ ] | **Social bio Zenodo links** | Copy-paste text ready for Mastodon, Bluesky, Twitter bios. | 0.1h | Founder login |
| [ ] | **IP: High-Temp filing decision** | Already DECIDED (DO NOT FILE, 2026-05-19). Revisit if funding arrives. | 0.5h | Funding event |
| [ ] | **P11 Formal verification** | CLOSED — no external dependencies. Lean 4 verification of ultrametric QEC threshold requires collaborators. Revisit if collaborator found. | — | Collaborator |

---

## Spinoff Projects (Delegated to Projects Agent)

Projects scaffolded with handoff briefings. Ready for execution when capacity allows.

| # | Project | Directory | Status |
|:--|:--------|:----------|:-------|
| P44 | Ultrametric Game of Life | `projects/ultrametric-game-of-life/` | Handoff ready — 9 tasks |
| P49 | Hierarchy as Ultrametricity | `projects/Hierarchy as Ultrametricity/` | Handoff ready — 10 tasks |

---

## Application Tracker

| # | Application | Organization | Type | Status | Submitted | Notes |
|:--|:------------|:-------------|:-----|:-------|:----------|:------|
| 1 | VSD | Deep Science Ventures College | Venture-creation PhD | Rejected | May 2026 | Bans LLM use, prohibits existing IP |
| 2 | FRO Abstract | Convergent Research | Focused Research Org ($20-50M) | Pending | May 2026 | Abstract stage only |
| 3 | EWOR Fellowship | EWOR | Fellowship for outlier founders | Pending | May 2026 | Written application |
| 4 | Emergent Ventures | Mercatus Center | Moonshot grant | Pending | May 2026 | Tyler Cowen's program |
| 5 | Harmonic.ai | Harmonic | Startup database | Pending | May 2026 | VC discovery platform |
| 6 | LinkedIn Co-Founder | Stealth Startup | Co-founder position | Pending | May 2026 | Physics-informed AI SaaS. San Jose. Conflicts with D4+D6. |

---

## Completed & Archived

### Program Milestones (Sprint 1-12)

| Sprint | Date | Description |
|:-------|:-----|:------------|
| S1-S7 | May 11-15 | ultrametric_v2: 7 sprints, 28 tasks, 26 files, 260K+ MC trials |
| S8 | May 16 | Buffer campaign setup, K1 verification |
| S9 | May 17-18 | Strategic harmonization, cross-project sync, VENUE-REGISTRY |
| S10 | May 19 | Repository curation, domain column, credential doc v2 |
| S11 | May 20-22 | Artifact spinoff (A1-A5), Three.js bundling, error counter fix |
| S12 | May 23 | Test suite (164/164), interactive enhancements, close-out |

### Publications

| P# | Title | DOI | Date |
|:---|:------|:----|:-----|
| P4 | Computational Validation of Ultrametric Error Confinement | 10.5281/zenodo.20134944 | 2026-05-12 |
| P24 | Ultrametric Quantum Computing Foundations | 10.5281/zenodo.20154557 | 2026-05-15 |
| P26 | Symmetric Extension of Ultrametric Error Confinement | 10.5281/zenodo.20208437 | 2026-05-16 |
| P27 | Cross-Domain Synthesis: Ultrametric Geometry as Common Structure | 10.5281/zenodo.20265907 | 2026-05-17 |
| P31 | ultrametric_v2 Companion Paper | 10.5281/zenodo.20208437 | 2026-05-16 |
| P6 | Q-PNA v2.0 Research Specification | 10.5281/zenodo.20287742 | 2026-05-17 |

### Artifact Demos

| Artifact | URL | Status |
|:---------|:----|:-------|
| A1 Error Confinement | https://qnfo.github.io/ultrametric-error-confinement/ | Deployed |
| A2 Q-PNA Architecture | https://qnfo.github.io/Q-PNA/ | Deployed |
| A3 Convergence Explorer | https://qnfo.github.io/ultrametric-convergence/ | Deployed |
| A4 Tree Distance | https://qnfo.github.io/tree-distance/ | Deployed |
| A5 Hardware Pathway | https://qnfo.github.io/hardware-pathway/ | Deployed |
| K1 Hub | https://qnfo.github.io/QWAV/ | Deployed |

### Strategy Documents (Completed)

| P# | Document | File |
|:---|:---------|:-----|
| P7 | Patent timeline | `strategy/0.2.md` |
| P8 | Competitive landscape | `strategy/0.5.md` |
| P16 | MIT implosion carving | `strategy/0.7.md` |
| P33 | Credential doc refresh | `Ultrametric Quantum Computing Foundations.md` |
| P34 | $q$-ary scatter talking point | `strategy/0.4.md` |
| P37 | Benchmarking methodology | `strategy/0.5.1.md` |
| P39 | Tree Distance cross-reference | Various |
| P41 | Assumption-to-physical mapping | `strategy/0.6.md` |
| P42 | Heydeman et al. analysis | `strategy/0.5.2.md` |
| P43 | Boettcher analysis | `strategy/0.5.2.md` |
| P58 | QNFO org README | `briefings/QNFO-org-README.md` |
| P59 | Inbound email template | `briefings/inbound-email-template.md` |
| P60 | Zenodo cross-link audit | `briefings/zenodo-crosslink-audit.md` |

### Cancelled / Superseded

| P# | Item | Reason |
|:---|:-----|:-------|
| P10 | Cold outreach to labs | Superseded by P32 |
| P11 | Formal verification | Closed — requires external collaborators |
| P12 | High-Temp filing | Decided: DO NOT FILE (2026-05-19) |
| P13,P14,P15 | IP drafting/review/verification | Superseded by strategy/0.1.md and 0.2.md |
| P17-P22 | All email outreaches | Cancelled — email not aligned with QWAV strategy |
| P23,P35 | arXiv submission | Cancelled — requires endorsement. Zenodo is primary |
| P32 | Neutral atom lab outreach | Cancelled — same rationale as P17-P22 |
| P36 | Cophenetic distance bridge | Integrated into P27 |
| P38 | Open-source codebase | Same as P28 (completed) |
| P40 | Cross-domain synthesis | Superseded by P27 |

---

*End of backlog. Items are prioritized top-to-bottom within each tier. Work from P0 → P1 → P2 → P3.*
