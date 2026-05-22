---
template: PROJECT-CHARTER
version: "1.0"
---

# QWAV — Project Charter

**Date:** 2026-05-22
**Status:** Active
**Program:** QWAV

## Scope

### In Scope

- Computational validation of ultrametric ($p$-adic, tree-based) quantum computing architectures
- Specification and validation of glass-box AI architectures (Q-PNA) on Bruhat-Tits trees
- Open-access publication of all results on Zenodo with registered DOIs
- Interactive artifact development for every publication (D13 compliance)
- Spinoff project initiation and handoff to Projects agent
- Social media distribution via Buffer (Mastodon, Bluesky, Twitter/X)
- Strategy documentation and maintenance (7 core docs + phase docs)
- Application submission to merit-based funding programs
- Cross-project coordination with sibling projects (ultrametric_v2, Tree Distance Cophenetic, etc.)
- Maintenance of the 673-release Obsidian corpus as intellectual genealogy

### Out of Scope

- Physical laboratory experiments (no hardware access — D1)
- Peer-reviewed journal submissions (D2 — open-access only)
- Live pitching, networking, or conference attendance (D3 — written-only)
- Team-building or co-founder recruitment (D4 — solo founder)
- Credential-based evaluation pathways (D5 — substance-first)
- External collaborator dependencies (D12 — single LLM thread completable)
- Paper-only publications without interactive companion (D13)
- Cold outreach emails (inbound-only engagement)
- Patent filings without funded conversion plan
- Entity formation without specific funding trigger
- VC/accelerator path

## Success Criteria

| # | Criterion | How Measured |
|:--|:----------|:-------------|
| 1 | 5 interactive artifacts deployed on GitHub Pages | Each artifact live at QNFO.github.io/, verified via browser |
| 2 | qwav.tech public site live with thesis, evidence, and artifact directory | Site deployed, all links functional, geometric aesthetic |
| 3 | Publication cadence: 1 new Zenodo publication every 2-4 weeks | Zenodo community page shows regular activity |
| 4 | At least one substantive inbound contact from published work | Email or message from qualified researcher who engaged with artifacts |
| 5 | At least one application acceptance from merit-based programs | Acceptance letter or funding award from submitted application |
| 6 | Evidence Deck grows monthly with new computational results | Monthly commit to Evidence Deck with verified new data |
| 7 | All 7 core documentation files maintained and committed per session | git log confirms documentation commits per session |

## Constraints

| Constraint | Value | Why |
|:-----------|:------|:----|
| Human attention budget | Solo founder — all decisions flow through one person | Force-Multiplier model: human time is the scarce resource |
| Session limit | 1-2 sessions/day, ~30 sessions/month max | Sustainable pace for solo founder with LLM augmentation |
| Deliverable deadline | None — cadence-based, not deadline-based | Quality and sustainability over artificial urgency |
| Domain boundaries | No wet lab work, no experimental physics, no hardware fabrication | Computational physics and AI specification only |
| Publication model | Open-access Zenodo with DOIs only | No paywalls, no peer review gatekeeping |
| Distribution model | Interactive artifacts > papers. Inbound-only engagement. | Evidence shows papers aren't read; artifacts engage |
| Git model | Feature branches only. Never commit to main. | CPL L1, L20: prevents cross-contamination |

## Dependencies

| Depends On | Type | Status |
|:-----------|:-----|:-------|
| Projects agent (DeepChat) | Resource — executes spinoff computational work | Active |
| Buffer API | Resource — social media distribution | Active |
| Zenodo API / manual upload | Resource — DOI registration and publication | Active |
| GitHub (QNFO org) | Resource — code hosting, artifact deployment | Active |
| DeepSeek/DeepChat LLM | Resource — strategy, writing, analysis | Active |
| Domain registrar (qwav.tech, qwav.org) | Decision — DNS configuration for live site | Requires founder action |

## Deliverables

| # | Deliverable | Type | DoD Reference |
|:--|:------------|:-----|:--------------|
| 1 | A1: Error Confinement Live Demo (interactive Bruhat-Tits tree) | Web App | DEFINITION-OF-DONE.md §WEB APP TASK |
| 2 | A2: Q-PNA Classifier Playground | Web App | DEFINITION-OF-DONE.md §WEB APP TASK |
| 3 | A3: Ultrametric Convergence Explorer | Web App | DEFINITION-OF-DONE.md §WEB APP TASK |
| 4 | A4: Tree Distance Sandbox | Web App | DEFINITION-OF-DONE.md §WEB APP TASK |
| 5 | A5: Hardware Pathway Visualizer | Web App | DEFINITION-OF-DONE.md §WEB APP TASK |
| 6 | K1: qwav.tech public site | Web App | DEFINITION-OF-DONE.md §WEB APP TASK |
| 7 | K2: Intellectual Genealogy (30 publications) | Document | DEFINITION-OF-DONE.md §DOCUMENT TASK |
| 8 | K3: Evidence Deck (scrollable results) | Web App | DEFINITION-OF-DONE.md §WEB APP TASK |
| 9 | K4: Public Research Roadmap | Document | DEFINITION-OF-DONE.md §DOCUMENT TASK |
| 10 | Monthly evidence updates | Analysis | DEFINITION-OF-DONE.md §ANALYSIS TASK |

## Prior Work (from §0.1.4 Discovery)

| Source | Relevance | Action |
|:-------|:----------|:-------|
| 673 releases in Obsidian/releases/ (2024-2026) | Intellectual genealogy — the raw material from which QWAV thesis was refined | Curate top 30 as K2 |
| ultrametric_v2 project (7 sprints, 260K+ MC trials) | Computational validation engine — all Tier 0/1 evidence | Cite DOIs, deploy code as interactive artifact |
| Tree Distance Cophenetic (DOI: 10.5281/zenodo.20213043) | Triadic rigidity theorem, resolution-dependence bridge | Deploy as A4 interactive sandbox |
| Can Math Prove Physics (DOI: 10.5281/zenodo.20266032) | Epistemological foundation for assumptions audit | Cite in evidence deck |
| CROSS-PROJECT-LEARNINGS.md (L1-L40) | 40 lessons from 11 archived projects | Read at session start; apply relevant lessons |
| 18 expired provisional patents | Cautionary tale — $6K spent, 0 conversions | Lesson captured in D12, L4 |

## Human Sign-Off

- [ ] Scope reviewed and approved
- [ ] Success criteria are measurable and realistic
- [ ] Constraints are accurate
- [ ] Prior work acknowledged

---
*Generated from PROJECT-CHARTER-TEMPLATE.md v1.0*
