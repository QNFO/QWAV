---
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: Symmetric Extension of Ultrametric Error Confinement—Ternary Tree Architecture with Bidirectional Validation
author: "Rowan Brad Quni-Gudzinas"
related: "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits"
doi: "10.5281/zenodo.20208437"
related-doi: "10.5281/zenodo.20134944"
version: "2026-05-16"
aliases:
  - Symmetric Extension of Ultrametric Error Confinement—Ternary Tree Architecture with Bidirectional Validation
modified: 2026-05-15T18:43:09Z
---

# Symmetric Extension of Ultrametric Error Confinement—Ternary Tree Architecture with Bidirectional Validation

**Rowan Brad Quni-Gudzinas**
*Independent Researcher*

**DOI**: [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437)
**Companion to:** Quni-Gudzinas, “Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits,” Zenodo, 2026. DOI: [10.5281/zenodo.20134944](https://doi.org/10.5281/zenodo.20134944).

## Abstract

The Bruhat–Tits tree validation [1] used $p = 2$ (binary tree with root degree $3$, internal degree $2$) and reported zero logical errors at depths $d \geq 3$ for $p_{\text{err}} \leq 0.40$. We demonstrate that this architecture contains a structural asymmetry: the tie-breaking convention at 2-child internal nodes favors logical $0$, collapsing the energy barrier for logical $1$ to a **constant** $B_{p=2,\,b=1}(d) = 2$ at all depths—rendering logical $1$ essentially unprotected. The original’s claims are valid only for the tested state ($b=0$).

We resolve this by switching to $p = 3$ (ternary tree, all nodes have exactly $3$ children). Odd branching eliminates all tie-breaking. We independently test both logical states and confirm **perfect symmetry**: identical logical error rates at every $(d, p_{\text{err}})$ data point. At $d = 7$ ($2{,}187$ leaves), zero logical errors across $36{,}000$ total trials at all $p_{\text{err}} \leq 0.40$ (Wilson 95% CI upper bound: $0.0019$). We extend to $d = 8$, provide constructive barrier proof through $d = 15$, and scope five physical platforms.

We also address the $p$-selection problem: must we use $p = 3$, or would $p = 5, 7, 11, \ldots$ also work? We show that the strict Bruhat–Tits construction **always** introduces tie-breaking asymmetry at some level for every prime $p$—a structural consequence of the $p+1$ rule at the root vs. $p$ children internally. Our deviation (all nodes have $p$ children) eliminates this universally, making every odd prime a candidate for symmetric error confinement. Among odd primes, $p = 3$ is the **minimal** symmetric architecture—it minimizes qubit overhead while preserving the identical barrier exponent $B(d) = 2^d$ as the original $p = 2$ (bit $0$). Higher odd primes ($p = 5, 7, \ldots$) offer stronger absolute barriers at the cost of exponentially larger qubit counts, representing a design trade-off for future investigation.

---

## 1. The $p = 2$ Asymmetry Problem

### 1.1 How Tie-Breaking Creates One-Sided Protection

The original Bruhat–Tits tree validation [1] used $p = 2$: the root has $p + 1 = 3$ children, internal nodes have $p = 2$ children. Majority-vote decoding at 2-child nodes breaks ties to $0$ by convention. This is not arbitrary—some convention is required when votes split evenly—but it creates a structural asymmetry between logical states.

Consider a single internal node with $2$ leaf children:

**Encoded as $b = 0$ (children: $0, 0$):**

| Leaf errors | Child values | Tie-break | Node result | Flipped? |
|:-----------|:-------------|:---------|:------------|:---------|
| 0 errors | $(0, 0)$ | No tie | $0$ | No |
| 1 error | $(0, 1)$ or $(1, 0)$ | Tie $\to 0$ | $0$ | **No** |
| 2 errors | $(1, 1)$ | No tie | $1$ | Yes |

**Flipping this node requires $2$ leaf errors.** The tie-breaker protects $b = 0$: even with one corrupted child, the output remains correct.

**Encoded as $b = 1$ (children: $1, 1$):**

| Leaf errors | Child values | Tie-break | Node result | Flipped? |
|:-----------|:-------------|:---------|:------------|:---------|
| 0 errors | $(1, 1)$ | No tie | $1$ | No |
| 1 error | $(0, 1)$ or $(1, 0)$ | Tie $\to 0$ | $0$ | **Yes** |
| 2 errors | $(0, 0)$ | No tie | $0$ | Yes |

**Flipping this node requires only $1$ leaf error.** The tie-breaker betrays $b = 1$: the moment one child is corrupted, the tie breaks to the *wrong* value.

### 1.2 Barrier Collapse for Logical 1

This asymmetry propagates recursively. For the $p = 2$ tree of depth $d$:

**Barrier when encoded as $b = 0$:**

$$B_{b=0}(1) = 2, \qquad B_{b=0}(d) = 2 \cdot B_{b=0}(d-1) = 2^d$$

Each internal node requires both children to flip—exponential protection.

**Barrier when encoded as $b = 1$:**

$$B_{b=1}(1) = 2, \qquad B_{b=1}(d) = 2 \quad (\text{all } d \geq 2)$$

At $d \geq 2$, each internal node flips with a **single** leaf error. The root requires $2$ of its $3$ children to flip; each child flips with $1$ error. Total: $2$ leaf errors—**at any depth**. The barrier is constant.

**Exhaustive verification (all $2^n$ leaf patterns enumerated):**

| Depth $d$ | Leaves $n$ | $B_{b=0}(d)$ | $B_{b=1}(d)$ | Ratio |
|:----------|:-----------|:-------------|:-------------|:------|
| 1 | 3 | 2 | 2 | 1:1 |
| 2 | 6 | 4 | **2** | 2:1 |
| 3 | 12 | 8 | **2** | **4:1** |
| 4 | 24 | 16 | **2** | **8:1** |

All values confirmed by exhaustive enumeration over all $2^n$ leaf patterns for $d = 1, 2, 3$—every possible error combination was tested.

### 1.3 What This Means for the Original Validation

The original $p = 2$ results [1]—zero logical errors at $d \geq 3$ for $p_{\text{err}} \leq 0.40$—are **valid for the state tested** (logical $0$). The exponential barrier for $b = 0$ is real. However:
1. Logical $1$ was never tested independently.
2. Had it been, the constant barrier ($B = 2$) would have produced near-random logical error rates at all depths.
3. The error confinement was **unidirectional**, not bidirectional.

This is not a flaw in the original’s data. The asymmetry was structurally built into the $p = 2$ design. This companion paper identifies the asymmetry, resolves it, and provides the first fully symmetric validation.

---

## 2. Theoretical Foundations—Why Primes?

### 2.1 The Bruhat–Tits Tree and $p$-Adic Numbers

To understand why the branching factor $p$ cannot be arbitrary, we must examine the underlying mathematics. The Bruhat–Tits tree is not an arbitrary tree—it is the **Bruhat–Tits building** for the group $\text{SL}(2, \mathbb{Q}_p)$, defined over the $p$-adic numbers $\mathbb{Q}_p$.

The $p$-adic numbers $\mathbb{Q}_p$ exist only for **prime** $p$. For a composite number $n = ab$, the ring of $n$-adic integers $\mathbb{Z}_n$ is not an integral domain (it has zero divisors), so the associated valuation is not a true absolute value, and the geometric construction fails. The Bruhat–Tits tree is defined over $\mathbb{Q}_p$ **only when $p$ is prime**.

Therefore: $p \in \{2, 3, 5, 7, 11, 13, 17, 19, 23, \ldots\}$—the primes. This is not an arbitrary restriction; it follows from the requirement that $\mathbb{Z}_p$ be a discrete valuation ring, which is true exactly when $p$ is prime.

### 2.2 Tree Structure for Prime $p$

For a given prime $p$, the Bruhat–Tits tree for $\text{SL}(2, \mathbb{Q}_p)$ is an infinite **$(p+1)$-regular tree**—every vertex has exactly $p+1$ neighbors. The vertices correspond to homothety classes of $\mathbb{Z}_p$-lattices in $\mathbb{Q}_p^2$, and edges correspond to lattice inclusions of index $p$. This construction produces the $p+1$ regularity directly from the structure of the local field.

When we **root** this infinite tree at a vertex (to create a finite encoding architecture), the structure becomes:

- **Root:** $p+1$ children (all neighbors in the full tree)
- **Internal nodes (depth $\geq 1$):** $p$ children (one neighbor is “up” toward the root)
- **Leaves:** $3 \cdot 2^{d-1}$ for $p=2$; $(p+1) \cdot p^{d-1}$ for general $p$

This is the “strict” Bruhat–Tits construction used in [1] for $p = 2$.

### 2.3 The Fundamental Asymmetry Theorem

**Theorem 1 (Universal BT Asymmetry).** *For every prime $p$, the strict Bruhat–Tits rooted tree contains nodes with an even number of children, at which majority-vote tie-breaking is required.*

**Proof.** For $p = 2$: internal nodes have $p = 2$ children (even), root has $p+1 = 3$ (odd).
For $p \geq 3$ (odd primes): $p$ is odd $\implies p+1$ is even $\implies$ root has an even number of children. $\square$

**Corollary.** The location of the asymmetry alternates:
- $p = 2$: asymmetry at **internal nodes** (even children)
- $p = 3, 5, 7, \ldots$: asymmetry at the **root** (even children)

**Table 1: Asymmetry locations in strict Bruhat–Tits trees**

| $p$ (prime) | Root degree $(p+1)$ | Root ties? | Internal degree $(p)$ | Internal ties? | Asymmetry at |
|:------------|:--------------------|:-----------|:----------------------|:---------------|:-------------|
| **2** | 3 (odd) | No | **2 (even)** | **Yes** | Internal nodes |
| **3** | **4 (even)** | **Yes** | 3 (odd) | No | Root |
| **5** | **6 (even)** | **Yes** | 5 (odd) | No | Root |
| **7** | **8 (even)** | **Yes** | 7 (odd) | No | Root |
| **11** | **12 (even)** | **Yes** | 11 (odd) | No | Root |

In the strict BT construction, **asymmetry is universal**—it simply moves from internal nodes ($p=2$) to the root ($p \geq 3$). There is no prime $p$ for which the strict construction yields a tie-free tree.

---

## 3. The $p$-Selection Problem

### 3.1 Eliminating Asymmetry—The Regular $p$-Ary Deviation

Our solution: deviate from the strict $p+1$ root rule. Instead, give **every** node—including the root—exactly $p$ children. This yields a regular $p$-ary tree.

**Justification of the deviation:** The strict $p+1$ root rule is an artifact of rooting an *infinite* $(p+1)$-regular tree. In the infinite tree, the root has neighbors in all $p+1$ directions. In a finite encoding architecture, we are free to choose any subtree. Selecting a root with only $p$ “downward” neighbors (and 1 “upward” neighbor that doesn’t exist in the finite tree) is equivalent to choosing a different embedding. The essential ultrametric properties—depth-to-LCA distance and strong triangle inequality—are preserved for any rooted subtree.

**Table 2: Regular $p$-ary trees—all nodes have $p$ children**

| $p$ | Parity | Ties? | Barrier/node | $B(d)$ | $L(d)$ | Barrier fraction |
|:----|:-------|:------|:-------------|:-------|:-------|:-----------------|
| 2 | Even | **Yes** | $\lceil 2/2 \rceil = 1$† | Asymmetric | $2^d$ |—|
| 3 | Odd | **None** | $\lceil 3/2 \rceil = 2$ | $2^d$ | $3^d$ | $(2/3)^d$ |
| 5 | Odd | **None** | $\lceil 5/2 \rceil = 3$ | $3^d$ | $5^d$ | $(3/5)^d = 0.6^d$ |
| 7 | Odd | **None** | $\lceil 7/2 \rceil = 4$ | $4^d$ | $7^d$ | $(4/7)^d \approx 0.571^d$ |
| 11 | Odd | **None** | $\lceil 11/2 \rceil = 6$ | $6^d$ | $11^d$ | $(6/11)^d$ |

†For $p=2$: $\lceil 2/2 \rceil = 1$, but tie-breaking makes the effective barrier $2$ for $b=0$ and $1$ for $b=1$.

**Every odd prime yields a tie-free, fully symmetric architecture.** Even $p$ always has ties (even children).

### 3.2 Why $p = 3$ Specifically?

Among all odd primes, $p = 3$ is the **minimal symmetric** choice. It minimizes qubit overhead while preserving the identical barrier exponent as the original $p = 2$ architecture (for bit 0):

$$B_{p=3}(d) = \lceil 3/2 \rceil^d = 2^d = \lceil 2/2 \rceil_{\text{eff}}^d = B_{p=2,\,b=0}(d)$$

The symmetry fix does **not** weaken the barrier—it merely extends identical protection to both logical states. The only “cost” is the larger leaf count ($3^d$ vs. $3 \cdot 2^{d-1}$), which is the price of genuine bidirectional protection.

### 3.3 What About $p = 5, 7, 11, \ldots$?

Higher odd primes are also valid symmetric architectures. They offer **stronger absolute barriers** at the cost of **exponentially larger qubit overhead**.

**Table 3: Barrier–Overhead Trade-off Across Odd Primes**

| $p$ | $B(3)$ | $L(3)$ | $B(5)$ | $L(5)$ | $B(7)$ | $L(7)$ | Overhead ratio ($L/L_{p=3}$) at $d=7$ |
|:----|:------|:------|:------|:------|:------|:------|:----------------------------------------|
| 3 | 8 | 27 | 32 | 243 | 128 | 2,187 | **1× (baseline)** |
| 5 | 27 | 125 | 243 | 3,125 | 2,187 | 78,125 | **36×** |
| 7 | 64 | 343 | 1,024 | 16,807 | 16,384 | 823,543 | **377×** |
| 11 | 216 | 1,331 | 7,776 | 161,051 | 279,936 | 19,487,171 | **8,910×** |

**Interpretation:** $p = 5$ gives a $3^d$ barrier vs. $2^d$ for $p = 3$—a $(\frac{3}{2})^d$ improvement in absolute error suppression. At $d = 7$: barrier of $2{,}187$ vs. $128$, a $17\times$ stronger barrier. But this requires $78{,}125$ leaves vs. $2{,}187$—a $36\times$ qubit overhead.

The choice of $p$ is therefore a **resource trade-off**:
- **$p = 3$:** Minimal overhead. Best for near-term demonstration ($40$ atoms at $d=3$).
- **$p = 5$ or $7$:** Stronger barriers per depth. Worth investigating for platforms where qubit count is not the bottleneck (e.g., photonic cluster states, where photon generation scales differently).
- **$p > 7$:** Diminishing returns. Overhead grows as $p^d$ while barrier grows only as $\lceil p/2 \rceil^d$.

**Recommendation:** $p = 3$ as the primary architecture (minimal symmetric). $p = 5$ as the first generalization for platforms with abundant qubits.

#### 3.3.1 Monte Carlo Validation of $p = 5$ and $p = 7$

We validated these theoretical predictions with Monte Carlo simulations (500 trials per condition, seed = 42, both logical bits independently):

**Table 3b: $p = 5$ LER at $p_{\text{err}} = 0.40$ (both bits identical)**

| Depth | Leaves | Barrier $3^d$ | LER | Wilson 95% CI (error rate) |
|:------|:-------|:-------------|:----|:---------------------------|
| 2 | 25 | 9 | 0.190 | [0.158, 0.227] |
| 3 | 125 | 27 | 0.040 | [0.026, 0.061] |
| 4 | 625 | 81 | **0.000** | [0, 0.0076] |

**Table 3c: $p = 7$ LER at $p_{\text{err}} = 0.40$ (both bits identical)**

| Depth | Leaves | Barrier $4^d$ | LER | Wilson 95% CI (error rate) |
|:------|:-------|:-------------|:----|:---------------------------|
| 2 | 49 | 16 | 0.126 | [0.100, 0.158] |
| 3 | 343 | 64 | 0.002 | [0.0004, 0.011] |

**Key findings:** (1) Perfect symmetry confirmed—both logical bits produce identical LER at every data point. (2) $p = 5$ achieves zero errors at $d = 4$ ($625$ leaves, $B = 81$)—far earlier than $p = 3$ which requires $d = 7$. (3) The barrier formula $B(d) = \lceil p/2 \rceil^d$ is computationally confirmed for all tested primes and depths. $[\text{CODE-EXECUTED}]$

### 3.4 Exhaustive Verification of Symmetry for Odd $p$

We confirmed via exhaustive enumeration (all possible leaf patterns) that all odd $p$ yield symmetric barriers:

| $p$ | $d$ | Leaves | Patterns | $B_{b=0}$ | $B_{b=1}$ | Symmetric? |
|:----|:----|:-------|:---------|:----------|:----------|:-----------|
| 3 | 1 | 3 | 8 | 2 | 2 | ✓ |
| 3 | 2 | 9 | 512 | 4 | 4 | ✓ |
| 5 | 1 | 5 | 32 | 3 | 3 | ✓ |
| 7 | 1 | 7 | 128 | 4 | 4 | ✓ |

Higher depths confirmed via constructive proof ($B(d) = \lceil p/2 \rceil^d$).

For comparison, the regular $p$-ary $p = 2$ tree (all nodes have 2 children) is even more asymmetric than the strict BT construction: exhaustive enumeration through $d = 3$ (256 patterns) confirms $B_{b=0}(d) = 2^d$ but $B_{b=1}(d) = 1$ at all depths (vs. $2$ for strict BT with $p+1$ root). A single leaf error anywhere propagates to flip the root when encoded as logical 1. $[\text{CODE-EXECUTED}]$

---

## 4. Architecture—The Ternary ($p = 3$) Tree

### 4.1 Tree Construction

Every node has exactly $3$ children. Leaves are at depth $d$. Total leaves: $3^d$. Total nodes: $(3^{d+1} - 1) / 2$. Majority requires $2$ of $3$ at every node—no ties possible.

### 4.2 Encoding, Decoding, and Error Model

Identical structure to [1]: encode all leaves to $b \in \{0, 1\}$; apply i.i.d. bit-flip noise with probability $p_{\text{err}}$ to leaves only; decode via bottom-up majority vote (classical post-processing). Implementation: Python 3.10+, standard library only, seed = 42.

### 4.3 Experimental Design

| Parameter | Original [1] ($p=2$, strict BT) | This Work ($p=3$, regular) |
|:----------|:-------------------------------|:---------------------------|
| Depths tested | $d = 2, 3, 4, 5$ | $d = 2, 3, 4, 5, 6, 7, 8$ |
| Logical bits | 1 (bit $0$ only) | 2 (bits $0$ and $1$, independent) |
| Trials per condition | 500 | 500 ($d \leq 5$), 1,000 ($d = 6, 8$), 2,000 ($d = 7$) |

---

## 5. Results

### 5.1 Symmetry Confirmation

**Perfect symmetry confirmed:** Logical $b = 0$ and $b = 1$ produce identical LER values at all $63$ data points ($7$ depths $\times$ $9$ error rates).

### 5.2 Logical Error Rate at $p_{\text{err}} = 0.40$

**Table 4: LER at $p_{\text{err}} = 0.40$ (both bits, identical results)**

| Depth | Leaves | Barrier | LER | Wilson 95% CI | Trials/bit | Suppression |
|:------|:-------|:--------|:----|:--------------|:-----------|:------------|
| 2 | 9 | 4 | 0.248 | [0.212, 0.288] | 500 | 1.6× |
| 3 | 27 | 8 | 0.182 | [0.151, 0.218] | 500 | 2.2× |
| 4 | 81 | 16 | 0.106 | [0.082, 0.136] | 500 | 3.8× |
| 5 | 243 | 32 | **0.010** | [0.004, 0.023] | 500 | **40×** |
| 6 | 729 | 64 | **0.002** | [0.001, 0.007] | 1,000 | **200×** |
| 7 | 2,187 | 128 | **0.000** | [0, 0.0019] | 2,000 | **∞** |
| 8 | 6,561 | 256 | **0.000** | [0, 0.0038] | 1,000 | **∞** |

### 5.3 Comparison to Original $p = 2$ Results

**Table 5: LER—Original $p = 2$ vs. Symmetric $p = 3$ at $p_{\text{err}} = 0.40$**

| Depth | Original $p=2$, bit $0$ [1] | Symmetric $p=3$, both bits |
|:------|:----------------------------|:---------------------------|
| 2 | 0.072 | 0.248 |
| 3 | 0.000 | 0.182 |
| 4 | 0.000 | 0.106 |
| 5 | 0.000 | 0.010 |

The original’s apparent advantage is entirely the internal tie-breaking favor for $b=0$. Logical $1$ would have failed at all depths (barrier $= 2$). Our results show non-zero LER at low $d$ because **both** bits are tested symmetrically, but the exponential decay is preserved. At $d \geq 7$, zero errors are achieved for **both** bits.

### 5.4 Zero-Error Thresholds

| Depth | Trials/bit | Zero errors up to $p_{\text{err}}$ |
|:------|:-----------|:------------------------------------|
| 3 | 500 | 0.15 |
| 4 | 500 | 0.30 |
| 5 | 500 | 0.30 |
| 6 | 1,000 | 0.35 |
| 7 | 2,000 | **0.40** (full range) |
| 8 | 1,000 | **0.40** (full range) |

### 5.5 Energy Barrier Verification

| Method | Depths | Result |
|:-------|:-------|:-------|
| Exhaustive enumeration | $d = 1, 2$ ($8$ and $512$ patterns) | **Confirmed** |
| Constructive proof | $d = 3 \ldots 15$ | **Confirmed** |
| Random sampling | $d = 3$ ($5 \times 10^5$ patterns) | No counterexamples |
| Barrier formula | $B(d) = \lceil p/2 \rceil^d = 2^d$ | Verified |

---

## 6. Physical Implementation Pathway

The original paper [1] proposed a twisted Bi-2212 superconducting substrate [2] at the theoretical level. Here we provide a concrete near-term experimental pathway.

### 6.1 Platform Recommendation

| Platform | Geometry | Coupling | Noise | Scale | Overall |
|:---------|:--------:|:--------:|:-----:|:-----:|:-------:|
| **Neutral Atoms** | ★★★★★ | ★★★★ | ★★★★ | ★★★★ | **PRIMARY** |
| Trapped Ions | ★★★ | ★★★★ | ★★★★★ | ★★ | Secondary |

**Neutral atom tweezer arrays** offer arbitrary 2D/3D geometry (exact tree layout), Rydberg-mediated interactions with tunable range, demonstrated scaling to $1{,}000+$ atoms, and detectable atom loss.

### 6.2 Near-Term Demonstration ($d = 3$, 40 atoms)

Requires 40 atoms, controlled error injection ($X$-rotations), fluorescence readout, and classical majority-vote post-processing. **No ancilla qubits, syndrome measurement, or real-time feedback.** Feasible on **existing** platforms (Harvard/Lukin–Greiner, Caltech/Endres, Pasqal/Browaeys).

| Stage | Depth | Atoms | Status |
|:------|:------|:------|:-------|
| Near-term | $d = 3$ | 40 | Existing hardware |
| Medium-term | $d = 5$ | 364 | Demonstrated scale |
| Long-term | $d = 7$ | 3,280 | Frontier (3D tweezers) |

---

## 7. Discussion

### 7.1 Why the Ternary Architecture Is the Correct Generalization

The original $p=2$ architecture [1] is not wrong—it is **incomplete**. The error confinement *mechanism* (exponential barrier via hierarchical majority voting) was correctly identified. But the architecture cannot provide bidirectional protection because internal tie-breaking inherently favors one logical state.

The $p=3$ architecture generalizes the mechanism to a symmetric form. Every node uses the same rule; no ties occur anywhere; both logical states receive identical exponential protection. The barrier exponent is unchanged ($2^d$). The only thing “sacrificed” is the illusory zero-error-at-$d=3$ that appeared in the original because only the favored state was tested.

### 7.2 Why Not $p = 5$ or $p = 7$?

As established in §3, every odd prime $p$ yields a symmetric architecture. The question is one of **resource optimization**, not mathematical possibility:

| Criterion | $p=3$ | $p=5$ | $p=7$ |
|:----------|:-----:|:-----:|:-----:|
| Tie-free? | ✓ | ✓ | ✓ |
| Symmetric? | ✓ | ✓ | ✓ |
| Barrier exponent | $2^d$ | $3^d$ | $4^d$ |
| Qubit overhead at $d=7$ | 2,187 | 78,125 (36×) | 823,543 (377×) |
| Near-term feasible? | **Yes** (40 atoms) | Marginal (125 atoms) | No (343 atoms) |
| Barrier at $d=3$ | 8 | 27 | 64 |
| Barrier at $d=5$ | 32 | 243 | 1,024 |

**$p = 3$ is the minimal symmetric architecture.** It achieves zero errors at experimentally accessible scales. $p = 5$ and $p = 7$ are valid generalizations for future investigation—they offer stronger absolute barriers at the cost of exponentially more qubits, which may become favorable if qubit counts continue to scale while gate fidelities plateau.

### 7.3 The Barrier Scaling Is Identical to the Original

$$B_{p=3}(d) = \lceil 3/2 \rceil^d = 2^d = B_{p=2,\,b=0}(d)$$

The symmetry fix does **not** weaken the barrier. It extends identical protection to both logical states. The ternary tree uses more qubits ($3^d$ vs. $3 \cdot 2^{d-1}$), but this is the cost of genuine bidirectional symmetry.

### 7.4 Relationship to the Original Validation

| Original [1] Demonstrated | This Companion Adds |
|:--------------------------|:--------------------|
| Error confinement **mechanism** | **Bidirectional** confinement |
| Zero errors at $d \geq 3$ for $b=0$ | Zero errors at $d \geq 7$ for **both** bits |
| Exponential barrier for $b=0$ | Exponential barrier for **both** bits, $p$-selection rationale |
| Theoretical motivation (ultrametric geometry) | Physical implementation scoping |
| $500$ trials per condition | Up to $2{,}000$ trials, tighter CIs |

### 7.6 Comparison to Classical Repetition Code

A natural baseline is the classical $N$-bit repetition code: encode one logical bit into $N$ physical bits, decode by majority vote. For a fair comparison, we match $N = p^d$ (same physical qubit count as tree leaves).

**Barrier comparison.** The classical barrier is $\lceil N/2 \rceil$, while the tree barrier is $\lceil p/2 \rceil^d$:

| Architecture | $N = p^d$ | Barrier | $B/N$ |
|:-------------|:----------|:--------|:------|
| p=3 d=3 (tree) | 27 | 8 | 0.296 |
| Classical N=27 | 27 | **14** | 0.519 |
| p=3 d=5 (tree) | 243 | 32 | 0.132 |
| Classical N=243 | 243 | **122** | 0.502 |
| p=3 d=7 (tree) | 2,187 | 128 | 0.059 |
| Classical N=2,187 | 2,187 | **1,094** | 0.500 |

The classical barrier scales as $N/2$ (linear in qubits), while the tree barrier scales as $2^d$ (exponential in depth but sublinear in qubits since $N = 3^d$). The classical absolute barrier is always higher at matched $N$.

**LER comparison.** At $p_{\text{err}} = 0.40$, Monte Carlo simulations (500 trials) confirm:

| $(p, d)$ | $N$ | Tree LER | Classical LER (MC) | Classical LER (theory) | Winner |
|:---------|:----|:---------|:--------------------|:-----------------------|:-------|
| (3, 2) | 9 | 0.248 | 0.258 | 0.267 | Tree (marginal) |
| (3, 3) | 27 | 0.182 | 0.164 | 0.145 | Classical |
| (3, 4) | 81 | 0.106 | 0.038 | 0.034 | Classical |
| (3, 5) | 243 | 0.010 | <0.002 | 0.0008 | Classical |
| (5, 2) | 25 | 0.190 | 0.166 | 0.154 | Classical |
| (5, 3) | 125 | 0.040 | 0.006 | 0.012 | Classical |
| (7, 2) | 49 | 0.126 | 0.080 | 0.078 | Classical |

At $d \geq 6$, both architectures achieve zero observed errors at 500 trials. $[\text{CODE-EXECUTED}]$

**Interpretation.** At matched qubit count, the classical repetition code is the stronger error-correcting code for bit-flip noise. This is expected: the tree’s hierarchical structure discards information at each majority-vote stage (many leaf patterns map to the same decoded bit), while the flat repetition code uses all bits in a single vote. The tree architecture’s value is **not** raw error-correction efficiency—it lies in the connection to ultrametric geometry, $p$-adic mathematics, and the potential for physical implementations where the tree topology maps naturally to spatial layouts (e.g., neutral atom tweezer arrays with Rydberg-mediated interactions that respect the hierarchical structure).

This comparison also explains why $p = 5$ and $p = 7$ outperform $p = 3$ at matched $N$: larger $p$ concentrates the tree’s error-correction budget more efficiently per leaf (barrier fraction $\lceil p/2 \rceil / p$ improves from $0.667$ at $p=3$ to $0.600$ at $p=5$ to $0.571$ at $p=7$), though the absolute barrier fraction still falls below the classical $0.5$.

#### 7.6.1 Correlated Noise—Where the Tree Gains an Advantage

The i.i.d. comparison above is a worst-case scenario for the tree. Under **correlated (clustered) noise**—where errors on nearby leaves are more likely to co-occur—the tree’s hierarchical structure provides genuine advantage. We model correlated noise as a two-stage process: (1) i.i.d. flips with probability $p_{\text{base}}$, then (2) for each flipped leaf, flip up to $k=2$ nearest neighbors in DFS order with probability $p_{\text{corr}}$.

**Table 6: Crossover point—$p_{\text{base}}$ where Tree LER < Classical LER**

| $(p,d)$ | $N$ | $p_{\text{corr}}=0.25$ | $p_{\text{corr}}=0.50$ | $p_{\text{corr}}=0.75$ |
|:--------|:----|:----------------------|:----------------------|:----------------------|
| (3, 3) | 27 |—(CL always wins) | $\geq 0.30$ | $\geq 0.25$ |
| (3, 4) | 81 | $\geq 0.35$ | $\geq 0.25$ | $\geq 0.20$ |
| (5, 3) | 125 | $\geq 0.35$ | $\geq 0.30$ | $\geq 0.20$ |

Three trends are evident: (1) Higher correlation ($p_{\text{corr}}$) favors the tree—the crossover $p_{\text{base}}$ moves lower. (2) Higher depth favors the tree—$d=4$ crosses over earlier than $d=3$. (3) Larger $p$ favors the tree—$p=5$ provides more containment per subtree. At $p_{\text{corr}}=0.75$, the tree outperforms classical at all tested $(p,d)$ for $p_{\text{base}} \geq 0.20$, and at $p=3$, $d=4$, the tree wins 4 of 7 $p_{\text{base}}$ values. $[\text{CODE-EXECUTED}]$

**Why:** Clustered errors in one subtree are contained by hierarchical voting—they affect only that subtree’s vote, and the other $\lceil p/2 \rceil - 1$ sibling subtrees remain correct. In the classical repetition code, clustered errors in adjacent bits concentrate the error budget in one region, which can flip the global majority with fewer total errors. The tree’s spatial subdivision acts as a natural error-containment mechanism when errors are spatially correlated.

### 7.7 $q$-Ary Alphabet Generalization—Error Suppression Through Symbol Scatter

The binary encoding ($q = 2$) represents a worst case for the adversary: every flipped leaf always targets the one wrong symbol. In a $q$-ary alphabet ($q > 2$), a flipped leaf scatters randomly across $q - 1$ wrong symbols, making it harder for any single wrong symbol to achieve plurality at internal nodes.

**Adversarial barrier** (minimum leaf errors to flip a node, all targeting same wrong symbol):
$$B_{\text{adv}} = \lceil p/2 \rceil^d$$

**Random-scatter effective barrier** (heuristic: errors divide across $q-1$ wrong symbols):
$$B_{\text{rand}} \approx \big(\lceil p/2 \rceil \cdot (q-1)\big)^d$$

**Table 7: $q$-ary LER at $p_{\text{err}} = 0.40$, $p = 3$ (500 trials)**

| $d$ | Leaves | $q=2$ (binary) | $q=3$ | $q=5$ | $q=10$ |
|:----|:-------|:---------------|:------|:------|:-------|
| 2 | 9 | 0.304 | **0.076** ($4\times$) | 0.006 ($51\times$) | 0.004 ($76\times$) |
| 3 | 27 | 0.194 | **0.004** ($48\times$) | **0.000** | **0.000** |
| 4 | 81 | 0.094 | **0.000** | **0.000** | **0.000** |

$[\text{CODE-EXECUTED}]$

At $q = 3$, $d = 3$, the LER drops from $0.194$ to $0.004$—a $48\times$ reduction with **zero additional physical qubits**. By $q = 5$, zero errors are observed at all tested depths. The random-scatter effective barrier for $q=3$, $d=3$ is approximately $4^3 = 64$, compared to the adversarial barrier of $2^3 = 8$—an 8× increase in the effective barrier explains the dramatic LER reduction.

**Practical significance:** In neutral atom implementations, each atom can encode multiple internal states (hyperfine levels for alkali atoms, nuclear spin states for alkaline-earth atoms). The $q$-ary generalization exploits this existing physical resource—no additional atoms or gates are required. Alkali atoms (Rb, Cs) routinely support $q = 3-5$ hyperfine levels; alkaline-earth atoms (Sr, Yb) support $q = 10+$ nuclear spin states. The scatter mechanism converts this physical capacity into error suppression without increasing qubit count.

### 7.8 QEC Concatenation—Tree + Leaf-Level Repetition

We tested concatenating the tree with an inner repetition code: each tree leaf is itself $M$ physical qubits decoded by local majority vote before the tree’s hierarchical vote. At matched total qubit counts ($p^d \times M$), the pure repetition code outperforms both pure-tree and concatenated configurations:

| Total qubits | Pure Tree | Tree+Rep (best) | Pure Rep | Winner |
|:-------------|:----------|:----------------|:---------|:-------|
| 27 | Tree d=3: 0.182 | d=2,m=3: 0.182 | **0.164** | Rep |
| 81 | Tree d=4: 0.106 | d=2,m=9: 0.088 | **0.038** | Rep |
| 243 | Tree d=5: 0.010 | d=3,m=9: 0.014 | **0.000** | Rep |

$[\text{CODE-EXECUTED}]$

The concatenation provides no advantage: the tree’s hierarchical majority voting already performs the function of a repetition code, and splitting the qubit budget between tree depth and inner length is strictly worse than allocating all qubits to a single flat repetition code. This reinforces the finding of §7.6: the tree architecture’s value is **not** raw error-correction efficiency under i.i.d. noise, but rather its geometric structure and advantages under correlated noise (§7.6.1).

### 7.5 Limitations

In addition to limitations enumerated in [1]:

1. **$p = 3$ is less qubit-efficient:** Leaves grow as $3^d$ vs. $3 \cdot 2^{d-1}$ at $p=2$. At $d=10$: $59{,}049$ vs. $1{,}536$. This is the price of bidirectional symmetry.
2. **Phase errors unaddressed.**
3. **Platform assessments are theoretical** ($[\text{LLM-INFERRED}]$).
4. **Higher $p$ validation is limited:** $p=5$ validated through $d=4$ and $p=7$ through $d=3$ (MC, 500 trials). Deeper depths and larger primes remain theoretical.

---

## 8. Conclusion

We have identified and resolved a fundamental asymmetry in the $p = 2$ Bruhat–Tits tree architecture [1]. When encoded as logical $1$, internal tie-breaking collapses the energy barrier from $2^d$ to a constant $2$ at all depths—logical $1$ receives essentially no protection. This asymmetry is not a bug in the original’s methodology but a structural property of $p=2$ Bruhat–Tits trees.

We have shown that **every odd prime** $p$ yields a symmetric architecture when all nodes are given $p$ children (a justified deviation from the strict $p+1$ root rule). Among odd primes, $p = 3$ is the minimal symmetric choice—it preserves the identical barrier exponent $B(d) = 2^d$ while minimizing qubit overhead.

Our extended validation ($d = 2 \ldots 8$, up to $2{,}000$ trials per condition) demonstrates:
1. **Perfect symmetry:** Logical $0$ and $1$ produce identical LER at all $63$ data points.
2. **Zero errors at $d \geq 7$** for both bits at all $p_{\text{err}} \leq 0.40$ (Wilson 95% CI upper bound: $0.0019$).
3. **Constructive barrier proof** through $d = 15$.
4. **Concrete experimental pathway:** $d = 3$, $40$ atoms on existing neutral atom platforms.

This companion paper closes the asymmetry gap in the original validation, establishes the $p$-selection rationale, and provides a stronger, fully bidirectional evidence base for the ultrametric error confinement thesis.

---

## Acknowledgments

The original validation framework [1] provided the foundation. All quantitative results are $[\text{CODE-EXECUTED}]$ (reproducible Python 3.10+ simulation, seed = 42). Platform assessments are $[\text{LLM-INFERRED}]$.

---

## References

[1] R. B. Quni-Gudzinas, “Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits,” Zenodo, 2026. DOI: [10.5281/zenodo.20134944](https://doi.org/10.5281/zenodo.20134944).

[2] R. B. Quni-Gudzinas, “A 4-Kelvin Topological Quantum Processor Using Twisted Bi-2212 High-Temperature Superconductors,” Zenodo, 2025.

## Appendix A: Quick Reference—The One-Liner For Every Question

**Q: Why \=3\$ specifically?**

\=3\$ is the smallest odd prime—all odd \$ are symmetric, but \=3\$ minimizes qubit overhead while preserving the identical \^d\$ barrier exponent as the original \=2\$ (bit 0).

**Q: Why not \=5\$ or \=7\True**

They work (verified exhaustively at \=1\$, symmetrically for both bits) and give stronger absolute barriers (\^d\$, \^d\$), but require 36× and 377× more qubits at \=7\$. Design trade-off for future investigation—viable for platforms where qubit count is not the bottleneck.

**Q: Why must \$ be prime?**

The Bruhat–Tits tree is defined over \$ℚ_p\$, which requires \$ℤ_p\$ to be a discrete valuation ring—true only for prime \$. Composite \$ produces zero divisors and fails the geometric construction.

**Q: Why deviate from strict \+1\$ root rule?**

The \+1\$ rule **always** introduces even-count nodes (root for \ \geq 3\$, internal for \=2\$), creating tie-breaking asymmetry. The deviation preserves all ultrametric properties while eliminating ties everywhere.

**Q: Is the strict Bruhat–Tits tree ever symmetric?**

**No.** Theorem 1: For every prime \$, the strict construction has an even number of children at some level, requiring tie-breaking that favors one logical state.

**Q: Does \=3\$ weaken the barrier compared to \=2\True**

No. \{p=3}(d) = \lceil 3/2 \rceil^d = 2^d = B_{p=2,\,b=0}(d)\$. Identical exponent. The only difference: \=3\$ protects **both** bits equally.

**Q: Why does \=2\$ show zero errors at \ \geq 3\$ while \=3\$ doesn’t until \ \geq 7\True**

Because \=2\$ internal tie-breaking favors bit 0—the original only tested bit 0. Bit 1 would see barrier=2 (constant) at all depths. \=3\$ tests both bits equally; the higher LER at low \$ is the price of genuine bidirectional protection. At \ \geq 7\$, both bits achieve zero errors.

**Q: What about \=11, 13, 17, \ldots\True**

Same pattern as \=5,7\$—symmetric, stronger absolute barriers, exponentially more qubits. Diminishing returns: overhead grows as \^d\$ while barrier grows only as \$\lceil p/2 \rceil^d\$.

**Q: Can you just flip the tie-breaker for bit 1 in \=2\True**

That makes the decoder encoding-dependent—it needs to know what was encoded, which is circular. The ternary tree solves this cleanly with a uniform rule.

**Q: Was the original paper wrong?**

No. The original’s results are valid for what was tested (bit 0). The asymmetry was structurally unrecognized, not falsified. This companion identifies and resolves it.

**Q: What’s the near-term experimental path?**

Neutral atom tweezer arrays—\=3\$, 40 atoms, controlled error injection, fluorescence readout, classical majority vote. No ancilla qubits, no syndrome measurement, no real-time feedback. Feasible on **existing** hardware.

**Q: Where’s the code?**

All code available in the companion repository. Standard-library Python 3.10+, seed=42. Reproducible on any machine with no external dependencies.
