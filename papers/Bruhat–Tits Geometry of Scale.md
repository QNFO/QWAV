---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
modified: 2026-05-07T14:46:58Z
title: "The Tree of Frequencies: A Bruhat–Tits Geometry of Scale"
aliases:
  - "The Tree of Frequencies: A Bruhat–Tits Geometry of Scale"
---

# A Bruhat–Tits Geometry of Scale

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.20071716](http://doi.org/10.5281/zenodo.20071716)
**Date:** 2026-05-07
**Version:** 0.9

## Abstract

Ostrowski’s theorem (1916) establishes that every absolute value on $\mathbb{Q}$ is equivalent to either the real absolute value or a $p$-adic one—there is no third option. Physics has been built entirely on $\mathbb{R}$. We propose that the fundamental geometry of physical frequencies is a **Bruhat–Tits tree** $\mathcal{T}_p$, the natural geometry for the $p$-adic numbers $\mathbb{Q}_p$. Choosing a multiplicative ruler with scaling ratio $q$ partitions frequencies into bands, and the sequence of $q$-ary sub-band choices defines paths on a rooted tree. The tree distance $d_T = q^{-\ell}$ satisfies the strong (ultrametric) triangle inequality. This geometry has testable consequences: quantum states are superpositions of tree-paths, measurement truncates the tree to finite depth, and time emerges from correlations between dual trees via a Page–Wootters mechanism. The framework makes three falsifiable predictions and points to two research directions: (1) non-Markovian decoherence oscillations in superconducting qubit–resonator systems; (2) log-periodic oscillations in the CMB power spectrum, constrained to amplitude $A \lesssim 5\%$ by Planck and testable to $A \sim 0.5\%$ by CMB-S4; (3) a hierarchical organization of fermion masses. Two additional directions—tree-based quantum error correction and adelic unification via the Langlands program—are identified as longer-term consequences of the tree geometry. The same tree geometry—if confirmed with a common scaling ratio $q$—would produce signatures spanning eighteen orders of magnitude in scale, from superconducting qubits to the cosmic microwave background. Confirming the same $q$ in both domains would be a rare connection between quantum measurement and cosmic structure through a single geometric principle.

---

## 1. Introduction

In 1916, Alexander Ostrowski proved a theorem that has been called one of the most underappreciated results in mathematics: every notion of distance on the rational numbers is equivalent to exactly one of two fundamentally distinct types—the familiar Archimedean absolute value that gives us the real numbers $\mathbb{R}$, or one of the $p$-adic absolute values that give us the $p$-adic numbers $\mathbb{Q}_p$. There is no third option. Yet all of conventional physics—classical mechanics, quantum field theory, general relativity—is built exclusively on $\mathbb{R}$. Coordinates are real numbers. Time is a real parameter. Frequencies are real numbers measured in Hertz. The other half of Ostrowski’s dichotomy has been almost entirely absent.

This paper proposes that this absence is an illusion. The fundamental geometry of physical frequencies is not the continuous real line, but a discrete, ultrametric tree—specifically, a **Bruhat–Tits tree** whose boundary is a $p$-adic projective line. What we measure as a real-valued frequency in the laboratory is an emergent, Archimedean shadow cast by an underlying $p$-adic structure. The tree is not an auxiliary mathematical tool; it is the primitive object.

The idea is simple. Combine Einstein’s $E = mc^2$ with Planck’s $E = h\nu$, and every mass is a frequency: the Compton frequency $f = mc^2 / h$. Frequency is the universal coordinate of physical scale. But frequencies in nature do not organize themselves on a featureless line. They appear in multiplicative bands—electromagnetic spectra, particle masses, atomic transitions—where the natural operation is not addition but multiplication, and the natural question is not “how far apart?” but “at what scale do two frequencies first diverge?” This question is answered by a tree: each branching represents a choice among $q$ sub-bands, and the depth of the deepest common ancestor of two frequencies defines an ultrametric distance between them.

The tree framework sits at the intersection of four independent lines of inquiry. In **number theory**, Ostrowski’s theorem and the Bruhat–Tits tree provide the mathematical backbone. In **particle physics**, the renormalization group organizes scale transformations hierarchically, and spin glasses exhibit ultrametric organization of states. In **condensed matter**, the Multiscale Entanglement Renormalization Ansatz (MERA) represents quantum many-body states as tensor networks on a tree geometry. In **signal processing**, discrete wavelet transforms decompose signals into dyadic trees of scale and translation. That the same discrete, hierarchical, ultrametric structure appears in all four domains—independently—suggests it is not a coincidence but a signal.

The consequences are concrete and testable. If frequency space is a tree, then:
- Quantum states are **paths** on the tree, and measurement is **truncation to finite depth**.
- Superposition and collapse have geometric interpretations as branching and path selection.
- Time is not fundamental but emerges from correlations between two trees via a Page–Wootters mechanism.
- The arrow of time runs from coarser to finer scales on the tree.
- Decoherence is not Markovian; it exhibits **oscillations** with a period set by the tree depth.
- The cosmic microwave background carries **log-periodic** signatures of the tree structure imprinted at the Planck scale.
- Fermion masses should exhibit a hierarchical, tree-like organization.

This paper synthesizes and extends previous work (Phases 0.1 and 0.2) into a unified presentation. Section 2 constructs the tree geometry of frequency from first principles. Section 3 derives the physical consequences for quantum mechanics, time, and measurement. Section 4 presents the three falsifiable predictions and two research directions, and their current status. Section 5 provides the mathematical foundations in greater depth. Section 6 discusses open questions, the continuum limit, and connections to other research programs.

**How to read this paper.** Readers primarily interested in experimental consequences can read Sections 1, 2.1–2.4 (tree basics), and 4 (predictions), skipping the mathematical foundations (Section 5) on first pass. Readers seeking the mathematical rigor should read Section 2.5–2.6 and all of Section 5. The physical picture of states, measurement, and time (Section 3) is essential for understanding the deeper implications but not required to evaluate the experimental predictions. The “Honest Audit” (Section 6.5) provides a candid assessment of the framework’s strengths and weaknesses and is recommended for all readers.

---

## 2. The Tree Geometry of Frequency

### 2.1 Frequency as the Universal Coordinate of Scale

Combine the two most famous equations of twentieth-century physics—Einstein’s $E = mc^2$ and Planck’s $E = h\nu$—and a profound fact emerges: every mass is a frequency. The **Compton frequency** of a particle of mass $m$ is

$$
f = \frac{m c^2}{h}.
$$

The electron’s Compton frequency is $\sim 1.24 \times 10^{20}$ Hz; the proton’s is $\sim 2.27 \times 10^{23}$ Hz (ratio 1836); the Planck frequency is $\sim 2.95 \times 10^{42}$ Hz. Every physical scale—temporal periods, spatial wavelengths, rest energies, masses—is expressible as a frequency. Frequency is the universal coordinate of physical scale, the single number that tells you where in the hierarchy of nature a process lives.

### 2.2 The Multiplicative Ruler

The organization of frequencies into bands is a fact about measurement: when we ask questions about scale—“is this frequency closer to radio or to microwave?”—we implicitly compare ratios, not differences. The operation that matters is multiplication, not addition. This is a choice of **measurement convention**, not a claim about ontology.

However, Ostrowski’s theorem (Section 5.1) tells us something deeper: there are exactly two consistent geometries for completing the rational numbers—Archimedean ($\mathbb{R}$) and non-Archimedean ($\mathbb{Q}_p$). The choice of ruler (additive vs. multiplicative) selects which of these two geometries is made manifest in measurement. If nature’s fundamental geometry of frequency is ultrametric, then a multiplicative ruler is the **correct** choice—the one that reveals the underlying tree structure. If nature’s geometry is Archimedean, an additive ruler is correct, and the tree is a measurement artifact. The experimental predictions (Section 4) are designed to distinguish these two possibilities: they test nature, not our measurement conventions.

Formally, fix a **scaling ratio** $q \geq 2$ (integer). Common choices include $q = 2$ (octaves) or values tied to the prime $p$ in the $p$-adic construction (e.g., $q = 3, 5, 7, \ldots$); see the terminology note in Section 2.5 for the relationship between the general $q$-ary tree and the Bruhat–Tits tree $\mathcal{T}_p$. Non-integer values such as $q = e$ (natural log scaling) describe a continuum limit and do not correspond to a discrete tree; they are included in the search range for experimental fits but do not represent a physical tree with $e$ branches. The $k$-th level of the hierarchy covers frequencies in the interval

$$
[f_0 q^k,\; f_0 q^{k+1}),
$$

where $f_0$ is an arbitrary reference frequency. Each level differs from its neighbors by a factor of $q$.

### 2.3 Base-$q$ Expansion and Paths on a Tree

Any frequency $f$ can be expressed in base $q$ as

$$
\frac{f}{f_0} = d_0 . d_1 d_2 d_3 \ldots_q,
$$

where each digit $d_i \in \{0, 1, \ldots, q-1\}$. The integer part $d_0$ selects the band; the first fractional digit $d_1$ selects a sub-band among $q$ possibilities; $d_2$ selects a sub-sub-band; and so on. Specifying a frequency to finite precision is making a finite sequence of $q$-ary choices.

This sequence of choices defines a **path** on a rooted, $q$-ary tree (see Figure 1 in the supplementary file `0.8_fig_tree.png`). The root represents the set of all frequencies. Its $q$ children represent the $q$ bands at the first level. Each of those has $q$ children, and so on ad infinitum. The set of all infinite paths is the set of all frequencies specified to infinite precision—the **boundary** of the tree.

Crucially, a tree is not merely a log scale drawn with branches. A log scale indexes levels by a single integer $k$; a tree has $q^k$ distinct intervals at depth $k$. The tree is the minimal geometry that supports the operation “identify a frequency to a factor of $q^k$ by making $k$ choices among $q$ alternatives.” The branching reflects a physical fact: at any given scale, there are multiple physically distinct types of oscillators (photons, phonons, fermionic excitations, collective modes), and the tree organizes them all within a single geometric object.

### 2.4 Ultrametric Distance

The tree defines a natural notion of closeness between frequencies. Given two frequencies $f_1$ and $f_2$ with base-$q$ expansions, let $\ell$ be the depth of the **most recent common ancestor**—the vertex where their paths from the root first diverge. The tree distance between them is

$$
d_T(f_1, f_2) = q^{-\ell}.
$$

Frequencies that share a long common prefix (deep common ancestor) are close; frequencies that diverge near the root are far apart. The maximum distance is $q^0 = 1$ (they differ at the root); the minimum approaches zero as their paths coincide to ever-greater depth.

This distance satisfies the **strong triangle inequality**:

$$
d_T(x, z) \leq \max\big(d_T(x, y),\; d_T(y, z)\big),
$$

a property strictly stronger than the ordinary triangle inequality $d(x,z) \leq d(x) + d(y,z)$. All triangles in this geometry are **isosceles with a short base**: of the three pairwise distances, the two largest are always equal. Equivalently, two balls in the tree metric either are disjoint or one contains the other—there is no partial overlap.

This is the defining signature of an **ultrametric** space, and it is the geometric fingerprint that distinguishes the tree from any Euclidean or Riemannian manifold. In Section 4, we will argue that this fingerprint is directly observable in laboratory decoherence experiments.

### 2.5 The Bruhat–Tits Tree

The mathematical object that realizes these properties with minimal structure is the **Bruhat–Tits tree** $\mathcal{T}_p$. For any prime $p$, $\mathcal{T}_p$ is an infinite $(p+1)$-regular tree. Its vertices correspond to equivalence classes of lattices in $\mathbb{Q}_p^2$; its boundary $\partial\mathcal{T}_p$ is the $p$-adic projective line $\mathbb{P}^1(\mathbb{Q}_p)$.

In the tree framework, we take $p = q$ (or, more generally, any integer $q \geq 2$ obtained as a product of primes). The Bruhat–Tits tree is then the **fundamental geometry of frequency space**. Each vertex at depth $k$ represents a frequency band; each of its $q$ children represents a sub-band; the boundary points represent frequencies specified to infinite precision in the $p$-adic completion.

**A note on terminology.** Throughout this paper, we use “the tree” to refer to a general $q$-ary rooted tree with branching factor $q \geq 2$ (integer). This general tree possesses the essential physical properties—ultrametric distance $d_T = q^{-\ell}$, strong triangle inequality, discrete spectral density—that generate the experimental predictions of Section 4. The Bruhat–Tits tree $\mathcal{T}_p$ is the special case where $q = p$ (prime), providing the rigorous number-theoretic foundation in $\mathbb{Q}_p$. When $q$ is composite, the $q$-ary tree is a product of Bruhat–Tits factors. In both cases, the physical predictions are identical—they depend on the tree structure, not on the primality of $q$. The Bruhat–Tits construction anchors the framework in Ostrowski’s theorem; the general $q$-ary tree anchors it in experiment.

The only primitive notion on the tree is integer **depth** $k$. A vertex at depth $k$ is identified by a sequence of $k$ branching choices:

$$
\text{vertex} \;\longleftrightarrow\; (d_0, d_1, d_2, \ldots, d_{k-1}), \qquad d_i \in \{0, 1, \ldots, q-1\}.
$$

This is a pure count—$k$ integers, nothing more. There is no “time,” no “seconds,” no “Hertz” at this level. As we will see in Section 3, what we call time emerges from correlations between two such trees. The Archimedean continuum $\mathbb{R}$ of laboratory frequencies is an emergent approximation to the boundary of this tree in the limit of large depth.

### 2.6 Why a Tree? Four Independent Discoveries

The tree geometry is not an arbitrary construction. The same discrete, hierarchical, ultrametric structure has been discovered independently in four distinct domains:

1. **Number theory.** Ostrowski’s theorem (1916) establishes that the only two completions of $\mathbb{Q}$ are $\mathbb{R}$ and $\mathbb{Q}_p$. The Bruhat–Tits tree is the natural geometry of $\mathbb{Q}_p$. If the fundamental geometry of scale is not $\mathbb{R}$, it must be this tree.

2. **Particle physics.** The renormalization group (RG) organizes scale transformations multiplicatively and hierarchically. Wilson’s RG flows on theory space have a tree-like structure. Spin glasses, solved by Parisi, exhibit ultrametric organization of equilibrium states—a direct physical realization of tree geometry.

3. **Condensed matter.** The Multiscale Entanglement Renormalization Ansatz (MERA) represents quantum many-body ground states as tensor networks living on a tree (specifically, a hyperbolic tiling). MERA captures scale-invariant critical systems by explicitly removing entanglement at each scale—the tree is the computational geometry of quantum matter.

4. **Signal processing.** Discrete wavelet transforms decompose signals into a dyadic tree of scale and translation. The fast wavelet transform is an algorithm that walks a binary tree, and the resulting coefficients are naturally organized in a hierarchical, logarithmic structure.

That the tree appears in all four domains—independently and for entirely different reasons—strongly suggests that the tree is not an artifact of any one formalism. It is the natural geometry of scale itself.

---

## 3. Physical Consequences

If frequency space is a tree, the standard formalism of quantum mechanics—Hilbert spaces, superpositions, measurement, time evolution—acquires a geometric interpretation. This section derives the physical picture that follows from taking the tree seriously.

### 3.1 States as Paths

On the tree, a frequency specified to infinite precision is an infinite path from the root to the boundary. In quantum mechanics, we rarely have infinite precision—and indeed the theory tells us we cannot. A quantum state of a system at a given scale is not a single path, but a **superposition of paths** that are unresolved at the current depth.

Formally, let the tree have branching factor $q$ and depth $D$ (which may be infinite). The set of all paths of length $D$ forms the boundary $\partial\mathcal{T}$. A Hilbert space $\mathcal{H}$ can be constructed by taking square-integrable functions on $\partial\mathcal{T}$ with respect to a natural measure. Basis states correspond to individual paths (frequencies at infinite precision). At finite depth $k < D$, a state that is localized to a particular vertex is a uniform superposition over all paths passing through that vertex:

$$
|v_k\rangle = \frac{1}{\sqrt{q^{D-k}}} \sum_{\text{paths through } v_k} |\text{path}\rangle.
$$

The state space at depth $k$ has dimension $q^k$. Descending one level (increasing $k$ by 1) multiplies the dimension by $q$—each vertex splits into $q$ children. Information about which sub-band a system occupies is encoded in which branch of the tree the state lives on.

### 3.2 Measurement as Truncation to Finite Depth

A measurement of frequency—or of any observable conjugate to scale—does not access the full infinite boundary. It resolves the system only to some finite depth $k_{\text{meas}}$, corresponding to the precision of the apparatus. The measurement outcome is a vertex at depth $k_{\text{meas}}$: a frequency band of width determined by $q^{-k_{\text{meas}}}$.

In this picture, the **collapse of the wavefunction** is not a mysterious non-unitary process but a geometric operation: selecting a single path among the $q$ children at each branching, down to the resolved depth. Before measurement, the state is spread across an unresolved subtree; after measurement, it is localized to a single branch. The Born rule emerges from the uniform weighting of paths at each branching:

$$
P(\text{outcome } v_k) = \frac{\text{number of paths through } v_k \text{ consistent with the state}}{\text{total number of paths in the state}}.
$$

**Derivation.** At the tree root, all $q^D$ boundary paths are equally weighted (the maximum-entropy prior). Descending the tree, at each vertex, the $q$ children are equally probable by symmetry—the tree has no preferred branch. The probability of reaching vertex $v_k$ (depth $k$) is the product of $1/q$ at each of the $k$ branchings: $P(v_k) = q^{-k}$. This is equivalent to the uniform measure on the boundary. When a quantum state is a superposition over a subtree $S$ containing $N_S$ boundary paths, and measurement selects a vertex $v_k$ whose subtree contains $N_{v_k}$ paths, the conditional probability is $P(v_k | S) = N_{v_k} / N_S$—a ratio of path counts. In the continuum limit $q \to 1^+$, this path-counting measure converges to the Lebesgue measure on $\mathbb{R}$, and the Born rule $|\psi(x)|^2 dx$ is recovered as the density of paths per unit frequency interval. The tree-level Born rule is thus the discrete, uniform-path-counting ancestor of the continuum Born rule.

This yields a geometric interpretation of probability as a ratio of path counts on the tree.

A crucial consequence: **measurements at different depths do not commute in the same way as in the continuum.** Two measurements that resolve the system to depths $k_1$ and $k_2$ correspond to different partitions of the tree boundary. The non-commutativity of scale and phase observables arises naturally from the tree geometry (see Section 3.3).

### 3.3 Dual Trees and Complementarity

The tree framework requires not one but **two** dual tree structures to capture the full phase space of a quantum system. The first tree organizes frequencies $f$ (the **scale tree**). The second organizes **phases** $\phi$ (the **phase tree**). A complete specification of a harmonic oscillator requires both a frequency and a phase.

These two trees are complementary in the sense of a Fourier transform. To see this explicitly, consider characters on the tree boundary. A character $\chi_u(f)$ on the frequency tree boundary $\partial\mathcal{T}_f$ is parameterized by a point $u$ on the phase tree boundary $\partial\mathcal{T}_\phi$. In the $p$-adic case, these are the additive characters $\chi_u(f) = \exp(2\pi i \{u f\}_p)$, where $\{ \cdot \}_p$ is the fractional $p$-adic part. A frequency state localized to depth $k_f$ on the scale tree (a narrow band of width $q^{-k_f}$) corresponds, under the character transform, to a phase state delocalized over the first $\sim k_f$ levels of the phase tree—a broad superposition over $q^{k_f}$ phase branches.

Conversely, precise phase localization (deep on the phase tree, depth $k_\phi$) forces frequency delocalization over $q^{k_\phi}$ scale branches. This reciprocity is the tree-geometric origin of the **uncertainty principle**:

$$
\Delta f \cdot \Delta\phi \;\sim\; q^{-|k_f - k_\phi|},
$$

where $k_f$ and $k_\phi$ are the localization depths on the two trees. The product of uncertainties is minimized when the depths are balanced ($k_f \approx k_\phi$); it grows when one tree is probed deeply and the other shallowly.

This complementarity is not an epistemic limitation but a geometric fact about dual tree structures: one cannot simultaneously be deep on both trees because depth on one corresponds to breadth on the other. The standard Heisenberg uncertainty relation $\Delta E \Delta t \geq \hbar/2$ is the Archimedean, continuum limit of this tree-level complementarity, recovered as $q \to 1^+$ with the depth variables mapped to continuous real parameters. The tree framework thus embeds the uncertainty principle in a discrete, number-theoretic foundation—it is a consequence of Pontryagin duality on the boundary of the Bruhat–Tits tree.

### 3.4 Time Emergence: The Page–Wootters Mechanism on the Tree

If the fundamental geometry is a static tree, where does time come from? The tree framework adopts the **Page–Wootters** mechanism: time is not a fundamental parameter but an emergent correlation between two subsystems.

Consider two trees: a **clock tree** $\mathcal{T}_C$ and a **system tree** $\mathcal{T}_S$. Neither contains time. But correlations between them—specifically, the alignment of their depth indices—define a joint state:

$$
|\Psi\rangle = \sum_k |k\rangle_C \otimes |\psi(k)\rangle_S,
$$

where $|k\rangle_C$ is a state of the clock tree at depth $k$, and $|\psi(k)\rangle_S$ is the state of the system conditioned on the clock reading $k$. The integer $k$ serves as an internal time parameter. As $k$ increases, the system state evolves—not because time flows, but because conditioning on larger $k$ selects finer-scale correlations.

The **arrow of time** on the tree runs from coarser to finer scales (increasing $k$). This is the direction in which branching creates new degrees of freedom, new distinguishability, and new entanglement. The thermodynamic arrow aligns with the tree-depth arrow: entropy increases as information flows from the unresolved root toward the resolved leaves. This provides a geometric origin for the second law that does not require special initial conditions—it is built into the directed structure of the tree itself.

**Caveat.** The increase in the number of states with depth—from $q^k$ vertices at level $k$—is a kinematic fact about the tree geometry. The alignment of this kinematic arrow with the thermodynamic arrow of the Second Law requires additional structure: a statistical ensemble on the tree boundary and a dynamics that drives the Page–Wootters clock parameter $k$ monotonically forward. The tree framework supplies the kinematic arrow (the directed branching structure) but does not yet provide the dynamical mechanism that links it to thermodynamic entropy production. The conjecture that the tree-depth arrow and the thermodynamic arrow coincide is natural—both point from less to more information—but remains to be demonstrated within a complete tree-level dynamics (see Open Question 3, Section 6.4).

### 3.5 The Central Structural Equation: Spectral Density

The physical content of the tree framework is encoded in the **spectral density** $J(\omega)$, which describes how a quantum system couples to its environment as a function of frequency. On the tree, the spectral density is not a smooth function but a sum of discrete peaks, one at each vertex:

$$
J(\omega) = \sum_{k=0}^{D} \sum_{v \in \text{vertices at depth } k} \gamma_{v} \, \delta(\omega - \omega_v),
$$

where $\omega_v$ is the characteristic frequency of vertex $v$, and $\gamma_v$ is the coupling strength at that vertex. The hierarchical, discrete structure of $J(\omega)$ is the central structural equation of the framework. It is this discrete spectral density that produces the non-Markovian decoherence oscillations predicted in Section 4.1.

In the continuum limit $q \to 1^+$, the sum over vertices becomes an integral, and the discrete peaks merge into a smooth function—recovering the standard Caldeira–Leggett spectral density of open quantum systems. The tree framework is thus not a rejection of the continuum but an embedding of it: the continuum is what you see when you refuse to resolve the individual branchings of the tree.

---

## 4. Experimental Predictions

The tree framework makes **three concrete falsifiable predictions** (Sections 4.1–4.3) and identifies **two research directions** (Sections 4.4–4.5). Two predictions—non-Markovian decoherence oscillations and log-periodic CMB modulations—are ready for near-term experimental testing. Each prediction and direction is accompanied by specific falsification criteria where applicable.

---

### 4.1 Prediction 1: Non-Markovian Decoherence Oscillations

**Status:** Ready for near-term superconducting qubit experiment. Numerical simulation available (`0.8_pred1_sim.py`).

#### 4.1.1 The Setup—A Tree-Structured Bath

Couple a superconducting qubit to a set of $d$ microwave resonators whose frequencies are geometrically spaced:

$$
\omega_k = \omega_0 \, q^k, \qquad k = 1, \ldots, d.
$$

With $q = 2$ (octave spacing) and $\omega_0 = 0.5$ GHz, four resonators cover 1, 2, 4, and 8 GHz—all within the operational range of standard transmon qubits. The qubit–resonator couplings decay with frequency:

$$
g_k = g_0 \, q^{-\gamma k},
$$

with $\gamma = 1$ (each octave halves the coupling) and $g_0/2\pi = 50$ MHz. The system operates at $T = 10$ mK.

The Hamiltonian is the standard pure-dephasing spin–boson model:

$$
H = \frac{\omega_q}{2} \hat{\sigma}_z + \sum_{k=1}^{d} \omega_k \hat{a}_k^\dagger \hat{a}_k + \hat{\sigma}_z \otimes \sum_{k=1}^{d} g_k (\hat{a}_k + \hat{a}_k^\dagger).
$$

Here $\omega_q = 5$ GHz is chosen off-resonant from all $\omega_k$ to ensure the dispersive regime ($|\omega_q - \omega_k| \gg g_k$).

**Why geometric spacing creates a structured bath.** A qubit coupled to a continuum of harmonic oscillators normally experiences exponential (Markovian) decay if the spectral density is smooth and broad. Here the tree framework provides a **discrete, finite set** of resonators with geometric frequencies $\omega_k = \omega_0 q^k$. This “comb” of modes, weighted by couplings $g_k = g_0 q^{-\gamma k}$, synthesises an effective spectral density

$$
J(\omega) = \pi \sum_{k=1}^{d} g_k^2 \,\delta(\omega - \omega_k)
\;\xrightarrow{d\to\infty}\; J(\omega) \propto \omega^{-2\gamma} \quad (\text{over the comb frequencies}).
$$

For $\gamma = 1$ this yields a $1/\omega^2$ decay of the spectral density. Because the number of modes is **finite** and the frequencies are **widely spaced** (octaves, $q = 2$), the bath’s correlation function does not decay monotonically. Instead, it exhibits long-lived oscillations that beat at the mode frequencies. These coherent beats cause **information backflow** from the bath to the qubit—the defining signature of non-Markovian dynamics.

With finite resonator quality factors, the delta functions broaden into Lorentzians:

$$
J(\omega) = \sum_{k=1}^{d} g_k^2 \, \frac{\eta_k / \pi}{(\omega - \omega_k)^2 + \eta_k^2}, \qquad \eta_k = \frac{\omega_k}{Q}.
$$

The tree structure enters entirely through this discrete, geometrically-spaced spectral density. For the default simulation parameters ($d = 4$, $Q = 10^6$), the resonators span 1–8 GHz with linewidths $\eta_k/2\pi = 1$–$8$ kHz. All are well within the dispersive regime ($|\omega_q - \omega_k| \geq 1$ GHz, $g_k \leq 25$ MHz, ratio $\geq 160\times$).

#### 4.1.2 The Signature—Decoherence Oscillations

If the qubit starts in a superposition $(|0\rangle + |1\rangle)/\sqrt{2}$ and the interaction is pure dephasing ($\sigma_z \sum g_k (a_k + a_k^\dagger)$), the off-diagonal coherence $\rho_{01}(t)$ evolves as

$$
\rho_{01}(t) = \rho_{01}(0) \prod_{k=1}^{d}
\exp\!\Big[ -\Big(\frac{g_k}{\omega_k}\Big)^2 (1 - \cos\omega_k t)
\coth\frac{\hbar\omega_k}{2k_B T} \Big].
$$

At $T = 10$ mK, $k_B T \approx 0.2$ GHz, so the lower modes (0.5–2 GHz) have non-negligible thermal populations ($n_{\text{th}} \lesssim 0.1$). The product form leads to **partial revivals** whenever the cosine terms from different modes accidentally re-phase. For octave spacing (frequencies 1, 2, 4, 8 GHz), the least common multiple period is long, so the initial decay is followed by irregular oscillations rather than perfect revivals. The coherence shows:

- A **fast initial drop** governed by the strongest-coupled low-frequency modes.
- **Oscillatory “kicks”** with frequencies $\omega_k$ and their harmonics.
- An overall envelope that decays more slowly than a single exponential; the decay becomes power-law if the number of modes is large.

At $T = 0$ and with finite resonator linewidths $\eta_k = \omega_k / Q$, the exact coherence function reduces to

$$
C(t) \equiv \frac{|\rho_{01}(t)|}{|\rho_{01}(0)|}
= \exp\!\left[-2\sum_{k=1}^{d} \left(\frac{g_k}{\omega_k}\right)^{\!2}
\Bigl(1 - e^{-\eta_k t}\cos\omega_k t - \frac{\eta_k}{\omega_k} e^{-\eta_k t}\sin\omega_k t\Bigr)\right].
$$

Expanding for small $(g_k/\omega_k)^2$:

$$
C(t) \approx e^{-\kappa} \Bigl[1 + 2\sum_k a_k e^{-\eta_k t}\cos\omega_k t + \mathcal{O}(a^2)\Bigr],
$$

where $a_k \equiv (g_k/\omega_k)^2$ and $\kappa \equiv 2\sum_k a_k$. The coherence oscillates at the resonator frequencies $\omega_k$ with amplitudes $2(g_k/\omega_k)^2$. For realistic parameters ($g_0/2\pi = 50$ MHz, $\omega_1/2\pi = 1$ GHz, $Q = 10^6$), the fundamental oscillation amplitude is $2(g_1/\omega_1)^2 \approx 0.12\%$.

If the coupling is transverse ($\sigma_x$ instead of $\sigma_z$), the qubit exhibits **population oscillations** in addition to dephasing, showing similar non-Markovian structure. The pure-dephasing case is the cleanest test of the tree geometry since it isolates the spectral density’s influence on coherence without energy exchange.

#### 4.1.3 Measurement Strategy

The primary strategy is **frequency-domain noise spectroscopy**:
- **CPMG / spin-locking** sequences act as bandpass filters for environmental noise.
- Sweeping the filter frequency probes $J(\omega)$.
- The tree prediction is a **sparse spectrum**: narrow peaks at geometrically-spaced frequencies $\omega_k$, with negligible spectral weight in the gaps.

The distinctive signature is the **absence** of noise between tree levels—the ultrametric “no partial overlap” property as an observable.

**Experimental realization.** The parameters are carefully chosen to match standard superconducting qubit hardware. The resonator frequencies (1–8 GHz) are easily reached with lumped-element resonators or transmission-line stubs. The decaying coupling law $g_k \propto 1/\omega_k$ (for $\gamma = 1$) can be engineered by varying coupling capacitances or by deliberately shaping the qubit’s electromagnetic environment to produce the desired spectral density. All four resonators can be implemented as separate on-chip cavities capacitively coupled to a single transmon qubit. The qubit frequency is placed at 5 GHz, far from any resonator, to ensure the coupling is well-approximated by a dispersive interaction. Time-domain measurements of the qubit’s $T_2^*$ or Ramsey fringes directly reveal the oscillatory decoherence envelope.

At 10 mK, the 1 GHz mode has $n_{\text{th}} \approx 0.008$—essentially at vacuum. The higher modes are even colder. This small thermal population adds a slight incoherent dephasing channel but does not wash out the non-Markovian oscillations. The dominant noise source is intrinsic qubit dephasing ($T_2^* \sim 20\ \mu\text{s}$, corresponding to a 50 kHz dephasing rate), which exceeds the tree-induced decay rate (9 Hz) by a factor of $\sim 5,500$. Detecting the tree signal therefore requires either longer integration or frequency-domain filtering to isolate the narrow spectral peaks from the broadband qubit noise floor.

#### 4.1.4 Falsification Criteria

Falsified at $\geq 5\sigma$ if, for any $q \in [1.5, 3.0]$:
1. No narrow spectral peaks are observed at integer powers of $q$, **or**
2. The measured spectral density between peaks exceeds $0.1 \times$ the peak height, **or**
3. The peak coupling strengths do not satisfy $g_k = g_0 q^{-\gamma k}$ for any $\gamma \in [0, 2]$.

**Detection requirement.** Validating criterion (1) requires sensitivity to at least two tree vertices—i.e., detection of narrow spectral peaks at two distinct frequencies whose ratio is an integer power of $q$. A single detected peak is consistent with the tree framework (it identifies one vertex) but is insufficient to verify the geometric spacing $\omega_k = \omega_0 q^k$ or to independently measure $q$. A realistic SNR analysis (see Section 6.5) shows that with present cQED parameters ($g_0/2\pi = 50$ MHz, $Q = 10^6$, $T = 10$ mK, $10^6$ repetitions), only the fundamental harmonic (1 GHz, SNR $\sim 6\sigma$) is practically measurable; higher harmonics fall below the $5\sigma$ detection threshold. Detecting a second harmonic and thereby measuring $q$ requires either stronger coupling ($g_0/2\pi \gtrsim 200$ MHz), longer integration, or frequency-domain noise spectroscopy with enhanced sensitivity.

#### 4.1.5 Why This Matters

Non-Markovian oscillations are not merely a curiosity—they demonstrate that the qubit retains a memory of its environment and can, in principle, recover lost coherence. In quantum technologies, such structured baths can be harnessed for **coherence protection** (dynamical decoupling or error-corrected gates) or as a resource for **quantum memory**. The geometric tree structure is a minimal model of a fractal spectral density. Its experimental realization would validate the tree framework’s central claim—that frequency space possesses discrete, ultrametric structure—and open the door to engineering arbitrary open-system dynamics on a chip. Moreover, detecting the same scaling ratio $q$ in both a tabletop quantum experiment (Prediction 1) and the cosmic microwave background (Prediction 2) would connect the smallest controllable quantum systems to the largest observable structure, unified by a single geometric principle.

---

### 4.2 Prediction 2: Log-Periodic CMB Oscillations

**Status:** Constrained by Planck 2018 ($A \lesssim 5\%$ at 95% CL). CMB-S4 will provide a definitive test.

#### 4.2.1 From Frequency Tree to Cosmological Perturbations

If frequency space is a discrete tree, Fourier duality implies that primordial density perturbations inherit the same discrete scale invariance (DSI):

$$
\mathcal{P}_\mathcal{R}(q k) = \mathcal{P}_\mathcal{R}(k).
$$

The general solution is a log-periodic modulation of the standard spectrum:

$$
\boxed{\mathcal{P}_\mathcal{R}(k) = A_s \left(\frac{k}{k_*}\right)^{n_s-1}
\times \left[1 + A \cos\!\left(\frac{2\pi}{\log q} \log\frac{k}{k_*} + \phi\right)\right]},
$$

where $A$ is the modulation amplitude ($\sim 0.5\%$–$5\%$), $k_*$ is the pivot scale, and the period in $\log_{10} k$ is $\log_{10} q$ ($\approx 0.301$ for $q = 2$).

#### 4.2.2 Observable in the CMB

The CMB temperature power spectrum inherits the same log-periodic pattern:

$$
\mathcal{D}_\ell^{\rm TT} = \mathcal{D}_\ell^{\rm TT, \Lambda{\rm CDM}}
\times \left[1 + A_{\rm eff} \cos\!\left(\frac{2\pi}{\log q} \log\frac{\ell}{\ell_*} + \tilde{\phi}\right)\right].
$$

For $q = 2$ and $\ell_* \approx 700$, there are $\sim 10$ full oscillation cycles in the Planck range $2 \leq \ell \leq 2500$.

#### 4.2.3 Current Constraints

| Observatory | $5\sigma$ Sensitivity to $A$ (for $q=2$) |
|:---|---:|
| Planck 2018 | $\sim 3.2\%$ |
| CMB-S4 (projected) | $\sim 0.7\%$ |
| **Tree prediction range** | $A \sim 0.5\%$–$5\%$ |
| **Falsification threshold** | $A < 0.1\%$ (requires beyond-CMB-S4 sensitivity) |

Current Planck searches constrain generic log-periodic modulations to $A \lesssim 5\%$ at 95% CL. The tree prediction survives but is under pressure. A Fisher forecast (see `0.8_pred2_cmb.py`) gives CMB-S4 a $5\sigma$ detection floor of $A_{\min} \approx 0.67\%$ for $q=2$. CMB-S4 can therefore **constrain** the tree prediction to the $A \lesssim 0.7\%$ level but cannot reach the definitive $A < 0.1\%$ falsification threshold—that would require a next-generation CMB experiment with $\gtrsim 7\times$ the sensitivity of CMB-S4.
#### 4.2.4 Falsification Criteria

Falsified at 95% CL if:
1. A dedicated search for log-periodic modulations with period $\log q$ for any $q \in [1.5, 3.0]$ yields $A < 0.5\%$ (CMB-S4 $3\sigma$ level; definitive falsification at $A < 0.1\%$ requires a next-generation experiment), **or**
2. The modulation pattern is inconsistent with the lab-measured value of $q$ from Prediction 1.

A positive detection would be extraordinary: the same tree geometry, with the same $q$, shaping both a tabletop quantum experiment and the CMB.

---

### 4.3 Prediction 3: Fermion Mass Hierarchy

**Status: Data-limited.** The tree fit to the nine known fermion masses (3 charged leptons + 6 quarks) yields $p = 0.346$ for $q=2$ under the uniform-span null model—not statistically significant at the 95% confidence level. The three neutrino masses remain unmeasured individually. This prediction should be understood as a **structural hypothesis awaiting data**: it makes a definite claim about how masses should organize (near tree vertices, with log-ratios approximating integer multiples of $\log q$), but this claim cannot be tested at the $p < 0.01$ level until neutrino masses are measured with sufficient precision. The prediction sharpens in parallel with neutrino experiments (KATRIN, Project 8, cosmological surveys).

If the tree organizes all frequencies, then the rest masses of fundamental fermions—which are Compton frequencies $f = mc^2/h$—should exhibit a hierarchical, tree-like organization. The twelve fermion masses (three charged leptons, six quarks, three neutrinos) span roughly twelve orders of magnitude from the lightest neutrino to the top quark.

**Quantitative prediction:** When expressed as Compton frequencies and plotted on a logarithmic scale, the twelve masses should cluster at tree vertices—their log-ratios should approximate integer multiples of $\log q$ for some scaling ratio $q$ consistent with Predictions 1 and 2. The tree framework constrains the mass **ratios**, not the absolute scale, so the prediction is independent of the unknown overall mass scale.

**Current status—charged leptons and quarks:**

| Particle | Mass (MeV/$c^2$) | $\log_{10}(m/m_e)$ |
|:---------|:-------------------|:---------------------|
| $e$ | 0.511 | 5.708 |
| $u$ | 2.16 | 6.335 |
| $d$ | 4.67 | 6.669 |
| $s$ | 93.4 | 7.970 |
| $\mu$ | 105.66 | 8.024 |
| $c$ | 1275 | 9.106 |
| $\tau$ | 1776.86 | 9.250 |
| $b$ | 4180 | 9.621 |
| $t$ | 172,500 | 11.237 |

**Tree fit analysis (Python-executed, $n_{\text{trials}} = 10^4$, uniform-span null model):** For $q = 2$ (octave scaling, the value from Prediction 1), the RMS residual between the observed mass logarithms and the nearest tree vertex is 0.0806 in $\log_{10}$ units—meaning typical masses are within a factor of $10^{0.08} \approx 1.2$ of a tree vertex. A randomization test yields $p = 0.346$, meaning the observed clustering is not statistically distinguishable from random placement at the 95% confidence level. The best-fit $q$ among $\{1.5, 2.0, e, 3.0\}$ is $q = 1.5$ by RMS (0.0510), with $q = 2$ at 0.0806; however, no $q$ achieves statistical significance. Full results in Section 4.3.1.

**Neutrino masses:** The three neutrino masses are known only through mass-squared differences from oscillation experiments ($\Delta m^2_{21} \approx 7.5 \times 10^{-5}$ eV$^2$, $|\Delta m^2_{31}| \approx 2.5 \times 10^{-3}$ eV$^2$). Individual masses are bounded above by KATRIN ($m_{\nu_e} < 0.8$ eV) and cosmological constraints ($\sum m_\nu < 0.12$ eV). Once absolute neutrino masses are measured (e.g., by KATRIN, Project 8, or future cosmological surveys), three additional data points will be added to the tree fit, substantially improving statistical power.

**Falsification criteria:** The tree framework is falsified for mass ratios if:
1. A statistically significant fit ($p < 0.01$) to integer powers of any $q \in [1.5, 3.0]$ cannot be achieved given the precision of all twelve masses (including neutrinos), **or**
2. The best-fit $q$ from the mass hierarchy differs from the laboratory-measured $q$ from Prediction 1 at $>3\sigma$.

**Current assessment:** Prediction 3 is **data-limited**—the neutrino mass uncertainties preclude a definitive test. The hierarchical, factor-of-10 to factor-of-100 spacing between the three fermion generations is qualitatively consistent with a tree structure, but quantitative confirmation awaits improved neutrino mass measurements. This prediction sharpens in parallel with experimental progress in neutrino physics.

#### 4.3.1 Reproducible Tree Fit Results

The analysis was reproduced and extended in `0.8_fermion_mass.py`. Results for four candidate scaling ratios (10,000-trial randomization test, uniform-span null):

| q | RMS residual | p-value | Significance |
|:--|:-------------|:--------|:-------------|
| 1.5 | 0.0510 | 0.527 | Not significant |
| 2.0 | 0.0806 | 0.346 | Not significant |
| e $\approx$ 2.7 | 0.1046 | 0.151 | Not significant |
| 3.0 | 0.1221 | 0.243 | Not significant |

No q achieves p < 0.05 with the current nine known masses. The table uses the uniform-span null model (random placement of 9 points over the observed span), which is the simpler and more transparent baseline. Both the header analysis and this reproducible table agree: Prediction 3 is **not currently falsifiable**.

#### 4.3.2 Generation Structure

Ratios between successive fermion generations reveal suggestive but statistically inconclusive patterns:

| Ratio | Value | $\log_{10}$ | Nearest tree k | Deviation |
|:------|:------|:-------------|:---------------|:----------|
| m$_\mu$ / m$_e$ | 206.8 | 2.315 | k = 8 | 30.8% |
| m$_\tau$ / m$_\mu$ | 16.8 | 1.226 | k = 4 | **7.2%** |
| m$_c$ / m$_u$ | 590.3 | 2.771 | k = 9 | 20.5% |
| m$_t$ / m$_c$ | 135.3 | 2.131 | k = 7 | **8.0%** |
| m$_b$ / m$_s$ | 44.8 | 1.651 | k = 5 | 48.4% |

The $\tau/\mu$ and t/c ratios align with integer tree steps to within <10% of the tree period—the cleanest signals in the current data. The b/s ratio (48.4% deviation) is the worst fit. The generation structure does not reach collective statistical significance.

#### 4.3.3 Koide Formula

The charged lepton masses satisfy the Koide relation to high precision:

$$
K = \frac{m_e + m_\mu + m_\tau}{(\sqrt{m_e} + \sqrt{m_\mu} + \sqrt{m_\tau})^2} = 0.666659 \approx \frac{2}{3}.
$$

In the tree framework, a relation of this form could arise if the three charged lepton masses occupy three specific tree vertices. For q = 2, the best-fit vertex depths are k = 0 (e), k = 8 ($\mu$), k = 12 ($\tau$), giving log$_{10}$ ratios of 2.408 and 3.613 vs. observed 2.315 and 3.541. The Koide formula constrains the absolute mass scale—information the pure tree fit (which constrains only ratios) does not provide. A tree-theoretic derivation of the Koide formula would require specifying the absolute scale (see Open Question 5, Section 6.4).

#### 4.3.4 Neutrino Sensitivity

A Monte Carlo power analysis (5000 trials per scenario) adding 1–3 neutrino masses in the 0.001–0.1 eV range shows that even with all three neutrino masses known, the median RMS residual remains $\sim$0.08 and the p-value distribution does not cross the p < 0.05 threshold. The limiting factor is not only the missing neutrino masses but the intrinsic scatter among the nine known masses. Achieving p < 0.01 will require either a larger fermion sample (e.g., beyond-Standard-Model particles) or a statistical method that incorporates the $\gtrsim 10\%$ uncertainties on light quark masses.

Figure 2 (see `0.8_fig_fermion_mass.png`) visualizes the tree fit for q = 2, showing observed masses and their nearest tree vertices.

---

### 4.4 Direction 1: Fault-Tolerant Quantum Architecture

**Status:** Theoretical proposal—engineering timeline set by quantum computing maturation, not by this framework.

The tree geometry is both a description of nature and a **prescription for engineering**. The ultrametric property—balls are nested or disjoint, never partially overlapping—has a computational interpretation: errors on different branches are naturally isolated.

**Consequence:** A quantum computer whose logical qubits are encoded on the boundary of a Bruhat–Tits tree, with error correction implemented hierarchically, would achieve a fault-tolerance threshold that scales **exponentially** with tree depth (versus polynomially for surface codes). This is a theoretical claim about the information-theoretic properties of tree geometries, not a near-term experimental prediction.  

Concretely, the ultrametric property—balls never partially overlap—eliminates crosstalk between logically distinct error-correction patches: a physical error on one branch cannot propagate to neighboring branches because the tree structure enforces nested-or-disjoint boundaries. In surface codes, the overhead to suppress logical error to probability $p_L$ scales as $\mathcal{O}(\log^2(1/p_L))$; a tree-based code with $q$-ary branching at depth $k$ handles $q^k$ logical qubits with only $k$ levels of syndrome processing. At $q=2$ and depth $k=20$, this supports $\sim 10^6$ logical qubits with 20 levels of classical post-processing—a dramatic reduction in classical decoding complexity. The proposal remains theoretical; no physical realization of tree-based error correction has been demonstrated.

---

### 4.5 Direction 2: Adelic Unification

**Status:** Long-term mathematical research program—not constrained by current experimental capabilities.

Ostrowski’s theorem: $\mathbb{R}$ and $\mathbb{Q}_p$ are the only two completions of $\mathbb{Q}$. If both play physical roles—$\mathbb{R}$ for spacetime, $\mathbb{Q}_p$ (via the Bruhat–Tits tree) for frequency space—then the full symmetry group of nature should be **adelic**.

**Consequence:** Physical laws should treat all places (Archimedean and $p$-adic) on an equal footing. The adele ring $\mathbb{A}_\mathbb{Q}$ is the natural object for a unified formulation. This connects the tree framework to the Langlands program in number theory.

**Testability:** Adelic unification is the least experimentally constrained prediction. Its primary test is internal consistency: can the known forces and particles be organized into adelic representations? This is a mathematical program running in parallel with the experimental predictions 1–4.  

A concrete entry point: the Standard Model gauge group $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ may be a “real-place shadow” of adelic objects—the adele ring $\mathbb{A}_\mathbb{Q}$ is the natural home for representations of all completions of $\mathbb{Q}$ simultaneously. If the gauge group at the real place emerges from a product over all places, the observed coupling constants should be constrained by adelic consistency conditions. This connects to the Langlands program’s goal of expressing automorphic $L$-functions—which naturally live on $\mathbb{A}_\mathbb{Q}$—as physical observables. The connection remains speculative but provides a mathematical roadmap for unification that does not require postulating new symmetries beyond those already forced by Ostrowski’s theorem.

---

## 5. Mathematical Foundations

This section provides the rigorous mathematical backing for the tree framework, intended for readers who wish to verify the claims at full depth. The material is self-contained at the level of advanced undergraduate mathematics (real analysis, abstract algebra) but can be skipped on a first reading.

### 5.1 Ostrowski’s Theorem

**Theorem (Ostrowski, 1916).** Every non-trivial absolute value $|\cdot|$ on $\mathbb{Q}$ is equivalent either to the standard real absolute value $|\cdot|_\infty$ or to a $p$-adic absolute value $|\cdot|_p$ for some prime $p$.

Here, “equivalent” means they induce the same topology. An **absolute value** is a function $|\cdot| : \mathbb{Q} \to \mathbb{R}_{\geq 0}$ satisfying:
1. $|x| = 0 \iff x = 0$,
2. $|xy| = |x|\,|y|$,
3. $|x + y| \leq |x| + |y|$ (Archimedean) or $|x + y| \leq \max(|x|, |y|)$ (non-Archimedean).

The real absolute value satisfies the ordinary triangle inequality; the $p$-adic absolute value satisfies the **strong triangle inequality** (ultrametric). Ostrowski’s theorem states that these are the **only** two types.

**Physical significance.** Any physical theory built on a notion of distance derived from $\mathbb{Q}$ must choose between these two geometries. Conventional physics chooses the Archimedean completion $\mathbb{R}$. The tree framework proposes that frequency space is the non-Archimedean completion $\mathbb{Q}_p$.

### 5.2 $p$-adic Numbers

For a fixed prime $p$, any non-zero rational $x \in \mathbb{Q}$ can be written uniquely as

$$
x = p^{v_p(x)} \cdot \frac{a}{b},
$$

where $v_p(x) \in \mathbb{Z}$ (the $p$-adic valuation) and $a, b$ are integers coprime to $p$. The $p$-adic absolute value is:

$$
|x|_p = p^{-v_p(x)}, \qquad |0|_p = 0.
$$

Numbers divisible by high powers of $p$ are “small” in the $p$-adic sense. The completion of $\mathbb{Q}$ with respect to $|\cdot|_p$ is the field $\mathbb{Q}_p$ of $p$-adic numbers. Elements of $\mathbb{Q}_p$ can be represented as infinite series:

$$
x = \sum_{n = v_p(x)}^{\infty} a_n p^n, \qquad a_n \in \{0, 1, \ldots, p-1\},
$$

convergent in the $p$-adic metric. This is a direct analogue of decimal expansion for $\mathbb{R}$, but with the crucial difference that the ultrametric property makes convergence behave very differently.

### 5.3 The Bruhat–Tits Tree $\mathcal{T}_p$

The **Bruhat–Tits tree** $\mathcal{T}_p$ is an infinite $(p+1)$-regular tree that serves as the natural geometric object for $\mathbb{Q}_p$. Its construction:

**Vertices.** Equivalence classes of $\mathbb{Z}_p$-lattices in $\mathbb{Q}_p^2$. Two lattices $L_1, L_2$ are equivalent if $L_1 = \lambda L_2$ for some $\lambda \in \mathbb{Q}_p^\times$. The set of vertices forms an infinite tree where each vertex has degree $p+1$.

**Edges.** Two vertices are adjacent if their representative lattices satisfy $pL_1 \subset L_2 \subset L_1$ (or vice versa).

**Boundary.** The set of ends (equivalence classes of infinite geodesic rays) is the $p$-adic projective line:

$$
\partial\mathcal{T}_p \;\cong\; \mathbb{P}^1(\mathbb{Q}_p) = \mathbb{Q}_p \cup \{\infty\}.
$$

Each boundary point corresponds to a $p$-adic number (or $\infty$), specified to infinite precision—exactly as the infinite paths on the frequency tree correspond to frequencies at infinite precision.

**Ultrametric on the boundary.** For $x, y \in \partial\mathcal{T}_p$, the tree distance is:

$$
d_T(x, y) = p^{-\ell},
$$

where $\ell$ is the depth of the vertex where the unique geodesics from a fixed root to $x$ and $y$ first diverge. This satisfies the strong triangle inequality identically to the frequency tree distance of Section 2.4.

### 5.4 From Tree to Continuum: The Limit $q \to 1^+$

**Mathematical note.** The Bruhat–Tits tree $\mathcal{T}_p$ (Section 5.3) is defined for a prime $p$ and is $(p+1)$-regular. The general $q$-ary tree used throughout the physics sections (Sections 2–4) is defined for integer $q \geq 2$. These are distinct objects: $\mathcal{T}_p$ provides the rigorous $p$-adic foundation; the general $q$-ary tree provides the physical phenomenology. The two coincide when $q$ is prime (see the terminology note in Section 2.5). The continuum limit discussed below applies to the general $q$-ary tree; a continuum limit of $\mathcal{T}_p$ itself would instead be obtained through the adelic product over all primes (Section 5.5).

The standard continuous frequency line $\mathbb{R}$ is not an alternative to the tree—it is a **limit** of the tree when the branching factor approaches unity. Consider a sequence of $q$-ary trees with $q = 1 + \varepsilon$, $\varepsilon \to 0^+$. As the branching becomes infinitely fine:

- The number of vertices at depth $k$ is $q^k = (1+\varepsilon)^k$, which grows without bound for any fixed $k$ as $\varepsilon$ decreases. The continuous limit requires the simultaneous limit $k \to \infty$, $\varepsilon \to 0$ with $k\varepsilon$ held finite.
- The ultrametric distance $d_T = q^{-\ell}$ becomes an exponential of the continuous depth parameter.
- The spectral density $J(\omega) = \sum_k \sum_v \gamma_v \delta(\omega - \omega_v)$ becomes an integral $J(\omega) = \int \gamma(u) \, du$ over a continuous parameter $u$.
- The discrete sum over paths becomes a path integral over continuous functions.

In this limit, the Schrödinger equation emerges as the infinitesimal generator of depth evolution, and the standard formalism of quantum mechanics on $\mathbb{R}$ is recovered. The tree framework is thus not a rival to standard quantum theory but an **ultraviolet completion** of it—the discrete tree provides the short-distance regulator that the continuum lacks.

The physical value of $q$ is not determined *a priori* by the framework. It is an empirical parameter, to be measured in the laboratory (Prediction 1). The fact that $q$ could be $2$, $e$, $3$, or any other value reflects the choice of multiplicative ruler (Section 2.2). The prime $p$ in the Bruhat–Tits construction would then be either $p = q$ (if $q$ is prime) or a product of primes.

### 5.5 Langlands Program and Adelic Unification

The tree framework naturally points toward the **Langlands program**, a vast web of conjectures connecting number theory (Galois representations) to harmonic analysis (automorphic forms). The Bruhat–Tits tree is a central object in the $p$-adic Langlands correspondence for $\mathrm{GL}_2$.

In physical terms: if frequency space is a Bruhat–Tits tree, then the “wavefunctions” on the tree boundary are automorphic forms, and the symmetry group acting on the tree is $\mathrm{PGL}_2(\mathbb{Q}_p)$. The adele ring $\mathbb{A}_\mathbb{Q}$—the restricted product of $\mathbb{R}$ and all $\mathbb{Q}_p$—is the natural object on which to formulate a theory that treats all completions of $\mathbb{Q}$ on an equal footing.

This connects the tree framework to the broader program of **adelic physics**, which seeks to ground physical law in the number-theoretic structure of the rational numbers. While this is the most speculative aspect of the framework, it is also the one with the deepest mathematical pedigree.

---

## 6. Discussion

### 6.1 What the Tree Framework Is—and What It Is Not

The tree framework is a **geometric proposal**: the appropriate geometry for the space of physical frequencies is a discrete, ultrametric Bruhat–Tits tree. It is not a new force, a new particle, or a modification of the Standard Model Lagrangian. It is a claim about the underlying mathematical structure of scale—a structure that, once taken seriously, generates concrete, testable predictions.

The framework is not a rejection of the continuum. It is an **embedding** of the continuum as an emergent limit. Just as fluid dynamics emerges from molecular dynamics when you coarse-grain over many particles, the continuous frequency line $\mathbb{R}$ emerges from the tree when you refuse to resolve individual branchings. The standard formalism of quantum mechanics—Hilbert spaces, unitary evolution, the Schrödinger equation—is the $q \to 1^+$ limit of the tree framework.

### 6.2 The Scaling Ratio $q$ and the Fine-Structure Constant

A central open question: **what determines $q$?** The tree framework does not predict $q$ from first principles; it treats $q$ as an empirical parameter to be measured. But one possibility, tantalizing and highly speculative, is that $q$ is related to the fine-structure constant $\alpha \approx 1/137$. The electron’s Compton frequency and the Rydberg frequency are related by a factor of $\alpha^2/2$; the ratio of the electron to proton mass is approximately $6\pi^5 \approx 1836$. These numerical coincidences, if they are not coincidences, suggest that dimensionless ratios in physics may encode the tree’s branching structure. If $q$ is measured as $2.000 \pm 0.001$ in the laboratory (Prediction 1), the question of why nature chose that particular value becomes pressing.

### 6.3 Connections to Other Programs

**Tensor networks and holography.** The Multiscale Entanglement Renormalization Ansatz (MERA) represents quantum critical ground states as tensor networks on a tree. The tree geometry of MERA is a discrete realization of the hyperbolic geometry of anti-de Sitter space—the bulk geometry in the AdS/CFT correspondence. This suggests a deep connection: if frequency space is a tree, then the “frequency direction” in physical theories may be geometrically analogous to the radial direction in AdS. The tree framework may provide a new entry point to holographic duality, with the tree boundary playing the role of the CFT and the tree interior playing the role of the bulk.

**Quantum gravity.** The tree framework cures the Planck-scale ultraviolet catastrophe without quantizing gravity per se: by making high-frequency modes discrete and physically inaccessible, it provides a natural short-distance cutoff. The Planck frequency is simply the deepest resolvable vertex on the tree, and modes beyond it do not exist because the tree does not branch further.

**Conformal field theory.** The scaling operator in conformal field theory generates multiplicative rescalings of coordinates—exactly the operation that moves between levels on the tree. The discrete spectrum of scaling dimensions in rational CFTs may reflect an underlying tree structure in the space of scaling operators.

### 6.4 Open Questions

1. **What is $q$?** Is it $2$, a prime, or something else? Can it be derived from first principles (e.g., from the fine-structure constant or the Langlands program) or must it be measured?

2. **Why one tree?** Ostrowski’s theorem gives one $p$-adic completion per prime $p$. Is there a *single* $p$ (a single tree) for all of physics, or does each interaction have its own tree with its own $p$? If q is measured as $2.000 \pm 0.001$ in Prediction 1, does that select a specific prime or remain ambiguous?

3. **Tree dynamics.** The framework describes the static geometry of frequency space, but what are the tree’s dynamics? How do states evolve on the tree, and what are the equations of motion for tree-level degrees of freedom? The Page–Wootters mechanism provides a kinematic arrow of time (Section 3.4), but what is the Hamiltonian that drives evolution along that arrow?

4. **Gravity.** How does general relativity—a theory of smooth spacetime—couple to a discrete frequency tree? Does the tree framework modify the gravitational sector, or only the matter sector? If the tree provides a UV cutoff at the Planck frequency, does this affect the cosmological constant problem?

5. **The measurement problem.** The tree framework provides a geometric interpretation of wavefunction collapse (Section 3.2), but does it solve the measurement problem, or merely reframe it? The Born rule emerges from uniform path-counting, but the transition from superposition to a single branch remains a selection rule—what picks the branch?

6. **Neutrino mass timeline.** When will absolute neutrino mass measurements reach the precision needed to bring the fermion mass tree fit (Section 4.3) below p < 0.01? KATRIN’s projected sensitivity is $m_{\nu_e} \sim 0.2$ eV (90% CL); Project 8 aims for $\sim 0.04$ eV. Even with all three masses measured, the power analysis (Section 4.3.4) suggests p < 0.01 requires either a larger fermion sample or a method that incorporates quark mass uncertainties.

7. **q universality across sectors.** The framework assumes the same q applies to all three predictions—decoherence (electromagnetic/weak), CMB (gravitational/primordial), and fermion masses (Yukawa). But is q-universality required by the framework, or could different sectors have different q values while still being organized as trees? A positive detection with different q values in different experiments would constrain the “one tree vs. many trees” question.

8. **Adelic dynamics.** If the adelic framework (Section 5.5) is correct, what does a dynamical equation look like that simultaneously involves the real place ($\mathbb{R}$) and all $p$-adic places ($\mathbb{Q}_p$)? Is there an adelic Schrödinger equation, and does it make predictions beyond those of the single-tree framework?

9. **Connection to holography.** The tree geometry (MERA) has a known connection to AdS/CFT holography (Section 6.3). Does the frequency tree correspond to a specific bulk geometry? Can holographic techniques be used to compute tree-level observables?

10. **What would falsify the framework decisively?** The paper provides falsification criteria for each prediction, but what is the *minimal* experimental result that would kill the entire framework—not just one prediction? If Prediction 1 fails but Prediction 2 succeeds, does the framework survive in modified form?

    **Answer.** The entire framework rests on a single physical claim: that the spectral density $J(\omega)$ of quantum systems is discrete and tree-structured, with peaks at $\omega_k = \omega_0 q^k$ for some $q$. The minimal fatal result is therefore: **a dedicated search for log-periodic signatures in any physical domain—decoherence, CMB, or fermion masses—that excludes $A > 0.1\%$ for all $q \in [1.5, 3.0]$ with a tree-structured pattern.** Concretely, if CMB-S4 or a successor experiment constrains log-periodic modulation to $A < 0.1\%$ across the full $q$ range, and if Prediction 1 finds no sparse spectral peaks after a dedicated search in cQED systems (null result at $>5\sigma$ on criterion 4.1.4 for all $q$), then the tree framework has no empirical support and should be abandoned as a physical theory—though it may survive as a useful phenomenological tool (like the renormalization group). A mixed outcome (e.g., Prediction 1 positive but Prediction 2 null) would constrain but not kill the framework: it would indicate that the tree geometry is sector-dependent, requiring multiple trees with different $q$ values.

### 6.5 Honest Audit

The tree framework is speculative. It makes contact with established mathematics (Ostrowski, Bruhat–Tits, Langlands) and established physics (open quantum systems, CMB cosmology, the renormalization group), but the central claim—that frequency space *is* a tree—is radical. The framework could be wrong in several ways:

- Prediction 1 could yield null results: the spectral density of a multi-resonator system could show no sparse structure, or the measured peak spacings could be inconsistent with any $q$.
- **Near-term limitation—single-harmonic detection.** Even if Prediction 1 returns a positive result, a realistic analysis with $g_0/2\pi = 50$ MHz, $Q = 10^6$, $T = 10$ mK, and $10^6$ repetitions shows that only the fundamental harmonic (1 GHz, SNR $\sim 6\sigma$) is practically measurable. Higher harmonics fall below a $5\sigma$ detection threshold unless coupling strengths exceed $\sim 200$ MHz—challenging in current cQED platforms. Consequently, confirming the geometric progression $\omega_k = \omega_0 q^k$ (and thereby measuring $q$) will require either stronger coupling, longer integration times, or frequency-domain noise spectroscopy with enhanced sensitivity. Until at least two tree vertices are resolved, Prediction 1 can establish the existence of a single spectral peak but cannot independently verify the tree geometry.
- Prediction 2 could be constrained by CMB-S4: log-periodic modulations can be excluded to $A \lesssim 0.7\%$ ($5\sigma$), putting pressure on the tree parameter space. A definitive falsification at $A < 0.1\%$ requires a next-generation CMB experiment—CMB-S4 alone cannot reach this threshold (see Fisher forecast, Section 4.2.3).
- The tree might be a useful *effective* description (like the renormalization group) rather than a *fundamental* geometry—a phenomenological tool rather than a truth about nature.
- The entire framework might be a mathematical coincidence: the tree appears in number theory, MERA, spin glasses, and wavelets for independent reasons, with no deep physical connection between them.

The honest position is that the tree framework is a **bold conjecture awaiting experimental judgment**. The virtue of the framework is not that it is certainly true, but that it is certainly testable.

---

## 7. Conclusion

This paper has proposed that the fundamental geometry of physical frequencies is not the continuous real line $\mathbb{R}$ but a discrete, ultrametric Bruhat–Tits tree $\mathcal{T}_p$. The proposal is motivated by:

1. **Ostrowski’s theorem:** $\mathbb{R}$ and $\mathbb{Q}_p$ are the only two completions of the rationals. Physics has built everything on $\mathbb{R}$; the tree framework explores what happens when we take $\mathbb{Q}_p$ seriously for the space of frequencies.

2. **The multiplicative structure of measurement:** When we choose a multiplicative ruler for frequency, the natural geometry is a tree—not because nature is “banded” but because the ruler itself imposes a hierarchical structure.

3. **Four independent discoveries:** The same tree geometry appears in number theory (Bruhat–Tits), particle physics (RG, spin glasses), condensed matter (MERA), and signal processing (wavelets). The convergence is unlikely to be an accident.

4. **Testable predictions:** The framework makes three concrete falsifiable predictions. Two—non-Markovian decoherence oscillations and log-periodic CMB modulations—are within reach of current or near-term experiments. A third—a hierarchical organization of fermion masses—sharpens as measurements improve. Two additional research directions—tree-based quantum error correction and adelic unification—are identified as longer-term consequences.

The framework is speculative. It could be wrong. But it is wrong in a precise, testable way, and that is its chief virtue. If a superconducting qubit coupled to geometrically-spaced resonators shows a sparse noise spectrum with peaks at $\omega_0 q^k$, and if the CMB shows log-periodic modulations with the same period $\log q$, then something deep is happening—something that connects a tabletop quantum experiment to the largest structure in the observable universe through the geometry of a tree.

If these signatures are absent—if the noise spectrum is smooth, if the CMB is featureless at the $0.1\%$ level—then the tree framework is falsified, and we will have learned that the geometry of frequency, whatever it is, is not a tree. Either outcome advances our understanding.

The tree framework is offered in that spirit: as a precise conjecture, awaiting experimental judgment.


## References

1.  **Ostrowski, A.** (1916). Über einige Lösungen der Funktionalgleichung $\varphi(x) \cdot \varphi(y) = \varphi(xy)$. *Acta Mathematica*, 41, 271–284.  
    *The theorem that every absolute value on $\mathbb{Q}$ is either Archimedean or $p$-adic.*

2.  **Bruhat, F. & Tits, J.** (1972). Groupes réductifs sur un corps local I. *Publications Mathématiques de l’IHÉS*, 41, 5–251.  
    *Construction of the Bruhat–Tits tree and its role in $p$-adic Lie groups.*

3.  **Page, D. N. & Wootters, W. K.** (1983). Evolution without evolution: Dynamics described by stationary observables. *Physical Review D*, 27(12), 2885–2892.  
    *The proposal that time is an emergent correlation between subsystems.*

4.  **Wheeler, J. A.** (1968). Superspace and the nature of quantum geometrodynamics. In *Battelle Rencontres* (pp. 242–307). Benjamin.  
    *The Hamiltonian constraint and the problem of time in quantum gravity.*

5.  **Wilson, K. G.** (1971). Renormalization group and critical phenomena. I & II. *Physical Review B*, 4(9), 3174–3205.  
    *The renormalization group as a hierarchical organization of scale transformations.*

6.  **Parisi, G.** (1979). Infinite number of order parameters for spin-glasses. *Physical Review Letters*, 43(23), 1754–1756.  
    *Ultrametric organization of equilibrium states in spin glasses.*

7.  **Mézard, M., Parisi, G., & Virasoro, M. A.** (1987). *Spin Glass Theory and Beyond*. World Scientific.  
    *Comprehensive treatment of ultrametricity in disordered systems.*

8.  **Vidal, G.** (2007). Entanglement renormalization. *Physical Review Letters*, 99(22), 220405.  
    *The Multiscale Entanglement Renormalization Ansatz (MERA) as a tree tensor network.*

9.  **Vidal, G.** (2008). Class of quantum many-body states that can be efficiently simulated. *Physical Review Letters*, 101(11), 110501.  
    *MERA and the discrete hyperbolic geometry of quantum critical systems.*

10. **Mallat, S.** (2009). *A Wavelet Tour of Signal Processing* (3rd ed.). Academic Press.  
    *Wavelet transforms as dyadic tree decompositions of signals.*

11. **Caldeira, A. O. & Leggett, A. J.** (1983). Quantum tunnelling in a dissipative system. *Annals of Physics*, 149(2), 374–456.  
    *The spin-boson model and spectral density formalism for open quantum systems.*

12. **Breuer, H.-P. & Petruccione, F.** (2002). *The Theory of Open Quantum Systems*. Oxford University Press.  
    *Non-Markovian dynamics, decoherence, and the CPMG noise spectroscopy formalism.*

13. **Planck Collaboration** (2020). Planck 2018 results. I. Overview and the cosmological legacy of Planck. *Astronomy & Astrophysics*, 641, A1.  
    *Primary CMB temperature and polarization data constraining log-periodic modulations.*

14. **Planck Collaboration** (2020). Planck 2018 results. X. Constraints on inflation. *Astronomy & Astrophysics*, 641, A10.  
    *Planck searches for features in the primordial power spectrum.*

15. **CMB-S4 Collaboration** (Abazajian, K. et al.) (2016). CMB-S4 Science Book, First Edition. arXiv:1610.02743.  
    *Projected sensitivity of next-generation CMB experiments.*

16. **Vladimirov, V. S., Volovich, I. V., & Zelenov, E. I.** (1994). *$p$-adic Analysis and Mathematical Physics*. World Scientific.  
    *The $p$-adic Fourier transform (Vladimirov operator) and its physical applications.*

17. **Langlands, R. P.** (1970). Problems in the theory of automorphic forms. In *Lectures in Modern Analysis and Applications III* (pp. 18–61). Springer.  
    *The Langlands program connecting number theory to harmonic analysis.*

18. **Gelbart, S.** (1984). An elementary introduction to the Langlands program. *Bulletin of the AMS*, 10(2), 177–219.  
    *Accessible overview of the Langlands correspondences.*

19. **Manin, Yu. I.** (1991). *Topics in Noncommutative Geometry*. Princeton University Press.  
    *Connections between $p$-adic geometry and physics; the adelic perspective.*

20. **Maldacena, J.** (1999). The large-$N$ limit of superconformal field theories and supergravity. *International Journal of Theoretical Physics*, 38(4), 1113–1133.  
    *The AdS/CFT correspondence; MERA as a discrete realization of holography.*


## Glossary

| Term | Definition |
|:-----|:-----------|
| **Bruhat–Tits tree** $\mathcal{T}_p$ | An infinite $(p+1)$-regular tree whose vertices are equivalence classes of lattices in $\mathbb{Q}_p^2$ and whose boundary is $\mathbb{P}^1(\mathbb{Q}_p)$ |
| **Ultrametric** | A distance function satisfying the strong triangle inequality $d(x,z) \leq \max(d(x,y), d(y,z))$; characteristic of tree geometries |
| **Scaling ratio** $q$ | The multiplicative factor defining tree levels; $q > 1$; values of interest include $q=2$ (octaves) and primes $p$ |
| **Depth** $k$ | An integer labeling a vertex on the tree; the number of branching choices from the root |
| **Boundary** $\partial\mathcal{T}$ | The set of infinite paths from the root; corresponds to frequencies specified to infinite precision |
| **Spectral density** $J(\omega)$ | The function describing how a quantum system couples to environmental modes at frequency $\omega$; on the tree, a sum of discrete peaks |
| **$p$-adic numbers** $\mathbb{Q}_p$ | The completion of $\mathbb{Q}$ with respect to the $p$-adic absolute value; a non-Archimedean field |
| **Strong triangle inequality** | $d(x,z) \leq \max(d(x,y), d(y,z))$; implies all triangles are isosceles with a short base |
| **Page–Wootters mechanism** | The proposal that time emerges from correlations between a “clock” system and the system of interest |
| **Log-periodic** | A function satisfying $f(qx) = f(x)$ for some $q$; oscillatory when expressed in $\log x$ |
| **MERA** | Multiscale Entanglement Renormalization Ansatz; a tensor network on a tree geometry |
| **CPMG** | Carr–Purcell–Meiboom–Gill dynamical decoupling sequence; a bandpass filter for environmental noise |
| **Fisher matrix** | A measure of the information an observable carries about a parameter; determines minimum detectable signal amplitude |
| **Adeles** $\mathbb{A}_\mathbb{Q}$ | The restricted product of $\mathbb{R}$ and all $\mathbb{Q}_p$; the natural object for unifying Archimedean and $p$-adic physics |
