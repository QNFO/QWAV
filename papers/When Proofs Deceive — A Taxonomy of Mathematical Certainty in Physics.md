---
title: "When Proofs Deceive: A Taxonomy of Mathematical Certainty in Physics"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-05-18"
doi: "10.5281/zenodo.20266032"
version: "v1.0"
abstract: >
  Mathematics proves logical consistency under stated assumptions; it does not prove physical reality.
  This essay develops a four-type taxonomy of mathematical proofs in physics (consistency, impossibility,
  existence, guarantee) and shows what each can and cannot deliver. Using an ultrametric error confinement
  architecture based on Bruhat-Tits trees as a case study, and the detailed technical review it received,
  I demonstrate how the "assumptions gap" operates in practice. Historical failures are balanced against
  successes (Noether, Bell, Dirac) to show that mathematics succeeds in physics when its assumptions are
  well-matched to physical constraints and its predictions are testable. The essay proposes a "proof-physics
  contract" as a practical tool for making the assumptions gap visible, and concludes that while mathematics
  cannot prove physics, it can tell us exactly what would follow if certain conditions held—leaving experiment
  to determine whether those conditions obtain.
keywords: ["mathematical proof", "physics", "assumptions gap", "operational realism", "ultrametric error confinement", "formal verification", "philosophy of science"]
license: "CC-BY-4.0"
modified: 2026-05-18T09:34:02Z
---
# When Proofs Deceive — A Taxonomy of Mathematical Certainty in Physics

**Author**: [Rowan Brad Quni-Gudzinas](mailto://rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**DOI:** [10.5281/zenodo.20266032](https://doi.org/10.5281/zenodo.20266032)
**Date:** 2026-05-18

**Abstract**: Mathematics proves logical consistency under stated assumptions; it does not prove physical reality. This essay develops a four-type taxonomy of mathematical proofs in physics (consistency, impossibility, existence, guarantee) and shows what each can and cannot deliver. Using an ultrametric error confinement architecture based on Bruhat–Tits trees as a case study, and the detailed technical review it received, I demonstrate how the “assumptions gap” operates in practice. Historical failures (surface code overconfidence, Hawking’s premature conclusion, solar system “proofs”) are balanced against successes (Noether’s theorem, Bell’s theorem, Dirac’s positron) to show that mathematics succeeds in physics precisely when its assumptions are well-matched to physical constraints and its predictions are testable. The essay proposes a “proof-physics contract” as a practical tool for making the assumptions gap visible, and concludes that while mathematics cannot prove physics, it can tell us exactly what would follow if certain conditions held — leaving experiment to determine whether those conditions obtain.

## 1. Beyond the Binary: Four Things Mathematical Proof Does for Physics

The standard response to “can math prove physics?” is admirably clear: no. Mathematics proves theorems; physics discovers facts about the world. A proof in Lean that some error-correction code suppresses noise under idealized conditions does not and cannot demonstrate that a physical qubit operating at millikelvin temperatures will exhibit that behavior.

This answer is correct but incomplete. It treats mathematical proof as a single thing that either succeeds or fails at a single task. In reality, mathematical reasoning serves at least four distinct functions in physics, and each has a different relationship to physical truth.

### 1.1 Consistency Proofs

A consistency proof demonstrates that a set of assumptions does not contain logical contradictions. If you assume $X$, $Y$, and $Z$, then $W$ follows — and no contradiction emerges. This is the most common type of proof in mathematical physics. The surface code threshold theorem is a consistency proof: *if* noise is independent and identically distributed below a certain threshold, *then* logical error rates can be made arbitrarily small. The “if” carries the full weight of physical responsibility.

**What it delivers to physics:** Confidence that the theory is not self-defeating. It eliminates one failure mode (internal contradiction).

**What it cannot deliver:** Any guarantee about the world. The assumptions may be false, incomplete, or inapplicable to real systems.

### 1.2 Impossibility Proofs

An impossibility proof demonstrates that no physical system satisfying certain constraints can achieve a specified outcome. The no-cloning theorem is an impossibility proof: given unitary evolution, no operation can produce an exact copy of an arbitrary unknown quantum state. Shannon’s capacity theorem is an impossibility proof: you cannot transmit information above channel capacity with vanishing error.

**What it delivers:** Genuine physical constraints — provided the assumptions are true of the physical system. Impossibility proofs are the strongest mathematical contribution to physics because they say “nature cannot do this” rather than “nature can do this.”

**What it cannot deliver:** Certainty that the assumptions hold. The no-cloning theorem assumes unitary quantum mechanics. If quantum mechanics is not the final theory, the impossibility may be conditional.

### 1.3 Existence Proofs

An existence proof demonstrates that a mathematical object with certain properties exists. It says: “there is at least one configuration that works.” Existence proofs are common in coding theory and complexity theory. They show that good codes exist without providing efficient construction methods.

**What it delivers:** A bound on what is logically possible. If even the mathematics can’t find a solution, the physics certainly can’t. If the mathematics can find one, the physics might.

**What it cannot deliver:** A construction method, an engineering blueprint, or evidence that the mathematical object corresponds to anything physically realizable.

### 1.4 Guarantee Proofs

A guarantee proof — the holy grail, and the most dangerous — attempts to demonstrate that a specific physical system, described by specific equations, will exhibit specific behavior. This is what the ultrametric error confinement theorem aimed to be, and what the surface code threshold theorem is often (incorrectly) treated as.

**What it delivers:** Conditional certainty. If the system satisfies the assumptions, the behavior follows.

**What it cannot deliver:** Unconditional certainty about physical hardware. Every guarantee proof contains an “assumptions gap” between the mathematical model and the physical system.

This taxonomy clarifies what is at stake in any claim that mathematics “proves” something about physics. The question is never whether the proof is mathematically valid — it almost always is. The question is what type of proof it is and whether its type matches the epistemic claim being made.

---

## 2. The Assumptions Gap: Anatomy of a Specific Failure Mode

*Before examining the case study: quantum error correction (QEC) protects fragile quantum information by encoding a “logical qubit” across many “physical qubits.” When errors occur, a decoder determines what correction to apply based on syndrome measurements — parity checks that detect errors without collapsing the quantum state. Most QEC approaches, such as the surface code, actively measure syndromes and apply corrections. The ultrametric approach explored here takes a different path: it uses the geometric structure of the encoding space itself to passively confine errors, reducing the need for active intervention. The question is whether this geometric confinement can be mathematically proved — and whether that proof transfers to physical hardware.*

The ultrametric error confinement architecture provides a worked example of how the assumptions gap operates in practice. The proposal uses Bruhat–Tits trees — mathematical objects with a natural ultrametric distance — to organize quantum error correction. The ultrametric structure guarantees a strong triangle inequality: for any three nodes $x$, $y$, $z$, the distances satisfy $d(x, z) \leq \max\{d(x, y), d(y, z)\}$. This geometric constraint forces errors to remain localized in tree neighborhoods, enabling error confinement without active syndrome measurement.

The proposal received detailed technical feedback raising four specific objections:

1. **Asymmetric decoder:** The simulation assumed a symmetric decoder, but with $b = 2$ children per node and a tie-breaker fixed to logical $0$, the decoder becomes AND-not-majority, making logical $1$ exponentially fragile. Only logical $0$ was tested.

2. **AGP theorem priority:** The error confinement conjecture matches the Aliferis–Gottesman–Preskill (2006) threshold theorem for concatenated codes. If the result is not novel, what is the contribution?

3. **Classical vs. quantum scope:** The simulation uses classical bits and classical majority vote. A formal proof would establish a classical coding theorem, not a quantum error correction result.

4. **Missing literature:** Heydeman et al. (2018) on holographic QEC on Bruhat–Tits trees; Boettcher (2020) on quantum ultra-walk non-localization.

Each objection is mathematically legitimate. Each also illustrates a different dimension of the assumptions gap.

The first objection is a **model-specification failure**: the proof claims something about a system with property $P$, but the simulated system has property $P’$ — and $P’$ is a proper subset of $P$. The symmetric decoder assumption excluded the very cases where the scheme would fail. This is not a flaw in the mathematics of ultrametric error confinement under symmetric decoding; it is a flaw in the claim that the mathematics applies to the system as actually configured.

The third objection is a **scope failure**: the proof establishes something about classical bits, but the claim is about quantum error correction. The mathematics is valid within its domain; the error is in asserting that the domain covers the intended application.

These are not exotic philosophical concerns. They are exactly the kind of problems that formal verification is supposed to catch — and, importantly, that formal verification *would* catch if the assumptions were stated with sufficient precision. The irony is that these objections are themselves a form of verification: checking whether the proof’s premises match the physical claims being made. That is not a mathematical operation; it is a physical one.

The author’s response — “Are you raising objections that matter for the math, or are you pointing out that the math can’t guarantee the physics? Those are different conversations” — cuts to the core. It acknowledges that mathematical validity and physical applicability are distinct concerns. A theorem can be true while its interpretation is false.

---

## 3. Four Papers, One Position: Operational Realism as a Coherent Alternative

The ultrametric case study surfaces a question the rest of this essay must answer: *why* is the assumptions gap ineradicable, and what should we do about it? The answer requires a philosophical framework — one that explains the relationship between mathematical models and physical reality. The following four papers, my published work spanning 2025–2026, develop precisely such a framework.

My published work develops a philosophical framework that explains *why* the assumptions gap is ineradicable and what to do about it. Read together, four papers — spanning 2025–2026 — articulate a position I will call **operational realism**.

*These papers represent my own research program; the position they articulate is offered here as a coherent alternative to mathematical Platonism, not as a settled consensus. Their value for this essay is that they provide a worked philosophical framework — one that explains why the assumptions gap matters and what to do about it.*

### 3.1 The Mathematical Trap

In “Reassessing the Foundations of Quantum Computation” (2025), I argue that Shor’s algorithm is a mathematical trap: mathematically elegant, but its assumptions (fault-tolerant logical qubits, coherent control at scale) are so demanding that physical realization at scale remains an open question, not a guaranteed outcome. The argument is not that Shor’s algorithm contains a mathematical error — it doesn’t. It is that the assumptions required for its implementation (fault-tolerant logical qubits, coherent control at scale) are so demanding that the algorithm functions more as a proof of concept than as an engineering roadmap. The mathematics *proves* that factoring can be done efficiently in a formal model of quantum computation; it does not *prove* that any physical system will ever run Shor’s algorithm at cryptographically relevant scales.

The trap structure is: a mathematical proof of possibility is misinterpreted as a guarantee of feasibility. The precision of the proof masks the gap between the model and the world.

### 3.2 The Entropic-Operational Turn

“The Entropic-Operational Paradigm” (2025) provides the philosophical foundation. It rejects mathematical Platonism — the view that mathematical structures are the true reality and physical systems are imperfect instantiations. Instead, it adopts an operational realism: only what can be measured or operated on is physically real. Gravity and quantum mechanics are not fundamental mathematical structures that happen to be realized in the world; they are emergent regularities in thermodynamic information processing.

This position has direct consequences for the math-physics relationship. If physical reality is fundamentally operational — defined by what can be done and measured — then no purely formal derivation can establish physical truth. Mathematical consistency is necessary for good theory but insufficient for physical knowledge. The arrow of validation runs from experiment to mathematics, not the reverse.

### 3.3 Noise as Resource

“Epistemic Noise as Computational Resource” (2026) develops a practical implication: if noise is not an enemy to be eliminated but a resource to be managed, then the entire framework of error “correction” changes. The ultrametric error confinement approach exemplifies this shift. Rather than actively measuring and correcting errors (the surface code approach), it uses the geometric structure of Bruhat–Tits trees to confine errors passively — letting the substrate do the work.

This connects to superdeterminism: noise is not random in the frequentist sense but is structured by the same physical laws that govern the computational substrate. The “i.i.d. noise” assumption of the surface code threshold theorem is not just a simplification — it is a category error. Real noise has structure, and that structure can be exploited.

### 3.4 Phase Transitions of Logic

“Phase Transitions of Logic” (2026) extends the program to fault tolerance itself. The thesis is that substrate-level fault tolerance — achieved through physical geometry rather than active error correction — may exhibit phase-transition behavior: below a critical noise threshold, errors remain confined; above it, they propagate. This is mathematically analogous to the surface code threshold theorem but philosophically different: the threshold is a property of the physical substrate, not of a logical encoding layered on top of it.

Taken together, these four papers form a coherent position: mathematics is essential for physics *as a tool for reasoning*, not as a source of ontological guarantees. The role of mathematical proof is to clarify assumptions, identify contradictions, establish bounds, and guide experiment — not to replace experiment.

---

## 4. Failure Modes: When Mathematical Certainty Misled Physics

The ultrametric case study is one example of a broader pattern. History provides several cases where mathematical proof gave unwarranted confidence about physical systems.

### 4.1 The Surface Code and the Coherence Gap

The surface code threshold theorem proves that if physical error rates are below approximately $1\%$ and errors are independent and identically distributed, then logical error rates can be made arbitrarily small by increasing code distance. This is a mathematically beautiful result. It has driven two decades of qubit engineering.

But real qubits do not exhibit i.i.d. noise. They exhibit correlated errors, leakage, $1/f$ noise, and crosstalk. The theorem proves something about an idealized noise model; it does not prove that real qubits, with real noise, can achieve fault tolerance by scaling code distance. The assumptions gap here is not a minor technicality — it is the difference between the theorem’s domain and the laboratory’s reality. And yet the theorem is routinely cited as though it *guarantees* that fault tolerance is “just an engineering problem.”

This is the most dangerous failure mode of mathematical proof in physics: a guarantee proof is treated as a physical guarantee, when it is only a mathematical one.

### 4.2 Hawking Radiation and the Information Paradox

Hawking’s 1974 calculation showing that black holes radiate thermally was mathematically rigorous given the assumptions of quantum field theory in curved spacetime. The calculation *proved* that black holes evaporate. But it also appeared to prove that information is destroyed — a result in tension with unitarity in quantum mechanics.

The mathematical proof was correct. The physical interpretation was debated for forty years. The resolution (still not fully settled) required recognizing that the semiclassical approximation — quantum fields on a classical spacetime background — breaks down at the Planck scale. The mathematics was valid; the physical conclusion was premature. The proof proved something about *a model*, not about *black holes*.

### 4.3 The Stability of the Solar System

For two centuries after Newton, mathematicians attempted to prove the stability of the solar system. Laplace “proved” it in 1773 — but his proof assumed that planetary perturbations were periodic. Lagrange and Poisson extended the analysis. By the late 19th century, mathematicians believed they had demonstrated that the solar system was stable.

Then came Poincaré. In 1889, he showed that the three-body problem admits chaotic solutions. The “proofs” of stability had all smuggled in assumptions — convergence of series, absence of resonances — that did not hold. The solar system *is* approximately stable on human timescales, but it is not provably stable in the sense that 18th-century mathematicians claimed. The mathematics had proved something about idealized systems; nature declined to cooperate.

### 4.4 The Pattern

The pattern across these cases is consistent: a mathematical proof is valid within its stated assumptions. The assumptions are then forgotten, or their physical applicability is overstated. The proof’s certainty is transferred — illegitimately — from the mathematical domain to the physical one. The failure is not in the mathematics; it is in the epistemology.

---

## 5. When Math Got It Right: Counterexamples and What They Teach

The argument so far has emphasized cases where mathematical proof misled physics. Intellectual honesty requires acknowledging cases where mathematical reasoning successfully established physical truth. These counterexamples do not refute the assumptions gap — they clarify the conditions under which it can be bridged.

### 5.1 Noether’s Theorem: Symmetry Becomes Conservation

In 1918, Emmy Noether proved that every continuous symmetry of a physical system corresponds to a conserved quantity. Time-translation symmetry implies conservation of energy; spatial-translation symmetry implies conservation of momentum; rotational symmetry implies conservation of angular momentum. This is an impossibility proof of the strongest kind: given a system with certain symmetries, certain quantities *must* be conserved.

Why did Noether’s theorem succeed as a physical claim? Because the assumptions — that the laws of physics are describable by a Lagrangian, and that the Lagrangian possesses continuous symmetries — are extraordinarily well-matched to physical reality. The assumptions gap was small. The proof transferred.

Noether’s theorem fits the taxonomy as an impossibility proof that delivered genuine physical constraints. It succeeded not because mathematics overcomes the assumptions gap, but because the assumptions happened to be true.

### 5.2 Bell’s Theorem: Local Realism Constrained

In 1964, John Bell proved that any local hidden-variable theory must satisfy an inequality that quantum mechanics violates. The proof established a mathematical constraint on a class of physical theories — and experiments subsequently confirmed the quantum-mechanical prediction, ruling out local hidden-variable theories.

Bell’s theorem is a hybrid: it is an impossibility proof (local realism *cannot* reproduce quantum correlations) wrapped in a consistency proof (quantum mechanics *predicts* the violation). Its assumptions — locality, realism, and the statistical predictions of quantum mechanics — were precise enough that experiment could test them directly. The theorem told physicists what to measure; nature provided the verdict.

### 5.3 Dirac’s Positron: Mathematical Consistency Predicts Matter

In 1928, Paul Dirac formulated a relativistic wave equation for the electron. The equation had solutions with negative energy — mathematically consistent but physically puzzling. Rather than discarding them, Dirac interpreted them as predicting a new particle: the positron, discovered experimentally in 1932.

This is a consistency proof that successfully crossed the assumptions gap. Dirac’s assumption — that the equation correctly described electrons — turned out to be true, and the mathematical structure of the equation contained more information than initially recognized. The success was not that math “proved” the positron existed; it was that math identified a *necessary consequence* of the theory, and experiment confirmed the theory.

### 5.4 The Pattern Across Successes

The cases where mathematical proof succeeded in establishing physical truth share a common structure:

1. **Precise assumptions** — the mathematical claim was explicitly conditional on well-defined physical conditions.
2. **Testable predictions** — the proof directed attention to something measurable.
3. **Experimental confirmation** — measurement, not mathematics, established the physical claim.
4. **Small assumptions gap** — the mathematical assumptions were unusually well-matched to physical reality.

In each case, the proof did not replace experiment. It told experiment what to look for, and nature confirmed the finding. This is the pattern the proof-physics contract (Section 6.1) is designed to generalize: make the assumptions explicit, identify what would confirm or refute the physical correspondence, and test.

### 5.5 What the Counterexamples Do Not Show

The counterexamples do not show that mathematics can prove physics in the strong sense — that a formal derivation alone establishes physical truth. Noether’s theorem is a mathematical truth (symmetry $\to$ conservation) whose physical applicability depends on nature having the symmetries it does. Bell’s theorem is a mathematical truth whose physical conclusion required experimental confirmation. Dirac’s positron required a physical discovery.

What the counterexamples *do* show is that mathematics can be an extraordinarily effective guide to physical discovery when its assumptions are well-chosen and its predictions are testable. The assumptions gap does not make mathematics useless for physics — it makes explicit the conditions under which mathematical reasoning transfers to the physical world. The successes occurred when those conditions were met, not when they were ignored.

### 5.6 Limitations and Scope

This essay is not a comprehensive survey of mathematical physics. Several important topics fall outside its scope: the role of approximation and asymptotic reasoning (where proofs establish error bounds rather than exact claims), the distinction between constructive and non-constructive proof in physics, the historical role of mathematics in classical mechanics (Newton, Euler, Lagrange), and the philosophical literature on structural realism and model-dependent realism. These are productive directions for extension but would expand the essay beyond its intended focus on the specific question: can math *prove* physics?

---

## 6. A Framework for Proof-Aware Physics

Drawing on the taxonomy of Section 1, the case study of Section 2, the philosophical position of Section 3, and the counterexamples of Section 5, I propose a framework for thinking about the relationship between mathematical proof and physical validation.

### 6.1 The Proof-Physics Contract

Every mathematical proof that makes a claim about physical systems should be accompanied by an explicit statement of:

1. **Proof type:** Which of the four types (consistency, impossibility, existence, guarantee) is being claimed?
2. **Assumptions inventory:** What mathematical assumptions does the proof require?
3. **Physical correspondence:** For each assumption, what physical condition must hold for the assumption to be applicable?
4. **Known gaps:** What is known about the correspondence between each assumption and physical reality?
5. **Vulnerability analysis:** Which assumptions, if violated, would invalidate the physical conclusion?

This contract would not eliminate the assumptions gap — nothing can. But it would make the gap visible. It would transform mathematical proof from a black-box oracle of certainty into a transparent tool for reasoning.

### 6.2 The Role of Formal Verification

Formal verification systems like Lean serve a specific function within this framework: they verify consistency proofs with extreme rigor. When Lean checks a theorem, it confirms that the conclusion follows from the stated premises — no more, no less. This is valuable precisely because it eliminates a class of errors (logical mistakes in derivation) that plague informal mathematical reasoning.

But Lean cannot replace the proof-physics contract’s physical correspondence check. A Lean proof that “under i.i.d. noise with rate $p < p_{\text{th}}$, the logical error rate is exponentially suppressed” tells you that the mathematics is internally consistent. It does not tell you that any physical qubit experiences i.i.d. noise, or that $p_{\text{th}}$ is achievable in hardware, or that the tree geometry can be physically instantiated. Even impossibility proofs — the strongest type — remain conditional on their assumptions holding in the physical system under study.

This is not a limitation of Lean specifically — it is a limitation of any formal system. The assumptions gap is not a bug in formal verification; it is a feature of the relationship between formal systems and the world. Formal verification makes the gap *precise* — it tells you exactly which assumptions would need to be true for the conclusion to hold — but it cannot close it.

### 6.3 The Ultrametric Test: What Would Success Look Like?

The ultrametric error confinement architecture provides a natural experiment for this framework. Suppose we:

1. State the assumptions explicitly (symmetric decoder, $b \ge 3$, i.i.d. bit-flip noise with rate $p_{\text{err}}$, tree geometry with branching factor $b$).
2. Prove — in Lean or on paper — that under these assumptions, the logical error rate $p_L(d)$ satisfies $p_L(d) \le C \cdot p_{\text{err}}^{k \cdot d}$.
3. Build a physical system that approximates these assumptions (e.g., a photonic lattice with ultrametric coupling, or a trapped-ion graph with tree-structured interactions).
4. Measure the actual logical error rate as a function of depth $d$ and compare to the mathematical bound.

If the measured rates match the bound, we have not “proven physics.” We have demonstrated that *in this case*, the assumptions gap was small enough that the mathematical guarantee transferred approximately to the physical system. This is a success — but it is a success of engineering (building a system that approximates the assumptions) and experimental validation (measuring the correspondence), not a success of pure mathematics.

If the measured rates deviate significantly from the bound, we have not “disproven mathematics.” We have discovered that one or more assumptions fail to hold in the physical implementation — and identifying which assumption failed is itself scientifically valuable. The proof remains mathematically valid; its physical applicability is what’s tested.

This is the proper role of mathematical proof in physics: not as an oracle of physical truth, but as a precise statement of *what would follow if certain conditions held*. The proof tells you what to look for; experiment tells you whether you found it.

---

## 7. Conclusion: The Productive Gap

I began with a question — “Can math prove physics?” — and gave the standard answer: no, math proves logical consistency, not physical reality. But the deeper insight is that this gap is not a failure of mathematics or physics. It is the engine of scientific progress.

Mathematical proof provides precision: it tells us exactly what assumptions are required for a conclusion to hold. Experiment provides contact with reality: it tells us whether those assumptions are approximately satisfied in the world. The gap between them is where science happens — where we discover that our assumptions were too strong (the asymmetric decoder), too narrow (classical vs. quantum scope), or insufficiently grounded (i.i.d. noise vs. real noise spectra).

The four technical objections raised against the ultrametric error confinement paper were not obstacles to formalization — they were *clarifications* of the assumptions gap. Each objection identified a place where the mathematical claim and the physical system diverged. Responding to them required not better mathematics but clearer statements of what was assumed, what was simulated, and what was claimed.

My published work — operational realism, epistemic noise as resource, phase transitions of logic — provides the philosophical infrastructure for this view. It argues that mathematics is indispensable for physics precisely because it forces us to be explicit about our assumptions. The value of formal proof is not that it replaces experiment but that it makes the assumptions gap visible and measurable.

So: can math prove physics? No. But math can do something better: it can tell us exactly what we would need to believe for a physical claim to follow — and then physics can tell us whether we should believe it. The gap is not a weakness of either discipline. It is the space in which knowledge grows.

---

*This essay builds on the philosophical framework developed in Quni-Gudzinas (2025–2026) and the ultrametric error confinement architecture. The exchange with a mathematician colleague who provided detailed technical feedback is reconstructed from project notes; the earlier philosophical essay “Can Math Prove Physics?” (0.1.1) provides the starting position that this essay deepens.*
