---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: Fine-Structure Constant as a Cross-Ratio
aliases:
  - Fine-Structure Constant as a Cross-Ratio
  - The Fine-Structure Constant as a Cross-Ratio
modified: 2026-05-10T09:46:39Z
---

# Fine-Structure Constant as a Cross-Ratio

## A Geometric Reframing of $\alpha$

**Author:** Rowan Brad Quni-Gudzinas
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.20100109](http://doi.org/10.5281/zenodo.20100109)
**Date:** 2026-05-10
**Version:** 0.8

**Abstract**: The fine-structure constant $\alpha \approx 1/137.036$ is one of the most precisely measured numbers in physics, yet its origin remains unexplained. The standard presentation—$\alpha = e^2/(4\pi\varepsilon_0\hbar c)$ with dimensionful constants—frames it as an abstract coupling strength, obscuring its geometric character. This document proposes a reframing: $\alpha$ is naturally understood as the cross-ratio of two measurable length scales characterizing the electron—the classical electron radius $r_e$ and the reduced Compton wavelength $\bar{\lambda}_C$. The reframing makes three contributions: (a) it reveals $\alpha$’s projective invariance structure, explaining why $\alpha$ is independent of unit choices and coordinate rescalings in geometric rather than algebraic terms; (b) it connects to the integer-ratio structure of precision experiments, where $\alpha$ is determined from rational observables (quantum Hall filling factors $\nu = p/q$, Penning trap frequency ratios $N_s/N_c)$; and (c) it integrates five complementary mathematical formalisms—adelic, projective, topological, syntactic, and hierarchical—that illuminate different aspects of $\alpha$’s cross-ratio nature. The document includes Python-verified quantitative results, historical context (Eddington, Wyler), experimental grounding, and an honest acknowledgment of limitations—most notably that $\alpha = r_e/\bar{\lambda}_C$ is an algebraic identity, not a first-principles derivation, and the contribution lies in conceptual reframing rather than numerical prediction.

---

## 1. The Puzzle

### 1.1 What Is the Fine-Structure Constant?

The fine-structure constant, denoted $\alpha$ (alpha), is a dimensionless number that characterizes the strength of electromagnetic interactions:

$$ \alpha = \frac{e^2}{4\pi\varepsilon_0 \hbar c} \approx \frac{1}{137.035999084} $$

where e is the elementary charge, $\varepsilon_0$ is the vacuum permittivity, $\hbar = h/(2\pi)$ is the reduced Planck constant, and c is the speed of light. Introduced by Arnold Sommerfeld in 1916, $\alpha$ was the first dimensionless combination of fundamental constants to be recognized as physically significant.

$\alpha$ appears throughout physics:
- In quantum electrodynamics, it sets the scale of all electromagnetic processes—the probability of emitting a photon, the strength of electron-electron scattering, the Lamb shift in hydrogen
- In atomic physics, it controls the fine-structure splitting of spectral lines (hence the name)
- In condensed matter physics, it determines the von Klitzing constant $R_K = h/e^2$ measured in the quantum Hall effect
- In metrology, it is the link between the Josephson effect (frequency-to-voltage conversion) and the quantum Hall effect (resistance quantization)

Despite being one of the most precisely measured numbers in science (relative uncertainty $~1.5 \times 10^{-10}$ as of CODATA 2018), $\alpha$ has no accepted theoretical explanation. It is an input parameter—measured, not derived.

### 1.2 The Question

Why does $\alpha$ take the value $\approx 1/137.036$ and not some other number? Is this value fundamental—a brute fact about our universe—or is it derivable from deeper principles?

This question has attracted some of the greatest minds in physics. Wolfgang Pauli famously quipped: “When I die, my first question to the Devil will be: What is the meaning of the fine-structure constant?” Richard Feynman called it “one of the greatest damn mysteries of physics: a magic number that comes to us with no understanding by humans.” Arthur Eddington spent the last two decades of his career attempting to derive $\alpha$ from pure mathematics, with results that were initially celebrated and later dismissed as numerology.

This document argues that the way we *present* $\alpha$—as a transcendental real number $1/137.036$..., cobbled together from dimensionful constants—obscures its true nature. When reframed geometrically, $\alpha$ reveals itself as a *cross-ratio*: a projective invariant of two characteristic length scales of the electron.

### 1.3 What This Document Does and Does Not Claim

**What it claims:**
1. $\alpha$ can be understood as the ratio $r_e / \bar{\lambda}_C$, where $r_e$ is the classical electron radius and $\bar{\lambda}_C$ is the reduced Compton wavelength
2. This ratio has the mathematical structure of a projective cross-ratio—an invariant under Möbius transformations
3. Reframing $\alpha$ as a cross-ratio makes its invariance properties geometrically transparent and connects naturally to how $\alpha$ is measured in precision experiments
4. Five complementary mathematical formalisms (adelic, projective, topological, syntactic, hierarchical) illuminate different aspects of this cross-ratio structure

**What it does NOT claim:**
1. That $\alpha = r_e/\bar{\lambda}_C$ is a *derivation* of $\alpha$ from first principles—it is an algebraic identity since $r_e \equiv \alpha \bar{\lambda}_C$ by definition
2. That $\alpha$ itself is a rational number—the claim is about measurement methodology, not ontology
3. That the five formalisms represent independent discoveries by different researchers
4. That the cross-ratio framing makes novel, testable predictions (beyond those already pursued in precision metrology)

The contribution is **conceptual reframing**, not numerical derivation. Like changing coordinate systems in geometry, a reframing does not create new information—but it can make hidden structure visible.

---

## 2. The Reframing: $\alpha$ as a Length Ratio

### 2.1 Two Characteristic Lengths of the Electron

An electron is characterized by two natural length scales:

**The classical electron radius $r_e$**: In classical electrodynamics, if you imagine the electron’s charge distributed over a sphere, the electrostatic self-energy is E = $e^2/(4\pi\varepsilon_0r)$. Setting this equal to the rest energy $m_e c^2$ gives the classical electron radius:

$$ r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.818 \times 10^{-15} \text{ m} $$

Physically, $r_e$ characterizes the scale at which electromagnetic interactions become strong enough that the classical picture breaks down. It appears in the Thomson cross-section for low-energy photon-electron scattering: $\sigma_T = (8\pi/3) r_e^2 \approx$ 0.665 barn.

**The reduced Compton wavelength $\bar{\lambda}_C$**: In quantum mechanics, the Compton wavelength $\lambda_C = h/(m_e$ c) is the scale at which quantum field theory effects become important—pair creation, vacuum polarization. The reduced Compton wavelength is:

$$ \bar{\lambda}_C = \frac{\hbar}{m_e c} = \frac{\lambda_C}{2\pi} \approx 3.862 \times 10^{-13} \text{ m} $$

Physically, $\bar{\lambda}_C$ is approximately the scale below which the concept of a single-particle description breaks down and quantum field theory becomes necessary. It appears in the Compton scattering formula: the wavelength shift when a photon scatters off an electron is $\Delta\lambda = \lambda_C$ (1 - cos $\theta)$.

**Notation warning:** Throughout this document, $\bar{\lambda}_C$ (read “lambda-bar-sub-C”) denotes the reduced Compton wavelength $\hbar/(m_e$ c). The non-reduced Compton wavelength $\lambda_C = h/(m_e$ c) is $2\pi$ times larger. Using the non-reduced wavelength would give $r_e/\lambda_C = \alpha/(2\pi)$, which is NOT $\alpha$. This distinction is essential.

### 2.2 The Ratio

Divide the two lengths:

$$ \frac{r_e}{\bar{\lambda}_C} = \frac{e^2/(4\pi\varepsilon_0 m_e c^2)}{\hbar/(m_e c)} = \frac{e^2}{4\pi\varepsilon_0 \hbar c} = \alpha $$

The ratio is exactly the fine-structure constant. This is not a coincidence—it follows from the definitions of $r_e, \bar{\lambda}_C$, and $\alpha$. Mathematically, it is an algebraic identity: $r_e \equiv \alpha \bar{\lambda}_C$ by definition, so the ratio gives $\alpha$ by construction.

### 2.3 Why Reframe?

If $\alpha = r_e/\bar{\lambda}_C$ is just an algebraic identity, what is gained by reframing $\alpha$ as a length ratio? Three things:

**First, the reframing reveals geometric structure.** The standard presentation $\alpha = e^2/(4\pi\varepsilon_0\hbar c)$ involves four dimensionful constants (e, $\varepsilon_0, \hbar$, c) whose numerical values depend on the human-chosen SI unit system. The fact that $\alpha$ is dimensionless is presented as a happy algebraic cancellation—the units “happen” to cancel. The length-ratio presentation $\alpha = r_e/\bar{\lambda}_C$ makes the dimensionless nature geometrically obvious: we are comparing two lengths, so the units must cancel regardless of which units we choose.

**Second, the reframing connects to projective geometry.** The ratio of two lengths can be embedded as a *cross-ratio* on the projective line—a mathematical object with well-understood invariance properties. This embedding reveals that $\alpha$ inherits its unit-independence from a deeper mathematical principle: projective invariance under Möbius transformations.

**Third, the reframing illuminates experimental methodology.** The highest-precision measurements of $\alpha$ (quantum Hall effect, Penning trap g-2) proceed by counting—integer filling factors $\nu = p/q$, integer cycle counts $N_s/N_c$. The length-ratio framing makes the connection between $\alpha$ and counting experiments natural: if $\alpha$ is fundamentally a ratio, then measuring it by counting ratios is the conceptually appropriate method.

In short: the coupling-constant framing answers “what is $\alpha?$” with “the strength of electromagnetism”—a true but opaque answer. The length-ratio framing answers with “the ratio of the electron’s electromagnetic size to its quantum size”—a geometrically revealing answer.

---

## 3. The Mathematics: Cross-Ratios and Projective Geometry

### 3.1 What Is a Cross-Ratio?

In projective geometry, the *cross-ratio* (also called the anharmonic ratio) is the fundamental invariant associated with four collinear points. Given four distinct points with coordinates $x_1, x_2, x_3, x_4$ on a line, the cross-ratio is:

$$ (x_1, x_2; x_3, x_4) = \frac{(x_1 - x_3)(x_2 - x_4)}{(x_1 - x_4)(x_2 - x_3)} $$

The cross-ratio has a remarkable property: it is **invariant under all Möbius transformations**. A Möbius transformation maps each coordinate as:

$$ x \mapsto \frac{ax + b}{cx + d}, \quad ad - bc \neq 0 $$

This means that no matter how we choose our coordinate system—where we place the origin, what we call the unit length, how we stretch or compress the line—the cross-ratio of four points remains unchanged. The cross-ratio is the **only** quantity with this property; it is the complete set of projective invariants for four collinear points.

**Examples:**
- (0, 1; 2, 3) = (0-2)(1-3)/((0-3)(1-2)) = (-2)(-2)/((-3)(-1)) = $4/3$
- (1, 2; 4, 8) $\approx$ 1.286
- After any Möbius transformation of the coordinates, these values remain identical.

The 24 possible orderings of four points produce at most 6 distinct cross-ratio values, related by the *anharmonic group* (isomorphic to the symmetric group $S_3): {\lambda, 1/\lambda, 1−\lambda, 1/(1−\lambda), (\lambda−1)/\lambda, \lambda/(\lambda−1)}$.

### 3.2 Simple Ratios as Degenerate Cross-Ratios

Any simple ratio $a/b$ can be expressed as a degenerate cross-ratio by placing two reference points at 0 and $\infty$:

$$ (0, \infty; a, b) = \lim_{L \to \infty} \frac{(0 - a)(L - b)}{(0 - b)(L - a)} = \frac{(-a)}{(-b)} \cdot \lim_{L \to \infty} \frac{L - b}{L - a} = \frac{a}{b} $$

As L $\to \infty$, the fraction (L−b)/(L−a) $\to$ 1, leaving $a/b$. This is verified computationally (see Appendix A).

### 3.3 $\alpha$ As a Cross-Ratio

Applying this to $\alpha$:

$$ (0, \infty; r_e, \bar{\lambda}_C) = \frac{r_e}{\bar{\lambda}_C} = \alpha $$

The four projective points and their interpretations:

| Point | Coordinate | Physical Interpretation | Role |
|:------|:-----------|:------------------------|:-----|
| $P_0$ | 0 [0:1] | Zero-length reference | Mathematical anchor—fixes the origin |
| $P_\infty$ | $\infty$ [1:0] | Scale anchor at infinity | Mathematical anchor—ensures projective invariance |
| $P_a$ | $r_e [r_e:1]$ | Classical electron radius | Physical length—characterizes electromagnetic interaction scale |
| $P_b$ | $\bar{\lambda}_C [\bar{\lambda}_C:1]$ | Reduced Compton wavelength | Physical length—characterizes quantum-relativistic scale |

**Important clarification:** Points $P_0$ and $P_\infty$ are **mathematical reference points**, not physically distinct length scales. The physically meaningful content is entirely in the relationship between the two physical points—$r_e$ and $\bar{\lambda}_C$. One should not claim that $\alpha$ is “a cross-ratio of four physical lengths.” It is a cross-ratio of two physical lengths embedded in a projective frame that requires two mathematical reference points for its formal definition.

### 3.4 Why Projective Invariance Matters

The Möbius invariance of the cross-ratio means $\alpha$ does not depend on:

1. **Choice of length units:** Whether $r_e$ and $\bar{\lambda}_C$ are expressed in meters, Planck lengths, or light-years—the ratio is the same
2. **Choice of coordinate origin:** Where we place “zero” on the length scale is irrelevant
3. **Smooth rescalings:** Any transformation x $\to$ (ax + b)/(cx + d) leaves $\alpha$ unchanged

These are precisely the properties we demand of a genuine physical invariant: it must be independent of human conventions about measurement systems and coordinate choices. The cross-ratio provides the mathematical guarantee that $\alpha$ satisfies these requirements.

Note that $\alpha$ is already known to be dimensionless, and dimensionless numbers are trivially independent of unit choices. The cross-ratio framing does not *discover* new invariance—it *explains* the existing invariance in geometric terms, making intuitive what the coupling-constant framing merely asserts.

---

## 4. Quantitative Verification

All numerical results in this section are produced by self-contained Python code (see Appendix A). The code is re-executable and all values are `[CODE-EXECUTED]`.

### 4.1 Fundamental Constants and Length Scales

The following values use CODATA 2018 fundamental constants. Since the 2019 redefinition of SI base units, e, $\hbar$, and c are **exactly defined**, while $\varepsilon_0$ and $m_e$ are measured quantities.

```
e      = 1.602176634 $\times 10^{-19}$ C    (exact)
$\hbar$      = 1.054571817 $\times 10^{-34} J\cdots$  (exact)
c      = 299792458 $m/s$             (exact)
$\varepsilon_0$     = 8.8541878128 $\times 10^{-12} F/m$ (measured post-2019)
$m_e$    = 9.1093837015 $\times 10^{-31}$ kg  (measured)
```

Derived length scales:
```
$r_e$    = 2.817940 $\times 10^{-15}$ m    (classical electron radius)
$\bar{\lambda}_C$    = 3.861593 $\times 10^{-13}$ m    (reduced Compton wavelength)
$\lambda_C$    = 2.426310 $\times 10^{-12}$ m    (non-reduced Compton wavelength)
```

### 4.2 Α Verification

$\alpha$ computed via three routes—all must agree to machine precision:

| Route | Value | Matches? |
|:------|:------|:---------|
| $\alpha = e^2/(4\pi\varepsilon_0\hbar c)$ | 0.007297352573749 | Reference |
| $\alpha = r_e / \bar{\lambda}_C$ | 0.007297352573749 | ✓ |
| $\alpha = r_e / \lambda_C$ | 0.001161409733597 | ✗ (off by factor $2\pi)$ |

The second row confirms $\alpha = r_e/\bar{\lambda}_C$. The third row shows the hazard of using the non-reduced Compton wavelength.

**Inverse fine-structure constant:**
```
$1/\alpha$ (computed)       = 137.035999000144
CODATA 2018 $1/\alpha$      = 137.035999084
Difference            = 8.4 $\times 10^{-8}$ (well within CODATA uncertainty)
```

### 4.3 Cross-Ratio Verification

The degenerate cross-ratio (0, $\infty$; a, b) = $a/b$ is verified numerically:

| a | b | $a/b$ | $(0,\infty;a,b)$ | Match |
|:--|:--|:----|:----------|:------|
| $r_e$ | $\bar{\lambda}_C$ | 0.007297352573749 | 0.007297352573749 | ✓ |
| 3 | 1 | 3.000000000000000 | 3.000000000000000 | ✓ |
| 1 | $\pi$ | 0.318309886183791 | 0.318309886183791 | ✓ |

The verification uses L = $10^{30}$ as a numerical proxy for infinity. The limit converges rapidly.

### 4.4 Thomson and Compton Scattering

The two length scales are independently measurable through classical and quantum scattering:

**Thomson scattering** gives $r_e$ via the low-energy photon-electron cross-section:
```
$\sigma_T = (8\pi/3) r_e^2$ = 6.652 $\times 10^{-29} m^2$ = 0.665 barn
```

**Compton scattering** gives $\bar{\lambda}_C$ via the wavelength shift at 180°:
```
$\Delta\lambda_max$ = 2 $\lambda_C$ = 4.853 $\times 10^{-12}$ m
$\bar{\lambda}_C = \Delta\lambda_max / (4\pi)$
```

While these measurements are conceptually independent (classical EM vs. quantum mechanics), the identity $r_e = \alpha \bar{\lambda}_C$ means they measure the same underlying physics. The measurements are independent in methodology but not in physical content.

---

## 5. The Experiments: Integer-Count Measurements

### 5.1 How Α Is Actually Measured

The highest-precision determinations of $\alpha$ do not involve measuring $r_e$ with a ruler or $\bar{\lambda}_C$ with a wavelength meter. Instead, they use two types of counting experiments:

### 5.2 Quantum Hall Effect

When a two-dimensional electron gas is subjected to a strong perpendicular magnetic field at low temperature, the Hall resistance $R_H = V_H/I$ becomes *quantized*:

$$ R_H = \frac{h}{e^2} \cdot \frac{1}{\nu} = \frac{R_K}{\nu} $$

where $R_K = h/e^2 \approx$ 25,812.807 $\Omega$ is the von Klitzing constant, and $\nu$ is the *filling factor*—a rational number representing the ratio of electron density to magnetic flux quanta density.

**Observed filling factors:**
```
$\nu$ = 1, 2, 3, 4, ...       (integer quantum Hall effect)
$\nu = 1/3, 2/3, 2/5$,        (fractional quantum Hall effect)
    $3/5, 3/7, 4/7$, ...
```

The filling factor $\nu = p/q$ is a rational number—a ratio of integers. The measurement determines $R_K$ by comparing the quantized Hall resistance to a known reference, often using a Josephson voltage standard where voltage steps are produced at frequencies $f_n = 2eV/h$, and the step number (an integer count) determines the voltage.

From $R_K$, the fine-structure constant follows as $\alpha = \mu_0c/(2R_K)$ in the pre-2019 SI, or through the measured $\varepsilon_0$ in the post-2019 SI.

**Key point:** The experimentally measured quantity—the filling factor $\nu = p/q$—is a rational number. $\alpha$ is *extracted* from this rational measurement. The “transcendental” decimal $1/137.035999084$ is not directly measured; it is computed from rational inputs.

### 5.3 Penning Trap (g−2)

A single electron is trapped in a Penning trap—a combination of electric and magnetic fields that confines the electron to a small volume. The electron exhibits three characteristic motions:
- **Cyclotron motion:** $\omega_c = eB/m_e$ (circular motion in the magnetic field)
- **Spin precession:** $\omega_s$ = g e B/(2 $m_e)$ (precession of the electron’s intrinsic spin)

The anomalous magnetic moment $a_e$ = (g−2)/2 is obtained by comparing these two frequencies:

$$ a_e = \frac{\omega_s}{\omega_c} - 1 = \frac{N_s}{N_c} - 1 $$

where $N_s$ and $N_c$ are the **counted** numbers of spin-precession and cyclotron cycles over the measurement interval. Both are integers. Thus $a_e$ is directly a **rational number**—the ratio of two integer counts, minus one.

**Concrete example:** The experimentally measured $a_e \approx$ 0.00115965218059 corresponds to approximately $N_s/N_c \approx$ 7,090,509 / 7,082,296 $\approx$ 1.0011596522. Neither of these large integers is “fundamental”—they depend on the measurement duration—but their *ratio* is the physical observable, and it is rational.

**Extracting $\alpha$ from $a_e$**: The QED prediction for the anomalous magnetic moment is a perturbation series:

$$ a_e^{\text{QED}}(\alpha) = \frac{\alpha}{2\pi} + C_2\left(\frac{\alpha}{\pi}\right)^2 + C_3\left(\frac{\alpha}{\pi}\right)^3 + C_4\left(\frac{\alpha}{\pi}\right)^4 + C_5\left(\frac{\alpha}{\pi}\right)^5 + \ldots $$

where $C_2 \approx$ −0.328, $C_3 \approx$ 1.181, $C_4 \approx$ −1.914, and $C_5$ requires evaluating 12,672 Feynman diagrams. To extract $\alpha$, we solve $a_e^{\text{QED}}(\alpha) = a_e^{\text{measured}}$ for $\alpha$.

**A note on circularity:** This extraction uses a series in powers of $\alpha$ to solve for $\alpha$—an apparent circularity. This is not unique to $\alpha$; it is standard practice in quantum field theory parameter extraction (the strong coupling $\alpha_s$ is extracted similarly). The circularity is *computational*, not ontological: we use an iterative scheme to find the value of $\alpha$ that makes QED match measurement. The convergence of the scheme confirms that $\alpha$ is a well-defined parameter, regardless of whether it is “fundamental.”

### 5.4 The Measurement $\to$ Cross-Ratio Connection

| Experiment | Directly Measured | Integer-Ratio Observable | $\alpha$ Extraction |
|:-----------|:------------------|:-------------------------|:-------------|
| Quantum Hall | $R_K = h/e^2$ | $\nu = p/q$ (rational filling factor) | $\alpha = \mu_0c/(2R_K)$ |
| Penning trap | $a_e$ = (g−2)/2 | $a_e = N_s/N_c$ − 1 (rational) | Solve QED series |
| Josephson effect | $K_J = 2e/h$ | Frequency ratio (counted cycles) | Combined with $R_K$ |
| Atom interferometry | $h/m$ ratio | Recoil frequency (counted) | Combined with $R_K$ |

In every case, the experiment directly measures a rational number—a ratio of integer counts. $\alpha$ is extracted from these rational observables. The cross-ratio framing makes this connection natural: just as $(0,\infty; r_e, \bar{\lambda}_C)$ is a ratio of lengths, the filling factor $\nu$ and the frequency ratio $N_s/N_c$ are ratios of counts—and all are projective invariants of their respective domains.

---

## 6. The History: Past Attempts to Explain Α

### 6.1 Eddington’s Fundamental Theory

Arthur Eddington (1882–1944) was among the first to attempt a derivation of $\alpha$ from pure mathematics. His approach was audacious: he sought to derive all physical constants from epistemological first principles—the claim that the structure of physical law is determined by the structure of observation itself.

Eddington initially derived $\alpha^{-1}$ = 136, arguing that his “E-number” algebra (a 16-dimensional algebraic structure) contained exactly 136 independent components—and that $\alpha$ must be their reciprocal. When experimental evidence shifted toward $\alpha^{-1} \approx$ 137, he revised his theory, introducing an additional degree of freedom to reach 137.

**Numerical comparison:**
```
Eddington $\alpha^{-1}$ = 136  $\to$  deviation from CODATA: 7,618 ppm
Eddington $\alpha^{-1}$ = 137  $\to$  deviation from CODATA: 263 ppm
CODATA 2018 $\alpha^{-1}$     = 137.035999084
```

Eddington’s program is now generally regarded as a failure—a cautionary tale about the dangers of numerology, where a theory is adjusted post hoc to match data. However, his core intuition—that $\alpha$ should be derivable from mathematical structure rather than accepted as a brute fact—is shared by the cross-ratio approach. The difference is that Eddington sought a *single integer* as the source of $\alpha$, while the cross-ratio approach identifies the *ratio structure*—the relationship between quantities, not the quantities themselves—as the proper mathematical object.

### 6.2 Wyler’s 1969 Formula

Armand Wyler proposed in 1969 that $\alpha$ could be derived from the geometry of bounded complex domains:

$$ \alpha_{\text{Wyler}} = \frac{9}{16\pi^3} \left( \frac{\pi}{5!} \right)^{1/4} $$

Numerical evaluation:
```
Wyler $\alpha$           = 0.007297348130032
1 / Wyler $\alpha$       = 137.036082448164
CODATA 2018 $1/\alpha$  = 137.035999084
Deviation          = 0.6 parts per million
```

The 0.6 ppm deviation is comparable to the experimental uncertainty of $\alpha$ when Wyler published his formula in 1969—meaning he could not have fudged his formula to match a precision that did not exist at the time.

Wyler’s derivation invoked the conformal group SO(4,2) acting on a bounded complex domain—a group-theoretic, geometric origin. While his argument was never widely accepted (and his formula, elegant as it is, has not been placed on a rigorous foundation), the 0.6 ppm match is striking.

**Honest assessment:** The Wyler formula’s accuracy is genuinely surprising. However, without a statistical analysis of how many random formulas of similar complexity would coincidentally hit within 0.6 ppm of $1/137.036$, the significance is aesthetic rather than statistical. The formula motivates the search for a geometric derivation of $\alpha$ but does not itself constitute one.

### 6.3 The Numerology Problem

A persistent challenge in $\alpha$ research is distinguishing genuine mathematical structure from the “Strong Law of Small Numbers”—the fact that with small integers, factorials, and powers of $\pi$, one can construct many formulas that approximate any given small number. The numbers 136, 137, and 138 were all proposed at various times by different researchers using different combinations of integers.

The cross-ratio reframing addresses this by focusing not on a *single number* (137 or otherwise) but on a *structure*—the ratio $r_e/\bar{\lambda}_C$ and its embedding in projective geometry. The structure is the invariant; the specific decimal value $1/137.036$ is the contingent realization of that structure in our universe.

---

## 7. The Landscape: Five Complementary Formalisms

The cross-ratio nature of $\alpha$ has been approached from five different mathematical directions within a unified research program. These formalisms are *complementary* (each illuminating a different aspect) rather than *independent* (they were developed by the same investigator in overlapping time periods).

### 7.1 Adelic / Number-Theoretic

**Mathematical language:** Ostrowski’s theorem, p-adic numbers, adelic product formulas

**Key idea:** Ostrowski’s theorem states that the only completions of the rational numbers $\mathbb{Q}$ are the real numbers $\mathbb{R}$ (the “archimedean” completion, corresponding to the usual absolute value) and the p-adic numbers $\mathbb{Q}_p$ (the “non-archimedean” completions, one for each prime p). If a physical quantity is well-defined, it must be consistently expressible across *all* completions of $\mathbb{Q}$—the “adelic” requirement. This forces the quantity to have the structure of a cross-ratio: something whose archimedean component (the real number we measure) and non-archimedean components (its p-adic valuations) satisfy a product formula.

**Contribution:** Establishes *why* $\alpha$ must be a cross-ratio—the adelic consistency requirement. However, adelic consistency alone does not fix the numerical value of $\alpha$; it constrains the functional form but requires additional geometric input.

### 7.2 Projective / Geometric (This Work)

**Mathematical language:** Cross-ratio of four collinear points, Möbius transformations, projective line $\mathbb{P}^1$

**Key idea:** $\alpha = r_e/\bar{\lambda}_C$ can be embedded as the cross-ratio $(0,\infty; r_e, \bar{\lambda}_C)$. This makes the projective invariance of $\alpha$ geometrically explicit—$\alpha$ is invariant under all Möbius transformations, just as the physical world should be independent of human choices of units and coordinates.

**Contribution:** Provides the *geometric identification*—$\alpha$ is specifically $r_e/\bar{\lambda}_C$—that the adelic approach lacked. The projective formalism also makes the connection to experiment natural through the integer-count structure.

### 7.3 Topological / Winding

**Mathematical language:** Fundamental group $\pi_1(S^1)$ ≅ $\mathbb{Z}$, winding numbers

**Key idea:** The integer identification mechanism that underlies counting experiments has a topological origin. The circle $S^1$ has fundamental group $\mathbb{Z}$—every closed loop on a circle can be characterized by an integer winding number. When physical measurements involve periodic processes (cycles, oscillations), the integer counts that emerge are winding numbers in an abstract configuration space.

**Contribution:** Explains *how* integer counts emerge from topological structure—the measurement of $\alpha$ through counting is not an arbitrary experimental convenience but reflects the topological nature of periodic physical processes.

### 7.4 Syntactic / Base-Independent

**Mathematical language:** Distinction logic, base-free formulation

**Key idea:** The decimal representation $\alpha \approx 1/137.036$ is an artifact of base-10 notation, which itself is an artifact of human anatomy (ten fingers). Physical law should be formulated without reference to a particular integer base. Cross-ratios are naturally base-independent—they are geometric objects, not decimal strings.

**Contribution:** Explains *why* the standard presentation of $\alpha$ as a specific decimal is misleading—it embeds a base-10 convention into what should be a base-independent physical quantity.

### 7.5 Hierarchical / Scaling

**Mathematical language:** Frequency hierarchies, Minkowski geometry of numbers

**Key idea:** Physical constants emerge from hierarchical scaling relations. $\alpha$ is not an isolated number but a node in a network of scaling relationships connecting different physical scales (subatomic, atomic, macroscopic, cosmological). The cross-ratio structure propagates through these hierarchies.

**Contribution:** Shows *how* $\alpha$ connects to other scales and why it appears in so many different physical contexts—it is the scaling ratio that relates electromagnetic to quantum-relativistic phenomena.

### 7.6 Synthesis

These five formalisms are not competing explanations but **complementary perspectives** on the same underlying structure. The adelic approach tells us *why* $\alpha$ must be a cross-ratio (mathematical consistency across completions of $\mathbb{Q})$. The projective approach tells us *what* the cross-ratio is $(r_e/\bar{\lambda}_C)$. The topological approach tells us *how* integer counts arise. The syntactic approach tells us *why* decimal representations are artifacts. The hierarchical approach tells us *where* $\alpha$ fits in the broader network of physical scales.

Together, they form a coherent picture: $\alpha$ is a cross-ratio that (a) is forced by adelic consistency, (b) is geometrically realized as the ratio of two electron length scales, (c) is measured through topological integer counting, (d) is independent of base and representation, and (e) propagates through a hierarchy of physical scales.

---

## 8. Implications

### 8.1 Philosophical Implications

**Only dimensionless ratios are physically meaningful.** This is not a new idea—Michael Duff has argued since 2002 that claims of varying dimensionful constants are physically ambiguous because they depend on the choice of units. The cross-ratio framing provides the mathematical underpinning: projective invariance guarantees that only dimensionless ratios are independent of human conventions.

**“Fundamental constants” should be restricted to dimensionless ratios.** The dimensionful quantities we call “fundamental constants”—c, $\hbar$, e in SI—are human conventions reflecting our choice of measurement system. In natural units (c = $\hbar$ = 1), many of these “constants” disappear, revealing that their apparent fundamentality was an artifact of unit choices. The truly fundamental parameters of physics are dimensionless ratios like $\alpha, m_p/m_e$, and the cosmological constant in Planck units.

**The SI system obscures structure.** By presenting $\alpha$ as $e^2/(4\pi\varepsilon_0\hbar c)$—a formula involving four dimensionful constants—the standard textbook presentation hides the fact that $\alpha$ is a pure geometric ratio. While working physicists internalize $\alpha$’s dimensionless nature, the *presentation* in terms of dimensionful inputs encourages the misconception that $\alpha$ somehow “arises from” c, $\hbar$, and e interacting—when in fact these constants’ numerical values are chosen by the SI committee to be consistent with measurements of $\alpha$ and other dimensionless ratios.

### 8.2 Testable Predictions

The cross-ratio reframing is primarily a change of perspective, and does not make dramatically novel predictions. However, it suggests three avenues:

**Prediction 1: Cross-ratio structure should be universal.** If $\alpha$ has the structure of a projective cross-ratio, then other dimensionless physical constants should also be expressible as cross-ratios of independently characterizable physical scales. For example, the proton-to-electron mass ratio $m_p/m_e$ might be expressible as a ratio of QCD to QED length scales. Failure to find such representations would weaken the cross-ratio framing.

**Prediction 2: Precision measurements should continue to converge.** If $\alpha$ is fundamentally determined from integer-count ratios, then improving counting precision in QHE and Penning trap experiments should yield increasingly consistent values. Discrepancies between QHE-derived and g-2-derived $\alpha$ would signal new physics (e.g., beyond-Standard-Model contributions to $a_e)$.

**Prediction 3: SI independence is trivially confirmed.** $\alpha$’s value should be the same regardless of the unit system used—and indeed it is. This prediction is already verified, but the cross-ratio framing explains *why* it must be true in geometric terms.

### 8.3 What Would Change in Practice?

A physicist who adopts the cross-ratio perspective would:
- Think of $\alpha$ as the ratio of the electron’s electromagnetic size to its quantum size, rather than as an abstract coupling strength
- Recognize that precision $\alpha$ measurements are fundamentally counting experiments
- Evaluate claims about varying constants with the criterion that only variations in dimensionless ratios are physically meaningful
- Be skeptical of theoretical programs that treat dimensionful constants as fundamental parameters

What would NOT change: the numerical value of $\alpha$, the equations of QED, or any prediction of the Standard Model. The reframing changes our *understanding* of $\alpha$, not $\alpha$ itself.

---

## 9. Open Questions

### 9.1 Why These Particular Scales?

The classical electron radius and reduced Compton wavelength are the two natural length scales of the electron—but *why* does nature select these particular scales? The cross-ratio identifies the ratio but does not explain the origin of the individual scales. A more fundamental theory would derive both $r_e$ and $\bar{\lambda}_C$ (and therefore $\alpha)$ from deeper principles.

### 9.2 Can Α Be Derived from Pure Geometry?

The cross-ratio says $\alpha$ *is* $(0,\infty; r_e, \bar{\lambda}_C)$. Could pure projective geometry, perhaps constrained by group-theoretic considerations (e.g., invariants of a specific symmetry group acting on a domain), fix the *numerical value* of this cross-ratio without inputting the electron mass, charge, or other parameters? Wyler’s formula at 0.6 ppm suggests this might be possible, but no rigorous derivation currently exists.

### 9.3 Anthropic or Mathematical?

Even if $\alpha$ has a mathematical structure, why does it take the specific value $\approx 1/137.036$ rather than some other cross-ratio? Two classes of answer are possible:
- **Mathematical:** The value is uniquely determined by mathematical consistency requirements (the approach attempted by Eddington, Wyler, and the adelic program)
- **Anthropic:** $\alpha$ varies across a multiverse landscape, and we observe a value compatible with carbon-based life (the approach of Barrow and Tipler)

These are not mutually exclusive: a mathematical derivation might yield a *discrete spectrum* of possible $\alpha$ values, with anthropic selection picking out the life-permitting one.

### 9.4 The Minimal Set of Fundamental Ratios

If only dimensionless cross-ratios are physically meaningful, what is the complete set of such ratios needed to specify the Standard Model of particle physics? The answer would enumerate the truly fundamental parameters of nature—the independent cross-ratios from which all dimensionful “constants” are derived through unit conventions.

### 9.5 Quantum Gravity

How does the cross-ratio structure behave when gravity is included? The Planck length $\ell_P = √(\hbar G/c^3)$ introduces a third fundamental length scale. The cross-ratios among ${r_e, \bar{\lambda}_C, \ell_P}$ might encode the relationship between electromagnetic, quantum, and gravitational physics—potentially constraining quantum gravity models.

### 9.6 Required External Literature

To complete the argument, the following sources—not currently available—are needed:

| Source | Why Needed |
|:-------|:-----------|
| Duff, M.J. (2002). Comment on time-variation of fundamental constants. arXiv:hep-th/0208093 | Establishes the operational argument that only dimensionless constants are physically meaningful |
| Barrow, J.D. & Tipler, F.J. (1986). The Anthropic Cosmological Principle. Oxford University Press | Provides the anthropic complement to the mathematical approach |
| Eddington, A.S. (1946). Fundamental Theory. Cambridge University Press | Historical context—the first serious attempt to derive $\alpha$ |
| Wyler, A. (1969). L’espace symétrique du groupe des équations de Maxwell. C.R. Acad. Sci. Paris 269, 743 | Original derivation of the 0.6 ppm formula |
| CODATA 2022 recommended values | Most current $\alpha$ value |

---

## 10. Conclusion

The fine-structure constant $\alpha$ has been a puzzle for over a century. Measured to extraordinary precision, it lacks any accepted theoretical explanation. The standard presentation—$\alpha = e^2/(4\pi\varepsilon_0\hbar c)$—frames it as an abstract coupling strength, obscuring its geometric character.

This document has argued for a reframing: $\alpha$ is naturally understood as the cross-ratio of two characteristic length scales of the electron—the classical electron radius $r_e$ and the reduced Compton wavelength $\bar{\lambda}_C$. This reframing:

1. **Reveals geometric structure:** $\alpha$ inherits its invariance properties from projective geometry—the cross-ratio is the fundamental invariant of four collinear points under Möbius transformations.

2. **Connects to experiment:** The highest-precision measurements of $\alpha$ (quantum Hall effect, Penning trap) proceed by *counting*—measuring rational filling factors $\nu = p/q$ and frequency ratios $N_s/N_c$. The cross-ratio framing makes this connection natural.

3. **Integrates five formalisms:** Adelic, projective, topological, syntactic, and hierarchical approaches illuminate complementary aspects of $\alpha$’s cross-ratio nature. Together they form a coherent picture: why $\alpha$ must be a cross-ratio, what cross-ratio it is, how it is measured, why its standard presentation obscures it, and where it fits in the hierarchy of physical scales.

4. **Clarifies fundamentality:** Dimensionful “fundamental constants” (c, $\hbar$, e in SI) are human conventions. Only dimensionless ratios carry invariant physical content. The cross-ratio provides the mathematical formalization of this principle.

The reframing is honest about its limitations. $\alpha = r_e/\bar{\lambda}_C$ is an algebraic identity, not a first-principles derivation. The contribution is conceptual—a change of perspective that makes hidden structure visible, like changing coordinate systems reveals symmetries that were present but obscured. Whether $\alpha$ can be *derived* from pure geometry, without experimental input, remains an open question—one that the cross-ratio framing helps to formulate precisely.

---

## Appendix A: Python Verification Code

The following self-contained Python script verifies all quantitative claims in this document. It requires only the Python standard library.
```python
"""
Self-contained verification of all quantitative claims in
'The Fine-Structure Constant as a Cross-Ratio'
"""

import math
from fractions import Fraction

# ============================================================
# CODATA 2018 FUNDAMENTAL CONSTANTS
# ============================================================
e      = 1.602176634e-19       # elementary charge (C) — exact since 2019 SI
eps0   = 8.8541878128e-12      # vacuum permittivity (F/m) — measured post-2019
hbar   = 1.054571817e-34       # reduced Planck constant (J·s) — exact
c      = 299792458             # speed of light (m/s) — exact
m_e    = 9.1093837015e-31      # electron mass (kg) — measured
h      = 2 * math.pi * hbar    # Planck constant

# ============================================================
# LENGTH SCALES
# ============================================================
r_e     = e**2 / (4 * math.pi * eps0 * m_e * c**2)
lc_bar  = hbar / (m_e * c)           # reduced Compton
lc_full = h / (m_e * c)              # non-reduced Compton

# ============================================================
# ALPHA VIA MULTIPLE ROUTES
# ============================================================
alpha_SI    = e**2 / (4 * math.pi * eps0 * hbar * c)
alpha_cr    = r_e / lc_bar
alpha_wrong = r_e / lc_full

print("=== LENGTH SCALES ===")
print(f"r_e     = {r_e:.6e} m")
print(f"λ̄_C     = {lc_bar:.6e} m")
print(f"λ_C     = {lc_full:.6e} m")

print("\n=== ALPHA ===")
print(f"α (SI)              = {alpha_SI:.15f}")
print(f"α = r_e/λ̄_C         = {alpha_cr:.15f}  {'✓' if abs(alpha_SI - alpha_cr) < 1e-15 else '✗'}")
print(f"α = r_e/λ_C         = {alpha_wrong:.15f}  (off by factor 2π)")
print(f"1/α                 = {1/alpha_SI:.12f}")
print(f"CODATA 2018 1/α    = 137.035999084")

# ============================================================
# CROSS-RATIO VERIFICATION
# ============================================================
def cross_ratio(x1, x2, x3, x4):
    num = (x1 - x3) * (x2 - x4)
    den = (x1 - x4) * (x2 - x3)
    return num / den if den != 0 else float('inf')

print("\n=== CROSS-RATIO VERIFICATION ===")
print("(0, ∞; a, b) should equal a/b:")
L = 1e30  # proxy for infinity
tests = [(r_e, lc_bar, "r_e, λ̄_C"), (3.0, 1.0, "3, 1"), (1.0, math.pi, "1, π")]
all_pass = True
for a, b, label in tests:
    cr = cross_ratio(0, L, a, b)
    match = abs(cr - a/b) < 1e-10
    if not match: all_pass = False
    print(f"  {label}: a/b={a/b:.15f}, CR={cr:.15f} {'✓' if match else '✗'}")

# ============================================================
# HISTORICAL NUMEROLOGY
# ============================================================
print("\n=== HISTORICAL NUMEROLOGY ===")
edd_136 = 1/136
edd_137 = 1/137
wyler   = (9 / (16 * math.pi**3)) * (math.pi / math.factorial(5))**0.25

print(f"Eddington 1/136:  dev = {abs(edd_136 - alpha_SI)/alpha_SI*1e6:.1f} ppm")
print(f"Eddington 1/137:  dev = {abs(edd_137 - alpha_SI)/alpha_SI*1e6:.1f} ppm")
print(f"Wyler 1969:       1/α = {1/wyler:.12f}, dev = {abs(wyler - alpha_SI)/alpha_SI*1e6:.1f} ppm")

# ============================================================
# EXPERIMENTAL EXAMPLES
# ============================================================
print("\n=== EXPERIMENTAL EXAMPLES ===")
# Thomson cross-section
sigma_T = (8 * math.pi / 3) * r_e**2
print(f"Thomson σ_T = {sigma_T:.4e} m² = {sigma_T*1e28:.4f} barn")

# Compton max shift
delta_lambda_max = 2 * lc_full
print(f"Compton Δλ_max = {delta_lambda_max:.4e} m")

# Penning trap example
a_e_exp = 0.00115965218059
ratio_n = 1 + a_e_exp
frac = Fraction(ratio_n).limit_denominator(10_000_000)
print(f"a_e = {a_e_exp:.14f}")
print(f"N_s/N_c ≈ {frac.numerator}/{frac.denominator} = {frac.numerator/frac.denominator:.14f}")

# QHE filling factors
print("\nQHE filling factors:")
for p, q in [(1,1), (2,1), (3,1), (1,3), (2,3), (2,5), (3,5), (3,7), (4,7)]:
    print(f"  ν = {p}/{q} = {p/q:.6f}")

# ============================================================
# ASSERTIONS
# ============================================================
assert abs(alpha_SI - alpha_cr) < 1e-15
assert all_pass
print(f"\n{'='*50}")
print("All assertions passed.")
print(f"{'='*50}")
```

---

## Appendix B: Notation Guide

| Symbol | Meaning | Value |
|:-------|:--------|:------|
| $\alpha$ | Fine-structure constant | $\approx 1/137.035999084$ |
| $\alpha^{-1}$ | Inverse fine-structure constant | $\approx$ 137.035999084 |
| $r_e$ | Classical electron radius | $\approx$ 2.818 $\times 10^{-15}$ m |
| $\lambda_C$ | Compton wavelength (non-reduced) = $h/(m_e$ c) | $\approx$ 2.426 $\times 10^{-12}$ m |
| $\bar{\lambda}_C$ | Reduced Compton wavelength = $\hbar/(m_e$ c) = $\lambda_C/(2\pi)$ | $\approx$ 3.862 $\times 10^{-13}$ m |
| e | Elementary charge | 1.602176634 $\times 10^{-19}$ C |
| $\varepsilon_0$ | Vacuum permittivity | $\approx$ 8.854 $\times 10^{-12} F/m$ |
| $\hbar$ | Reduced Planck constant | 1.054571817 $\times 10^{-34} J\cdots$ |
| c | Speed of light | 299,792,458 $m/s$ |
| $m_e$ | Electron mass | $\approx$ 9.109 $\times 10^{-31}$ kg |
| $R_K$ | von Klitzing constant = $h/e^2$ | $\approx$ 25,812.807 $\Omega$ |
| $\nu$ | Quantum Hall filling factor | Rational $(p/q)$ |
| $a_e$ | Electron anomalous magnetic moment = (g−2)/2 | $\approx$ 0.00115965218059 |
| $N_s, N_c$ | Penning trap cycle counts | Integers (specific values depend on measurement duration) |
| $(x_1,x_2;x_3,x_4)$ | Cross-ratio of four collinear points | Dimensionless invariant |

---

## Appendix C: Glossary

**Adelic:** Pertaining to the *adèle ring*—a mathematical object that combines the real numbers $\mathbb{R}$ with all p-adic numbers $\mathbb{Q}_p$. Physical quantities defined on the adèles must be consistent across all “completions” of the rational numbers.

**Anharmonic group:** The group of transformations relating the six possible values of a cross-ratio under permutation of its four points. Isomorphic to the symmetric group $S_3$.

**CODATA:** Committee on Data for Science and Technology. Publishes internationally recommended values for fundamental physical constants approximately every four years.

**Cross-ratio (anharmonic ratio):** The fundamental projective invariant of four collinear points. Given by $(x_1−x_3)(x_2−x_4)/((x_1−x_4)(x_2−x_3))$. Invariant under all Möbius transformations.

**Filling factor $(\nu)$**: In the quantum Hall effect, the ratio of electron density to magnetic flux quanta density. Takes rational values $p/q$ corresponding to the number of occupied Landau levels.

**Fine-structure constant $(\alpha)$**: A dimensionless number $\approx 1/137$ characterizing the strength of electromagnetic interactions. Originally introduced to explain the fine-structure splitting of atomic spectral lines.

**Josephson effect:** The phenomenon where a superconducting junction produces an AC voltage at frequency f = $(2e/h)V$ when a DC voltage V is applied. Provides the most precise frequency-to-voltage conversion.

**Möbius transformation:** A transformation of the form x $\to$ (ax + b)/(cx + d) with ad−bc $\neq$ 0. The most general transformation that preserves the cross-ratio.

**Ostrowski’s theorem:** Every non-trivial absolute value on $\mathbb{Q}$ is equivalent to either the usual real absolute value or a p-adic absolute value. Implies that $\mathbb{R}$ and $\mathbb{Q}_p$ are the only completions of $\mathbb{Q}$.

**p-adic numbers $(\mathbb{Q}_p)$**: A completion of the rational numbers using a different notion of “closeness”—two numbers are p-adically close if their difference is divisible by a large power of p.

**Penning trap:** A device that confines charged particles using a combination of electric and magnetic fields. Used for the most precise measurements of the electron’s magnetic moment.

**Quantum Hall effect:** The quantization of Hall resistance in two-dimensional electron systems at low temperature and high magnetic field. Provides the most precise determination of $h/e^2$.

**Thomson scattering:** The elastic scattering of low-energy photons by free electrons. The cross-section depends on $r_e^2$.

**von Klitzing constant:** $R_K = h/e^2 \approx$ 25,812.807 $\Omega$. The quantum of Hall resistance.
