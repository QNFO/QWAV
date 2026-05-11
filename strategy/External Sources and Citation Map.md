# EXTERNAL SOURCES & CITATION MAP

**Purpose:** Directly answers "where does this come from?" Every claim in the library is traceable to the definitive release document or the founder's published corpus. This file maps key claims to their sources.

---

## Primary Source

| Source | Location | Description |
|:-------|:---------|:------------|
| **Ultrametric Quantum Computation — An MVP Program for Passive Geometric Fault Tolerance** | `Obsidian/releases/2026/05/` (external research releases) | Definitive UQC architecture document. 46,042 characters, 57 numbered citations, formal mathematical definitions, 6 specific testable predictions, commercialization roadmap. **This is the authoritative technical reference for all library claims.** |

## Secondary Sources

| Source | Description |
|:-------|:------------|
| QWAV Technical Series (50+ documents) | Full UQC architecture series v0.1–v1.0 on Zenodo and ResearchGate |
| The Thermodynamic Imperative | Quantitative analysis of the 20,000× cooling gap |
| Q-PNA Framework | Quantum-Native p-Adic Neural Networks documentation |
| Syntactic Token Calculus | Variable-free physics model for auditable AI |
| 300+ publications | Full open-access corpus on Zenodo, ResearchGate, SSRN |

---

## Citation Map: Key Claims → Source

| Claim | Source | Citation(s) |
|:------|:-------|:------------|
| 20,000× cooling gap ($50\ \mu\text{W}$ at mK vs. $1\ \text{W}$ at $4\ \text{K}$) | UQC Release §2.1; Thermodynamic Imperative | [7], [31] |
| Strong triangle inequality enables passive fault tolerance | UQC Release §6.2–6.3 | [1], [5], [14] |
| Energy barriers scale as $E \propto q^d$ with tree depth | UQC Release §6.4 | [14], [22] |
| Thermal stability predicted at $\Gamma \approx 80$ | UQC Release §4.4, Table 1 | [28], [31] |
| $45^\circ$ twisted Bi-2212 as physical substrate | UQC Release §2.4 | [31], [42] |
| Q-PNA: quantum walks on Bruhat–Tits trees for ballistic speedup | UQC Release §3.3 | [8], [15] |
| Syntactic Token Calculus for glass-box AI | UQC Release §3.4 | [11], [18] |
| Surface code overhead ~1,000:1 physical:logical | UQC Release §2.2 | [19], [25], [44] |
| NV centers as validation platform | UQC Release §4.1 | [50] |
| Neutral atoms as validation platform | UQC Release §4.1 | [51] |
| Trapped ions as validation platform | UQC Release §4.1 | [53] |

---

## Citation Categories (from the 57 citations in the UQC Release)

### Mathematical Foundations (Citations 1–18)
$p$-adic numbers, ultrametric geometry, Bruhat–Tits trees, strong triangle inequality, non-Archimedean analysis. Key references: [1] (p-adic analysis), [5] (ultrametric calculus), [14] (Bruhat–Tits buildings).

### Quantum Error Correction (Citations 19–35)
Surface codes, bosonic codes, topological codes, active QEC overhead, thermodynamic limits. Key references: [19] (surface code overview), [25] (QEC resource estimates), [31] (cryogenic limits).

### Quantum Hardware Platforms (Citations 36–45)
NV centers, neutral atoms, trapped ions, superconducting qubits, twisted superconductors. Key references: [42] (Bi-2212), [44] (superconducting qubit scaling).

### AI & Neural Networks (Citations 46–52)
Explainable AI, neural network interpretability, quantum machine learning. Key references: [46] (XAI survey), [48] (physics-informed neural networks).

### Computational Validation (Tier 0) — NOT YET BUILT
Software simulations of Bruhat-Tits tree circuits demonstrating error confinement, energy barrier scaling, quantum walk speedup, and token calculus confluence. **This is the current priority (SPRINT.md P1).** See `strategy/Experimental Validation Roadmap.md` for detailed experiment specifications.

---

## Source Strength Matrix

| Claim Domain | Source Quality | Verification Status |
|:-------------|:--------------|:--------------------|
| Mathematical foundations ($p$-adic geometry) | HIGH — well-established mathematics | Open-access. Verifiable by anyone with mathematical training. |
| Thermodynamic wall analysis | HIGH — quantitative physics; experimentally measurable | Consistent with published cryogenic limits. Open-access. |
| Passive fault tolerance mechanism | MEDIUM — mathematically derived; computationally unvalidated | **Awaiting computational validation (Tier 0)** |
| 4-Kelvin thermal stability ($\Gamma \approx 80$) | MEDIUM — theoretically predicted; computationally unvalidated | **Awaiting Tier 0 energy barrier simulation** |
| Q-PNA ballistic speedup | MEDIUM — quantum walk speedups are mathematically proven; tree-specific claims unvalidated | Partially verified (quantum walk theory); tree implementation **awaiting computational validation** |
| UQC qubit overhead (~10:1–100:1) | LOW-MEDIUM — theoretically estimated; no simulation or experimental data | **Awaiting computational validation** |
| Tier 0 computational simulations | NOT YET BUILT — specified but not implemented | **P1 in SPRINT.md — zero external dependencies** |

---

## Priority Reading for Due Diligence

If someone wants to verify the claims themselves, direct them to:

1. **UQC Release** — Start here. Read the Executive Summary, §1–4 (core technical claims), and §4.4 (testable predictions).
2. **The Thermodynamic Imperative** — For the quantitative cooling gap analysis.
3. **UQC Architecture Series (v0.1–v1.0)** — For the full 50+ document technical development.
4. **Q-PNA Framework** — For the AI/glass-box side.

All documents are open-access on Zenodo and ResearchGate. No paywalls. No institutional access required.

---

*Citation Map v2.0 — Updated for computational validation strategy (May 2026). All citations reference the Ultrametric Quantum Computation release document. Full citation list with URLs available in the release document's References section. Update as validation data and new publications become available.*
