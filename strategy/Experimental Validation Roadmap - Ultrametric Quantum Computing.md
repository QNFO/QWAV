# COMPUTATIONAL VALIDATION ROADMAP

**Purpose:** A concrete, executable plan for testing the core claims of ultrametric quantum computing through computational simulation. This is the document that answers "where's the proof?" — the single most common objection from reviewers.

**Design principle:** Every simulation has a falsification criterion. Null results are valuable — they constrain the theory and guide the next iteration. The roadmap is designed to produce shareable, reproducible results at every stage, not just at the end.

**Constraint:** No lab access. No experimental collaborators. All validation MUST be computational — software simulation built from known parameters, physical theory, and the mathematical framework. This is legitimate. Computational physics is a real field. The simulations produce quantitative data, not hand-waving.

---

## Why Computational Validation (The Honest Framing)

The ultrametric paradigm challenges a mathematical assumption (Archimedean continuity) that underlies essentially all of modern physics and engineering. The burden of proof is on the challenger.

**What we can do without a lab:** Build computational models that demonstrate the mathematical principles at work. Encode quantum states on Bruhat-Tits trees. Apply noise. Measure error propagation. Compare with standard (Archimedean/flat) encodings under identical noise conditions. The simulation either shows geometric protection or it doesn't. Either outcome is informative.

**What we cannot do without a lab:** Demonstrate that physical qubits (NV centers, superconducting circuits, neutral atoms) can realize the ultrametric encoding with sufficient fidelity. This requires a collaborator with lab access — which is not the current path, but the simulation data makes the case to any potential collaborator who evaluates on substance.

**The computational path is not a consolation prize.** Many important physical effects were predicted by simulation before experimental confirmation. The simulation establishes: (a) the mathematical mechanism works in principle, (b) the specific conditions under which it works, and (c) quantitative predictions that any lab can test.

---

## Validation Strategy: Tiered Approach

### TIER 0: COMPUTATIONAL VALIDATION (PRIMARY PATH)

**Cost:** $0 | **Timeline:** 3-6 weeks | **Status:** NOT STARTED

This is the current focus. Everything below Tier 0 is conditional on finding a collaborator with lab access.

---

#### Experiment 0A: Error Confinement in Bruhat-Tits Tree Circuits

**Goal:** Demonstrate that quantum states encoded on a Bruhat-Tits tree structure exhibit error confinement that standard (Archimedean/flat) encodings do not. The strong triangle inequality should prevent errors at fine tree levels from propagating to coarse levels.

**Architecture:**
- Implement a Bruhat-Tits tree $\mathcal{T}_p$ for a small prime $p$ (e.g., $p = 2$, yielding a 3-regular tree)
- Encode logical qubits at coarse tree levels (shallow depth, near the root)
- Encode fine-grained information at deeper tree levels
- Apply controlled noise (bit flip, phase flip, depolarizing) at specific tree levels
- Measure whether logical states at coarse levels are affected

**Control experiment:** Run identical noise on a standard (flat, non-hierarchical) qubit register with the same number of physical qubits. Compare error rates at the logical level.

**Key Metrics:**
1. **Error propagation ratio** $R_{\text{prop}} = \varepsilon_{\text{coarse}} / \varepsilon_{\text{fine}}$ — the ratio of logical error rate to physical error rate. Prediction: $R_{\text{prop}} \ll 1$ for tree encoding; $R_{\text{prop}} \approx 1$ for flat encoding.
2. **Error suppression factor** $S(d) = \varepsilon_{\text{flat}} / \varepsilon_{\text{tree}}$ as a function of tree depth $d$. Prediction: $S(d)$ grows with $d$, indicating increasing protection.
3. **Strong triangle inequality verification:** For any three encoded states $x, y, z$, verify $d(x,z) \leq \max\{d(x,y), d(y,z)\}$ holds under noise.

**Falsification criterion:** $R_{\text{prop}} \not\ll 1$ — errors at fine levels propagate to coarse levels despite tree encoding, indicating the geometric protection does not manifest in simulation.

**Deliverable:** Python simulation code + output data + plots + technical writeup. Publishable as an open-access technical report.

---

#### Experiment 0B: Energy Barrier Scaling with Tree Depth

**Goal:** Measure the effective energy barrier separating states at different tree depths and verify the predicted scaling $E_{\text{barrier}} \propto q^d$.

**Architecture:**
- Prepare encoded states at tree depths $d = 2, 3, 4, \ldots, 8$
- Apply simulated thermal noise at temperature $T$ (corresponding to $k_B T$)
- Measure the probability of thermal excitation from one branch to another as a function of depth
- Fit the data to $P_{\text{excitation}} \propto \exp(-E_{\text{barrier}} / k_B T)$

**Key Metrics:**
1. **Barrier scaling exponent:** Extract $q$ from the fit. Compare with theoretical prediction.
2. **Thermal stability margin** $\Gamma = E_{\text{barrier}} / k_B T$ at 4 K. Prediction: $\Gamma \gg 1$ at sufficient depth.

**Falsification criterion:** Energy barrier does not scale exponentially with depth, or $\Gamma \leq 1$ at 4 K at all achievable depths — indicating thermal protection is insufficient.

**Deliverable:** Simulation code + energy barrier plots + thermal stability table.

---

#### Experiment 0C: Q-PNA Tree Walk Speedup

**Goal:** Demonstrate that quantum walks on Bruhat-Tits trees provide search speedup compared to classical random walks on the same tree structure.

**Architecture:**
- Build a Bruhat-Tits tree of $N$ nodes
- Hide a target node at a known depth
- Run classical random walk search: measure average time to target
- Run quantum walk search (using a simulated quantum random walk): measure average time to target
- Compare scaling: classical $O(N)$ vs. quantum $O(\sqrt{N})$ (ballistic)

**Key Metrics:**
1. **Speedup ratio** $T_{\text{classical}} / T_{\text{quantum}}$ as a function of $N$.
2. **Scaling exponent** from log-log fit. Prediction: classical exponent $\approx 1$, quantum exponent $\approx 0.5$.

**Falsification criterion:** No speedup beyond classical random walk — quantum walk on Bruhat-Tits tree provides no advantage.

**Deliverable:** Simulation code + speedup plots + scaling analysis.

---

#### Experiment 0D: Syntactic Token Calculus Confluence

**Goal:** Demonstrate that token-based computation paths on tree structures are deterministic (confluent) — every input produces exactly one output path, with no non-deterministic branching.

**Architecture:**
- Implement a token calculus evaluator on a Bruhat-Tits tree
- Feed test problems (classification, decision tasks)
- Verify that each input produces a unique, traceable path from root to leaf
- Verify that the path is deterministic: same input always yields same path

**Key Metrics:**
1. **Confluence ratio:** Fraction of inputs producing a single, deterministic path (target: 1.0).
2. **Path traceability:** Can the path be reconstructed from the output? (target: yes for all inputs).

**Falsification criterion:** Non-deterministic branching occurs — multiple paths possible for the same input — indicating token calculus does not provide guaranteed confluence.

**Deliverable:** Simulation code + confluence analysis + path traceability demonstration.

---

### TIER 1+: PHYSICAL VALIDATION (CONDITIONAL)

**Status:** NOT CURRENTLY PURSUABLE. Requires a lab collaborator.

**What would change this:** A collaborator with lab access (NV centers, neutral atoms, or superconducting qubits) who evaluates the computational data from Tier 0 and agrees to test the predictions on physical hardware.

**What Tier 0 data enables:** The computational results from Experiments 0A–0D provide:
- Specific, quantitative predictions that a lab can test
- Evidence that the mathematical mechanism works in simulation — justifying the cost and effort of physical testing
- A clear experimental protocol: "Here's exactly what we predict, here's how to test it, here's what success and failure look like"

**If a collaborator emerges, the validation ladder is:**

| Tier | Platform | Experiment | Timeline | Cost |
|:-----|:---------|:-----------|:---------|:-----|
| 1 | NV centers (room temp) | Ultrametric distance property on physical spin qubits | 3-6 months | $15K-$30K |
| 2 | Neutral atoms or superconducting | Geometric orientation codes; multi-qubit tree encoding | 6-12 months | $40K-$80K |
| 3 | Cryogenic (4 K) | Thermal stability measurement with twisted Bi-2212 or equivalent | 12-18 months | $60K-$120K |

**Until a collaborator exists, Tiers 1-3 are aspirational, not operational.** The computational path (Tier 0) is the current focus.

---

## Implementation Plan: Tier 0

### Technology Stack
- **Language:** Python 3 (standard library + NumPy for linear algebra, Matplotlib for visualization)
- **Output:** Runnable scripts, generated plots, data tables, technical writeup (Markdown)
- **Distribution:** Open-source on Zenodo + project repository

### Modular Architecture
```
btree_sim/
├── btree.py           # Bruhat-Tits tree construction and operations
├── encoding.py        # Qubit state encoding on tree nodes
├── noise.py           # Noise models (bit flip, phase flip, depolarizing, thermal)
├── metrics.py         # Error rate measurement, barrier calculation, speedup analysis
├── experiment_0a.py   # Error confinement experiment (run this → get results)
├── experiment_0b.py   # Energy barrier scaling experiment
├── experiment_0c.py   # Q-PNA tree walk speedup experiment
├── experiment_0d.py   # Token calculus confluence experiment
├── plots.py           # Visualization functions
└── README.md          # How to run, what to expect
```

### Schedule

| Week | Task | Output |
|:-----|:-----|:-------|
| 1 | Core library (btree.py, encoding.py, noise.py) | Tree construction, state encoding, noise injection |
| 2 | Experiment 0A implementation + metrics | Error confinement data and plots |
| 3 | Experiment 0B implementation | Energy barrier scaling data |
| 4 | Experiment 0C implementation | Quantum walk speedup data |
| 5 | Experiment 0D + integration testing | Confluence analysis |
| 6 | Writeup, polish, open-source release | Complete package on Zenodo |

---

## Falsification & Pivot Criteria

**The computational predictions are falsified if any of these results occur:**

1. **Experiment 0A:** Error propagation ratio $R_{\text{prop}} \approx 1$ for tree encoding — errors propagate freely despite tree structure
2. **Experiment 0B:** Energy barrier shows no exponential scaling with depth — $\Gamma \leq 1$ at 4 K
3. **Experiment 0C:** No quantum walk speedup — classical and quantum walks perform identically on Bruhat-Tits trees
4. **Experiment 0D:** Non-deterministic branching in token calculus — confluence fails

**If falsified, pivot options:**
1. **Revise the theory:** Parameter adjustments, different tree structure, different encoding scheme
2. **Narrow the claim:** The geometric protection may work for specific error models but not universally
3. **Focus on AI:** The Q-PNA / glass-box AI path may be viable even if the quantum hardware predictions fail
4. **Publish the null result:** Negative computational results are valuable — they constrain the theory and prevent wasted effort

**If confirmed:** The computational data strengthens every application, proposal, and outreach document. It becomes the evidence base that "this works in principle — now let's test it in hardware."

---

## What Success Looks Like

**Tier 0 success (achievable in 3-6 weeks):**
- All four experiments (0A-0D) produce results consistent with theoretical predictions
- Error confinement demonstrated in simulation: $R_{\text{prop}} \ll 1$
- Energy barrier scaling confirmed: $E_{\text{barrier}} \propto q^d$
- Open-source package released on Zenodo
- Technical writeup submitted as open-access report

**Post-Tier 0 success (unlocks next stage):**
- Computational data used in Emergent Ventures / Foresight applications
- Data shared with potential collaborators who evaluate on substance
- If data is compelling, it may attract: (a) a lab collaborator for Tier 1+, (b) fellowship/grant funding, or (c) a licensee for Strategy B

**The key insight:** Computational validation doesn't replace physical experiments. But it's what we can do now, with zero external dependencies, that meaningfully advances the credibility of the thesis. The alternative — writing more theory papers without computational or experimental evidence — produces diminishing returns. Simulation closes the gap between "mathematically interesting" and "demonstrably functional in silico."

---

*Computational Validation Roadmap v2.0 — Rewritten 2026-05-11. Previous version (v1.0) centered on lab experiments. This version centers computational validation as the primary path, with physical validation as conditional on collaborator emergence. See CHANGELOG.md for details.*
