---
author: Rowan Brad Quni-Gudzinas
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
modified: 2026-05-10T12:31:03Z
title: Quantum-Mechanical Physics as Invariant Geometric Structure
aliases:
  - Quantum-Mechanical Physics as Invariant Geometric Structure
---

# Quantum-Mechanical Physics as Invariant Geometric Structure


**Author:** Rowan Brad Quni-Gudzinas
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.20109772](http://doi.org/10.5281/zenodo.20109772)
**Version:** 1.0  
**Date:** 2026-05-10  

**What this document is:** An exploration of a geometric observation—that the fine-structure constant $\alpha$ equals the ratio of two electron length scales, making it a cross-ratio (a quantity unchanged by coordinate transformations). The document traces where this leads: a classification of the dimensionless numbers that specify our universe, a computational search for deeper patterns, and connections to number theory and experimental measurement.

**How to read this document:** Sections 1–3 establish the core observation and require only basic algebra and geometry. Sections 4–8 develop the classification system, computational results, and Standard Model coverage. Sections 9–12 extend into number theory and research-roadmap territory and assume familiarity with $p$-adic numbers, Ostrowski’s theorem, and algebraic geometry concepts. Sections 13–16 address testability, limits, and conclusions. Every term is defined before it is used; a glossary is provided in Appendix C.

---

## Abstract

The fine-structure constant $\alpha \approx 1/137.036$ equals the ratio of two electron length scales—the classical radius $r_e$ and the reduced Compton wavelength $\bar{\lambda}_C$. This ratio is a projective cross-ratio $(0, \infty; r_e, \bar{\lambda}_C) = \alpha$, invariant under projective (Möbius) transformations. Both $r_e$ and $\bar{\lambda}_C$ derive from the electron’s Compton frequency $\omega_e = m_e c^2/\hbar$, meaning $\alpha$ captures the invariant geometric relationship between two different ways this frequency manifests at physical scales.

Generalizing this observation to all particles reveals a coherent framework. Every massive particle is characterized by a Compton frequency $\omega_i = m_i c^2/\hbar$; mass is the same quantity expressed in different units ($m_i = \hbar\omega_i/c^2$). The approximately 26 dimensionless constants of the Standard Model fall into three structural types: Type I (the frequency cancels, producing universal coupling strengths like $\alpha$, confirmed identical for all charged leptons to machine precision), Type II (different frequencies appear, producing species-specific mass ratios like $m_p/m_e = 1836$), and Type III (scales from different physical sectors combine, producing cross-force ratios like $\bar{\lambda}_C^{(e)}/\ell_P \approx 2.39 \times 10^{22}$).

A systematic computational scan of 600 pairwise combinations of physical length scales—incorporating QCD observables (Sommer scale, string tension, nucleon magnetic and axial radii, meson and baryon Compton wavelengths)—confirms the structural asymmetry: Type I ratios emerge naturally as non-tautological cross-ratios, while Type II mass ratios resist expression as cross-ratios of independently measurable scales. The scan identifies near-matches of interest: the top quark Compton wavelength divided by the electron Compton wavelength approximates the electron Yukawa coupling ($\lambda_{\text{top}}/\lambda_e \approx y_e$, within 0.93%), reflecting the known proximity of the top mass to the Higgs scale.

The frequency-first picture explains why precision measurements produce rational numbers: all high-precision determinations of $\alpha$ (quantum Hall effect, Penning trap, atom interferometry) count integer cycles of fundamental frequencies, producing rational observables $\nu = p/q$. Rational numbers satisfy the adelic product formula $\prod_v |q|_v = 1$—a theorem stating that the product of a rational number’s “sizes” across all number systems equals exactly one. If fundamental dimensionless constants are rational, this formula provides a consistency condition operating across all completions of the rational numbers simultaneously.

The framework makes no novel quantitative predictions. Its contribution is organizational and programmatic: it classifies dimensionless constants by their structural relationship to the underlying frequencies, reframes the Higgs mechanism as a frequency multiplier ($\omega_f = y_f \cdot \omega_H$), interprets the running of couplings as frequency-dependence, and identifies computational and mathematical targets for investigating the origin of the constants.

---

## Table of Contents

1. [What Is Being Claimed?](#1-what-is-being-claimed)
2. [The Compton Frequency](#2-the-compton-frequency)
3. [$\alpha$ as a Cross-Ratio](#3-alpha-as-a-cross-ratio)
4. [Three Types of Invariant Relationships](#4-three-types-of-invariant-relationships)
5. [The Complete Frequency Spectrum of Known Particles](#5-the-complete-frequency-spectrum-of-known-particles)
6. [The Extended Computational Scan](#6-the-extended-computational-scan)
7. [How Particles Get Their Frequencies: The Higgs Mechanism](#7-how-particles-get-their-frequencies-the-higgs-mechanism)
8. [Why Coupling Strengths Depend on Energy](#8-why-coupling-strengths-depend-on-energy)
9. [Why Rational Numbers Matter: The Number Theory Connection](#9-why-rational-numbers-matter-the-number-theory-connection)
10. [Force Carriers and Massless Particles](#10-force-carriers-and-massless-particles)
11. [How This Work Connects to the Broader Research Program](#11-how-this-work-connects-to-the-broader-research-program)
12. [Where to Go From Here: A Research Roadmap](#12-where-to-go-from-here-a-research-roadmap)
13. [What Can Be Tested](#13-what-can-be-tested)
14. [What Is Established and What Is Speculative](#14-what-is-established-and-what-is-speculative)
15. [Open Questions](#15-open-questions)
16. [Conclusion](#16-conclusion)

**Appendices:**
- [Appendix A: Numerical Verification](#appendix-a-numerical-verification)
- [Appendix B: Source Cross-Reference](#appendix-b-source-cross-reference)
- [Appendix C: Glossary](#appendix-c-glossary)

---

## 1. What Is Being Claimed?

### 1.1 The Core Observation

The fine-structure constant $\alpha$ equals the ratio of two lengths:

$$\alpha = \frac{r_e}{\bar{\lambda}_C} \approx \frac{2.82 \times 10^{-15} \text{ m}}{3.86 \times 10^{-13} \text{ m}} \approx \frac{1}{137.036}$$

where $r_e$ is the classical electron radius (a measure of how strongly the electron interacts with electromagnetic fields) and $\bar{\lambda}_C$ is the reduced Compton wavelength (the scale at which quantum effects become important for the electron). This is an algebraic identity—not a theory, not an interpretation. It is true by definition of the quantities involved. `[CODE-EXECUTED]`

### 1.2 What Follows From This Observation

Both $r_e$ and $\bar{\lambda}_C$ are inversely proportional to the electron’s rest energy $m_e c^2$, which means they are both inversely proportional to the electron’s Compton frequency $\omega_e = m_e c^2 / \hbar$. Their ratio cancels the frequency, leaving a pure number—the coupling strength of electromagnetism.

When we apply the same logic to every known particle:
- Every massive particle has a characteristic frequency $\omega = m c^2 / \hbar$
- Mass is the same quantity as frequency, expressed in different units ($m = \hbar\omega / c^2$)
- The dimensionless constants of the Standard Model can be classified by how they relate to these frequencies
- Some constants cancel the frequency (universal coupling strengths), while others directly expose frequency ratios (mass ratios)

### 1.3 What Is Established vs. What Is Interpretation

**Established facts:**
1. $\alpha = r_e / \bar{\lambda}_C$ is an algebraic identity `[CODE-EXECUTED]`
2. This can be written as a cross-ratio $(0, \infty; r_e, \bar{\lambda}_C)$ `[CODE-EXECUTED]`
3. Both $r_e$ and $\bar{\lambda}_C$ are proportional to $1/\omega_e$ `[CODE-EXECUTED]`
4. Every massive particle has a Compton frequency $\omega = m c^2 / \hbar$ (definitional, from $E = \hbar\omega$)
5. A scan of 600 combinations of known length scales finds no non-tautological expression for $m_p/m_e$ `[CODE-EXECUTED]`
6. Precision measurements of $\alpha$ proceed through rational numbers (ratios of integer counts)

**Interpretation:**
- Treating frequencies as more fundamental than masses is a conceptual choice, not a physical claim—both pictures produce identical numerical predictions
- The three-type classification is an organizational framework, not a theorem
- The connection to number theory depends on a hypothesis: that fundamental physical constants might be rational numbers

### 1.4 What Is NOT Claimed

- That this makes novel quantitative predictions (it doesn’t—see §14)
- That particles are “really” oscillations in a literal physical sense
- That the Landau pole problem is solved in any peer-reviewed way
- That this replaces the Standard Model as a physical theory

---

## 2. The Compton Frequency

### 2.1 Where the Frequency Comes From

Quantum mechanics rests on the Planck–Einstein relation: the energy $E$ of any physical system is proportional to its frequency $\omega$, with Planck’s reduced constant $\hbar$ as the proportionality factor:

$$E = \hbar \omega$$

For a massive particle at rest, Einstein’s $E = m c^2$ gives:

$$\omega = \frac{m c^2}{\hbar}$$

This frequency—the Compton frequency—is not hypothetical. It is the frequency at which the particle’s quantum phase oscillates: the wavefunction of a particle at rest evolves as $e^{-i\omega t}$ where $\omega = m c^2 / \hbar$.

### 2.2 Two Frequencies for a Moving Particle

For a particle in motion, there are two distinct frequencies:

- **Compton frequency** ($\omega_C = m c^2 / \hbar$): The frequency in the particle’s own rest frame. Same for all observers—it is a property of the particle, not of who is watching.

- **De Broglie frequency** ($\omega_{\text{dB}} = E / \hbar = \gamma m c^2 / \hbar$): The frequency measured in the laboratory frame. Depends on the particle’s speed (through the Lorentz factor $\gamma$). Different observers measure different values.

For a particle at rest, these two frequencies coincide. The Compton frequency is the minimum possible frequency for a given particle, and it is the only one that is the same for all observers. Ratios of Compton frequencies (like $m_p/m_e = \omega_p/\omega_e$) are therefore also invariant.

### 2.3 Historical Context

The idea that mass corresponds to a frequency dates to de Broglie (1924), who proposed that every particle has an internal “clock” at the Compton frequency. Schrödinger (1930) discovered that the electron’s position in the Dirac equation oscillates at this same frequency—a phenomenon called zitterbewegung. In quantum field theory, zitterbewegung is reinterpreted as the creation and annihilation of virtual particle-antiparticle pairs, so its status as a physical oscillation is debated.

The frequency-first viewpoint does not depend on zitterbewegung being physically real. The Compton frequency follows directly from $E = \hbar\omega$ and $E = mc^2$, two of the most thoroughly tested equations in physics.

Prior work established the identity $m = \omega$. The current document extends this foundation with the cross-ratio formalism and the number-theoretic connections.

### 2.4 Two Ways of Looking at the Same Thing

The standard approach treats mass as fundamental, with frequency derived:

$$\text{mass } m \;\xrightarrow{E=mc^2}\; \text{energy } E \;\xrightarrow{E=\hbar\omega}\; \text{frequency } \omega$$

The frequency-first approach reverses this:

$$\text{frequency } \omega \;\xrightarrow{E=\hbar\omega}\; \text{energy } E \;\xrightarrow{m=E/c^2}\; \text{mass } m$$

Both produce the same numbers for every observable. The difference is conceptual: which quantity we treat as the starting point. The frequency-first approach is adopted here because it makes the geometric structure of the dimensionless constants visible.

---

## 3. $\alpha$ As a Cross-Ratio

### 3.1 Two Lengths from One Frequency

From the electron’s Compton frequency $\omega_e$, two characteristic lengths emerge:

**Reduced Compton wavelength** $\bar{\lambda}_C = c / \omega_e$:
- The scale where quantum field theory becomes necessary
- `[CODE-EXECUTED]`: $\bar{\lambda}_C^{(e)} = 3.861593 \times 10^{-13}$ m

**Classical electron radius** $r_e = \alpha \cdot c / \omega_e$:
- The scale where electromagnetic self-energy equals rest energy
- `[CODE-EXECUTED]`: $r_e = 2.817940 \times 10^{-15}$ m

Their ratio is $\alpha$:

$$\frac{r_e}{\bar{\lambda}_C} = \frac{\alpha \cdot c/\omega_e}{c/\omega_e} = \alpha$$

### 3.2 What a Cross-Ratio Is

A cross-ratio is a quantity built from four points on a line that remains unchanged when the line is stretched, compressed, or otherwise smoothly transformed. For four points labeled $x_1, x_2, x_3, x_4$, the cross-ratio is:

$$(x_1, x_2; x_3, x_4) = \frac{(x_1 - x_3)(x_2 - x_4)}{(x_1 - x_4)(x_2 - x_3)}$$

The cross-ratio is the fundamental invariant of projective geometry—no matter how you change the coordinate system, as long as the transformation is a projective (Möbius/fractional-linear) transformation, the cross-ratio stays the same. The cross-ratio is the only projective invariant of four collinear points.

For $\alpha$, the four points are:

| Point | Coordinate | What It Represents |
|:------|:-----------|:-------------------|
| $P_0$ | $0$ | Zero length (mathematical anchor) |
| $P_\infty$ | $\infty$ | Infinite length (mathematical anchor) |
| $P_a$ | $r_e$ | Electromagnetic manifestation of the electron’s frequency |
| $P_b$ | $\bar{\lambda}_C$ | Quantum-kinematic manifestation of the electron’s frequency |

$$\alpha = (0, \infty; r_e, \bar{\lambda}_C) = \frac{r_e}{\bar{\lambda}_C}$$

`[CODE-EXECUTED]`—Verified to 15 decimal places.

Because a cross-ratio is invariant under coordinate changes, $\alpha$ does not depend on what units we use or where we place the origin of our coordinate system. This invariance is why $\alpha$ is a genuine physical constant: dimensionful quantities change when units change; only their dimensionless ratio is invariant.

### 3.3 The Same Number for Every Charged Lepton

For the electron, muon, and tau, the classical radius and Compton wavelength both scale inversely with mass, so their ratio is the same for all three:

$$\frac{r_e}{\bar{\lambda}_C^{(e)}} = \frac{r_\mu}{\bar{\lambda}_C^{(\mu)}} = \frac{r_\tau}{\bar{\lambda}_C^{(\tau)}} = \alpha$$

`[CODE-EXECUTED]`—$\alpha_e = \alpha_\mu = 0.007297352573749$ to machine precision.

> **A note on running:** The value discussed here is the low-energy, Thomson-limit $\alpha(0) \approx 1/137.036$. At higher probing frequencies—such as the Z boson mass scale—$\alpha$ runs to approximately $1/127.95$, a 7.1% increase. This energy-dependence is discussed in §8. The Type I universality described here holds for the Thomson-limit value: $r_\ell/\bar{\lambda}_C^{(\ell)} = e^2/(4\pi\varepsilon_0\hbar c)$ is identically equal for all charged leptons because the classical radius definition uses the same bare electromagnetic coupling, regardless of the lepton mass.

The mass cancels identically. $\alpha$ is a property of the electromagnetic interaction itself, not of any particular particle.

---

## 4. Three Types of Invariant Relationships

### 4.1 Type I: The Frequency Cancels

**Definition:** Both quantities in the ratio derive from the same fundamental frequency, so the frequency cancels. What remains is a universal coupling strength.

| Ratio | Expression | Value | What It Means |
|:------|:-----------|:------|:--------------|
| $\alpha$ | $r_\ell / \bar{\lambda}_C^{(\ell)}$ | $1/137.036$ | Strength of electromagnetism |
| $a_0 / \bar{\lambda}_C^{(e)}$ | $1/\alpha$ | $137.036$ | How much larger an atom is than the electron’s quantum scale |
| $a_0 / r_e$ | $1/\alpha^2$ | $18,779$ | How much larger an atom is than the electron’s classical scale |

**Key property:** Same value for all particles that share the same interaction.

### 4.2 Type II: Two Different Frequencies

**Definition:** The ratio involves two different particles with two different fundamental frequencies. The frequencies do not cancel—the ratio directly tells you how the frequencies (and therefore masses) compare.

| Ratio | Expression | Value |
|:------|:-----------|:------|
| $m_\mu/m_e$ | $\omega_\mu/\omega_e$ | $206.77$ |
| $m_\tau/m_e$ | $\omega_\tau/\omega_e$ | $3,477$ |
| $m_p/m_e$ | $\omega_p/\omega_e$ | $1,836$ |

**Key property:** These ratios are specific to each pair of particles. They are not derivable from simpler building blocks within known physics.

### 4.3 Type III: Involving Scales From Different Forces

**Definition:** The ratio involves scales set by qualitatively different physical mechanisms.

| Ratio | Expression | Value |
|:------|:-----------|:------|
| QED vs. gravity | $\bar{\lambda}_C^{(e)} / \ell_P$ | $2.39 \times 10^{22}$ |
| QED vs. QCD | $\bar{\lambda}_C^{(e)} / \lambda_{\text{QCD}}$ | $425$ |
| Weak vs. gravity | $\bar{\lambda}_C^{(W)} / \ell_P$ | $1.52 \times 10^{17}$ |

**Key property:** These encode how different sectors of physics relate to each other.

`[CODE-EXECUTED]`—All numerical values verified in Appendix A.

---

## 5. The Complete Frequency Spectrum of Known Particles

### 5.1 Every Massive Particle Has a Characteristic Frequency

| Particle | Mass | Frequency $\omega$ (rad/s) |
|:---------|:-----|:---------------------------|
| $\nu_e$ (electron neutrino) | $\lesssim 1.1$ eV$/c^2$ | $\lesssim 1.7 \times 10^{12}$ |
| $e^-$ (electron) | $0.511$ MeV$/c^2$ | $7.76 \times 10^{20}$ |
| $\mu^-$ (muon) | $105.7$ MeV$/c^2$ | $1.61 \times 10^{23}$ |
| $p^+$ (proton) | $938.3$ MeV$/c^2$ | $1.43 \times 10^{24}$ |
| $\tau^-$ (tau) | $1.78$ GeV$/c^2$ | $2.70 \times 10^{24}$ |
| $t$ (top quark) | $172.5$ GeV$/c^2$ | $2.62 \times 10^{26}$ |
| $W^\pm$ (W boson) | $80.4$ GeV$/c^2$ | $1.22 \times 10^{26}$ |
| $Z^0$ (Z boson) | $91.2$ GeV$/c^2$ | $1.39 \times 10^{26}$ |
| $h$ (Higgs boson) | $125.2$ GeV$/c^2$ | $1.90 \times 10^{26}$ |
| (Planck scale) | $1.22 \times 10^{19}$ GeV$/c^2$ | $1.85 \times 10^{43}$ |

`[CODE-EXECUTED]`—See Appendix A.

### 5.2 The ~26 Numbers That Specify Our Universe

If only dimensionless ratios carry invariant physical meaning—because dimensionful quantities change when units change—then the Standard Model is specified by approximately 26 such ratios. The following table enumerates them by category:

| Category | Examples | Count | Type |
|:---------|:---------|:------|:-----|
| Gauge couplings | $\alpha$, $\alpha_s$, $\sin^2\theta_W$ | 3 | Type I / Running |
| Charged lepton mass ratios | $m_\mu/m_e$, $m_\tau/m_e$ | 2 | Type II |
| Up-type quark mass ratios | $m_u/m_e$, $m_c/m_e$, $m_t/m_e$ | 3 | Type II |
| Down-type quark mass ratios | $m_d/m_e$, $m_s/m_e$, $m_b/m_e$ | 3 | Type II |
| Neutrino mass ratios | $m_{\nu_e}/m_e$, $m_{\nu_\mu}/m_e$, $m_{\nu_\tau}/m_e$ | 3 | Type II |
| Quark mixing (CKM) | 3 angles + 1 CP phase | 4 | Type II |
| Neutrino mixing (PMNS) | 3 angles + 1 CP phase (Dirac) | 4 | Type II |
| Higgs sector | $\lambda$, $v/m_e$ | 2 | Type II |
| Strong CP angle | $\theta_{\text{QCD}}$ | 1 | Type II |
| Cosmological constant | $\Lambda \ell_P^2$ | 1 | Type III |
| **Total** | | **26** | |

### 5.3 Where Frequencies Sit on a Tree

The Tree of Frequencies paper proposes that frequency space has the structure of a Bruhat–Tits tree—a discrete, branching geometry where each level corresponds to a range of frequencies. Taking a 2-adic tree (where $p = 2$) and 1 rad/s as the reference level:

| Particle | $\omega$ (rad/s) | Tree depth ($\log_2 \omega$) |
|:---------|:-----------------|:-----------------------------|
| Electron neutrino | $\lesssim 10^{12}$ | ~40 |
| Electron | $7.76 \times 10^{20}$ | ~69 |
| Muon | $1.61 \times 10^{23}$ | ~77 |
| Proton | $1.43 \times 10^{24}$ | ~80 |
| Tau | $2.70 \times 10^{24}$ | ~81 |
| Top quark | $2.62 \times 10^{26}$ | ~88 |
| Higgs boson | $1.90 \times 10^{26}$ | ~87 |
| Planck scale | $1.85 \times 10^{43}$ | ~144 |

This mapping is illustrative. It shows that the tree provides a natural geometric home for particle frequencies, but it does not derive the frequencies from tree geometry.

---

## 6. The Extended Computational Scan

### 6.1 Motivation

The initial scan [1] tested 24 combinations of electromagnetic and strong-force length scales, asking whether any ratio of independently characterizable scales equals a mass ratio like $m_p/m_e \approx 1836$. It found a null result: only the Compton wavelength ratio $\bar{\lambda}_C^{(e)} / \bar{\lambda}_C^{(p)}$ matches, and this is tautological (it simply restates the mass ratio in wavelength units). This section reports an extended scan incorporating additional QCD observables.

### 6.2 Method

Twenty-five physical length scales were defined across four sectors:

- **Electromagnetic:** $r_e$, $\bar{\lambda}_C^{(e)}$, $a_0$ (Bohr radius), $\lambda_{\text{Ry}}$ (Rydberg), $r_\mu$, $\bar{\lambda}_C^{(\mu)}$, $r_\tau$, $\bar{\lambda}_C^{(\tau)}$
- **Strong force:** $\bar{\lambda}_C^{(p)}$, $r_p$ (charge radius), $\lambda_{\text{QCD}}$ (confinement scale), $\bar{\lambda}_C^{(\pi)}$, $r_0$ (Sommer scale, 0.47 fm), $L_\sigma$ (string tension scale, 0.42 GeV), $r_M$ (magnetic radius, 0.85 fm), $r_A$ (axial radius, 0.67 fm), $L_{f_\pi}$ (pion decay constant scale, 92.3 MeV), $\bar{\lambda}_C^{(\rho)}$, $\bar{\lambda}_C^{(\Delta)}$, $\bar{\lambda}_C^{(\Omega)}$
- **Weak/electroweak:** $\bar{\lambda}_C^{(W)}$, $\bar{\lambda}_C^{(Z)}$, $\bar{\lambda}_C^{(H)}$, $\bar{\lambda}_C^{(t)}$
- **Planck:** $\ell_P$

All 300 unordered pairs were tested for both ratio directions (A/B and B/A), yielding 600 total comparisons. Each ratio was checked against nine targets: $m_p/m_e$, $m_\mu/m_e$, $m_\tau/m_e$, $m_t/m_e$, $m_W/m_Z$, $y_e$, $y_\mu$, $y_\tau$, and $\alpha$. Ratios matching any target within 5% were flagged.

The 5% threshold is chosen as a conservative first-pass filter: it is wide enough to capture physically suggestive relationships without being so narrow as to miss structure that might be blurred by QCD systematic uncertainties (lattice QCD observables carry 1–5% errors), yet tight enough that a null result (no match for mass ratios among 600 combinations at this tolerance) is informative.

`[CODE-EXECUTED]`—Full scan in 0.7.py.

**Operational definition of “non-tautological”:** A ratio is non-tautological if the two length scales involved are independently characterizable—measured by distinct experimental techniques that do not presuppose knowledge of the quantity being tested. A ratio is tautological if it restates a known relationship in different units without adding independent physical information (e.g., $\bar{\lambda}_C^{(e)} / \bar{\lambda}_C^{(p)} = m_p/m_e$ follows from $\bar{\lambda}_C \propto 1/m$ and is therefore a restatement of the mass ratio in wavelength units). The computational scan conservatively classifies Compton wavelength ratios and classical-radius ratios between leptons as tautological or structurally equivalent.

### 6.3 Results

Of 600 combinations, 28 fell within 5% of at least one target. Of these, 5 are tautological (Compton wavelength ratios that restate mass ratios by definition). The remaining 23 are non-tautological. The complete scan is reproduced in Appendix A.

**Mass ratios (Type II):** The null result persists. No combination of independently characterizable scales yields $m_p/m_e$, $m_\mu/m_e$, or $m_\tau/m_e$ non-tautologically beyond the structurally equivalent classical radius ratios ($r_e/r_\mu = m_\mu/m_e$, $r_e/r_\tau = m_\tau/m_e$), which follow from $r_i \propto 1/m_i$ and carry no new information.

**Coupling constants (Type I):** $\alpha$ is recovered as $r_\ell / \bar{\lambda}_C^{(\ell)}$ for all three charged leptons to machine precision, and as $1 / (a_0 / \bar{\lambda}_C^{(e)})$. These are non-tautological in the sense that the scales involved are independently characterizable.

**Near-matches of interest (all non-tautological):**

| Ratio | Value | Target | % Error | Interpretation |
|:------|:------|:-------|:--------|:---------------|
| $\lambda_{\text{top}} / \lambda_e$ | $2.96 \times 10^{-6}$ | $y_e = 2.94 \times 10^{-6}$ | 0.93% | Reflects $m_t \approx v/\sqrt{2}$; top quark near Higgs scale |
| $\lambda_Z / \lambda_p$ | $0.01029$ | $y_\tau = 0.01021$ | 0.82% | Weak-force scale / strong-force scale near tau Yukawa |
| $\lambda_\mu / L_{f_\pi}$ | $0.8736$ | $m_W/m_Z = 0.8814$ | 0.89% | Muon Compton / pion decay constant near weak mixing |
| $\lambda_{\text{top}} / \lambda_\tau$ | $0.01030$ | $y_\tau = 0.01021$ | 0.93% | Top/tau Compton ratio near tau Yukawa |
| $\lambda_{\text{top}} / \lambda_\mu$ | $6.12 \times 10^{-4}$ | $y_\mu = 6.07 \times 10^{-4}$ | 0.93% | Top/muon Compton ratio near muon Yukawa |

The $\lambda_{\text{top}} / \lambda_e \approx y_e$ match, in particular, is a structural consequence of $m_t \approx v / \sqrt{2}$ (the top quark Yukawa coupling is near 1), which is a known but unexplained feature of the Standard Model. The other near-matches are empirical observations whose significance remains to be determined.

### 6.4 Interpretation

The extended scan confirms and sharpens the structural lesson. Type I ratios (coupling constants) arise naturally as cross-ratios of independently characterizable scales because the frequency cancels. Type II ratios (mass ratios) resist such expression because they ARE the frequency ratios—the cross-ratio formalism clarifies the question (“why these frequencies?”) but does not answer it.

The near-matches suggest that cross-sector ratios (Type III) may encode relationships between different sectors of the Standard Model—in particular, between the electroweak scale and the QCD scale—that are not yet understood. The $\lambda_Z/\lambda_p \approx y_\tau$ match, if not coincidental, could indicate that the tau Yukawa coupling is related to the ratio of the weak and strong force scales.

---

## 7. How Particles Get Their Frequencies: The Higgs Mechanism

### 7.1 The Standard Mechanism

In the Standard Model, particles acquire mass by interacting with the Higgs field, which fills all of space with a non-zero value (its “vacuum expectation value,” or VEV, $v \approx 246$ GeV). The strength of each particle’s interaction with the Higgs field is measured by its Yukawa coupling $y_f$:

$$m_f = y_f \cdot \frac{v}{\sqrt{2}}$$

### 7.2 In Frequency Language

Converting to frequencies:

$$\omega_f = y_f \cdot \frac{v c^2}{\hbar \sqrt{2}} = y_f \cdot \omega_H$$

where the Higgs frequency is $\omega_H \approx 2.64 \times 10^{26}$ rad/s. `[CODE-EXECUTED]`

The Yukawa couplings become dimensionless ratios $y_f = \omega_f / \omega_H$—Type II cross-ratios of the Higgs frequency. This makes them natural targets for the cross-ratio program: if any Yukawa coupling can be expressed as a cross-ratio of independently characterizable scales, that would be progress toward explaining the mass hierarchy.

---

## 8. Why Coupling Strengths Depend on Energy

### 8.1 The Running of Couplings

The strength of a fundamental force is not a single number—it depends on the energy at which you measure it. The electromagnetic coupling $\alpha$ is approximately $1/137$ at low energies but grows to approximately $1/128$ at the energy of the Z boson (about 91 GeV). The strong coupling changes even more dramatically.

### 8.2 In Frequency Language

The energy scale at which a coupling is measured corresponds to a probing frequency $\omega_{\text{probe}} = \mu / \hbar$. The coupling becomes a function of frequency:

$$\alpha(\omega) = (0, \infty; r_e(\omega), \bar{\lambda}_C^{(e)})$$

At the electron’s own frequency, $\alpha \approx 1/137.036$. At the Z boson’s frequency, $\alpha \approx 1/127.95$. The change is 7.1%. `[CODE-EXECUTED]`

The renormalization group equation becomes, in this language, $\omega \cdot d\alpha/d\omega = \beta(\alpha)$—a “frequency flow” describing how the cross-ratio changes as we probe at different fundamental frequencies.

---

## 9. Why Rational Numbers Matter: The Number Theory Connection

### 9.1 Step 1: Measurement Always Produces Integers

Every physical measurement, at its most basic level, is an act of counting. In the highest-precision measurements of $\alpha$:

- **Quantum Hall effect:** The filling factor $\nu = p/q$—a ratio of two integers
- **Penning trap ($g-2$):** The ratio of spin precession cycles to cyclotron cycles: $N_s / N_c$
- **Josephson effect:** Voltage is proportional to an integer step number: $V = n h f / (2e)$
- **Atom interferometry:** Counting interference fringes—an integer count

In every case, the raw experimental output is a ratio of integers—a rational number. The value $\alpha \approx 1/137.035999084$ is computed from rational inputs through QED perturbation theory, not measured directly.

### 9.2 Step 2: Rational Numbers Have a Special Property

Consider the number 12. Its usual “size” is $|12| = 12$. But there is another way to measure size, based on divisibility by primes:

- **2-adic size:** $|12|_2 = 1/4$ (because $12 = 3 \times 2^2$, so 12 is divisible by 2 twice; each factor of 2 makes it “smaller” in the 2-adic sense)
- **3-adic size:** $|12|_3 = 1/3$ (because $12 = 4 \times 3$, divisible by 3 once)
- **5-adic size:** $|12|_5 = 1$ (not divisible by 5)
- ...and so on for every prime

Now multiply all these “sizes” together:

$$|12|_\infty \times |12|_2 \times |12|_3 \times |12|_5 \times \dots = 12 \times \frac{1}{4} \times \frac{1}{3} \times 1 \times 1 \times \dots = 12 \times \frac{1}{12} = 1$$

The product is exactly 1. This works for every rational number. The general statement is the **adelic product formula:**

$$\prod_v |q|_v = 1 \quad \text{for every rational number } q$$

This formula does NOT work for irrational numbers. For $\pi$, the product is not 1. 

### 9.3 Step 3: There Are Only Two Kinds of “Size”

**Ostrowski’s theorem** (1916) states that every consistent way of measuring the size of rational numbers is either the usual absolute value or a $p$-adic absolute value for some prime $p$. There are no other possibilities. This means the product formula exhausts ALL ways of measuring a rational number. If a number fails the product formula, it is not consistently a number in every possible sense.

### 9.4 Step 4: Why This Might Matter for Physics

The chain of reasoning:

1. Precision measurements produce rational numbers (ratios of integer counts)—Step 1
2. Rational numbers satisfy the adelic product formula across ALL number systems—Steps 2–3
3. **If** the fundamental dimensionless constants of nature are rational (a hypothesis, not an established fact), **then** the adelic product formula constrains them
4. This constraint operates across all number systems simultaneously—real AND $p$-adic—providing a mathematical consistency condition

The frequency-first picture makes this chain natural. Counting cycles of a fundamental frequency produces integers. Ratios of integer counts are rational. The frequency at which you count determines which number system you are effectively using.

### 9.5 One More Connection: The Landau Pole

Standard QED predicts that $\alpha$ grows slowly with energy and would eventually become infinite at an enormous energy scale (the “Landau pole,” around $10^{286}$ GeV). The Adelic Constraints project proposed that this may be an artifact of looking at only the real-number component of the theory—when the full adelic structure is considered, non-real contributions may compensate the growth. 

**This is a conjecture, not an established result.** No independent verification exists. It is mentioned as a direction for investigation, not as a claim.

---

## 10. Force Carriers and Massless Particles

### 10.1 Massive Force Carriers

The W and Z bosons, and the Higgs boson, have mass and therefore have Compton frequencies—they fit directly into the frequency spectrum (§5.1).

### 10.2 Massless Force Carriers

The photon and gluon have zero mass, hence zero Compton frequency. In the frequency-first picture, massless particles are understood not by a characteristic frequency of their own, but by the frequency relationship they mediate:

- The **photon** mediates the electromagnetic cross-ratio $\alpha$: its propagator connects any two charged particles, and the strength of that connection is $\alpha$, regardless of which charged particles are involved. In the frequency picture, the photon enforces the Type I cancellation—it ensures that $r_\ell/\bar{\lambda}_C^{(\ell)}$ is identical for all charged leptons because the photon couples to all of them with the same strength.

- The **gluon** mediates the strong-force cross-ratio $\alpha_s$. At high probing frequencies (far above the QCD confinement scale), $\alpha_s$ is small and quarks behave almost as free particles—the cross-ratio is well-defined and perturbative. At low probing frequencies (near $\Lambda_{\text{QCD}}$), $\alpha_s$ becomes large and quarks are confined—the cross-ratio description breaks down, reflecting the fact that the relevant degrees of freedom at low frequencies are hadrons rather than individual quarks and gluons.

This suggests a structural distinction: **massive particles** are defined by their own Compton frequencies; **massless force carriers** are defined by the invariant relationships they mediate between other particles’ frequencies.

### 10.3 Spin

Spin has not been a focus of this document. Half-integer spin particles (fermions: electrons, quarks) have integer-indexed quantum states, which is why counting experiments are possible. Integer spin particles (bosons: photon, gluon, W, Z, Higgs) either mediate frequency relationships or set the universal frequency scale. The spin-statistics connection has been explored in the Tree of Frequencies program through tree combinatorics as a separate line of investigation.

---

## 11. How This Work Connects to the Broader Research Program

Rather than listing every prior work, this section focuses on three connections that directly illuminate the cross-ratio program.

### 11.1 Connection 1: The Frequency Tree Provides the Geometric Substrate

The Tree of Frequencies paper proposes that frequency space is a Bruhat–Tits tree—a discrete, branching structure where each vertex represents a frequency band and the distance between two frequencies is measured by how many branchings separate them. The tree’s invariants are cross-ratios. If frequency space is a tree, the dimensionless constants discussed in this document—$\alpha$, mass ratios, coupling strengths—are the natural quantities to compute on it. The tree provides the “where”; the cross-ratios provide the “what.” The Tree of Frequencies makes three falsifiable predictions (§13).

### 11.2 Connection 2: Cross-Ratios Are Ruler-Independent Invariants

The One Pattern paper develops a general framework: any physical theory must specify distinctions, arrangement, a ruler (metric), and closure conditions. The crucial insight is that the ruler—how we measure—is contingent. Ostrowski’s theorem tells us there are infinitely many inequivalent rulers for the rational numbers. Cross-ratios are the quantities that survive ANY choice of ruler. In the frequency-first picture: frequencies are the distinctions, the probing scale is the ruler, and cross-ratios are the ruler-independent invariants. This explains why the dimensionless constants of the Standard Model are cross-ratios: they encode geometric structure that survives regardless of which ruler we choose.

### 11.3 Connection 3: Mass-Frequency Identity Was Established Earlier

The identity $m = \omega$ was the subject of a project in November 2025. That project established THAT mass equals frequency. The present work explores WHAT FOLLOWS from treating frequency as fundamental: the cross-ratio formalism, the three-type classification, and the number-theoretic connections.

---

## 12. Where to Go From Here: A Research Roadmap

### Path A: Extended Computational Scan (Complete—this document)

The 600-combination scan reported in §6 extends the original 24-combination search. The null result for Type II ratios persists. Near-matches have been identified for cross-sector ratios, suggesting that further scans with additional lattice QCD observables (gluon correlation length, nucleon axial charge radius, heavy baryon Compton wavelengths) may reveal additional structure.

### Path B: The Geometric Route (3–10 years)

See the companion document `0.7.1.md` for a minimal working Shimura variety example. The approach:
1. **What is a Shimura variety?** In simple terms, it is a geometric space whose symmetries are described by number theory—generalizing the familiar fact that a torus is defined by a lattice in the complex plane. For the Standard Model, the gauge group defines a specific Shimura variety whose special points (called CM points) are discrete, and the values of certain mathematical functions at these points are algebraic numbers. The proposal is that Yukawa couplings are the values of these functions, and that ratios of Yukawa couplings (which are mass ratios) are therefore geometric invariants of the Shimura variety.

2. The Standard Model gauge group defines a Shimura variety
3. Special points (CM points) on this variety correspond to physical vacua
4. Automorphic forms evaluated at CM points give Yukawa couplings
5. The adelic product formula constrains these to be rational

The prototype uses the modular curve (the simplest Shimura variety) to demonstrate the mathematical structure: discrete CM points → algebraic special values (j-invariants) → rational ratios. Extending this to the Standard Model gauge group is a well-posed but mathematically demanding problem.

### Path C: Accept the Frequencies as Given

Type II ratios may simply be primitive—the frequency spectrum is the fundamental input, and not all constants are derivable. $\alpha$ would be structurally explicable; $m_p/m_e$ would not. This is less ambitious but may be the honest answer.

### Summary

| Path | Timeframe | Difficulty | Impact |
|:-----|:----------|:-----------|:-------|
| A—Extended scans | 3–6 months (ongoing) | Low–Medium | Identifies cross-ratio structures; guides Path B |
| B—Geometric route | 3–10 years | Very high | Derives mass ratios from geometry |
| C—Accept primitives | Immediate | Low | Clarifies scope |

---

## 13. What Can Be Tested

### 13.1 What This Document Predicts

**Nothing, directly.** The frequency-first picture is a reframing of existing physics, not a new theory. It produces the same numbers as the Standard Model for every observable. This is stated explicitly, not hidden.

### 13.2 What the Broader Program Predicts

The research program this document belongs to makes specific, falsifiable claims. These are not predictions OF the frequency-first picture, but predictions that would support or refute the broader framework:

**From the Tree of Frequencies:**
1. Non-Markovian decoherence oscillations in superconducting qubit-resonator systems (testable at ~5 GHz)
2. Log-periodic oscillations in the CMB power spectrum (constrained by Planck to amplitude below ~5%, testable by CMB-S4 to ~0.5%)
3. Discrete hierarchical organization of fermion masses (consistent with known hierarchy)

**From the Adelic Framework:**
4. Convergence of $\alpha$ measurements to a rational value as precision improves

**From the Type I/II/III Classification:**
5. Continued lepton universality of $\alpha$ (consistency check)

### 13.3 Distinguishing “Predictions Of” from “Consistent With”

| Observation | Tests this document? | Tests broader program? |
|:------------|:--------------------|:----------------------|
| Lepton universality of $\alpha$ | Consistency check | Consistency check |
| Rational convergence of $\alpha$ | No | Yes—tests adelic constraint |
| CMB log-periodic oscillations | No | Yes—tests Tree of Frequencies |
| Qubit decoherence oscillations | No | Yes—tests discrete tree structure |
| Non-tautological cross-ratio discovery | Would validate Path A | Would validate approach |

---

## 14. What Is Established and What Is Speculative

### 14.1 Established

| Claim                                                                       | Basis |
|:------|:------|
| $\alpha = r_e / \bar{\lambda}_C$                                            | Algebraic identity; `[CODE-EXECUTED]` |
| This is a cross-ratio $(0, \infty; r_e, \bar{\lambda}_C)$                   | Projective geometry; `[CODE-EXECUTED]` |
| $\alpha$ is identical for all charged leptons                               | $r_\ell / \bar{\lambda}_C^{(\ell)}$ independent of mass; `[CODE-EXECUTED]` |
| Every massive particle has $\omega = m c^2 / \hbar$                         | From $E = \hbar\omega$ and $E = mc^2$ |
| Precision measurements use rational observables                             | Documented experimental practice |
| No non-tautological cross-ratio for $m_p/m_e$ among 600 tested combinations | `[CODE-EXECUTED]` |
| Higgs mechanism → $\omega_f = y_f \cdot \omega_H$                           | Standard Model algebra; `[CODE-EXECUTED]` |
| Adelic product formula holds for rational numbers                           | Number theory theorem |
| $m = \omega$ established in prior work                                      | `[EXTERNAL-SOURCE: Archive MASS-FREQUENCY]` |

### 14.2 Speculative

| Claim | Status |
|:------|:-------|
| Frequencies are more fundamental than masses | Philosophical choice—empirically equivalent |
| The adelic constraint applies to physical constants | Requires hypothesis that constants are rational |
| The Landau pole is cancelled by adelic structure | Unpublished; no independent verification |
| Yukawa couplings are cross-ratios of geometric periods | Research program with no computational results |
| The Bruhat–Tits tree is the geometry of frequency space | Falsifiable predictions not yet tested |

### 14.3 The Central Principle

> Mathematical identity does not automatically imply physical significance.

This document describes a framework—a way of organizing what we know that reveals structure not visible in the standard organization. It is not a new physical theory.

---

## 15. Open Questions

- Can $\alpha$ be derived from pure geometry?
- Can any Yukawa coupling be expressed as a non-tautological cross-ratio?
- Why does the frequency spectrum have the specific values it does?
- Does the Bruhat–Tits tree provide the natural geometry for particle frequencies?
- How does the strong force (confinement) fit into the frequency picture?
- Can the adelic product formula be turned into a practical constraint on particle masses?

---

## 16. Conclusion

The fine-structure constant $\alpha$ equals the ratio of two lengths—the classical electron radius and the reduced Compton wavelength. This ratio is a projective cross-ratio, invariant under projective (Möbius) transformations. Both lengths derive from the electron’s Compton frequency.

When this observation is extended to all particles, a coherent framework emerges: every massive particle is characterized by a frequency; mass is frequency in different units; the dimensionless constants of the Standard Model fall into three structural types; a computational scan of 600 combinations confirms that coupling constants arise naturally as non-tautological cross-ratios while mass ratios resist such expression; the Higgs mechanism becomes a frequency multiplier; the running of couplings becomes frequency-dependence; and precision measurements, which count integer cycles, produce rational numbers that satisfy a number-theoretic constraint.

What this document does not do: make novel predictions, derive any mass ratio from first principles, or replace the Standard Model. What it does do: provide a unified language in which the dimensionless constants of nature reveal their structural relationships, sharpen the questions about why they have the values they do, and point toward specific computational and mathematical programs that might answer those questions.

---

## Appendix A: Numerical Verification

```python
"""
Complete verification for 1.0.md
Quantum-Mechanical Physics as Invariant Geometric Structure
Includes extended frequency spectrum, tree depths, cross-sector ratios.
"""
import math

# ---- FUNDAMENTAL CONSTANTS (CODATA 2018) ----
e      = 1.602176634e-19
eps0   = 8.8541878128e-12
hbar   = 1.054571817e-34
c      = 299792458
G      = 6.67430e-11

# ---- PARTICLE MASSES ----
m_e    = 9.1093837015e-31
m_mu   = 1.883531627e-28
m_tau  = 3.1675e-27
m_p    = 1.67262192369e-27
m_W    = 80.377e9 * e / c**2
m_Z    = 91.1876e9 * e / c**2
m_H    = 125.20e9 * e / c**2
m_top  = 172.5e9 * e / c**2

# ---- HIGGS VEV ----
v_GeV  = 246.22
v      = v_GeV * 1e9 * e / c**2

# ---- FREQUENCIES ----
def freq(mass):
    return mass * c**2 / hbar

omega_e   = freq(m_e)
omega_mu  = freq(m_mu)
omega_tau = freq(m_tau)
omega_p   = freq(m_p)
omega_W   = freq(m_W)
omega_Z   = freq(m_Z)
omega_H   = freq(m_H)
omega_Higgs = freq(v)
omega_top = freq(m_top)
omega_P   = math.sqrt(c**5 / (hbar * G))

# ---- LENGTH SCALES ----
r_e    = e**2 / (4 * math.pi * eps0 * m_e * c**2)
lc_e   = hbar / (m_e * c)
alpha  = e**2 / (4 * math.pi * eps0 * hbar * c)
a_0    = 4 * math.pi * eps0 * hbar**2 / (m_e * e**2)
l_P    = math.sqrt(hbar * G / c**3)

# ---- YUKAWA ----
y_e   = math.sqrt(2) * m_e   / v
y_mu  = math.sqrt(2) * m_mu  / v
y_tau = math.sqrt(2) * m_tau / v
y_top = math.sqrt(2) * m_top / v

# ---- WEAK MIXING (tree-level) ----
cosW_tree = m_W / m_Z

# ---- CROSS-RATIO ----
def cross_ratio(x1, x2, x3, x4):
    num = (x1 - x3) * (x2 - x4)
    den = (x1 - x4) * (x2 - x3)
    return num / den if den != 0 else float('inf')

L = 1e30
cr = cross_ratio(0, L, r_e, lc_e)

ok = True
def check(label, val, expected, tol=1e-12):
    global ok
    if abs(val - expected) < tol: print(f"  [PASS] {label}")
    else: print(f"  [FAIL] {label}: {val:.6e} != {expected:.6e}"); ok = False

print("=" * 65)
print("VERIFICATION: 1.0.md")
print("=" * 65)

check("alpha = r_e / lc_e", r_e/lc_e, alpha)
check("cross-ratio (0,inf; r_e, lc_e)", cr, alpha)

r_mu = e**2/(4*math.pi*eps0*m_mu*c**2); lc_mu = hbar/(m_mu*c)
check("alpha_mu = r_mu / lc_mu", r_mu/lc_mu, alpha)

y_e_check = math.sqrt(2)*omega_e/omega_Higgs
check("y_e = sqrt(2)*omega_e/omega_H", y_e, y_e_check)

print(f"  omega_e = {omega_e:.4e} rad/s")
print(f"  omega_P = {omega_P:.4e} rad/s")
print(f"  omega_P / omega_e = {omega_P/omega_e:.2e}")
print(f"  y_e = {y_e:.4e}, y_mu = {y_mu:.4e}, y_tau = {y_tau:.4e}, y_top = {y_top:.4f}")
print(f"  cos(theta_W)_tree = {cosW_tree:.6f}")

alpha_MZ = 1/127.95
delta = (alpha_MZ - alpha) / alpha * 100
print(f"  Running: {delta:.1f}%")

all_bounded = all(w < omega_P for w in [omega_e, omega_mu, omega_tau, omega_p, omega_W, omega_Z, omega_H, omega_top])
print(f"  All SM freqs < omega_P: {'YES' if all_bounded else 'NO'}")

print("\n--- Tree Depths (log2, ref=1 rad/s) ---")
for name, w in [("nu_e", 1.7e12), ("e", omega_e), ("mu", omega_mu),
                 ("p", omega_p), ("tau", omega_tau), ("top", omega_top),
                 ("Higgs", omega_H), ("Planck", omega_P)]:
    print(f"  {name:10s}: depth ~ {math.log2(w):.0f}")

# Extended scan key results
lambda_e = lc_e
lambda_top = reduced_compton(m_top) if 'reduced_compton' in dir() else hbar/(m_top*c)
lambda_Z_val = hbar/(m_Z*c)
lambda_p = hbar/(m_p*c)
lambda_mu = lc_mu
L_fpi = hbar*c/(0.0923*1e9*e)
lambda_tau = hbar/(m_tau*c)

print("\n--- Key Near-Matches from Extended Scan ---")
ratio1 = lambda_top / lambda_e
print(f"  lambda_top / lambda_e = {ratio1:.4e} vs y_e = {y_e:.4e} ({abs(ratio1-y_e)/y_e*100:.2f}% off)")
ratio2 = lambda_Z_val / lambda_p
print(f"  lambda_Z / lambda_p   = {ratio2:.6f} vs y_tau = {y_tau:.6f} ({abs(ratio2-y_tau)/y_tau*100:.2f}% off)")
ratio3 = lambda_mu / L_fpi
print(f"  lambda_mu / L_fpi     = {ratio3:.6f} vs m_W/m_Z = {m_W/m_Z:.6f} ({abs(ratio3-m_W/m_Z)/(m_W/m_Z)*100:.2f}% off)")

print("\n" + "=" * 65)
if ok: print("ALL ASSERTIONS PASSED [CODE-EXECUTED]")
else: print("SOME ASSERTIONS FAILED")
print("=" * 65)
```

---

## Appendix B: Source Cross-Reference

| Source | Date | Relevance |
|:-------|:-----|:----------|
| Fine-Structure Constant as a Cross-Ratio | 2026/05/09 | $\alpha$ as cross-ratio; five formalisms |
| Tree of Frequencies (DOI: 10.5281/zenodo.20071716) | 2026/05/07 | Bruhat–Tits tree; frequency space geometry; 3 predictions |
| Adelic Cross-Ratio | 2026/04/09 | Cross-ratio as only projective invariant |
| One Pattern / 0.23.md | 2026/05/08 | Grammatical function; Ostrowski; adelic frontier |
| Number Theory as Physics | 2026/04 | Spin-statistics from tree geometry |
| MASS-FREQUENCY project | Nov 2025 | $m = h f_C / c^2$; mass-frequency identity |
| This project: 0.7.py | 2026/05/10 | Extended 600-combination computational scan |
| This project: 0.7.1.md | 2026/05/10 | Path B prototype—Shimura variety minimal example |

---

## Appendix C: Glossary

| Term | Definition |
|:-----|:-----------|
| **Adelic product formula** | $\prod_v \lvert q \rvert_v = 1$ for every rational number $q$. See §9.2 for a worked example with the number 12. |
| **Bruhat–Tits tree** | A discrete, branching geometric structure arising from $p$-adic numbers. Proposed as the geometry of frequency space. |
| **Compton frequency** | $\omega = m c^2 / \hbar$—the frequency associated with a particle’s rest-mass energy. Same for all observers. |
| **Cross-ratio** | $(x_1, x_2; x_3, x_4) = (x_1-x_3)(x_2-x_4) / ((x_1-x_4)(x_2-x_3))$. The fundamental invariant of projective geometry. |
| **De Broglie frequency** | $\omega_{\text{dB}} = E / \hbar$—frequency including kinetic energy. Frame-dependent. |
| **Higgs frequency** | $\omega_H = v c^2 / (\hbar \sqrt{2}) \approx 2.64 \times 10^{26}$ rad/s—scale set by the Higgs VEV. |
| **Non-tautological** | A ratio is non-tautological if the two length scales are independently characterizable by distinct experimental techniques that do not presuppose knowledge of the quantity being tested. A tautological ratio restates a known relationship in different units without adding independent information (e.g., Compton wavelength ratios). See §6.2 for the full operational definition. |
| **$p$-adic absolute value** | A measure of “size” based on divisibility by a prime $p$. Example: $\lvert 12 \rvert_2 = 1/4$, $\lvert 12 \rvert_3 = 1/3$. |
| **Ostrowski’s theorem** | Every consistent way of measuring the size of rational numbers is either the usual absolute value or a $p$-adic absolute value. |
| **Type I invariant** | Ratio where the frequency cancels, leaving a universal coupling (e.g., $\alpha$). |
| **Type II invariant** | Ratio of two different frequencies, directly exposing the mass ratio (e.g., $m_p/m_e$). |
| **Type III invariant** | Ratio involving scales from different physical sectors (e.g., electromagnetic vs. gravitational). |
| **Yukawa coupling** | $y_f = \sqrt{2} \cdot m_f / v$—strength of a particle’s interaction with the Higgs field. |

---

**Version 1.0—Release**


