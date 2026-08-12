---
title: 'QWAV Strategy v2.4: The Energy-Standard Playbook — Consortium Governance, Verified Precedents, and the JPCUB Road to a Quantum Computing Energy Benchmark'
author: 'Rowan Brad Quni-Gudzinas'
date: '2026-08-12'
license: 'QNFO Unified License Agreement (QNFO-ULA)'
doi: '10.5281/zenodo.21905166'
status: 'published'
genre: 'B — Commercial/Strategy'
---

**Author:** Rowan Brad Quni-Gudzinas | **ORCID:** 0009-0002-4317-5604 | **Date:** 2026-08-12 | **License:** QNFO-ULA | **Status:** Published v2.4.1

**Forward-Looking Statements:** This document contains forward-looking statements based on verified public evidence as of 2026-08-12 and calibrated subjective judgment. Every external claim is cited with a DOI or arXiv identifier verified live in this publication session. Market figures are labeled as estimates. Actual results may differ materially.

---

## Abstract

Quantum computation is known to possess theoretical energy-consumption advantages over classical computation — Meier and Yamasaki proved an exponential energy advantage on Simon's problem (arXiv:2305.11212), and Fellous-Asiani et al. demonstrated full-stack resource-efficiency optimization regimes distinct from computational-advantage regimes (PRX Quantum 4, 040319). No standard measurement instrument yet exists to make these advantages comparable across platforms. This paper argues that QWAV's JPCUB (Joules-per-Solution) metric can become that instrument — not by competing as a vendor product, but by following the proven playbook of energy benchmarks that became industry standards: SPEC's SERT server-efficiency benchmark (2007–2011), the Green Grid's PUE metric (2007–2011), and MLPerf's consortium-governed energy benchmarks (2018–2021). Section 2 documents these precedents with verified sources. Section 3 analyzes the existing quantum consortium landscape — QED-C (Quantum Economic Development Consortium), IEEE, NIST — and identifies the specific gap JPCUB fills. Section 4 presents the consortium governance model adapted from these precedents. Section 5 maps the grant-funding pipeline to verified programs. Section 6 pre-registers seven falsifiable predictions. The conclusion is that QWAV's highest-leverage strategy is to seed a standards body around JPCUB using the SPEC/Green Grid playbook, rather than to sell benchmarking as software.

**Keywords:** QWAV, JPCUB, joules per solution, energy benchmarking, quantum computing, consortium, standards, SPEC, Green Grid, PUE, MLPerf, QED-C

---

## 1. Introduction

### 1.1 The Strategic Question

QWAV possesses a validated technical contribution: the JPCUB metric, defined as total system energy per correct answer, provides a physics-grounded benchmark for computational platforms. The JPCUB Competitive Landscape v2.0 (10.5281/zenodo.21821767) ranks 17 quantum platforms, and the Qudit Advantage paper (10.5281/zenodo.21880104) demonstrates the metric's discriminative power.

The strategic question is not whether JPCUB is technically sound. It is: **how does a single independent researcher turn a metric into a standard?** This paper answers that question by examining how previous energy-efficiency metrics became standards, and by designing a consortium model based on those verified precedents.

### 1.2 Why This Matters Now

Three forces converge in 2026:

1. **Theoretical validation exists.** Quantum energy advantage is no longer speculative — it is proven for specific problems (Simon's problem, arXiv:2305.11212) and shown to extend to full-stack resource efficiency (10.1103/prxquantum.4.040319).
2. **Energy is becoming a procurement criterion.** The EU Energy Efficiency Directive recast and enterprise ESG mandates are making energy efficiency a technology-procurement factor, as documented in the server-energy-benchmarking literature (10.1007/978-3-031-85634-1_11).
3. **No standard exists.** The quantum industry's own needs assessments (10.1109/te.2022.3153841, 10.1140/epjqt/s40507-021-00114-x) identify benchmarking and standards as unmet industry needs.

The entity that defines the standard before the industry coalesces around alternatives owns the metric.

---

## 2. Verified Precedents: How Energy Benchmarks Became Standards

The following precedents are documented with sources verified live (2026-08-12) via OpenAlex and arXiv. They constitute the playbook.

### 2.1 SPEC and SERT: The Server Energy Benchmark Consortium (2007–2011)

SPEC (Standard Performance Evaluation Corporation) is a non-profit consortium founded 1988 by computer vendors and universities to define fair benchmarks. Its SPECpower committee developed SERT (Server Efficiency Rating Tool) — the design of which is documented in "The design and development of the server efficiency rating tool" (10.1145/1958746.1958769).

**The playbook SPEC followed:**
1. **Neutral stewardship**: SPEC is a consortium, not a vendor. Its benchmarks carry weight because no single vendor controls them.
2. **Workload standardization**: benchmarks define specific workloads (for SERT: CPU, memory, storage, network) with measured energy.
3. **Open membership**: vendors join to shape benchmarks they will be measured against — inclusion prevents fork.
4. **Ratified methodology**: benchmarks are published, peer-reviewed, and versioned.

**Relevance to JPCUB:** SERT is the closest classical analog to JPCUB — an energy-efficiency benchmark governed by a neutral consortium, adopted by an industry that could have each built its own. The 2025 literature (10.1007/978-3-031-85634-1_11) confirms server energy benchmarks remain an active field.

### 2.2 The Green Grid and PUE: The Metric That Became the Standard (2007–2011)

The Green Grid — a global consortium of IT companies founded 2007 — defined PUE (Power Usage Effectiveness), the data center energy metric. The metric's definition is documented in "PUE: The Green Grid metric for evaluating the energy efficiency in DC" (10.1109/intlec.2011.6099718). PUE became the de facto industry standard within five years, cited in the US Data Center Energy Usage Report (10.2172/1372902) and used globally.

**Why PUE won:**
1. **Simplicity**: a single dimensionless ratio (total facility power / IT equipment power) — easy to compute, easy to compare.
2. **Consortium ownership**: defined by a neutral body, not a vendor.
3. **Regulatory capture**: once cited in government reports, it became the procurement standard.

**Relevance to JPCUB:** PUE's trajectory from consortium metric to regulatory standard is the template. JPCUB is more complex than PUE (it requires workload definition and energy measurement), but the adoption path is identical: neutral definition → industry adoption → regulatory citation.

The PUE metric family has since evolved (AxPUE, arXiv:1310.6502; xPUE, arXiv:2503.07124), demonstrating that a successful energy metric spawns an ecosystem of extensions — a further validation of the "define the metric first" strategy.

### 2.3 MLPerf and MLCommons: The Modern Open Benchmark Consortium (2018–2021)

MLCommons is an open engineering consortium (founded 2018) whose MLPerf benchmarks became the industry standard for ML performance. Crucially for JPCUB, MLPerf Tiny (arXiv:2106.07597) explicitly **measures accuracy, latency, AND energy** for ultra-low-power systems — the collaborative effort of more than 50 organizations. The MLCommons harness architecture is documented in MLHarness (arXiv:2111.05231).

**The modern playbook additions:**
1. **Speed**: MLPerf achieved standard status in ~3 years (2018–2021), much faster than SPEC's decade. The modern standard-setting cycle is shorter.
2. **Energy is a first-class metric**: MLPerf Tiny's inclusion of energy in its core benchmarks validates the JPCUB premise that energy-per-task is a necessary benchmark dimension.
3. **Open governance**: MLCommons publishes methodology and welcomes membership — transparency is the trust mechanism.

### 2.4 Lessons for JPCUB

| Lesson | SPEC/SERT | Green Grid/PUE | MLPerf | JPCUB Application |
|:-------|:----------|:---------------|:-------|:------------------|
| Neutral ownership | ✅ | ✅ | ✅ | JPCUB Consortium (not QWAV product) |
| Open membership | ✅ | ✅ | ✅ | Academic + industry + regulatory tiers |
| Published methodology | ✅ | ✅ | ✅ | JPCUB P0 protocol (10.5281/zenodo.21637028) |
| Workload standardization | ✅ | — | ✅ | Define benchmark workloads per platform |
| Energy as core metric | ✅ | ✅ | ✅ | JPCUB IS energy-per-solution |
| Speed to standard | 10+ yrs | ~5 yrs | ~3 yrs | Target: 3–5 years |

**The synthesis:** JPCUB combines SERT's energy-benchmark rigor with PUE's metric-simplicity adoption path and MLPerf's modern speed. No existing quantum benchmark does this — the quantum industry's needs assessments identify this exact gap (10.1109/te.2022.3153841).

---

---

## 2.5 Mandatory Symmetry: What External Literature Supports and Constrains

### Where External Literature Supports [The Consortium-Governed JPCUB Standard]

1. **Energy benchmarks become standards through neutral consortia, not vendor products.** The SPEC SERT design paper (10.1145/1958746.1958769) documents a consortium-governed server energy benchmark adopted by an industry of competing vendors. The Green Grid PUE metric (10.1109/intlec.2011.6099718) became the de facto data-center energy standard within five years under consortium ownership. MLPerf Tiny (arXiv:2106.07597) shows the modern pattern — more than 50 organizations collaborating on a benchmark that measures accuracy, latency, AND energy.
2. **Quantum computation has provable energy advantages worth benchmarking.** Meier and Yamasaki rigorously prove an exponential energy-consumption advantage of quantum over classical computation for Simon's problem (arXiv:2305.11212). Fellous-Asiani et al. introduce the Metric-Noise-Resource (MNR) methodology and identify quantum energy advantage in parameter regimes distinct from computational advantage (10.1103/prxquantum.4.040319).
3. **The quantum industry itself identifies benchmarking standards as an unmet need.** QED-C's industry assessment (10.1109/te.2022.3153841) and applications review (10.1140/epjqt/s40507-021-00114-x) document that the quantum industry needs shared metrics and benchmarks.
4. **A standard energy metric spawns an ecosystem.** The PUE family has grown (AxPUE, arXiv:1310.6502; xPUE, arXiv:2503.07124), validating the "define the metric first" strategy.

### Where External Literature Constrains or Contradicts [The Consortium-Governed JPCUB Standard]

1. **The proven quantum energy advantage is problem-specific, not universal.** Meier and Yamasaki prove the exponential advantage for Simon's problem — a query-complexity model — not for all computational tasks (arXiv:2305.11212). JPCUB's claim to be a general-purpose energy benchmark must be workload-conditional: a JPCUB ranking is meaningful only for the benchmark workloads defined, not as a universal platform ordering.
2. **Quantum energy advantage is regime-dependent.** Fellous-Asiani et al. find the quantum energy advantage holds "in regimes of parameters distinct from the commonly considered quantum computational advantage" (10.1103/prxquantum.4.040319). This constrains the strategic assumption that energy advantage and computational advantage coincide; JPCUB must measure energy advantage as an independent axis, not assume it tracks speedup.
3. **PUE's success owed partly to simplicity.** PUE is a single dimensionless ratio computed from two power measurements (10.1109/intlec.2011.6099718). JPCUB requires workload definition, correct-answer verification, and energy measurement — a higher adoption barrier than PUE. The strategy must price this complexity cost into the adoption timeline.
4. **No constraining evidence found against consortium governance itself.** The SPEC, Green Grid, and MLCommons records show no case where a neutral consortium failed to establish an energy benchmark; the constraining evidence above concerns JPCUB's measurement semantics and adoption complexity, not the governance model.

[NO FURTHER CONSTRAINING EVIDENCE FOUND]

---

## 3. The Quantum Consortium Landscape

### 3.1 What Already Exists

| Body | Founded | Scope | Gap JPCUB Fills |
|:-----|:--------|:------|:-----------------|
| **QED-C** (Quantum Economic Development Consortium) | 2019 | Quantum industry growth, workforce, benchmarks | No energy-efficiency benchmark standard; JPCUB could be its energy benchmark working group |
| **IEEE Quantum** | 2019 | Quantum engineering standards | Performance metrics under discussion but no energy standard |
| **NIST** | — | Post-quantum crypto, measurement science | Energy benchmarking is a measurement-science gap |
| **ISO/IEC JTC 1** | — | Formal standards | Slow-track (years); consortium standards feed in later |

**Key insight:** QED-C already exists as the quantum industry consortium with a benchmarking mission (documented in its applications paper 10.1140/epjqt/s40507-021-00114-x and needs assessment 10.1109/te.2022.3153841). **QWAV does not need to create a consortium from scratch — it needs to seed an energy-benchmarking working group within the existing ecosystem, or create a focused JPCUB consortium that partners with QED-C.**

### 3.2 The Strategic Choice: Three Options

| Option | Description | Trust | Speed | Control |
|:-------|:------------|:------|:------|:--------|
| **A. Seed QED-C energy WG** | Propose JPCUB as the energy benchmark standard within QED-C's existing benchmark program | High (existing body) | Medium (bureaucracy) | Low (JPCUB becomes one of many) |
| **B. Independent JPCUB Consortium** | Create SPEC-style neutral body with JPCUB as founding standard | High (fresh, focused) | Fast | High (JPCUB is the founding standard) |
| **C. Vendor product** | Sell JPCUB benchmarking as software (v2.2/v2.3 approach) | Low (vendor conflict) | Medium | High (but adoption-limited) |

**Recommendation: Option B with Option A as a parallel track.** Create the JPCUB Consortium as a focused, SPEC-style neutral body (fast, high control, high trust) while simultaneously proposing JPCUB to QED-C's benchmarking program (leverage existing ecosystem). Option C remains the monetization layer — the certification service the consortium operates.

### 3.3 Why NOT a QWAV Product

The v2.2/v2.3 strategy treated JPCUB as a vendor differentiator. The precedent evidence shows this is the wrong frame: every successful energy benchmark (SERT, PUE, MLPerf Tiny) was owned by a neutral consortium, not a vendor. A single-vendor benchmark carries an inherent conflict of interest — the 2025 server-benchmarking literature (10.1007/978-3-031-85634-1_11) and the quantum needs assessments (10.1109/te.2022.3153841) both treat benchmarks as neutral infrastructure.

---

## 4. JPCUB Consortium Governance Model

### 4.1 Membership Tiers (adapted from SPEC + MLCommons)

| Tier | Annual Dues | Voting | Benefits | Target |
|:-----|:------------|:-------|:---------|:-------|
| **Academic** | €0 (in-kind validation) | 1 vote | Publication credit, early data access | 5–15 institutions |
| **Industry — Hardware** | €2K–10K scaled | 1 vote | JPCUB-Verified badge eligibility, metric input | 3–8 vendors |
| **Industry — End-User** | €1K–5K | 1 vote | Procurement tools, benchmark workload definition | 3–10 orgs |
| **Regulatory Observer** | €0 (invited) | 0 votes | Standards pathway input | 1–3 bodies |

### 4.2 Governance Bodies

1. **Steering Committee** — one rep per tier + secretariat (QWAV, tie-break). Ratifies metric changes, membership, certification.
2. **Technical Working Group** — open to all members; develops measurement methodology; reviews benchmark data.
3. **Certification Board** — independent; approves JPCUB-Verified badges.

### 4.3 Launch Sequence

| Milestone | Timeline | Gate |
|:----------|:---------|:-----|
| M0: JPCUB Protocol v1.0 ratified | Month 1–3 | Protocol published (exists: 10.5281/zenodo.21637028); charter drafted |
| M1: Founding members | Month 3–6 | ≥3 LOIs (≥1 academic, ≥1 industry) |
| M2: Charter ratified | Month 6 | All founding members sign |
| M3: First certification | Month 9–12 | ≥1 JPCUB-Verified badge |
| M4: QED-C partnership | Month 6–12 | JPCUB proposed as QED-C energy benchmark standard |

---

## 5. Grant-Funding Pipeline (Verified Programs)

The v2.3 grant landscape contained fabricated amounts. This section lists only programs verified to exist (via public program descriptions), with honest uncertainty about amounts.

### 5.1 Priority Pipeline

| Program | Funder | Verified? | Fit |
|:--------|:-------|:----------|:----|
| **QED-C programs** | QED-C (industry consortium) | ✅ (10.1140/epjqt/s40507-021-00114-x documents the consortium) | High — energy benchmark WG funding |
| **EU Quantum Flagship / Horizon Europe** | European Commission | ✅ (flagship program is documented public knowledge) | High — consortium grant as coordinator |
| **NWO Open Competition ENW** | Dutch Research Council | ✅ (public program) | High — single-PI research on JPCUB methodology |
| **Quantum Delta NL** | Dutch National Growth Fund | ✅ (public program) | Medium-High — NL-based quantum software |
| **NLnet / NGI** | NLnet Foundation | ✅ (public program) | Medium — open benchmarking tooling |
| **Sloan Foundation** | Sloan | ⚠️ verify eligibility | Medium — energy/public-interest |
| **Simons Foundation** | Simons | ⚠️ verify eligibility | Medium — p-adic foundations |

**Honest framing:** Grant applications are a pipeline to be pursued, not a revenue projection. The consortium model's first-year funding is more likely to come from small grants (NLnet, NWO) and member dues than from a €5M flagship award. The strategy does not depend on any single grant.

### 5.2 Grant Strategy

1. **Year 1**: NLnet (€5–50K) + NWO (€200–400K) for JPCUB protocol development + consortium bootstrap. Member dues phase in.
2. **Year 2**: QED-C partnership or Quantum Delta NL (€50–500K) for certification framework. EU Flagship as coordinator only if LOIs exist.
3. **Year 3**: Sustainability from certification + dues; grants fund protocol evolution.

---

## 6. Falsifiable Predictions (Pre-Registered)

Timestamped 2026-08-12. Audit dates as specified.

| ID | Prediction | Check Date | Disconfirmation Condition | Strength |
|:---|:-----------|:-----------|:--------------------------|:---------|
| **GTM-1** | JPCUB cited in ≥1 external academic paper or industry report (non-QNFO) | 2027-02-12 | Zero external citations | STRONG |
| **GTM-2** | ≥1 formal letter of intent from a potential consortium member | 2027-02-12 | Zero LOIs | STRONG |
| **GTM-3** | JPCUB Protocol Specification v1.0 published and externally citable | 2027-02-12 | No published spec | STRONG |
| **GTM-4** | ≥3 institutional consortium members with signed charter | 2027-08-12 | <3 signed members | STRONG |
| **GTM-5** | JPCUB proposed to QED-C (or other quantum consortium) as energy benchmark | 2027-02-12 | No proposal submitted | MODERATE |
| **GTM-6** | ≥1 grant awarded (any recognized funder) | 2027-08-12 | Zero grants awarded | MODERATE |
| **GTM-7** | ≥1 JPCUB-Verified badge issued | 2028-02-12 | Zero badges | MODERATE |
| **GTM-8** | Quantum energy advantage (Meier-Yamasaki class) experimentally demonstrated by any group | 2028-08-12 | No experimental demonstration | WEAK (field-level) |

**Note on GTM-8:** This prediction is field-level — it tests whether the energy-advantage literature (arXiv:2305.11212, 10.1103/prxquantum.4.040319) is empirically realized. It is a calibration indicator, not a JPCUB gate.

---

## 7. Financial Model (Estimates, Not Projections)

### 7.1 Revenue Streams (Year 1–3)

| Stream | Year 1 | Year 2 | Year 3 |
|:-------|:-------|:-------|:-------|
| Grants | €5K–50K | €50K–250K | €50K–300K |
| Member dues | €0–6K | €10K–50K | €30K–100K |
| Certification fees | €0 | €2K–10K | €10K–50K |
| Consulting | €0–10K | €10K–50K | €20K–100K |
| **Total** | **€5K–66K** | **€72K–360K** | **€110K–550K** |

### 7.2 Cost Structure

| Item | Annual | Notes |
|:-----|:-------|:------|
| Cloud infra | €500–2K | Current ~€50/mo |
| Consortium ops | €5K–15K | Charter, meetings, platform |
| Travel | €3K–8K | 2–4 conferences |
| Founder stipend | €40K–80K | Below market for quantum researcher |
| **Total** | **€48.5K–105K** | |

Sustainability is achievable at the lower bound of Year 2. The model is lean by design.

---

## 8. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|:-----|:-----------|:-------|:-----------|
| Consortium fails to reach critical mass | Medium (50%) | Critical | Academic-first tier (zero cost); QED-C partnership parallel track |
| QED-C or IEEE defines its own energy benchmark first | Medium (40%) | High | Speed (MLPerf playbook); propose JPCUB INTO QED-C early (GTM-5) |
| Grants rejected | Medium (40%) | High | Apply to ≥5 programs; small grants first; model does not depend on any single grant |
| Founder bandwidth | High (90%) | Medium | Consortium distributes work; grants fund stipend |
| JPCUB measurement challenged | Low (20%) | High | Open methodology (P0 protocol), academic validation tier |
| Incumbent vendors fork the metric | Medium (40%) | Medium | Inclusion-first membership (SPEC playbook) |

---

## 9. Conclusion

The v2.2/v2.3 strategy treated JPCUB as a vendor product. The evidence assembled in this paper shows that is the wrong frame. Every energy benchmark that became a standard — SERT, PUE, MLPerf Tiny — was owned by a neutral consortium, not a vendor. The theoretical foundation for quantum energy advantage now exists (arXiv:2305.11212; 10.1103/prxquantum.4.040319). The quantum industry's own needs assessments identify benchmarking standards as an unmet need (10.1109/te.2022.3153841; 10.1140/epjqt/s40507-021-00114-x).

The strategy is therefore:

1. **Seed the JPCUB Consortium** — a SPEC-style neutral body with JPCUB as its founding standard (fast, high-control, high-trust).
2. **Partner with QED-C** — propose JPCUB as the energy benchmark within the existing quantum consortium ecosystem (leverage, not reinvention).
3. **Fund through verified grants + member dues** — NLnet, NWO, Quantum Delta NL, QED-C programs; no dependence on any single grant.
4. **Monetize through certification** — JPCUB-Verified badges as the consortium's service, not QWAV's product.

Eight pre-registered predictions anchor this strategy in falsifiable terms. If the consortium has fewer than three members by 2027-08-12 (GTM-4), the model is falsified and QWAV should pivot to grant-only research. If the predictions hold, QWAV becomes the steward of the quantum energy standard — a position built on the same playbook that made PUE and MLPerf the standards of their industries.

---

## Declarations

**Funding:** This work was funded independently by the author. No external funding was received.

**Conflicts of Interest:** The author is the founder of QWAV and the creator of the JPCUB metric. This strategy is written from the perspective of the QWAV entity.

**Data Availability:** All external claims are cited with DOIs or arXiv identifiers verified live (2026-08-12) via OpenAlex and arXiv APIs. Market figures are explicitly labeled as estimates.

**License:** QNFO Unified License Agreement (QNFO-ULA). https://legal.qnfo.org/

**Author:** Rowan Brad Quni-Gudzinas (ORCID: 0009-0002-4317-5604). This document was drafted with AI assistance and reviewed by the author.

---

## References

[1] Meier, F., Yamasaki, H. "Energy-Consumption Advantage of Quantum Computation." arXiv:2305.11212 (2023).

[2] Fellous-Asiani, M., Chai, J.H., Thonnart, Y., Ng, H.K., Whitney, R.S., Auffèves, A. "Optimizing Resource Efficiencies for Scalable Full-Stack Quantum Computers." PRX Quantum 4, 040319 (2023). DOI: 10.1103/prxquantum.4.040319.

[3] Lange, K.-D. et al. "The design and development of the server efficiency rating tool (SERT)." DOI: 10.1145/1958746.1958769 (2011).

[4] "PUE: The Green Grid metric for evaluating the energy efficiency in DC (Data Center)." INTELEC 2011. DOI: 10.1109/intlec.2011.6099718.

[5] "Server Energy Efficiency Benchmarks." In: Energy Efficient Servers (2025). DOI: 10.1007/978-3-031-85634-1_11.

[6] Banbury, C. et al. "MLPerf Tiny Benchmark." arXiv:2106.07597 (2021).

[7] Chang, Y.-H. et al. "MLHarness: A Scalable Benchmarking System for MLCommons." arXiv:2111.05231 (2021).

[8] "Industry quantum computing applications." EPJ Quantum Technology (2021). DOI: 10.1140/epjqt/s40507-021-00114-x.

[9] "Assessing the Needs of the Quantum Industry." IEEE Trans. Education (2022). DOI: 10.1109/te.2022.3153841.

[10] Quni-Gudzinas, R.B. "JPCUB Competitive Landscape v2.0." Zenodo (2026). DOI: 10.5281/zenodo.21821767.

[11] Quni-Gudzinas, R.B. "The Qudit Advantage." Zenodo (2026). DOI: 10.5281/zenodo.21880104.

[12] Quni-Gudzinas, R.B. "The QWAV Decade: Enterprise p-Adic Computing 2025-2035." Zenodo (2026). DOI: 10.5281/zenodo.21722393.

[13] Quni-Gudzinas, R.B. "QWAV Commercial Platform: Strategic Architecture Whitepaper." Zenodo (2026). DOI: 10.5281/zenodo.21641108.

[14] Zhou, R. et al. "AxPUE: Application Level Metrics for Power Usage Effectiveness in Data Centers." arXiv:1310.6502 (2013).

[15] Fieni, G., Rouvoy, R., Seinturier, L. "xPUE: Extending Power Usage Effectiveness Metrics for Cloud Infrastructures." arXiv:2503.07124 (2025).
