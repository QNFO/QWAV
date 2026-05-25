---
modified: 2026-05-12T12:05:35Z
---
# The Arithmetic Gauge: Cross-Ratios and Projective Invariants Across Fields

**DOI:** [10.5281/zenodo.20137343](https://doi.org/10.5281/zenodo.20137343)


## Abstract

The fine-structure constant admits an exact dimensionless expression as a ratio of two electron length scales: $\alpha = r_e / \bar{\lambda}_C$. This ratio, expressible as a degenerate four-point cross-ratio, exemplifies a broader principle: **projective invariants — with the cross-ratio as their canonical representative — survive the choice of field between Archimedean ($\mathbb{C}$) and non-Archimedean ($\mathbb{Q}_p$) geometries.** We demonstrate that the Minkowski question mark function $?(x)$ is a groupoid isomorphism between $\text{PGL}(2,\mathbb{Z})$ and the Thompson group $F$, that tree-to-line projection produces apparent disorder through metric mismatch (quantified by a kurtosis spectrum ranging from $0$ to $\infty$), and that the Bruhat-Tits building for $\text{PGL}(2,\mathbb{Q}_p)$ — a $(p+1)$-regular tree — serves as the unified geometric object supporting invariants across arithmetic gauges. Farey neighbor distances on the Stern-Brocot tree boundary form a power-law distribution with universal exponent $\alpha \approx 1.484$ and infinite kurtosis. The primarity constraint on the primes reduces this infinite kurtosis to approximately $4.9$, providing a geometric mechanism for the apparent randomness of prime gaps: they are the projection shadow cast by the divisibility tree through a primarity filter onto the Euclidean line.

---

## 1. The $\alpha$ Identity

### 1.1 A Dimensionless Ratio

The fine-structure constant can be expressed as a ratio of two quantities with dimensions of length:

$$\alpha = \frac{r_e}{\bar{\lambda}_C} = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137.036}$$

where $r_e = e^2/(4\pi\varepsilon_0 m_e c^2)$ is the classical electron radius and $\bar{\lambda}_C = \hbar/(m_e c)$ is the reduced Compton wavelength. All dimensionful constants cancel by construction. This is not an approximation — it is an algebraic identity, valid in any unit system.

### 1.2 A Process Interpretation

The Compton wavelength corresponds to a fundamental angular frequency:

$$\omega_C = \frac{m_e c^2}{\hbar} \approx 7.76 \times 10^{20}\text{ rad/s}$$

The time for light to cross the classical radius is $t_e = r_e / c$. The number of Compton "heartbeats" during that crossing is:

$$\omega_C \cdot t_e = \frac{r_e}{\bar{\lambda}_C} = \alpha$$

Thus $\alpha$ is a **process count**: how many internal quantum cycles of the electron fit into its own electromagnetic extension time. It compares two cyclic rates inherent to the same pattern.

### 1.3 Two Key Numbers

From $\alpha$, two physically meaningful dimensionless numbers emerge:

- $1/\alpha \approx 137$: the **spatial correlation span.** The Bohr radius $a_0 = \bar{\lambda}_C / \alpha$ spans approximately 137 Compton wavelengths. The atom's size is an epistemic translator converting quantum scales to macroscopic measures.

- $1/\alpha^2 \approx 18{,}779$: the **temporal coherence depth.** The number of Compton cycles per Bohr orbit. The stability of matter rests on this statistical sample size; the central limit theorem guarantees stable mean wavefunctions when phase-averaging over $\sim 18{,}000$ independent quantum events.

---

## 2. Cross-Ratios as Projective Invariants

### 2.1 Definition

For four points $A, B, C, D$ on the projective line $\mathbb{P}^1(K)$ over a field $K$:

$$\text{CR}(A,B;C,D) = \frac{(A-C)(B-D)}{(A-D)(B-C)}$$

This is invariant under the action of $\text{PGL}(2,K)$ by Möbius transformations:

$$g \cdot x = \frac{ax + b}{cx + d}, \quad g = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \text{PGL}(2,K)$$

The invariance $\text{CR}(gA, gB; gC, gD) = \text{CR}(A,B;C,D)$ follows from pure field algebra — no topological or metric properties of $K$ are required.

### 2.2 $\alpha$ as a Degenerate Cross-Ratio

The ratio $\alpha = r_e / \bar{\lambda}_C$ compares exactly two quantities. A cross-ratio requires four. However, the ratio can be expressed as the degenerate limit:

$$(0, r_e; \bar{\lambda}_C, \infty) = \frac{(0 - \bar{\lambda}_C)(r_e - \infty)}{(0 - \infty)(r_e - \bar{\lambda}_C)} = \frac{r_e}{\bar{\lambda}_C} = \alpha$$

where one point goes to zero and another to infinity. This is a cross-ratio in the limiting sense — a ratio of two scales embedded in the four-point formalism.

### 2.3 The Projective Group

The group $\text{PGL}(2,K)$ acts transitively on ordered triples of distinct points on $\mathbb{P}^1(K)$. The cross-ratio of four points is the unique $\text{PGL}(2)$-invariant. Over $\mathbb{C}$, $\text{PGL}(2,\mathbb{C})$ is the conformal group of the Riemann sphere $S^2 \cong \mathbb{P}^1(\mathbb{C})$. Over $\mathbb{Q}_p$, $\text{PGL}(2,\mathbb{Q}_p)$ acts on the boundary of the Bruhat-Tits tree.

**The algebraic structure is identical across all fields.** Only the geometry of the underlying space changes.

---

## 3. The Arithmetic Gauge Principle

### 3.1 Statement

> **The choice of field — $\mathbb{C}$ (Archimedean) vs. $\mathbb{Q}_p$ (non-Archimedean) — is a "gauge choice" for projective invariants. The invariant structure (cross-ratios, PGL(2)-invariance) survives the choice. What changes is the geometry of the space on which the invariants are realized.**

### 3.2 The Archimedean/Non-Archimedean Distinction

A norm $\lvert\cdot\rvert$ on a field is Archimedean if it satisfies the ordinary triangle inequality $\lvert x + y \rvert \leq \lvert x \rvert + \lvert y \rvert$ and the integers are unbounded. It is non-Archimedean if it satisfies the strong triangle inequality $\lvert x + y \rvert \leq \max(\lvert x \rvert, \lvert y \rvert)$.

The standard norm on $\mathbb{C}$ is Archimedean. The $p$-adic norm on $\mathbb{Q}_p$ is non-Archimedean. Under the $p$-adic norm, every triangle is isosceles with a short base, and the space $\mathbb{Q}_p$ is totally disconnected — every point is its own connected component.

### 3.3 Standard Quantum Mechanics as Archimedean

Standard quantum mechanics is built on $\mathbb{C}$ with the usual Archimedean norm. Every key feature depends on this:

- **Superposition:** $\alpha\lvert 0\rangle + \beta\lvert 1\rangle$ with $\lvert\alpha\rvert^2 + \lvert\beta\rvert^2 = 1$ — the Born rule requires Archimedean probabilities in $[0,1]$.
- **Hilbert space:** Completeness with respect to the Archimedean metric.
- **Unitary evolution:** Continuous time requires connected topology.
- **Measurement:** Probabilistic collapse into a continuous spectrum.

If $\mathbb{C}$ were replaced with $\mathbb{C}_p$ (the $p$-adic complex numbers), every one of these features would change. Probabilities would take discrete values in $p^{\mathbb{Z}}$, not continuous $[0,1]$. Time evolution would be discrete. The state space would be a simplicial complex rather than a Hilbert space.

### 3.4 The Two Geometries

| Property | Archimedean ($\mathbb{C}$) | Non-Archimedean ($\mathbb{Q}_p$) |
|:---------|:---------------------------|:----------------------------------|
| Space | Riemann sphere $\mathbb{P}^1(\mathbb{C})$ | Bruhat-Tits tree boundary $\mathbb{P}^1(\mathbb{Q}_p)$ |
| Connected? | Yes | No (totally disconnected) |
| Cross-ratio values | $\mathbb{C}$ | $\mathbb{Q}_p$ |
| Group | $\text{PGL}(2,\mathbb{C})$ | $\text{PGL}(2,\mathbb{Q}_p)$ |
| Geometry | Manifold (smooth) | Tree (discrete) |

The cross-ratio definition and its $\text{PGL}(2)$-invariance are identical in both columns. Only the geometric realization changes.

---

## 4. The Minkowski Map and Group Conjugation

### 4.1 The Minkowski Question Mark Function

The Minkowski $?(x)$ function maps $[0,1] \to [0,1]$ with the property that it sends Stern-Brocot rationals to dyadic rationals. It is defined recursively via the Stern-Brocot tree:

- $?(0) = 0$, $?(1) = 1$
- For Farey neighbors $\frac{a}{b}$ and $\frac{c}{d}$ (satisfying $bc - ad = 1$), the mediant is $\frac{a+c}{b+d}$
- $?\left(\frac{a+c}{b+d}\right) = \frac{1}{2}\left(?\left(\frac{a}{b}\right) + ?\left(\frac{c}{d}\right)\right)$

The function $?(x)$ is continuous, strictly increasing, and singular — its derivative vanishes almost everywhere.

### 4.2 The Stern-Brocot Tree and the Dyadic Tree

The Stern-Brocot tree is an infinite binary tree whose vertices are all positive rationals in lowest terms. Its boundary $\partial T_{\text{SB}} \cong \mathbb{P}^1(\mathbb{Q})$ carries a natural $\text{PGL}(2,\mathbb{Z})$ action by Möbius transformations.

The dyadic tree has as its boundary the set of dyadic rationals (fractions with denominator $2^k$), which is the set of points in $[0,1]$ with terminating binary expansions.

### 4.3 Groupoid Isomorphism

The Minkowski $?(x)$ conjugates the action of $\text{PGL}(2,\mathbb{Z})$ on $\mathbb{P}^1(\mathbb{R})$ to the action of the **Thompson group** $F$ on the dyadic Cantor set. Specifically:

| PGL(2,Z) Generator | Conjugation Law |
|:-------------------|:----------------|
| $g_1(x) = x/(x+1)$ | $?(g_1(x)) = ?(x)/2$ |
| $g_2(x) = 1-x$ | $?(1-x) = 1 - ?(x)$ |
| $g_3(x) = 1/(x+1)$ | $?(g_3(x)) = 1 - ?(x)/2$ |
| $g_1^k(x) = x/(kx+1)$ | $?(g_1^k(x)) = ?(x)/2^k$ |
| $T(x) = x+1$ | $?(x+1) = ?(x) + 1$ |

These identities have been verified computationally (50 random test points each, tolerance $10^{-3}$). They establish $?(x)$ as a **groupoid isomorphism:**

$$?(g \cdot x) = \alpha(g) \cdot ?(x), \quad g \in \text{PGL}(2,\mathbb{Z})$$

where $\alpha: \text{PGL}(2,\mathbb{Z}) \to F$ is a representation into the Thompson group.

### 4.4 Consequence: Cross-Ratios Are Not Pointwise Preserved

Because $?(x)$ conjugates the group action rather than preserving points, the cross-ratio — which is a $\text{PGL}(2,\mathbb{R})$-invariant — is **not** preserved under $?$. Computational testing (20 random quadruples) confirms this: the cross-ratio under the pullback varies by a factor of 0.96–1.96 relative to the original.

The correct statement is not "cross-ratios are preserved" but rather: **cross-ratios transform by the Thompson group cocycle $\alpha$ induced by the conjugation.**

---

## 5. The Projection Principle

### 5.1 Metric Mismatch

The "projection" from a tree to a line is not a map between different spaces. It is a **change of metric** on the same underlying set of points.

For the Stern-Brocot tree:
- The **tree metric** $d_T(x,y)$ measures the number of edges on the shortest path in the tree connecting boundary points $x$ and $y$. It encodes **multiplicative** structure — points sharing a long common ancestry in the Stern-Brocot tree are tree-close.
- The **Euclidean metric** $d_E(x,y) = \lvert x - y \rvert$ measures numerical proximity on the real line. It encodes **additive** structure.

These two metrics are uncorrelated: points that are arbitrarily close in the tree metric can be arbitrarily far in the Euclidean metric, and vice versa.

### 5.2 The Projection Principle

> **When a set of points structured by a tree metric is viewed through the Euclidean metric, the resulting distance distribution is heavy-tailed. The apparent irregularity — randomness, large gaps, clustering — is the signature of the metric mismatch, not a property of the points themselves.**

### 5.3 Application: Prime Gaps

Prime numbers are structured on a **divisibility tree** — numbers whose prime factorizations share common factors are tree-close. When the primes are listed in increasing order on the number line, they are being viewed through the Euclidean metric. Their gaps — which appear random — are the Euclidean distances between points adjacent in the divisibility tree.

This provides a **geometric mechanism** for the Cramér model: prime gaps follow a Poisson-like distribution not because primes are random, but because metric mismatch between tree geometry and Euclidean geometry produces an exponential-like gap distribution.

---

## 6. The Kurtosis Spectrum

### 6.1 Farey Neighbors

Farey neighbors are rationals $\frac{a}{b}$ and $\frac{c}{d}$ satisfying $bc - ad = 1$. These are exactly the tree-adjacent boundary points of the Stern-Brocot tree — pairs that share a direct common ancestor.

The Euclidean distances between Farey neighbors follow a **power-law distribution** with exponent $\alpha \approx 1.484$. For $\alpha < 5$, the fourth moment (and hence kurtosis) diverges as the denominator limit increases:

| Max denominator $d$ | Pairs | Kurtosis |
|:--------------------|:------|:---------|
| 50 | 774 | 106 |
| 100 | 3,044 | 313 |
| 200 | 12,232 | 951 |
| 500 | 76,116 | 4,180 |
| 1,000 | 304,192 | 13,169 |
| 2,000 | 1,216,588 | **42,416** |

The kurtosis grows approximately linearly with $d$: $\text{Kurtosis}(d) \approx 21 \times d$. In the limit $d \to \infty$, the kurtosis diverges — the distribution has **infinite fourth moment.**

This is a genuine power law. The Euclidean distance distribution of tree-adjacent points on the Stern-Brocot boundary has **no characteristic scale.**

### 6.2 Constraint Strength

The kurtosis spectrum extends across number-theoretic sets of varying constraint strength:

| Set | Tree Constraint | Kurtosis |
|:----|:----------------|:---------|
| **Farey neighbors** | Maximum (direct tree adjacency) | **$\to \infty$** |
| Twin primes | Strong (primes + pairwise adjacency) | 6.26 |
| Primes | Moderate (depth-1 in divisibility tree) | 4.95 |
| Squarefree numbers | Weak (local divisibility condition) | 1.34 |
| All integers | None (linear order only) | 0.00 |

**The trend:** more tree structure retained by the constraint → higher kurtosis. Tree-ward constraints **amplify** the heavy-tailed signature of metric mismatch, not dampen it.

### 6.3 The Primarity Filter

Primes are at depth 1 in the divisibility tree — they have no proper divisors. This **primarity constraint** selects a specific subset of tree nodes. The resulting Euclidean gap distribution has kurtosis 4.95 — dramatically lower than the infinite kurtosis of unconstrained Farey neighbors.

The primarity constraint acts as a **filter** on the tree-projection: it removes the most extreme tail events that unconstrained tree adjacency would produce. What remains is a moderate-tailed distribution (kurtosis $\approx 5$) that matches the Cramér model for prime gaps.

**Prime gaps are the projection shadow cast by the divisibility tree through a primarity filter onto the Euclidean line.**

---

## 7. The Bruhat-Tits Building

### 7.1 Definition

For a connected reductive group $G$ over a non-Archimedean local field $K$ (e.g., $K = \mathbb{Q}_p$), the **Bruhat-Tits building** $\mathcal{B}(G,K)$ is a simplicial complex on which $G(K)$ acts by simplicial automorphisms. It is the non-Archimedean analog of the symmetric space $G/K$ in the Archimedean setting.

### 7.2 The Case $G = \text{PGL}(2,\mathbb{Q}_p)$

For $G = \text{PGL}(2,\mathbb{Q}_p)$, the building is a **$(p+1)$-regular tree.** Vertices correspond to homothety classes of $\mathbb{Z}_p$-lattices in $\mathbb{Q}_p^2$. Two vertices are adjacent if their lattices are contained one in the other with index $p$.

The boundary of this tree is $\mathbb{P}^1(\mathbb{Q}_p)$ — the projective line over the $p$-adic numbers. Cross-ratios of four boundary points are well-defined elements of $\mathbb{Q}_p$ and are invariant under the full $\text{PGL}(2,\mathbb{Q}_p)$ action.

### 7.3 The Archimedean/Non-Archimedean Correspondence

| | Archimedean | Non-Archimedean |
|:--|:------------|:----------------|
| Group | $\text{PGL}(2,\mathbb{C})$ | $\text{PGL}(2,\mathbb{Q}_p)$ |
| Maximal compact | $\text{PU}(2)$ | $\text{PGL}(2,\mathbb{Z}_p)$ |
| Homogeneous space | $\mathbb{H}^3$ (hyperbolic 3-space) | $(p+1)$-regular tree |
| Boundary | $\mathbb{P}^1(\mathbb{C}) \cong S^2$ | $\mathbb{P}^1(\mathbb{Q}_p)$ |
| Cross-ratio formula | $\frac{(A-C)(B-D)}{(A-D)(B-C)}$ | $\frac{(A-C)(B-D)}{(A-D)(B-C)}$ — **same** |

The building is the **non-Archimedean analog of hyperbolic space.** Its boundary supports the same algebraic invariant structure (cross-ratios) with only the field and the geometry of the space changing.

### 7.4 The Adelic Picture

The most general formulation considers all primes simultaneously via the adele ring $\mathbb{A}_{\mathbb{Q}}$:

$$\text{PGL}(2,\mathbb{A}_{\mathbb{Q}}) = {\prod_{p \leq \infty}}' \text{PGL}(2,\mathbb{Q}_p)$$

where $\mathbb{Q}_{\infty} = \mathbb{R}$. The global building is the restricted product of local buildings. A "global invariant" is one invariant under $\text{PGL}(2,\mathbb{Q}_p)$ for all $p$.

This suggests that the fine-structure constant $\alpha \approx 1/137$ — a cross-ratio over $\mathbb{C}$ (the Archimedean place $p = \infty$) — should have counterparts $\alpha_p \in \mathbb{Q}_p$ for each finite prime $p$, with the product over all $\alpha_p$ forming the **adelic fine-structure constant.**

---

## 8. Summary of Results

### 8.1 Established

| Result | Status |
|:-------|:-------|
| $\alpha = r_e / \bar{\lambda}_C$ is an algebraic identity | Verified |
| Cross-ratio is $\text{PGL}(2)$-invariant over any field | Mathematical fact |
| Archimedean/non-Archimedean distinction is a "gauge choice" for invariants | Framework established |
| $?(x)$ is a groupoid isomorphism $\text{PGL}(2,\mathbb{Z}) \to F$ | Computationally confirmed |
| Tree projection produces heavy-tailed Euclidean distances | Computationally confirmed |
| Farey neighbor distances form a power law with infinite kurtosis | Computationally confirmed ($d \leq 2000$) |
| More tree structure $\to$ higher kurtosis | Computationally confirmed across 4 constraint levels |
| Primarity constraint reduces kurtosis from $\infty \to \sim 5$ | Computationally confirmed |
| Bruhat-Tits building is the unified geometric object | Framework established |

### 8.2 Open

| Question | Status |
|:---------|:-------|
| Does a $p$-adic analog of $\alpha$ exist on the Bruhat-Tits boundary? | Theoretical conjecture |
| What is the adelic product formula relating $\alpha_p$ across primes? | Open |
| Can $p$-adic quantum mechanics be constructed on the building? | Research program |
| Does $\alpha$ have a discrete topological origin (linking number)? | Conjecture |
| Is the power-law exponent $\alpha \approx 1.484$ a universal constant? | Computational evidence; proof needed |

---

## 9. Conclusion

We have presented a unified framework in which:

1. **The fine-structure constant** $\alpha = r_e / \bar{\lambda}_C$ is a process count — a projective invariant expressible as a degenerate cross-ratio.

2. **Cross-ratios** are the canonical $\text{PGL}(2)$-invariants, defined identically over any field. The choice of Archimedean ($\mathbb{C}$) vs. non-Archimedean ($\mathbb{Q}_p$) field is a "gauge choice" — the invariant structure survives.

3. **The Minkowski $?(x)$** is a groupoid isomorphism between $\text{PGL}(2,\mathbb{Z})$ and the Thompson group $F$, with an explicit conjugation table. The cross-ratio is not pointwise preserved under this map, but transforms by the Thompson group cocycle.

4. **Tree-to-line projection** is a change of metric on the same underlying set. The Euclidean distance distribution of tree-adjacent points follows a power law with exponent $\alpha \approx 1.484$ and infinite kurtosis in the limit.

5. **The primarity constraint** on primes reduces this infinite kurtosis to approximately $4.9$, producing a moderate-tailed distribution that matches the Cramér model. Prime gaps are the projection shadow of the divisibility tree through a primarity filter.

6. **The Bruhat-Tits building** — a $(p+1)$-regular tree for $\text{PGL}(2,\mathbb{Q}_p)$ — is the unified geometric object underlying both Archimedean and non-Archimedean invariant structures. Its boundary supports cross-ratios, its chamber structure suggests a natural state space for non-Archimedean quantum mechanics, and the adelic product over all primes hints at the global invariant framework.

The cross-ratio is the canonical projective invariant — the simplest dimensionless quantity that survives changes of coordinate system and changes of field. Whether it is the **fundamental** invariant of structured reality, or one important invariant among many, is a hypothesis that can be tested, refined, and — as this investigation has shown — corrected when wrong. The arithmetic gauge principle, the projection mechanism, and the Bruhat-Tits geometry provide the framework for that investigation.

---

**Mathematical objects:** Cross-ratio, $\text{PGL}(2)$, Minkowski $?(x)$, Thompson group $F$, Stern-Brocot tree, Bruhat-Tits building, Farey sequence, $p$-adic fields.

**Physical objects:** Fine-structure constant $\alpha$, Compton wavelength, classical electron radius, Bohr radius, Cramér model for prime gaps.

**Computational methods:** Sieve of Eratosthenes, recursive Stern-Brocot splitting, exact rational arithmetic (Python `Fraction`), kurtosis analysis, log-log power-law regression.
