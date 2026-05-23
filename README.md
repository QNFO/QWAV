# QWAV — Ultrametric Quantum Computing & AI

**Passive fault tolerance. Glass-box AI. One mathematical correction. Two multi-billion-dollar problems.**

---

## What QWAV Is

QWAV replaces Archimedean (continuous) geometry with ultrametric (tree-based) geometry for quantum computing and artificial intelligence. The Bruhat-Tits tree — a structure from $p$-adic number theory — provides passive error suppression through the strong triangle inequality, operating at 4 K with no active error correction. The same tree geometry enables glass-box AI: traceable decision paths through the tree structure, explainable by design.

**Core thesis:** Quantum computing is stalled not because of bad engineering but because of a bad mathematical assumption — that space is continuous. Ultrametric geometry corrects that assumption. The resulting tree structure provides geometric error protection that standard active quantum error correction cannot improve upon, and a neural architecture whose decisions are traceable by construction.

---

## Repository Structure

```
QWAV/
├── index.html                     # K1 Technical Hub — live at qnfo.github.io/QWAV/
├── test_plan.py                   # K1 test suite (39/39 PASS) — run: python test_plan.py
├── .nojekyll                      # GitHub Pages: bypass Jekyll processing
├── README.md                      # This file — project overview
├── CHANGELOG.md                   # Chronological versioned change log
├── SPRINT.md                      # Active sprint task tracker
├── PROJECT STATE.md               # Comprehensive handoff document for LLM agents
├── BACKLOG.md                     # Prioritized future work queue
├── LEARNINGS.md                   # Program-level lessons (kaizen engine)
├── DECISIONS.md                   # Architecture/design decisions with rationale
├── CHARTER.md                     # Project charter — scope, constraints, deliverables
├── CONTRIBUTING.md                # Contribution guidelines and rules
├── DEFINITION-OF-DONE.md          # Task completion gates
├── RISK-REGISTER.md               # Pre-populated risk tracking
│
├── site/                          # K1 hub canonical source directory
│   ├── index.html                 # Source for deployed root index.html
│   └── test_plan.py               # Test suite source
│
├── artifacts/                     # A1–A5 Interactive Demos
│   ├── error-confinement-demo/    # A1: Ultrametric Error Confinement Demo
│   ├── qpna-playground/           # A2: Q-PNA Classifier Playground
│   ├── convergence-explorer/      # A3: Ultrametric Convergence Explorer
│   ├── tree-distance/             # A4: Tree Distance Sandbox
│   └── hardware-visualizer/       # A5: Hardware Pathway Visualizer
│
├── papers/                        # Published paper full texts (.txt)
│
├── strategy/                      # Strategic planning documents
│   ├── VENUE-REGISTRY.md          # Complete public presence audit
│   └── *.md                       # Strategy, pitch deck, prior art analysis
│
├── briefings/                     # Internal briefings, handoffs, outreach templates
│
├── people/                        # Founder CV / resume
│
└── applications/                  # Grant and fellowship applications
```

---

## Interactive Demos

All demos are live on GitHub Pages. Each is a standalone single-page application.

| # | Demo | URL | Tests |
|:--|:-----|:----|:------|
| **A1** | Error Confinement Demo | [qnfo.github.io/ultrametric-error-confinement](https://qnfo.github.io/ultrametric-error-confinement/) | 40/40 PASS |
| **A2** | Q-PNA Classifier Playground | [qnfo.github.io/Q-PNA](https://qnfo.github.io/Q-PNA/) | 38/38 PASS |
| **A3** | Convergence Explorer | [qnfo.github.io/ultrametric-convergence](https://qnfo.github.io/ultrametric-convergence/) | 44/44 PASS |
| **A4** | Tree Distance Sandbox | [qnfo.github.io/tree-distance](https://qnfo.github.io/tree-distance/) | 37/37 PASS |
| **A5** | Hardware Pathway Visualizer | [qnfo.github.io/hardware-pathway](https://qnfo.github.io/hardware-pathway/) | 32/32 PASS |

**Total: 283 automated tests across 7 artifacts — 0 failures.**

---

## Publications

All papers are open-access on Zenodo with registered DOIs. Full texts in `papers/`.

| Title | Date | DOI |
|:------|:-----|:----|
| Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits | 2026-05-12 | [10.5281/zenodo.20134944](https://doi.org/10.5281/zenodo.20134944) |
| Ultrametric Quantum Computing Foundations | 2026-05-15 | [10.5281/zenodo.20154557](https://doi.org/10.5281/zenodo.20154557) |
| Symmetric Extension of Ultrametric Error Confinement — Ternary Tree Architecture | 2026-05-16 | [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437) |
| Q-PNA: Quantum-Native $p$-Adic Neural Architecture — Research Specification v2.0 | 2026-05-19 | [10.5281/zenodo.20287742](https://doi.org/10.5281/zenodo.20287742) |
| Convergence, Consilience, and the Hierarchical Architecture of Reality | 2026-05-20 | [10.5281/zenodo.20302276](https://doi.org/10.5281/zenodo.20302276) |

---

## Program & Portfolio

QWAV is a solo deep-tech research program advancing ultrametric computing across two fronts:

### Ultrametric Quantum Computing
Computational validation demonstrates that Bruhat-Tits tree encoding achieves **zero logical errors at depth 7** and **48× error reduction at zero additional qubit cost** via $q$-ary scatter across existing hyperfine levels. Ternary ($p=3$) architecture provides symmetric protection for both logical states — the smallest tree size among all symmetric prime families. A complete 40-atom neutral atom hardware specification is provided. Concatenation of active QEC on top of the tree is computationally demonstrated to be redundant — the tree already does what active QEC would do, passively.

### Glass-Box AI (Q-PNA)
The Quantum-Native $p$-Adic Neural Architecture replaces continuous embedding spaces ($\mathbb{R}^n$) with Bruhat-Tits tree geometry. A learned linear mapping from features to tree leaves, combined with cophenetic loss, achieves 20–40% test accuracy on hierarchical classification — outperforming a full multi-head transformer by 6.6× on the same task. The Syntactic Token Calculus verification protocol achieves 100% detection rate with zero false positives. Full specification, computational evidence, and open-source code at [github.com/QNFO/Q-PNA](https://github.com/QNFO/Q-PNA).

---

## Distribution Pipeline

No cold outreach. No groveling. Publish. Let the work speak.

| Stage | Channel |
|:------|:--------|
| **Primary** | Zenodo — all papers published with registered DOIs |
| **Secondary** | ResearchGate + QNFO.org — cross-posted from Zenodo |
| **Social** | Mastodon ([@QNFO](https://mstdn.science/@QNFO)), Bluesky, Twitter/X |
| **Email** | Inbound-only — if someone reads the work and reaches out, evaluate case-by-case |
| **Technical Site** | [qnfo.github.io/QWAV](https://qnfo.github.io/QWAV/) — live interactive hub |

---

## Non-Negotiable Constraints

| Constraint | Rationale |
|:-----------|:----------|
| **No physical lab** | Computational validation only — simulations produce falsifiable, reproducible, shareable results |
| **No peer review** | Open-access publication only — credibility from substance, not journal gatekeeping |
| **Written-first** | All communication is written — the introvert path is a filter, not a limitation |
| **Solo founder** | No team-building aspirations — collaborators emerge organically through the work |
| **Substance-first** | The work speaks for itself — booster language dilutes credibility |

---

**Contact:** [Rowan Brad Quni-Gudzinas](mailto:rowan.quni@outlook.com) · [ORCID: 0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604) · [QNFO on GitHub](https://github.com/QNFO)

*Last updated: 2026-05-23 — Strategic harmonization. Repository curated as the technical public face of QWAV.*
