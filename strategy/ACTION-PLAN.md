# Action Plan — From Library to Reality

> **Consolidates:** `NEXT STEPS - From Library to Reality.md` + `Experimental Validation Roadmap - Ultrametric Quantum Computing.md` + `MANUFACTURING-BLUEPRINT.md` (May 2026)
> **Archived:** 2026-05-26 → `sessions/2026/05/strategy-archive/`
> **Note:** `An Introvert's Deep-Tech Startup Path.md` remains standalone (personal narrative, distinct genre)
> **Status:** Canonical action plan | **Updated:** 2026-05-26 (manufacturing blueprint integration)

---

## Phase 0: Architecture Publication (NOW — May 2026)
*"QWAV does not manufacture. QWAV designs architectures that others manufacture."*
- [ ] Publish tree topology mask designs as GDSII specification documents
- [ ] Release open-source tree code transpiler v0.1 (Python, Qiskit-compatible)
- [ ] Publish decoding ASIC specification (RTL reference)
- [ ] Create "Tree Topology Implementation Guide" per platform (neutral atom, superconducting, spin, photonic, trapped ion)
- [ ] Publish `MANUFACTURING-BLUEPRINT.md` with Zenodo DOI (this document)
- [ ] Update `IP-STRATEGY.md` with specific patentable manufacturing assets

## Phase 1: Validation (Current)
- [ ] Tier 1 paper — depolarizing + dephasing simulation results
- [ ] Tier 1.5 paper — hardware-parameterized decoherence validation
- [ ] Outreach to 3-5 neutral atom labs for experimental feedback (see `lab-outreach-template.md`)
- [ ] Q-PNA v2.0 — tree embedding integration completed

## Phase 2: Experimental
- [ ] Tier 2 — multi-platform simulation (100+ qubit)
- [ ] Independent validation by external researcher
- [ ] Conference presentation (target: APS March Meeting, QEC, or FQXi)
- [ ] Preprint on arXiv

## Phase 2.5: Cloud Validation (Piggyback — Software Only)
*"Run tree codes on EXISTING cloud hardware with a SOFTWARE change."*
- [ ] Pathway A: Tree-encoded circuits on PASQAL/QuEra neutral atom hardware (AWS Braket) — ~$10-50K
- [ ] Pathway E: Tree-encoded circuits on IonQ/Quantinuum trapped ion hardware — ~$10-50K
- [ ] Pathway B (prep): Tree code transpiler pass for IBM Qiskit superconducting backends
- [ ] Publish multi-platform benchmark: tree code vs. unencoded baseline

## Phase 3: Commercialization (Fabless IP Model)
- [ ] Tier 3 — hardware collaboration with neutral atom lab
- [ ] IP strategy executed (see IP-STRATEGY.md)
- [ ] Grant applications: SBIR Phase I, FQXi, national quantum programs
- [ ] Industry partnerships for hardware access

## Phase 3.5: Foundry Engagement (Piggyback — Fab)
*"Submit tree-topology mask designs to EXISTING foundries."*
- [ ] Submit tree-topology GDSII masks for silicon spin MPW run (TSMC/GF/IMEC) — ~$50-500K
- [ ] Submit tree-topology waveguide masks for photonic MPW run (AIM Photonics/LioniX) — ~$20-100K
- [ ] File provisional patents on tree topology implementations per platform
- [ ] Engage neutral atom hardware companies for native tree-topology chip development

## Phase 4: Commercial Licensing (2028+)
*"QWAV = ARM Holdings for quantum computing."*
- [ ] First tree-topology logical qubit demonstration (on any platform)
- [ ] Execute IP licensing agreements with hardware partners (royalty-bearing or flat-fee)
- [ ] Enterprise support offering for tree code transpiler
- [ ] Revenue target: $1-10M by 2030

## Validation Roadmap Detail (from Experimental Validation Roadmap)

### Simulation Tiers
| Tier | Description | Qubits | Status |
|:-----|:------------|:-------|:-------|
| 0 | Classical simulation | N/A | ✅ Published |
| 1 | Depolarizing + dephasing | 8-40 | ⬜ Draft |
| 1.5 | Hardware-parameterized | 8-40 | ⬜ Research |
| 2 | Multi-platform comparison | 100+ | ⬜ Planned |
| 3 | Physical neutral atom | TBD | 🔴 Blocked |

### Key Metrics
- Logical error rate reduction: target >10x over uncorrected baseline
- Temperature scaling: 4K → room temperature feasibility analysis
- Hardware compatibility: Rydberg blockade gate fidelity requirements

## See Also
- Full original: `sessions/2026/05/strategy-archive/NEXT STEPS - From Library to Reality.md` (8KB)
- Full original: `sessions/2026/05/strategy-archive/Experimental Validation Roadmap - Ultrametric Quantum Computing.md` (13KB)
- Related: `An Introvert's Deep-Tech Startup Path.md` (personal narrative)
- Related: `briefings/outreach/` (lab outreach templates)
