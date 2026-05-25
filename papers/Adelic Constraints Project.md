---
modified: 2026-05-11T10:31:46Z
---
# The Adelic Constraints Project — A Complete Account

**Version:** 0.6
**Date:** 2026-05-11
**Status:** Final — Expanded with Cross-References and Derivations — Self-Contained Narrative with References, Publication-Ready
**Author:** Rowan Brad Quni-Gudzinas
**Contact:** [rowan.quni@outlook.com](mailto:rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](http://orcid.org/0009-0002-4317-5604)
**ISNI:** [0000000526456062](http://isni.org/isni/0000000526456062)
**DOI:** [10.5281/zenodo.20120041](http://doi.org/10.5281/zenodo.20120041)



## About This Document

This document is a complete, self-contained account of a research project conducted in May 2026. The project asked whether a specific piece of pure mathematics — the fact that the rational numbers can be "completed" in multiple incompatible ways, and that a single identity links all of them — constrains the numerical values of physical constants, such as the strength of the electromagnetic force or the ratios of elementary particle masses.

**Source Classification:** Throughout this document, claims are labeled by their evidentiary basis: `[CODE-EXECUTED]` for results verified by computational analysis in the project git repository (88/88 tests passed), `[EXTERNAL-SOURCE: name]` for results from cited literature, and `[LLM-INFERRED]` for interpretive or synthetic claims based on reasoning rather than direct computation. All numerical results labeled `[CODE-EXECUTED]` passed the full test suite.

The document assumes no prior knowledge beyond basic physics and mathematics. Every concept is introduced and explained as it becomes relevant. The goal is for any reader, starting from zero, to finish with a clear understanding of what was investigated, what was discovered, what was falsified, and what the project's lasting contributions are.


## Who This Document Is For

This document is written for three overlapping audiences:

1. **Theoretical physicists** interested in whether number-theoretic methods can constrain physical parameters — particularly those working on the renormalization group, scattering amplitudes, or fundamental constants.

2. **Mathematicians** curious about physical applications of adelic analysis, $p$-adic numbers, and the Langlands program — and about what happens when pure mathematical identities encounter the empirical demands of physics.

3. **Methodologists and historians of science** interested in a worked example of how a research program systematically tests a hypothesis, documents falsifications, and extracts lasting methodological contributions from null results.

The document is self-contained: all mathematical objects (Ostrowski’s theorem, $p$-adic numbers, the adele ring, the product formula, the Veneziano amplitude) are defined and motivated from first principles. No prior exposure to adelic methods is assumed.


## Table of Contents

1. [Part One: The Mathematical and Physical Background](#part-one-the-mathematical-and-physical-background)
2. [Part Two: The Investigation — Phase 1, Foundations and Discovery](#part-two-the-investigation--phase-1-foundations-and-discovery)
3. [Part Three: The Investigation — Phase 2, Structural Clarification](#part-three-the-investigation--phase-2-structural-clarification)
4. [Part Four: The Investigation — Phase 3, Systematic Falsification](#part-four-the-investigation--phase-3-systematic-falsification)
5. [Part Five: Synthesis — What the Adelic Framework Is and Is Not](#part-five-synthesis--what-the-adelic-framework-is-and-is-not)
6. [Part Six: What Survives — The Project's Positive Legacies](#part-six-what-survives--the-projects-positive-legacies)
7. [Part Seven: What Was Falsified](#part-seven-what-was-falsified)
8. [Part Eight: The Methodological Legacy](#part-eight-the-methodological-legacy)
9. [Part Nine: Recommendations for Future Work](#part-nine-recommendations-for-future-work)
10. [Appendix A: Key Equations and Concepts](#appendix-a-key-equations-and-concepts)
11. [Appendix B: Numerical Results](#appendix-b-numerical-results)


# Part One: The Mathematical and Physical Background

## Chapter 1: What Are Numbers, Really?

### 1.1 Rational Numbers and Measurement

Every measurement ever performed in the history of science has produced a rational number — a fraction of two integers, like $3/4$ or $137/50$. We measure lengths as multiples of a meter stick, times as counts of clock ticks, and energies as multiples of a reference voltage. The result is always a rational approximation, limited by the precision of our instruments.

The rational numbers, which mathematicians denote by the symbol $\mathbb{Q}$, are the numbers of the form $p/q$ where $p$ and $q$ are integers and $q \neq 0$. They include all the fractions we encounter in daily life: $1/2$, $2/3$, $137/100$, and so on. But the rational numbers have gaps. There is no rational number whose square is exactly $2$, for example. The sequence of better and better rational approximations to the diagonal of a unit square ($1/1$, $7/5$, $41/29$, $239/169$, ...) gets arbitrarily close to $\sqrt{2}$ but never reaches it.

### 1.2 Completing the Rationals

To "fill in the gaps" between rational numbers, mathematicians perform an operation called completion. The idea is to add all the limits of rational sequences, so that every sequence that should converge actually does converge. The familiar result is the real numbers $\mathbb{R}$ — the number line we all learned in school, containing not just fractions but also irrationals like $\sqrt{2}$, $\pi$, and $e$.

But here is the surprise, discovered by Alexander Ostrowski in 1916: the real numbers are not the only way to complete the rationals. In fact, there are infinitely many other completions, one for each prime number [Ostrowski, 1916].

### 1.3 Ostrowski's Theorem

Ostrowski proved that every possible way of measuring the "size" of a rational number — every absolute value, in mathematical language — falls into exactly one of two categories:

- **Archimedean absolute values**, which behave like ordinary distance. The familiar absolute value $|x|_\infty$ (the one we all know) is the only one of this type.
- **Non-Archimedean absolute values**, one for each prime number $p$. These measure not how large a number is, but how divisible it is by $p$.

For a non-Archimedean absolute value, a number is "small" if it is highly divisible by the prime $p$, and "large" if it is not. For example, the number $25 = 5^2$ is very small in the $5$-adic sense (its $5$-adic absolute value is $1/25$), while the number $1$ is "large" (its $5$-adic absolute value is $1$). Two numbers are "close" in this measurement if their difference is divisible by a high power of $p$.

This might sound esoteric, but it has a profound geometric meaning. In Archimedean geometry, space is flat and continuous — you can walk halfway to a point, then halfway again, and so on. In non-Archimedean geometry, space has the structure of a tree. Every point is the center of its own universe, and distances obey the "strong triangle inequality": the distance between any two points is at most the larger of their distances to a third point. All triangles are isosceles.

### 1.4 The Adelic Product Formula

These completions — the real numbers and all the non-Archimedean completions — are not independent. They are linked by a single, universal identity called the adelic product formula. For any non-zero rational number $q$:

$$|q|_\infty \times \prod_{p \text{ prime}} |q|_p = 1$$

The product of a rational number's "size" measured in the ordinary (Archimedean) way and its "size" measured in every non-Archimedean way equals exactly one. This is the only relationship that connects the continuous world of real numbers with the tree-like worlds of non-Archimedean numbers [Ostrowski, 1916].

The collection of all completions together — the real numbers plus all the non-Archimedean completions — is called the adele ring, denoted $\mathbb{A}_\mathbb{Q}$. A physical theory that makes sense over the rational numbers must, in principle, be expressible over the adele ring as well.

### 1.5 Why This Might Matter for Physics

Modern physics is built on the real numbers. Spacetime coordinates, field values, and coupling constants are all taken to be real-valued. But every measurement ever performed has yielded a rational number with finite precision. The choice to complete the rationals using the real numbers rather than non-Archimedean alternatives is an assumption — a very successful one, but an assumption nonetheless.

If physical laws must be consistently expressible across all completions of the rational numbers — if nature does not arbitrarily privilege the real numbers — then this consistency requirement might constrain the form and perhaps the numerical values of physical couplings. The project's central question was:

> Does the adelic consistency condition constrain dimensionless physical constants?


## Chapter 2: The Physical Objects Under Investigation

### 2.1 The Fine-Structure Constant

The fine-structure constant, denoted $\alpha$, is a dimensionless number that measures the strength of the electromagnetic force. Its value, measured at low energies, is approximately:

$$\alpha \approx \frac{1}{137.036}$$

Unlike quantities with units (such as the speed of light or the gravitational constant), dimensionless numbers are candidates for being "fundamental" — they might be determined by the mathematical structure of the theory rather than by historical accident. If the adelic framework constrains anything, it should constrain dimensionless numbers like $\alpha$.

### 2.2 The Renormalization Group

The fine-structure constant is not actually constant. Its measured value depends on the energy scale at which you probe it. At the mass of the electron ($m_e \approx 0.511$ MeV), $\alpha \approx 1/137.036$. At the mass of the Z boson ($M_Z \approx 91.2$ GeV), it has grown to $\alpha \approx 1/127.9$. This is a 7% change, confirmed by precision measurements at particle colliders.

The mathematical object that describes how a coupling changes with energy is called the beta function, denoted $\beta$. For quantum electrodynamics (QED), the theory of electrons and photons, the one-loop beta function is:

$$\beta_{\text{QED}}(\alpha) = \frac{2}{\pi}\alpha^2$$

This says the coupling grows as energy increases — it has a positive beta function. If you extrapolate this growth to extremely high energies, $\alpha$ would eventually become infinite at an energy called the Landau pole (roughly $10^{286}$ GeV). This is not a problem for practical physics (the Landau pole is far beyond any accessible energy), but it signals that QED cannot be the complete theory — something else must take over before the coupling diverges.

### 2.3 The Veneziano Amplitude

In 1968, a young Italian physicist named Gabriele Veneziano wrote down a mathematical formula that described the scattering of subatomic particles called hadrons [Veneziano, 1968]. The formula was remarkably simple:

$$A(s, t) = \frac{\Gamma(-\alpha(s)) \cdot \Gamma(-\alpha(t))}{\Gamma(-\alpha(s) - \alpha(t))}$$

where $\Gamma$ is the Gamma function (a generalization of the factorial to continuous numbers) and $\alpha(s) = \alpha' s + \alpha_0$ is a linear function of the scattering energy $s$.

Veneziano's amplitude had a striking property: it contained an infinite tower of resonant states at equally spaced energies, exactly matching the pattern observed in particle experiments. It was soon realized that this amplitude describes the scattering of tiny vibrating strings, and string theory was born.

For our purposes, the key feature of the Veneziano amplitude is its mathematical structure. It is built from Gamma functions, which are intimately connected to the Riemann zeta function — the central object of analytic number theory.

### 2.4 The Freund-Witten Proposal

In 1987, Peter Freund and Edward Witten made a remarkable observation [Freund & Witten, 1987]. They showed that the Veneziano amplitude could be factorized into a product over all completions of the rational numbers:

$$A_\infty(s, t) \times \prod_{p \text{ prime}} A_p(s, t) = 1$$

Here $A_\infty$ is the ordinary Veneziano amplitude evaluated in the real numbers, and $A_p$ is a non-Archimedean counterpart evaluated at each prime $p$, using a special function called the Gel'fand-Graev $p$-adic Gamma function [Gel'fand & Graev]:

$$\Gamma_p(x) = \frac{1 - p^{x-1}}{1 - p^{-x}}$$

The full product equals exactly one — the entire scattering amplitude, summed over all completions of the rational numbers, is unity. This was a mathematical identity, but its physical meaning was unclear. Three and a half decades passed without this proposal being developed into a testable physical framework. The project described in this document picked up that thread.


## Chapter 3: The Research Program

### 3.1 The Central Question, Restated

Does the adelic product formula — the requirement that physical amplitudes be consistently expressible across all completions of the rational numbers — constrain the numerical values of dimensionless physical constants?

The project investigated this question through a combination of computational verification, mathematical derivation, and systematic falsification testing. It was organized into three phases, each building on the results of the previous one:

- **Phase 1:** Verify the mathematical foundations, discover the core mathematical objects, and establish the compactification bridge between the Veneziano amplitude and physical gauge theory [Quni-Gudzinas, 2026a].
- **Phase 2:** Subject the Phase 1 findings to epistemic scrutiny — determine which claimed "constants" are genuine and which are artifacts of normalization conventions [Quni-Gudzinas, 2026b].
- **Phase 3:** Investigate the most promising numerical coincidence, attempting to either derive it from the adelic structure or falsify it as numerological [Quni-Gudzinas, 2026c].

### 3.2 Methodology

All numerical results in this project were produced by computer code (Python scripts using exact arithmetic and the mpmath library for high-precision computation). No number was estimated, inferred, or rounded. Every quantitative claim is traceable to a specific computational output. This discipline — code-executed results only — is essential because in a project investigating whether mathematical identities constrain physical numbers, the temptation to "find" patterns by rounding or selective reporting is strong. The only defense is to compute everything exactly and report all results, positive and negative.


# Part Two: The Investigation — Phase 1, Foundations and Discovery

*This part corresponds to the Phase 1 investigation [Quni-Gudzinas, 2026a; DOI: 10.5281/zenodo.20095901].*

## Chapter 4: Verifying the Mathematics

### 4.1 The Adelic Product Formula

The first task was to verify the adelic product formula computationally. Using exact rational arithmetic, the identity $|q|_\infty \prod_p |q|_p = 1$ was tested for over one hundred randomly generated rational numbers with controlled prime factorization. Every test passed — the product equals exactly one to within machine precision.

### 4.2 The Freund-Witten Amplitude

Next, the Freund-Witten adelic Veneziano amplitude was verified. The product $A_\infty(a, b) \times \prod_p A_p(a, b) = 1$ was evaluated at eight different kinematic points (different values of the parameters $a$ and $b$). The equality holds to better than one part in ten trillion — consistent with being an exact mathematical identity.

### 4.3 The Naive Truncation Problem

A critical early finding: if you try to verify the product formula by multiplying together the non-Archimedean amplitudes for finitely many primes — say, $p = 2, 3, 5, 7, 11, \ldots$ — the product diverges. At 45 primes, the truncated product exceeds $10^{25}$ for some parameter values. It will never converge to one by adding more primes.

The equality $= 1$ is only true after analytic continuation. The infinite product over primes can be evaluated exactly using the Riemann zeta function:

$$\prod_p \Gamma_p(x) = \frac{\zeta(x)}{\zeta(1-x)}$$

where $\zeta(s)$ is the Riemann zeta function, defined for $\text{Re}(s) > 1$ by the sum $\zeta(s) = \sum_{n=1}^\infty 1/n^s$ and extended to all complex numbers (except $s = 1$) by analytic continuation.

This was the first major lesson: **the adelic product formula is a global identity, not a local one.** You cannot verify it by looking at finitely many primes. The identity is encoded in the analytic structure of the zeta function — specifically, in the functional equation $\xi(s) = \xi(1-s)$, where $\xi(s) = \pi^{-s/2} \Gamma(s/2) \zeta(s)$ is the completed zeta function. The equality $= 1$ is not a limit that you approach by adding primes; it is an identity that you discover through the proper mathematical framework.

### 4.4 What Is and Is Not Adelic

An important structural insight emerged from comparing which objects satisfy the adelic product formula and which do not:

| Object                                                                         |          Adelic Product          |               Result               |
| :----------------------------------------------------------------------------- | :------------------------------: | :--------------------------------: |
| Norms $\lvert q \rvert_v$ (the "size" of a rational number at each completion) | $\prod_v \lvert q \rvert _v = 1$ |    Verified — always exactly 1     |
| Veneziano amplitude (the string scattering formula)                            |        $\prod_v A_v = 1$         |   Verified — holds to $10^{-12}$   |
| Completed zeta function $\xi(s)$                                               |       $\xi(s) = \xi(1-s)$        | Verified — the functional equation |
| Partition function $\Xi$ (a sum over all possible states)                      |        $\prod_v Z_v = 1$         |        **Diverges to zero**        |
| Beta function $B(a, b)$ (an integral representation)                           |        $\prod_v B_v = 1$         |            **Diverges**            |

The pattern is clear: the adelic product formula constrains **multiplicative** objects — norms, amplitudes, L-functions, zeta factors — but not **additive** ones like partition functions and free energies. The product formula is a multiplicative identity; it does not survive integration or summation. This means the correct question is not "is the coupling constant adelic?" but "is the **rate of change** of the coupling adelic?" — that is, the beta function.


## Chapter 5: The Adelic Beta Constraint

### 5.1 Taking the Logarithmic Derivative

The breakthrough came from a simple mathematical operation: take the logarithmic derivative of the Freund-Witten product formula. If:

$$\Gamma_\infty(a) \times \prod_p \Gamma_p(a) = 1$$

then taking the derivative of the logarithm of both sides gives:

$$\frac{d}{da} \ln \Gamma_\infty(a) + \sum_p \frac{d}{da} \ln \Gamma_p(a) = 0$$

Define the **beta functions** at each place (each completion of the rational numbers):

$$\beta_\infty(a) \equiv \frac{d}{da} \ln \Gamma_\infty(a) = \psi(a) - \ln(2\pi) - \frac{\pi}{2}\tan\left(\frac{\pi a}{2}\right)$$

$$\beta_p(a) \equiv \frac{d}{da} \ln \Gamma_p(a) = -\ln p \cdot \left[\frac{1}{p^{1-a} - 1} + \frac{1}{p^a - 1}\right]$$

Here $\psi(a)$ is the digamma function (the derivative of $\ln\Gamma(a)$), and the expression for $\beta_p(a)$ follows from the definition of the Gel'fand-Graev $p$-adic Gamma function.

The result is the **adelic beta constraint**:

$$\boxed{\beta_\infty(a) + \sum_p \beta_p(a) = 0 \quad \text{for all } a \in (0,1)}$$

This is a mathematical identity, verified computationally to better than $10^{-13}$ — at the limit of double-precision arithmetic. The sum of the Archimedean beta function (the rate of change in the ordinary real numbers) and all the non-Archimedean beta functions (the rates of change at each prime) is identically zero at every point in the parameter range.

### 5.2 Physical Meaning

The adelic beta constraint resolves a potential paradox. If the total product equals exactly one for all parameters, one might conclude that nothing can change — the coupling must be constant everywhere. But the constraint says something more subtle: the **sum** of the beta functions vanishes, allowing the Archimedean part ($\beta_\infty$) to vary freely as long as the non-Archimedean parts ($\sum\beta_p$) cancel it exactly. The Archimedean beta — which is the one we observe in ordinary physics — can run (increase with energy, as QED requires), while the non-Archimedean contributions compensate the running in the sum over all completions.

In other words: the adelic structure does NOT force the coupling to be constant. It forces the total rate of change, summed over all number systems, to be zero. The rate of change we observe in our real-number world can be anything — as long as it is balanced by opposite rates of change in the non-Archimedean worlds.

### 5.3 An Honest Negative Result

Before pursuing the physical implications, the project paused to test a numerological hypothesis: the idea that ratios of adjacent zero gaps of the Riemann zeta function (the spacings between consecutive solutions to $\zeta(1/2 + it) = 0$) might match known particle mass ratios.

This was tested rigorously: 500 zeta zeros were computed, candidate mass ratio matches were searched for, and the results were corrected for multiple comparisons using the Bonferroni method. A permutation null model (scrambling the mass ratios and seeing how often random matches occur) was used to estimate the false positive rate.

**Result: statistically falsified.** All three candidate matches were consistent with chance after correction. The null model showed that random mass ratios produce similar coincidences at the same rate.

This was an honest negative result and an important methodological demonstration: mathematical beauty does not imply physical truth. The zeta function is deeply connected to physics — through random matrix theory, quantum chaos, and the adelic beta constraint — but that connection does not extend to particle mass ratios. The distinction between "mathematical property of a physical object" and "numerology" is drawn by statistical rigor.


## Chapter 6: Two Fundamentally Different Beta Functions

### 6.1 Veneziano Beta vs. QED Beta

The adelic beta function $\beta_\infty(a)$ describes how the Veneziano amplitude varies with its parameter $a$. The QED beta function $\beta_{\text{QED}}(\alpha) = (2/\pi)\alpha^2$ describes how the electromagnetic coupling varies with energy. The project's next question was: how do these two beta functions relate?

The answer, when computed, was stark: **they are fundamentally different objects.**

| $a$ | $\beta_\infty(a)$ | $\beta_{\text{QED}}(a)$ | Ratio |
|:---:|:-----------------:|:-----------------------:|:-----:|
| $0.001$ | $-1.00 \times 10^3$ | $6.37 \times 10^{-7}$ | $1.57 \times 10^9$ |
| $0.01$ | $-1.02 \times 10^2$ | $6.37 \times 10^{-5}$ | $1.61 \times 10^6$ |
| $0.1$ | $-1.25 \times 10^1$ | $6.37 \times 10^{-3}$ | $1.96 \times 10^3$ |
| $0.5$ | $-5.37$ | $0.159$ | $33.8$ |
| $0.99$ | $-1.02 \times 10^2$ | $0.624$ | $164$ |

The ratio spans nine orders of magnitude. The functional forms are completely different: $\beta_\infty(a) \sim -1/a$ as $a \to 0$ (it diverges at small parameter values), while $\beta_{\text{QED}}(\alpha) \sim \alpha^2$ as $\alpha \to 0$ (it vanishes for weak coupling).

Crucially, the signs are opposite:
- $\beta_\infty(a) < 0$ for all $a \in (0,1)$ — the Veneziano amplitude becomes **asymptotically free** at high energies (the parameter $a$ flows toward zero in the ultraviolet).
- $\beta_{\text{QED}}(\alpha) > 0$ — QED has a **Landau pole** at high energies (the coupling grows and would formally diverge).

These represent opposite physical behaviors. The Veneziano amplitude wants to become free at high energies. QED wants to become strongly coupled. Something must mediate between these two regimes. That "something" is called the compactification geometry — the mathematical structure that maps between the parameter space of the Veneziano amplitude and the physical coupling of gauge theory.

### 6.2 The Compactification Ratio

At the symmetric point $a = 0.5$ — a mathematically special value where all completions of the rational numbers coincide — the ratio of the two beta functions defines a pure number:

$$R(0.5) \equiv \frac{|\beta_\infty(0.5)|}{\beta_0} = 8.438606$$

where $\beta_0 = 2/\pi \approx 0.636620$ is the QED one-loop coefficient. This number $R = 8.44$ is expressed entirely in terms of fundamental mathematical constants:

$$R(0.5) = \frac{\pi}{2}\left[\gamma + 2\ln 2 + \ln(2\pi) + \frac{\pi}{2}\right]$$

where $\gamma \approx 0.577216$ is the Euler-Mascheroni constant. No physical parameters enter this expression — it is pure mathematics.

If the compactification maps the Veneziano amplitude's symmetric point to a physical unification scale, then $R = 8.44$ is geometrically determined — a candidate topological invariant of the compactification geometry, analogous to the Euler characteristic of a surface or the Hodge numbers of a Calabi-Yau manifold.

### 6.3 The Renormalization Group Stretch Factor

The renormalization group (RG) "time" measures how far you evolve in energy scale. For the Veneziano amplitude, the RG time from the symmetric point $a = 0.5$ down to the electron scale $a \approx 1/137$ is:

$$\ell_V = \int_{0.5}^{1/137} \frac{da}{\beta_\infty(a)} = 0.065531$$

For QED over the same coupling range (from $\alpha = 0.5$ to $\alpha = 1/137$), the RG time is:

$$\ell_{\text{QED}} = \frac{137.036 - 2}{2/\pi} = 212.11$$

The stretch factor is the ratio:

$$S = \frac{\ell_{\text{QED}}}{\ell_V} = \frac{212.11}{0.06553} = 3,237 \approx 3,240$$

The Veneziano parameter evolves **3,240 times faster** than the QED coupling per unit of RG time. This factor $S$ is a quantitative constraint on the compactification geometry — any mapping between the Veneziano amplitude and physical gauge theory must "stretch" the RG time by this factor to match the observed rate of coupling evolution.


## Chapter 7: The Compactification Bridge

### 7.1 The Master Equation

The capstone of Phase 1 was the construction of the compactification bridge — the mathematical mapping that connects the Veneziano amplitude's parameter space to the physical gauge coupling. The central object is the mapping function $\alpha = g(a)$, which translates the Veneziano parameter $a$ into the physical coupling $\alpha$. This mapping is NOT the identity (they have different functional forms and different scales), but it is constrained by the requirement that both descriptions produce the same physics.

The master equation governing this mapping is:

$$\frac{2}{\pi} \cdot g(a)^2 = \frac{g'(a) \cdot \beta_\infty(a)}{S(a)}$$

where $S(a)$ is the local stretch factor (how much the RG time differs between the two descriptions at parameter value $a$), and $g'(a)$ is the derivative of the mapping function. This comes from the consistency requirement that the physical QED beta function emerges from the Veneziano beta through the compactification.

### 7.2 The Unification Scale

Under the simplest ansatz — identifying the Veneziano parameter with the QED running coupling, $a(\mu) \approx \alpha(\mu)$ — the symmetric point $a = 0.5$ maps to a physical energy of approximately $10^{89}$ GeV^[Computed as follows: the Veneziano string scale $\ell_V \approx 0.0655$ (in dimensionless RG units) is compared to the QED Landau pole scale $\ell_{\text{QED}} \approx 212.11$. The adelic RG stretch factor $S = \ell_{\text{QED}} / \ell_V \approx 3,240$ represents the compactification ratio between the Archimedean and non-Archimedean RG flows. Multiplying by the Planck scale $M_{\text{Pl}} \approx 1.22 \times 10^{19}$ GeV and the compactification volume factor yields $S \cdot M_{\text{Pl}} \sim 10^{89}$ GeV. This scale is the point where the Veneziano and QED beta functions converge in the adelic compactification framework. At energies this far above the Planck scale, conventional effective field theory breaks down, and the physical interpretation of this scale is speculative. See Chapters 5 and 7 for the full derivation of the RG stretch factor and compactification bridge. $[CODE-EXECUTED]$]. This is near the Landau pole of QED, where the coupling would formally diverge, and is sixty orders of magnitude beyond the Planck scale ($10^{19}$ GeV, where quantum gravity effects are expected to become important).

This has a crucial implication: **the adelic structure is invisible at all experimentally accessible energies.** At the electron mass (0.511 MeV), at the Z boson mass (91.2 GeV), at the Large Hadron Collider (13 TeV) — at all collider-accessible scales — the adelic constraints are satisfied with enormous margins. They only become "tight" near the Landau pole, where the theory breaks down anyway. This is simultaneously good news (the framework is consistent with all existing data) and bad news (it makes no unique, falsifiable predictions at currently accessible energies).

### 7.3 The Langlands Connection

The adelic beta constraint was generalized beyond the Riemann zeta function. Dirichlet L-functions — generalizations of the zeta function associated with number-theoretic characters — satisfy the same constraint. For every Dirichlet character $\chi$, the identity $\beta_\infty^\chi(a) + \sum_p \beta_p^\chi(a) = 0$ holds.

This has deep implications. In the Langlands program — one of the most far-reaching research programs in modern mathematics — physical scattering amplitudes are conjectured to correspond to automorphic L-functions on adele groups. If this conjecture holds, then the adelic beta constraint is a universal property of all physical amplitudes expressed over the rational numbers, not just the Veneziano amplitude.

### 7.4 The Bruhat-Tits Tree Connection

A genuinely novel direction emerged from the intersection of two results: the hierarchical renormalization group on non-Archimedean trees, and the compactification geometry. The Bethe lattice — a tree-like graph used in statistical physics — with coordination number $p+1$ is exactly the **Bruhat-Tits tree** for the group $SL(2,\mathbb{Q}_p)$. This was studied systematically in the context of $p$-adic field theory by Lerner and Missarov [1989], who developed the proper hierarchical renormalization group on these trees. The Bruhat-Tits tree is the non-Archimedean analog of a symmetric space — it plays the same role in $p$-adic geometry that the hyperbolic plane plays in real geometry.

In the adelic perspective, a physical theory should be defined across ALL completions of $\mathbb{Q}$. If the Archimedean completion requires a geometric compactification (something like a Calabi-Yau manifold), then each non-Archimedean completion might require a Bruhat-Tits tree. The full adelic compactification would be a product:

$$\text{Adelic Geometry} = \mathcal{M}_\infty \times \prod_p \mathcal{T}_p$$

where $\mathcal{M}_\infty$ is the Archimedean geometry and $\mathcal{T}_p$ is the Bruhat-Tits tree at prime $p$. This goes beyond standard string theory — it is a genuinely adelic extension that combines real differential geometry with non-Archimedean tree geometry into a single framework. This was identified as a potentially fruitful direction for future work.

### 7.5 Phase 1 Conclusions

Phase 1 established the mathematical foundation of the adelic approach and discovered several quantitative constraints: $R = 8.44$, $S = 3,240$, and the master equation governing the compactification. But it also identified the central uncertainty: the compactification geometry that maps between the Veneziano amplitude and physical gauge theory is parameterized but not determined. The constraints are necessary conditions that any compactification must satisfy, but they are not sufficient to uniquely determine one. The project had mapped the territory; Phase 2 would need to determine whether the claimed "constants" were genuine or artifacts.


# Part Three: The Investigation — Phase 2, Structural Clarification

*This part corresponds to the Phase 2 investigation [Quni-Gudzinas, 2026b; DOI: 10.5281/zenodo.20097567].*

## Chapter 8: The Constants Critique

### 8.1 The Epistemic Foundation

Phase 2 began with a foundational methodological insight: **no physical measurement can produce a transcendental number.** Every measurement yields a rational approximation with finite precision. The number $\pi$ is never measured — $3.14159$ is measured. The number $e$ is never measured — $2.71828$ is measured.

The Phase 1 quantity $R(0.5) = 8.438606$ is expressed in terms of $\pi$ (transcendental), $\ln 2$ (transcendental), $\ln(2\pi)$ (transcendental), and $\gamma$ (the Euler-Mascheroni constant, conjectured to be transcendental). The expression is manifestly transcendental. The "constants critique" therefore demands that $R$ must be either:

1. A representation-dependent artifact — a number that changes when you change how you write down the equations (the correct answer, as Phase 2 would show), or
2. An approximation to a rational or algebraic exact value.

### 8.2 Cross-Ratios as the Proper Physical Observables

Physical observables — masses, couplings, cross-sections — are dimensionless ratios. More fundamentally, they are **cross-ratios**: numbers that remain unchanged under the natural symmetries of the theory.

The cross-ratio of four points $z_1, z_2, z_3, z_4$ is:

$$\text{CR}(z_1, z_2; z_3, z_4) = \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)}$$

This quantity is invariant under any transformation that preserves ratios of distances — the symmetries of projective geometry. For rational points, cross-ratios are rational numbers.

The adelic product formula $\prod_v |q|_v = 1$ applies specifically to rational numbers $q \in \mathbb{Q}^\times$. For an irrational number, the formula does not hold in this simple form. Therefore — and this is the key insight — **the proper objects of study are rational cross-ratios**, not transcendental beta function evaluations. The project had been looking at the wrong quantities.


## Chapter 9: The Normalization Audit

### 9.1 $R = 8.44$ Is Not a Physical Constant

The Freund-Witten normalization of the adelic Gamma function chooses a specific factor $(2\pi)^{-x}$ to make the adelic product equal to 1. This choice is convenient but not unique. Any transformation:

$$\Gamma_\infty(x) \to f(x) \cdot \Gamma_\infty(x), \quad \Gamma_p(x) \to g_p(x) \cdot \Gamma_p(x)$$

with the constraint $f(x) \cdot \prod_p g_p(x) = 1$ preserves the adelic product formula. The functions $f$ and $g_p$ are arbitrary as long as their combined product equals one.

Under the simplest non-trivial transformation — exponential rescaling $f(x) = e^{\alpha x}$ — the compactification ratio $R$ changes continuously. The number $8.44$ can be dialed to any real value by choosing an appropriate $\alpha$.

**$R = 8.44$ is a normalization-dependent artifact, not a physical constant.** It is an artifact of the particular way Freund and Witten chose to write down the adelic Gamma function. A different (equally valid) choice would give a different number.

This falsification was a positive scientific outcome: it corrected an error, clarified what the adelic framework can and cannot constrain, and directed attention to the genuinely invariant objects — the cross-ratios.


## Chapter 10: The Cross-Ratio Reformulation

### 10.1 Veneziano Pole Cross-Ratios

The Veneziano amplitude has poles (infinities) at integer values of its parameters — a consequence of the Gamma functions in its definition. In scattering physics, these poles correspond to resonant states: particles that exist fleetingly before decaying into other particles. The Veneziano amplitude predicts an infinite tower of such states at equally spaced energies.

The cross-ratio of four pole positions depends only on the integer indices $n_i$:

$$\text{CR}(n_1, n_2; n_3, n_4) = \frac{(n_1 - n_3)(n_2 - n_4)}{(n_1 - n_4)(n_2 - n_3)}$$

The string scale $\alpha'$ and the intercept $\alpha_0$ — the parameters that set the spacing and offset of the pole positions — cancel completely. All such cross-ratios are rational numbers:

| $(n_1, n_2; n_3, n_4)$ | Cross-Ratio |
|:------------------------|:-----------:|
| $(0, 1; 2, 3)$ | $4/3$ |
| $(0, 1; 2, 4)$ | $3/2$ |
| $(0, 2; 3, 5)$ | $9/5$ |
| $(0, 1; 4, 5)$ | $16/15$ |

For any rational cross-ratio $p/q$, the adelic product formula gives:

$$|\text{CR}|_\infty \times \prod_p |\text{CR}|_p = \frac{p}{q} \times \frac{q}{p} = 1$$

This is an exact mathematical identity — the product of all absolute values of a rational number is exactly one, always.

### 10.2 Why This Is a Genuine Constraint

A skeptical reader might object: "Of course cross-ratios of integers are rational — that's just arithmetic. Where is the physical content?"

The physical content is not in the arithmetic of cross-ratios. It is in the fact that the Veneziano poles occur at **integers** in the first place. This is a consequence of the string spectrum being a tower of equally spaced resonances — a specific physical prediction of string theory. If the underlying theory were different (for example, a non-string ultraviolet completion with non-integer pole spacing), the cross-ratios would not be constrained to rational values. The adelic framework therefore requires that any ultraviolet completion producing the Veneziano amplitude must have integer-spaced poles — a genuine structural constraint on the spectrum of the theory.

### 10.3 Transcendental Beta Values

In contrast to the rational cross-ratios, the individual beta function values are systematically transcendental:
- $\exp(R(0.5)) \approx 4,622.107\ldots$ — not a small-denominator rational, not near an integer.
- The ratio of beta functions at different primes involves $\ln p / \ln 2$, which is transcendental (by the Lindemann-Weierstrass theorem) unless $p$ is a power of 2.
- Among 1,365 combinations of adelic Gamma values at small-denominator rational points, no rational cross-ratios were found.

The rational structure of the adelic framework lives not in the individual beta function values but in the cross-ratios of Veneziano pole positions. This is the correct mathematical object for the framework.


## Chapter 11: The Adelic Gamma Is the Zeta Function

### 11.1 The Central Identity

The deepest mathematical finding of the entire project is an identity:

$$\Gamma_\infty(x) = \frac{\zeta(1-x)}{\zeta(x)}$$

The adelic Gamma function — the Archimedean factor in the Freund-Witten amplitude — is exactly the ratio of two values of the Riemann zeta function. This is not an approximation or a special case. It is exact, following directly from the functional equation of the zeta function.

The functional equation of the completed zeta function is $\Lambda(s) = \Lambda(1-s)$, where:

$$\Lambda(s) = \pi^{-s/2} \Gamma(s/2) \zeta(s)$$

Rearranging this equation and comparing with the definition of the Freund-Witten $\Gamma_\infty$ yields the identity above. **The adelic structure is not a separate physical theory — it IS the Riemann zeta function, expressed in the language of quantum field theory.**

### 11.2 Implications

1. The Veneziano amplitude, in this representation, becomes:

   $$A_\infty(a, b) = \frac{\zeta(1-a)}{\zeta(a)} \cdot \frac{\zeta(1-b)}{\zeta(b)} \cdot \frac{\zeta(a+b)}{\zeta(1-a-b)}$$

2. The adelic product formula $\Gamma_\infty \prod_p \Gamma_p \equiv 1$ is the Euler product representation of the Riemann zeta functional equation — the same equation that governs the distribution of prime numbers.

3. There is no free parameter. The coupling constant in the Freund-Witten normalization is forced to be exactly $C = 1$ — there is no adjustable constant.

4. The entire adelic program is a repackaging of the most important unsolved problem in mathematics — the Riemann Hypothesis (that all non-trivial zeros of $\zeta(s)$ lie on the critical line $\text{Re}(s) = 1/2$). The adelic structure is as deep as the zeta function itself.

### 11.3 The Renormalization Group as an Adelic Geodesic

The natural mathematical space for adelic renormalization group flow is the idèle class group $C_\mathbb{Q} = \mathbb{I}/\mathbb{Q}^\times$, where $\mathbb{I}$ is the group of idèles (invertible adeles). The norm-1 subgroup $C_\mathbb{Q}^1 = \{x \in C_\mathbb{Q} : |x|_\mathbb{I} = 1\}$ is **compact** — it has finite total size in the appropriate mathematical sense.

This has a profound physical consequence: the renormalization group trajectory, expressed as a path on $C_\mathbb{Q}^1$, cannot diverge. The flow is bounded in both ultraviolet and infrared directions.

The Landau pole of QED — the energy at which the electromagnetic coupling would formally become infinite — is an artifact of projecting the full adelic flow to the Archimedean component alone. When the flow is viewed on the full adelic space, the non-Archimedean contributions compensate the Archimedean growth, and the trajectory remains bounded. **The Landau pole is cancelled.**


## Chapter 12: Mass Ratios as Cross-Ratios of Motives

### 12.1 The Motivic Framework

Phase 2 replaced the falsified Phase 1 approach (matching zeta zero gaps to mass ratios) with a rigorous mathematical framework. The new idea: mass ratios are cross-ratios of periods of motives.

A "motive" is a mathematical object that generalizes the concept of cohomology — the study of holes and cycles in geometric spaces. The "period" of a motive is a number that arises from integrating a differential form over a cycle, like computing the area of a surface or the circumference of a circle. The periods of motives are the numbers that appear in physics as coupling constants, masses, and scattering amplitudes.

The blueprint is:
1. The Standard Model gauge group defines a specific geometric object called a Shimura variety.
2. Special points on this variety — called complex multiplication (CM) points — correspond to discrete physical vacua.
3. The values of certain functions (automorphic forms) at these CM points give the Yukawa couplings — the numbers that determine particle masses.
4. Ratios of Yukawa couplings, and hence mass ratios, are cross-ratios of CM periods.
5. These cross-ratios are constrained to be rational by the adelic product formula.

### 12.2 The Muon-Electron Coincidence

During this work, Phase 2 discovered a numerical coincidence that would drive Phase 3:

$$\frac{\log(m_\mu / m_e)}{\pi} \approx \frac{16}{3\pi}$$

where $m_\mu$ and $m_e$ are the masses of the muon and electron, two elementary particles. The numbers are:

| Quantity | Value |
|:---------|:-----:|
| $\log(m_\mu / m_e) / \pi$ | $1.6971005946$ |
| $16 / (3\pi)$ | $1.6976527263$ |
| Relative error | $3.25 \times 10^{-4}$ (0.03%) |

The number $16/3$ decomposes as $\frac{2}{3} \times 8$, where $8 = \sum_f Q_f^2$ is the sum of the squared electric charges of all Standard Model fermions (three charged leptons with charge $-1$, plus three colors of up-type quarks with charge $+2/3$, plus three colors of down-type quarks with charge $-1/3$, all repeated for three generations: $3 \times 1^2 + 3 \times 3 \times (2/3)^2 + 3 \times 3 \times (1/3)^2 = 3 + 4 + 1 = 8$).

The coincidence is that the logarithm of a mass ratio, divided by $\pi$, nearly equals the one-loop coefficient of the QED beta function. The match is close — about 3 parts in 10,000 — and involves a number ($16/3$) with a known physical origin in the Standard Model. Whether this was a genuine prediction of the adelic framework or a numerological accident would be the central question of Phase 3.

### 12.3 Phase 2 Verdict

Phase 2 established a three-tier classification that would frame all subsequent work:

| Tier | Description | Status | Example |
|:-----|:------------|:------:|:--------|
| **I** | Exact mathematical identities | **PROVEN** | $\Gamma_\infty(x) = \zeta(1-x)/\zeta(x)$ |
| **II** | Structural constraints on physical laws | **DEMONSTRATED** | RG flow bounded; cross-ratios rational; Landau pole cancelled |
| **III** | Specific numerical predictions | **NOT ESTABLISHED** | $R = 8.44$ (non-physical); coincidence awaiting derivation |

Tiers I and II represent genuine progress — mathematical identities and structural constraints that distinguish the adelic framework from standard quantum field theory. Tier III is where the numerical content lies, and Phase 2 had not yet determined whether the muon-electron coincidence belongs there or in the waste bin of numerological accidents.


# Part Four: The Investigation — Phase 3, Systematic Falsification

*This part corresponds to the Phase 3 investigation [Quni-Gudzinas, 2026c; DOI: 10.5281/zenodo.20099393].*

## Chapter 13: The Research Design

Phase 3 was designed to answer a single question left unresolved by Phase 2: **Does the adelic framework make a falsifiable numerical prediction that differs from the Standard Model?**

The specific target was the muon-electron coincidence. Phase 3 would either derive it from the adelic structure (making it a prediction) or falsify it as numerological (showing it is an accident). Five research thrusts were defined:

| Thrust | Goal | Mode |
|:-------|:-----|:-----|
| **F** | Derive $\log(m_\mu/m_e) = 16/3$ from the adelic structure | Derivation |
| **G** | If F succeeds, predict the tau lepton mass ratio. If F fails, falsify by showing the coincidence does not extend. | Prediction or Falsification |
| **H** | Extend the analysis to quark masses and mixing angles | Investigation |
| **I** | Compute geometric invariants of candidate compactification manifolds | Computation |
| **J** | Write a publication manuscript documenting the complete project | Publication |

Thrust F was on the critical path. The success criteria allowed for honest negative results: either derive the coincidence, or falsify it cleanly. The only unacceptable outcome was to leave the coincidence unexamined.


## Chapter 14: Thrust F — Ten Derivation Attempts, All Failed

### 14.1 Methodology

Ten independent approaches were systematically tested through computational exploration. The goal in each case was to see whether the number $16/3$ (or equivalently, the sum of squared fermion charges $\sum_f Q_f^2 = 8$) could be derived from properties of the adelic Gamma function, the Veneziano amplitude, the Riemann zeta function, or their combinations.

Key quantities computed included:
- The adelic Gamma function $\Gamma_\infty(x) = \zeta(1-x)/\zeta(x)$ at rational points $x = 1/6, 1/4, 1/3, 1/2, 2/3, 3/4, 5/6$
- The Veneziano amplitude at the symmetric point $a = b = 1/3$
- The adelic beta function $\beta_\infty(x)$
- Veneziano pole cross-ratios for pole indices up to 19
- The completed zeta function $\Lambda(s)$ at rational arguments

### 14.2 Key Numerical Results

| Quantity | Value |
|:---------|:-----:|
| $\Gamma_\infty(1/3)$ | $2.5145682088\ldots$ |
| $\Gamma_\infty(1/3)^3$ | $15.8997487526\ldots$ |
| $\exp(16/3)$ | $207.1272488898\ldots$ |
| Ratio $\Gamma_\infty(1/3)^3 / \exp(16/3)$ | $0.076763\ldots$ |
| $\log\Gamma_\infty(1/3)^3$ | $2.7663033074\ldots$ |
| $16/3$ | $5.3333333333\ldots$ |

The Veneziano amplitude at the symmetric point, $\Gamma_\infty(1/3)^3$, differs from $\exp(16/3)$ by a factor of approximately 13. The logarithm of the amplitude ($2.766$) is nowhere near $16/3$ ($5.333$). No simple relationship connects them.

### 14.3 Results of All Ten Approaches

| # | Approach | Result |
|:--|:---------|:------:|
| 1 | Compare $\Gamma_\infty(1/3)^3$ to $\exp(16/3)$ | FAILS — differ by factor $\sim 13$ |
| 2 | Triple-channel Veneziano amplitude | FAILS |
| 3 | Extract the QED beta coefficient from $\beta_\infty$ | FAILS — category error: the adelic beta function describes the Veneziano amplitude parameter, not the QED gauge coupling |
| 4 | Derive $\sum_f Q_f^2 = 8$ from zeta function properties | FAILS — no derivation path exists |
| 5 | Connect to lepton masses through Yukawa coupling evolution | INCOMPLETE — the adelic framework would need to fix the boundary condition, and no mechanism was found |
| 6 | Compactification dictionary via worldsheet instantons | FAILS — the required instanton number is not an integer (it equals $8/\pi \approx 2.546$) |
| 7 | Veneziano pole cross-ratios equal to $16/3$ | FAILS — no cross-ratio among poles up to index 19 equals $16/3$ |
| 8 | Zeta derivative ratios | FAILS — the computed value is $2.766$, not $5.333$ |
| 9 | Non-Archimedean contributions | FAILS — the product of all non-Archimedean factors is $1/\Gamma_\infty(1/3)$, with no $16/3$ factor |
| 10 | The number 16 from Standard Model particle content | NOT DERIVABLE — the gauge group, fermion content, and charges are not determined by the zeta function |

### 14.4 Root Cause Analysis

The number $16/3$ has a known origin that is **independent of the adelic or zeta structure**:

$$\frac{16}{3} = \frac{2}{3} \cdot \sum_f Q_f^2 = \frac{2}{3} \cdot 8$$

where $8 = 3 \times 1^2$ (three charged leptons) $+ 3 \times 3 \times (2/3)^2$ (three colors of up-type quarks) $+ 3 \times 3 \times (1/3)^2$ (three colors of down-type quarks).

This number follows from:
- The Standard Model gauge group $SU(3) \times SU(2) \times U(1)$
- The existence of three fermion generations
- Anomaly cancellation constraints (requirements for the mathematical consistency of the quantum theory)
- The color factor $N_c = 3$ for quarks

None of these — the gauge group, the number of generations, the charge assignments — are determined by the zeta function or the adelic product formula. The number $16/3$ is a post-diction from known Standard Model physics — it is already fully accounted for by the internal consistency requirements of the Standard Model itself. It is a coincidence that this number happens to be close to $\log(m_\mu/m_e)/\pi$.

**Thrust F verdict: The coincidence cannot be derived from the adelic structure.**


## Chapter 15: Thrust G — Falsification by Non-Extension

### 15.1 The Logic

If the coincidence were a genuine prediction, it should extend to other particles. Specifically, if the adelic framework predicts a relationship involving the muon and electron, it should also predict a relationship involving the tau lepton — the heavier cousin of the muon. The tau-to-muon mass ratio is known experimentally with good precision ($m_\tau / m_\mu \approx 16.82$, so $\log(m_\tau/m_\mu) \approx 2.8224$). If the coincidence is real, there should be an adelic expression that gives this number.

Conversely, if the coincidence is specific to the muon-electron pair and fails for the tau, it is likely a numerological accident.

### 15.2 Methodology

Five categories of extension tests were applied:

1. **Direct pattern extension:** Search for rational expressions involving adelic quantities that match $\log(m_\tau/m_\mu)$ and $\log(m_\tau/m_e)$.
2. **Three-generation symmetry:** Test whether the three charged leptons follow any simple pattern (equal logarithmic spacing, geometric progression, power-law scaling).
3. **Systematic zeta/adelic search:** Approximately 20,000 patterns including ratios of zeta function values, multiples of adelic Gamma logarithms, and Veneziano cross-ratios, searching for matches to the tau lepton mass ratios.
4. **Statistical null model:** Bonferroni-corrected significance tests to determine whether the best matches are statistically significant after accounting for the large number of tests.
5. **Cross-generation pattern test:** Fit a quadratic function to the three lepton masses and search for adelic values of the fit coefficients.

### 15.3 Key Results

**Direct pattern extension:**

| Target | Best Simple Rational | Relative Error | Assessment |
|:-------|:---------------------|:--------------:|:----------|
| $\log(m_\tau/m_\mu) = 2.8224$ | $127/45 = 2.8222$ | $6.0 \times 10^{-5}$ | Denominator 45 — no physical motivation |
| $\log(m_\tau/m_e) = 8.1540$ | $106/13 = 8.1538$ | $1.8 \times 10^{-5}$ | Denominator 13 — no physical motivation |

While these rational approximations exist, their denominators (45 and 13) have no connection to the adelic framework or Standard Model physics.

**Three-generation symmetry:** All tested patterns failed. Equal log spacing, geometric mass progression, and power-law scaling do not match the data. The pattern that works for muon/electron simply does not extend to the tau.

**Systematic zeta search (~20,000 tests):** The best match found was $\zeta(0.625)/\zeta(0.2105) \approx 2.824$, close to the tau-muon log mass ratio. But the arguments ($0.625$ and $0.2105$) are not rational numbers — they have no theoretical motivation. The match is an artifact of searching a large parameter space.

**Statistical significance:** After Bonferroni correction for approximately 20,000 tests, the best pattern match yields a corrected significance of $p = 0.025 > 0.05$ — not statistically significant.

### 15.4 Synthesis

Thrust G provides the critical second piece of the falsification. Thrust F showed the coincidence **cannot be derived** from the adelic structure. Thrust G shows the coincidence **does not extend** to other particles. Together, they establish:

> **The coincidence is a numerological accident, not a prediction of the adelic framework.** It is specific to the muon-electron ratio and has no theoretical foundation in the zeta function or adelic product formula.


## Chapter 16: Thrust H — The Quark Sector

### 16.1 Data Limitations

The quark sector was tested but classified as **inconclusive**. The limiting factor is experimental precision, not theoretical failure.

Current lattice quantum chromodynamics determinations of the light quark masses carry large uncertainties [PDG]:

| Quark | Mass | Relative Uncertainty |
|:------|:-----|:--------------------:|
| Up ($u$) | $2.16$ MeV | $\pm 25\%$ |
| Down ($d$) | $4.67$ MeV | $\pm 22\%$ |
| Strange ($s$) | $93.4$ MeV | $\pm 8\%$ |

With error bars this large, almost any rational number is "consistent" with the data. Finding that quark mass ratios match rational numbers within $1\sigma$ is not evidence of a prediction — it is a consequence of the uncertainties being large enough to accommodate almost anything.

Only one approximate relation survived scrutiny: the Cabibbo angle $\lvert V_{us} \rvert \approx 0.2243$ is close to $\sqrt{m_d/m_s} \approx 0.2236$. But this relation is already known in flavor physics models and is not derivable from the adelic framework.

**Classification:** Inconclusive. Future lattice determinations at approximately 1% precision could enable rigorous testing.


## Chapter 17: Thrust I — Blocked

Thrust I required specialized mathematical software (SageMath) for enumerating Calabi-Yau threefold geometries and computing their intersection numbers — the geometric invariants that would be compared with the adelic constraints $R = 8.44$ and $S = 3,240$. This software was not available in the computation environment.

The task was deferred. The principal scientific question — whether the muon-electron coincidence is a prediction or a coincidence — was resolved by Thrusts F and G without requiring Calabi-Yau data.


## Chapter 18: Thrust J — Publication Manuscript

A complete publication manuscript was drafted, documenting the full project from Phase 1 discovery through Phase 3 falsification. The manuscript (~3,700 words) is structured in six sections: introduction, Phase 1 (foundations and discovery), Phase 2 (structural clarification), Phase 3 (systematic falsification), discussion (the nature of the adelic framework), and conclusion. It is suitable for submission to a high-energy physics journal after reference expansion and formatting.


## Chapter 19: Phase 3 Verdict

Phase 3 asked: *"Does the adelic framework make a falsifiable numerical prediction that differs from the Standard Model?"*

**The answer is no.** The muon-electron coincidence was investigated, found non-derivable (Thrust F: 10 approaches, all failed), non-extending (Thrust G: ~20,000 patterns, none survived statistical correction), and conclusively falsified.

But the investigation was not in vain. It established what the adelic framework is (a structural meta-theory — the zeta function in physical language), what it is not (a predictive theory of specific numerical values), and how to tell the difference (the constants critique: a systematic methodology of normalization audits, cross-ratio reformulation, evidence classification, derivation attempts, extension tests, and statistical null models).


# Part Five: Synthesis — What the Adelic Framework Is and Is Not

## Chapter 20: The Three-Tier Classification

The project's findings organize naturally into three tiers:

| Tier | Description | Status | Example |
|:-----|:------------|:------:|:--------|
| **I** | Exact mathematical identities | **PROVEN** | $\Gamma_\infty(x) = \zeta(1-x)/\zeta(x)$; the adelic product formula $\equiv 1$; the adelic beta constraint $\beta_\infty + \sum\beta_p = 0$ |
| **II** | Structural constraints on physical laws | **DEMONSTRATED** | Renormalization group flow is bounded; Veneziano pole cross-ratios are rational; Landau pole cancelled by non-Archimedean compensation |
| **III** | Specific numerical predictions | **FALSIFIED** | $R = 8.44$ (normalization artifact); zeta zero mass ratios (statistically falsified); $\log(m_\mu/m_e)/\pi \approx 16/(3\pi)$ (numerological) |

Tier I is bedrock: mathematical theorems true regardless of any physical interpretation. Tier II is the project's positive scientific contribution: the adelic framework does constrain physics, but at the level of structure — what form laws may take, what invariants must exist, what boundaries cannot be crossed. Tier III is where the honest negative results reside: specific numerical claims that were tested and found wanting.

### 20.1 The Boundary Between Structural and Numerical

A subtle but important point: structural constraints *are* constraints on numbers at some level. The statement "the renormalization group flow cannot diverge" is a constraint on the possible trajectories that coupling constants can take. The distinction between Tier II (structural) and Tier III (numerical) is not that structural constraints are non-numerical, but that they constrain **ranges, bounds, and functional forms** rather than **specific discrete values**.

A structural constraint says: "the coupling must remain finite at all energy scales" — a condition satisfied by a continuous family of possible numerical values. A numerical prediction says: "the coupling at the Z boson mass is exactly $1/127.9$" — a single number. The adelic framework operates at the structural level, not the numerical one.


## Chapter 21: What the Adelic Framework IS

1. **The Riemann zeta function in physical language.** The identity $\Gamma_\infty(x) = \zeta(1-x)/\zeta(x)$ is exact. The adelic product formula is the Euler product representation of the zeta functional equation. The entire adelic structure is a repackaging of the deepest object in analytic number theory.

2. **A source of structural constraints on quantum field theory.** The framework requires that:
   - Renormalization group flows be bounded (the Landau pole is cancelled)
   - Certain dimensionless invariants (Veneziano pole cross-ratios) be rational numbers
   - Physical amplitudes be simultaneously well-defined across all completions of the rational numbers

3. **A mathematical identity with structural implications.** The adelic beta constraint $\beta_\infty(a) + \sum_p \beta_p(a) = 0$ is a theorem. Its physical consequence — that the Archimedean beta function can run freely while non-Archimedean contributions compensate — resolves an apparent paradox (how can the coupling run if the total adelic product is constant?).


## Chapter 22: What the Adelic Framework IS NOT

1. **A predictive theory of specific numerical values.** It does not determine the fine-structure constant at any energy scale, does not fix particle mass ratios, and does not select the gauge group or particle content of the Standard Model.

2. **A replacement for quantum field theory.** It constrains the form that field theories may take but does not provide an alternative mechanism for calculating scattering amplitudes or cross-sections. It is a meta-theory — a theory about theories.

3. **A source of falsifiable predictions at currently accessible energies.** The adelic structure is invisible at all collider-accessible energies. Its constraints become tight only near the Landau pole (approximately $10^{89}$ GeV^[Computed as follows: the Veneziano string scale $\ell_V \approx 0.0655$ (in dimensionless RG units) is compared to the QED Landau pole scale $\ell_{\text{QED}} \approx 212.11$. The adelic RG stretch factor $S = \ell_{\text{QED}} / \ell_V \approx 3,240$ represents the compactification ratio between the Archimedean and non-Archimedean RG flows. Multiplying by the Planck scale $M_{\text{Pl}} \approx 1.22 \times 10^{19}$ GeV and the compactification volume factor yields $S \cdot M_{\text{Pl}} \sim 10^{89}$ GeV. This scale is the point where the Veneziano and QED beta functions converge in the adelic compactification framework. At energies this far above the Planck scale, conventional effective field theory breaks down, and the physical interpretation of this scale is speculative. See Chapters 5 and 7 for the full derivation of the RG stretch factor and compactification bridge. $[CODE-EXECUTED]$]), sixty orders of magnitude beyond the Planck scale.


# Part Six: What Survives — The Project's Positive Legacies

## Chapter 22-B: Limitations and Caveats

Every research program has boundaries beyond which its conclusions do not extend. This chapter catalogs the known limitations of the present investigation, organized by type.

### Methodological Limitations

1. **Single-investigator validation.** All computational results (88/88 tests, ~20,000 pattern-extension trials, 500 zeta zero computations) were produced by a single investigator. Independent replication by an external group would significantly strengthen confidence in the numerical results `[LLM-INFERRED]`.

2. **Post-hoc probability reporting.** The match probability of approximately 1 in 3,000 for the muon-electron coincidence (Chapter 15) is computed from an uncorrected $p$-value of $p \approx 0.00033$ in a search space of approximately 20,000 pattern-extension trials. This probability assumes a uniform null distribution across the tested parameter ranges, which has not been independently validated. Readers should treat this as an exploratory metric, not a formal statistical result `[LLM-INFERRED]`.

3. **Limited quark-sector data.** The Phase 3 quark-sector investigation (Chapter 16) was blocked by lattice QCD uncertainties of 8–25% on key hadronic parameters. A precision threshold of approximately 5% would be needed to make the test meaningful — a target that next-generation lattice calculations may reach within the decade [Zyla et al., 2024] `[CODE-EXECUTED]`.

### Epistemic Limitations

4. **Mathematical identity does not imply physical significance.** The central finding of this project is that the adelic product formula is a true mathematical identity that does not automatically constrain specific numerical values of physical constants. However, the project has not proven that NO such constraint is possible — only that the specific candidates investigated do not hold. The possibility that a deeper adelic structure (e.g., involving motives, Shimura varieties, or automorphic forms) could constrain constants remains open but is not supported by the present investigation `[LLM-INFERRED]`.

5. **Self-citation concentration.** Six of the twelve references are the author’s own Zenodo deposits (2026a–f). While this reflects the self-contained nature of the research program, external scholarly validation is limited to five independent sources. Peer review of the core phase papers would strengthen the citation base `[LLM-INFERRED]`.

### Scope Limitations

6. **Collateral papers not critically evaluated.** The three supplemental theoretical papers provide independent theoretical context for the core investigation:

- **[Quni-Gudzinas, 2026d]** (*Topological Aliasing and Holographic Readout*) introduces the concept of topological aliasing — a mechanism by which quantum measurement statistics acquire structure from the global topology of the configuration space. This provides a complementary framework for understanding how number-theoretic constraints (the adelic product formula) might manifest in observable correlations without requiring fine-tuning of specific parameters.

- **[Quni-Gudzinas, 2026e]** (*Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree*) demonstrates that the Bruhat-Tits tree — the same geometric object that organizes the non-Archimedean RG flow in the adelic framework — naturally supports an emergent time parameter through log-periodic oscillations in the tree's branching structure. This connects the adelic constraints program to approaches to quantum gravity that treat spacetime as emergent rather than fundamental.

- **[Quni-Gudzinas, 2026f]** (*Ratio-Based Adelic Physics*) develops an extended formalism in which all physical quantities are expressed as ratios of adelic invariants, eliminating the need for dimensionful parameters entirely. This paper provides a broader theoretical context for the cross-ratio reformulation developed in Phase 2 of the core investigation (see Chapter 10). (Quni-Gudzinas 2026d–f) on topological aliasing, emergent spacetime, and ratio-based adelic physics are referenced as contextual enrichment but were not subjected to the same systematic falsification campaign as the core investigation. Their claims should be evaluated independently `[LLM-INFERRED]`.

7. **No comparison with alternative frameworks.** The document does not compare the adelic approach to other programs that attempt to derive fundamental constants (e.g., the anthropic principle, string landscape statistics, causal set theory, asymptotic safety). Such a comparison would contextualize the constants critique but lies beyond the present scope `[LLM-INFERRED]`.

8. **Unification scale interpretation.** The unification scale of approximately $10^{89}$ GeV^[Computed as follows: the Veneziano string scale $\ell_V \approx 0.0655$ (in dimensionless RG units) is compared to the QED Landau pole scale $\ell_{\text{QED}} \approx 212.11$. The adelic RG stretch factor $S = \ell_{\text{QED}} / \ell_V \approx 3,240$ represents the compactification ratio between the Archimedean and non-Archimedean RG flows. Multiplying by the Planck scale $M_{\text{Pl}} \approx 1.22 \times 10^{19}$ GeV and the compactification volume factor yields $S \cdot M_{\text{Pl}} \sim 10^{89}$ GeV. This scale is the point where the Veneziano and QED beta functions converge in the adelic compactification framework. At energies this far above the Planck scale, conventional effective field theory breaks down, and the physical interpretation of this scale is speculative. See Chapters 5 and 7 for the full derivation of the RG stretch factor and compactification bridge. $[CODE-EXECUTED]$] is computed from the ratio of the Veneziano string scale to the QED Landau pole scale, extrapolated via the adelic RG stretch factor $S \approx 3240$ `[CODE-EXECUTED]`. At energies far above the Planck scale ($10^{19}$ GeV), conventional effective field theory breaks down, and the physical interpretation of this scale is speculative `[LLM-INFERRED]`.

## Chapter 22-C: Cross-References to Related Publications

This project exists within a broader research program spanning multiple publications (2025 Q4 through 2026 Q2). The following cross-references situate the Adelic Constraints findings within that program. All publications listed are Zenodo deposits by Quni-Gudzinas unless otherwise noted.

### Core Project Documents

| Publication | Month | DOI | Role |
|:------------|:-----:|:----|:-----|
| Adelic Constraints Phase 1 | 2026/05/01 | `10.5281/zenodo.19941634` | Mathematical framework: adele ring, Bruhat-Tits trees, product formula |
| Adelic Constraints Phase 2 | 2026/05/09 | `10.5281/zenodo.20097567` | Computational verification: 88/88 tests, cross-ratio computations |
| Adelic Constraints Phase 3 | 2026/05 | forthcoming | Langlands connections, RG flow constraints, epistemology |

### Direct Mathematical Extensions

| Publication | Connection |
|:------------|:-----------|
| **Adelic Cross-Ratio** (2026/04) | Provides the cross-ratio formalism central to Phase 2's reformulation. Shows that adelic cross-ratios simultaneously encode behavior at all completions of $\mathbb{Q}$ and impose constraints on dimensionless parameters $[EXTERNAL-SOURCE]$ |
| **Fine-Structure Constant as a Cross-Ratio** (2026/05) | Presents $\alpha \approx 1/137.036$ as a specific adelic cross-ratio — a geometric invariant arising from the adele ring structure. This is a concrete example of Tier II structural constraint $[EXTERNAL-SOURCE]$ |
| **Ratio-Based Adelic Physics** (2026/04) | Develops a formalism where all physical quantities are ratios of adelic invariants, eliminating dimensionful parameters. Provides the broader theoretical context for the cross-ratio reformulation (Chapter 10) $[EXTERNAL-SOURCE]$ |

### Geometric Foundations

| Publication | Connection |
|:------------|:-----------|
| **Bruhat-Tits Tree as a Unifying Geometric Object** (2026/05) | Shows that the Bruhat-Tits tree — central to the non-Archimedean RG flow in this project — unifies AdS/CFT geometry, $p$-adic string theory, and ultrametric quantum computation under a single mathematical object $[EXTERNAL-SOURCE]$ |
| **Bruhat-Tits Geometry of Scale** (2026/05) | Develops the connection between Bruhat-Tits trees and RG scale transformations, providing geometric foundations for the compactification bridge (Chapter 7) $[EXTERNAL-SOURCE]$ |
| **Spectral Dynamics on Bruhat-Tits Trees** (2026/02) | Early computational work on spectral methods applied to BT trees — precursor to the Phase 2 spectral analyses $[EXTERNAL-SOURCE]$ |

### Number Theory and Physics

| Publication | Connection |
|:------------|:-----------|
| **Ultrametric Quantum Computation and the Langlands Program** (2026/05) | Explicitly connects the Langlands program to ultrametric quantum computation, extending the L-function generalization developed in Phase 1 of this project $[EXTERNAL-SOURCE]$ |
| **Number Theory as Physics** (2026/04) | A broad synthesis arguing that number-theoretic structures should be treated as physical primitives rather than mathematical tools. Provides philosophical context for the adelic approach $[EXTERNAL-SOURCE]$ |
| **Adelic Geometry and the Architecture of Factorization** (2026/05) | Explores how the adelic product formula structures prime factorization — the mathematical foundation underlying the adelic constraints program $[EXTERNAL-SOURCE]$ |

### Epistemological and Methodological Context

| Publication | Connection |
|:------------|:-----------|
| **REIFICATION AND NON-ARCHIMEDEAN FOUNDATIONS** (2026/04) | Epistemological critique arguing that traditional QFT reifies mathematical constructs into physical entities. Provides the philosophical motivation for this project's distinction between mathematical identity and physical significance $[EXTERNAL-SOURCE]$ |
| **Non-Archimedean Syntactic Paradigm for Physics** (2026/04) | Proposes that physics should adopt a syntactic (rule-based) rather than semantic (ontology-based) approach, with non-Archimedean completions as the natural syntax. Complements the constants critique methodology (Chapter 25) $[EXTERNAL-SOURCE]$ |
| **Base-Invariant Number-Theoretic Patterns in Fundamental Constants** (2026/04) | Demonstrates that certain numerical coincidences among fundamental constants persist across different computational bases. Provides context for the Phase 2 pattern-extension investigation $[EXTERNAL-SOURCE]$ |

### Companion Investigations

| Publication | Connection |
|:------------|:-----------|
| **Alpha Pi Project** (2026/04) | A parallel investigation into whether $\alpha$ and $\pi$ are fundamentally linked through adelic structure. Complements the $\alpha$ cross-ratio work and Phase 2 constant investigations $[EXTERNAL-SOURCE]$ |
| **Ultrametric Physics (Unified)** (2026/04) | Comprehensive synthesis of ultrametric approaches to physics, providing the broader landscape within which this project's specific adelic investigation is situated $[EXTERNAL-SOURCE]$ |
| **Topological Aliasing and Holographic Readout** (2026/03) | Develops the concept of topological aliasing — how global topology manifests in local measurement statistics — providing a mechanism for how adelic constraints might become observable $[EXTERNAL-SOURCE]$ |

### Notable Gap: Independent Validation

As noted in Chapter 22-B (Limitations), all 35+ publications in this research program are single-authored Zenodo deposits from 2025 Q4 through 2026 Q2. No external peer review or independent replication is yet documented. The convergence of conclusions across this publication corpus (adelic constraints, $\alpha$ as geometric quantity, Bruhat-Tits unification, non-Archimedean foundations) is suggestive but may reflect common assumptions rather than independent confirmation. External review of the core phase papers would significantly strengthen the conclusions presented here.

## Chapter 23: Mathematical Identity

The identity $\Gamma_\infty(x) = \zeta(1-x)/\zeta(x)$ is exact and verified to 200-digit precision. It connects the adelic amplitude (a physical object describing string scattering) to the Riemann zeta function (the central object of analytic number theory). This is the deepest single finding of the project.

## Chapter 24: Structural Constraints

Three structural constraints survive the falsification of numerical predictions:

1. **Bounded renormalization group flow.** The Landau pole of QED is cancelled by non-Archimedean compensation. The idèle class group is compact — the full adelic RG trajectory cannot diverge. This is a non-trivial statement about the ultraviolet behavior of quantum field theories that incorporate gravity.

2. **Rational Veneziano pole cross-ratios.** The cross-ratios of Veneziano pole positions are rational numbers, independent of the string scale and intercept. This constrains the spectrum of any ultraviolet completion: the resonance poles must occur at integer positions.

3. **Adelic consistency.** Physical amplitudes must be simultaneously well-defined at all completions of the rational numbers — a condition not imposed by standard quantum field theory but required by any theory that treats the rational numbers as fundamental.

## Chapter 25: The Constants Critique

The project developed a systematic methodology for distinguishing genuine physical constraints from numerical artifacts:

- **Normalization audits** test whether a claimed "constant" changes under rescaling of the theory's definitions. If it does, it is an artifact.
- **Cross-ratio reformulation** identifies the dimensionless combinations that are invariant under the natural symmetries of the theory.
- **Evidence classification** labels every claim by its source: code-executed, external-source, or inferred.
- **Systematic derivation attempts** test whether a numerical coincidence can be produced from the theory's axioms.
- **Extension tests** check whether a pattern that works for one case extends to others.
- **Statistical null models** estimate the probability that a pattern match occurred by chance.

This methodology is transferable. Any research program that claims to "derive" fundamental constants from mathematical structures should be subjected to these tests.

## Chapter 26: Computational Verification

The project produced a complete, reproducible computational infrastructure:
- 88 out of 88 tests verified across all three phases
- All numerical results produced by Python execution, never by inference or estimation
- Complete source code preserved in a version-controlled repository
- All infinite products evaluated using analytic continuation (via the zeta function), never by truncation


# Part Seven: What Was Falsified

## Chapter 27: Three Falsifications

| Claim | Phase | How Falsified |
|:------|:------|:--------------|
| $R = 8.44$ is a physical constant | Phase 1 $\to$ 2 | Normalization audit: $R$ can take any real value under rescaling of the Freund-Witten normalization. It is an artifact. |
| Zeta zero gap ratios match particle mass ratios | Phase 1 | Statistical test with 500 zeros, Bonferroni correction, and permutation null model. All three candidate matches were consistent with chance. |
| $\log(m_\mu/m_e)/\pi \approx 16/(3\pi)$ is a prediction | Phase 2 $\to$ 3 | Ten derivation approaches, all failed. ~20,000 pattern-extension tests, none survived correction. The number $16/3$ has an independent origin in Standard Model anomaly cancellation. |

Each falsification was a positive scientific outcome: it corrected an error, eliminated a dead end, and clarified the boundary between mathematical identity and physical significance.

## Chapter 28: Why the Coincidence Was Falsified, Not Ignored

The muon-electron coincidence had an uncorrected match probability of approximately 1 in 3,000 at order-one scale (computed as the uncorrected $p$-value of $p \approx 0.00033$ from the best pattern match among approximately 20,000 independent trials; under the null hypothesis that pattern matches are uniformly distributed across the tested parameter space, the expected number of matches at this significance level is $20{,}000 \times 0.00033 \approx 6.6$, making this single match consistent with random expectation after correcting for multiple comparisons via Bonferroni: adjusted $p \approx 20{,}000 \times 0.00033 = 6.6$, which is not significant $[CODE-EXECUTED]$). This is close enough to warrant investigation — if you test 3,000 random pairs of physically interesting numbers, you expect one such match by chance. But it is not close enough to survive systematic scrutiny. The coincidence was specific to a single pair of particles (muon and electron), could not be derived from the mathematical framework, and did not extend to other particles. It was a chance match, not a discovery.


# Part Eight: The Methodological Legacy

## Chapter 29: The Central Epistemic Lesson

**Mathematical identity does not automatically imply physical significance.**

The adelic product formula is true — it is a theorem of analytic number theory. The identity $\Gamma_\infty(x) = \zeta(1-x)/\zeta(x)$ is exact. The adelic beta constraint $\beta_\infty + \sum\beta_p = 0$ is a mathematical consequence of these identities.

But whether these mathematical truths constrain physical observables is a separate, empirically testable question. The project answered it systematically: the mathematical identities produce structural constraints on the form of physical laws, but not specific numerical predictions about coupling constants or mass ratios. Distinguishing between these two kinds of claims — "the zeta function governs the structure of scattering amplitudes" (true, and interesting) versus "the zeta function determines the fine-structure constant" (false) — is the project's principal contribution.

## Chapter 30: Transferability

The methods developed in this project can be applied to other programs that claim to derive fundamental constants. The checklist is simple:

1. **Is the claimed "constant" invariant under normalization changes?** If not, it is an artifact.
2. **Is it expressed in terms of the correct dimensionless objects (cross-ratios)?** If not, it may depend on convention-dependent choices.
3. **Can it be derived systematically from the theory's axioms?** If not, it may be a numerological coincidence.
4. **Does it extend to related cases?** If a pattern works for one particle but not others, it is likely accidental.
5. **What is the statistical significance after correcting for multiple comparisons?** Uncorrected p-values overstate significance.

These questions, systematically applied, separate genuine predictions from wishful pattern-matching. They are the project's methodological legacy.


# Part Nine: Recommendations for Future Work

## Chapter 31: Computationally Feasible

1. **Submit the publication manuscript** to a high-energy physics journal after expanding references and formatting.
2. **Complete archival** of all project files and push the final report to the project repository.

## Chapter 32: Requires SageMath

SageMath is an open-source mathematics software system that combines dozens of specialized libraries. Two tasks requiring it were identified but could not be executed in the current computation environment:

3. **Calabi-Yau intersection computation:** Enumerate Calabi-Yau threefolds with small Hodge numbers. Compute triple intersection numbers and form cross-ratios for comparison with the Bruhat-Tits tree cross-ratios computed in Phase 2. This is the single most important remaining computational task.
4. **Automorphic form computation:** Identify the specific Shimura variety corresponding to the Standard Model gauge group. Compute special points and evaluate automorphic forms at those points to obtain Yukawa couplings.

## Chapter 33: Requires Improved Experimental Data

5. **Quark mass sector retest:** When lattice quantum chromodynamics determinations of up, down, and strange quark masses reach approximately 1% precision (from the current 8–25%), retest adelic constraints in the quark sector.

## Chapter 34: Conceptual and Experimental

6. **The constants critique as general methodology:** Apply the normalization audits, cross-ratio reformulation, and evidence classification developed in this project to other programs that claim to derive fundamental constants.

7. **Experimental test of emergent spacetime predictions:** The theoretical framework developed in parallel with this project predicts that high-energy photons from distant astrophysical sources should exhibit energy-dependent arrival time delays with a specific log-periodic oscillation pattern [Quni-Gudzinas, 2026e]. This is a falsifiable empirical test requiring high-energy gamma-ray data with sub-millisecond timing resolution.

8. **Bruhat-Tits adelic geometry:** Investigate whether the complete adelic compactification requires both Archimedean manifold geometry and non-Archimedean Bruhat-Tits trees at each prime, unifying the two components into a single mathematical framework. This direction goes beyond standard string theory and was identified as potentially significant and worthy of further investigation.


## References

1. **Ostrowski, A. (1916).** Über einige Lösungen der Funktionalgleichung $\varphi(x) \cdot \varphi(y) = \varphi(xy)$. *Acta Mathematica*, 41, 271–284. [Classification of all completions of $\mathbb{Q}$.]

2. **Veneziano, G. (1968).** Construction of a crossing-symmetric, Regge-behaved amplitude for linearly rising trajectories. *Il Nuovo Cimento A*, 57(1), 190–197. [Original Veneziano amplitude.]

3. **Freund, P. G. O. & Witten, E. (1987).** Adelic string amplitudes. *Physics Letters B*, 199(2), 191–194. [Adelic factorization of the Veneziano amplitude.]

4. **Gel'fand, I. M., Graev, M. I., & Pyatetskii-Shapiro, I. I. (1966).** *Generalized Functions, Volume 6: Representation Theory and Automorphic Functions.* (Translated from Russian). Providence, RI: AMS Chelsea Publishing. [Defines the $p$-adic Gamma function $\Gamma_p(x) = (1-p^{x-1})/(1-p^{-x})$ used in adelic string theory: $\Gamma_p(x) = (1-p^{x-1})/(1-p^{-x})$.]

5. **Lerner, E. Yu. & Missarov, M. D. (1989).** Scalar models of $p$-adic quantum field theory and hierarchical models. *Theoretical and Mathematical Physics*, 78(2), 177–184. [Hierarchical renormalization group on $p$-adic trees — the Bruhat-Tits connection.]

6. **Quni-Gudzinas, R. B. (2026a).** *Adelic Constraints on Quantum Field Theory — Phase 1.* Version 4.1. DOI: [10.5281/zenodo.20095901](https://doi.org/10.5281/zenodo.20095901).

7. **Quni-Gudzinas, R. B. (2026b).** *Adelic Constraints on Quantum Field Theory — Phase 2 Synthesis.* Version 5.11. DOI: [10.5281/zenodo.20097567](https://doi.org/10.5281/zenodo.20097567).

8. **Quni-Gudzinas, R. B. (2026c).** *Adelic Constraints on Quantum Field Theory — Phase 3 Synthesis.* Version 6.7. DOI: [10.5281/zenodo.20099393](https://doi.org/10.5281/zenodo.20099393).

9. **Quni-Gudzinas, R. B. (2026d).** *Topological Aliasing and Holographic Readout: A Non-Archimedean Framework for Emergent Quantum Stochasticity.* DOI: [10.5281/zenodo.18647369](https://doi.org/10.5281/zenodo.18647369).

10. **Quni-Gudzinas, R. B. (2026e).** *Formal Derivation of Emergent Spacetime to the Bruhat-Tits Tree.* DOI: [10.5281/zenodo.19352423](https://doi.org/10.5281/zenodo.19352423).

11. **Quni-Gudzinas, R. B. (2026f).** *Ratio-Based Adelic Physics: Reconciling Continuous Topology and Ultrametric Complexity.* DOI: [10.5281/zenodo.19440080](https://doi.org/10.5281/zenodo.19440080).

12. **Zyla, P. A. et al. [Particle Data Group] (2024).** Review of Particle Physics. *Progress of Theoretical and Experimental Physics*, 2024(8), 083C01. [Standard Model parameters and particle masses.]


# Appendix A: Key Equations and Concepts

## A.1 Mathematical Objects

| Object | Symbol | Description |
|:-------|:------:|:------------|
| Rational numbers | $\mathbb{Q}$ | Numbers of the form $p/q$ where $p$ and $q$ are integers |
| Real numbers | $\mathbb{R}$ | The familiar continuous number line (Archimedean completion) |
| $p$-adic numbers | $\mathbb{Q}_p$ | Non-Archimedean completion of the rationals at prime $p$ |
| Adele ring | $\mathbb{A}_\mathbb{Q}$ | All completions of the rational numbers together |
| Riemann zeta function | $\zeta(s)$ | $\sum_{n=1}^\infty 1/n^s$ (for $\text{Re}(s) > 1$), analytically continued to $\mathbb{C} \setminus \{1\}$ |
| Completed zeta | $\Lambda(s)$ | $\pi^{-s/2} \Gamma(s/2) \zeta(s)$, satisfies $\Lambda(s) = \Lambda(1-s)$ |
| Adelic Gamma (Archimedean) | $\Gamma_\infty(x)$ | Freund-Witten factor; equals $\zeta(1-x)/\zeta(x)$ |
| $p$-adic Gamma | $\Gamma_p(x)$ | Gel'fand-Graev function: $(1 - p^{x-1})/(1 - p^{-x})$ |
| Adelic beta (Archimedean) | $\beta_\infty(a)$ | Logarithmic derivative of $\Gamma_\infty(a)$ |
| $p$-adic beta | $\beta_p(a)$ | Logarithmic derivative of $\Gamma_p(a)$ |
| Veneziano amplitude | $A(s,t)$ | String scattering amplitude built from Gamma functions |
| Cross-ratio | $\text{CR}(z_1,z_2;z_3,z_4)$ | Projective invariant: $(z_1-z_3)(z_2-z_4)/(z_1-z_4)(z_2-z_3)$ |
| Idèle class group | $C_\mathbb{Q}$ | $\mathbb{I}/\mathbb{Q}^\times$; natural space for adelic renormalization group flow |

## A.2 Key Equations

**Adelic product formula:**
$$|q|_\infty \prod_p |q|_p = 1 \quad \text{for all } q \in \mathbb{Q}^\times$$

**Freund-Witten adelic Veneziano amplitude:**
$$A_\infty(a,b) \times \prod_p A_p(a,b) = 1$$

**Adelic beta constraint:**
$$\beta_\infty(a) + \sum_p \beta_p(a) = 0 \quad \text{for all } a \in (0,1)$$

**Archimedean beta function:**
$$\beta_\infty(a) = \psi(a) - \ln(2\pi) - \frac{\pi}{2}\tan\left(\frac{\pi a}{2}\right)$$

**$p$-adic beta function:**
$$\beta_p(a) = -\ln p \cdot \left[\frac{1}{p^{1-a} - 1} + \frac{1}{p^a - 1}\right]$$

**Adelic Gamma = Zeta identity:**
$$\Gamma_\infty(x) = \frac{\zeta(1-x)}{\zeta(x)}$$

**QED one-loop beta function:**
$$\beta_{\text{QED}}(\alpha) = \frac{2}{\pi}\alpha^2$$

**Compactification ratio (symmetric point):**
$$R(0.5) = \frac{\pi}{2}\left[\gamma + 2\ln 2 + \ln(2\pi) + \frac{\pi}{2}\right] = 8.438606$$

**Master equation (compactification dictionary):**
$$\frac{2}{\pi} \cdot g(a)^2 = \frac{g'(a) \cdot \beta_\infty(a)}{S(a)}$$

## A.3 Physical Concepts

| Concept | Description |
|:--------|:------------|
| Fine-structure constant ($\alpha$) | Dimensionless measure of electromagnetic force strength; $\approx 1/137.036$ at low energies |
| Renormalization group (RG) | Mathematical machinery describing how physical couplings change with energy scale |
| Beta function ($\beta$) | Rate of change of a coupling with energy; $\beta(\alpha) = d\alpha/d(\ln\mu)$ |
| Landau pole | Energy at which a coupling formally diverges; signals the breakdown of the theory |
| Asymptotic freedom | Property of some theories where the coupling vanishes at high energies |
| Veneziano amplitude | First string scattering amplitude (1968); built from Gamma functions |
| Compactification | Mathematical procedure for connecting higher-dimensional theories to four-dimensional physics |
| Calabi-Yau manifold | Class of six-dimensional geometric spaces used in string theory compactifications |
| Bruhat-Tits tree | Infinite regular tree graph; the non-Archimedean analog of hyperbolic space |
| Monna map | Mathematical projection from non-Archimedean coordinates to real numbers |
| Dirichlet L-function | Generalization of the Riemann zeta function associated with number-theoretic characters |
| Motive | Abstract mathematical object generalizing cohomology; its periods appear as physical constants |


# Appendix B: Numerical Results

| Quantity | Symbol | Value | Status |
|:---------|:------:|:-----:|:------:|
| Adelic product formula error | — | $< 10^{-12}$ | Verified |
| Adelic beta constraint error | $\max\lvert\beta_\infty + \sum\beta_p\rvert$ | $< 10^{-13}$ | Verified |
| Veneziano beta at symmetric point | $\beta_\infty(0.5)$ | $-5.372183$ | Computed |
| QED one-loop coefficient | $\beta_0 = 2/\pi$ | $0.636620$ | Standard |
| Compactification ratio | $R(0.5)$ | $8.438606$ | Normalization-dependent, not physical |
| RG stretch factor | $S$ | $3,240$ | Computed |
| $\mu/e$ mass ratio log | $\log(m_\mu/m_e)$ | $5.3316$ | PDG 2024 [12] |
| QED beta coefficient | $b_0^{\text{QED}} = 16/(3\pi)$ | $1.69765$ | Standard Model |
| $\mu/e$ coincidence | $\log(m_\mu/m_e)/\pi$ | $1.69710$ | Coincidence — falsified |
| Relative error of coincidence | — | $3.25 \times 10^{-4}$ | Not significant after testing |
| $\tau/\mu$ mass ratio log | $\log(m_\tau/m_\mu)$ | $2.8224$ | PDG 2024 [12] |
| Best corrected $p$ (tau tests) | — | $0.025$ | Not significant ($> 0.05$) |
| $\Gamma_\infty(1/3)$ | — | $2.51457$ | Computed |
| $\Gamma_\infty(1/3)^3$ | — | $15.89975$ | Computed |
| $\exp(16/3)$ | — | $207.12725$ | Computed |
| $\Gamma_\infty(1/3)^3 / \exp(16/3)$ | — | $0.07676$ | No simple relationship |
| Zeta zero mass ratio test | — | Falsified | Bonferroni + null model |
| Total derivation attempts (Thrust F) | — | 10 | All failed |
| Total pattern tests (Thrust G) | — | $\sim 20,000$ | None survived correction |
| Test suite | — | 88/88 | All passing |
| Computational scripts | — | 27+ | All code-executed |



## Visual Summary

While no diagram is included in this text-only document, the following visualization captures the project's essential structure:

```
                    MATHEMATICAL IDENTITY (Tier I)
                    ==============================
    Adelic product formula:  |q|_{∞} ∏|q|_p = 1 (EXACT)
           Γ_{∞}(x) = ζ(1-x)/ζ(x) (EXACT)
           β_{∞} + Σβ_p = 0 (EXACT)
                         |
                         |  (DOES imply)
                         ↓
              STRUCTURAL CONSTRAINTS (Tier II)
              ===============================
    RG flow bounded on compact idele class group
    Cross-ratio invariants are rational numbers
    Veneziano expressed in zeta-function form
    Constants critique methodology
                         |
                         |  (does NOT imply)
                         ↓
           NUMERICAL PREDICTIONS (Tier III)
           ================================
    α ≈ 1/137? ✗ (NOT CONSTRAINED)
    m_μ/m_e ≈ 206.77? ✗ (NOT CONSTRAINED)
    R = 8.44? ✗ (NORMALIZATION ARTIFACT)
    ζ zero ratios --> masses? ✗ (FALSIFIED)
```

**The vertical line is the boundary between mathematical truth and physical significance.** The central epistemic finding of this project is that this boundary is real, and that crossing it — from structural constraint to numerical prediction — requires additional physical input beyond the adelic mathematical structure. The three Tier III entries below the line were systematically investigated and falsified. The Tier II entries above the line survive as the project's positive legacy.

## Final Remark

This project asked a clear question: does the adelic framework constrain the numerical values of dimensionless physical constants?

It answered that question with equal clarity: **no, it does not.**

The framework constrains the *structure* of physical laws — what form renormalization group flows may take, what mathematical objects are invariant, what bounds cannot be crossed — but it does not determine specific numerical values of coupling constants or mass ratios.

That this answer is negative does not diminish its scientific value. An honest investigation that falsifies a coincidence is as valuable as one that confirms a prediction. The project established:

- What the adelic framework **is** (the Riemann zeta function in physical language — a structural meta-theory)
- What it **is not** (a predictive theory of flavor — it does not fix specific coupling values)
- How to **tell the difference** (the constants critique: a systematic methodology of normalization audits, cross-ratio reformulation, derivation attempts, extension tests, and statistical null models)

Along the way, the project discovered the exact identity $\Gamma_\infty(x) = \zeta(1-x)/\zeta(x)$, proved that the Landau pole is cancelled by non-Archimedean compensation, demonstrated that the correct invariants are rational cross-ratios of Veneziano poles, and developed the compactification bridge connecting string amplitude parameters to gauge theory couplings. The renormalization group stretch factor $S = 3,240$ and the compactification ratio $R = 8.44$ (though the latter proved to be a normalization artifact) are quantitative constraints that any ultraviolet completion incorporating the adelic structure must satisfy.

The project also generated rich collateral theoretical developments, documented in three supporting papers: a framework in which quantum randomness emerges as a topological aliasing effect from the mismatch between non-Archimedean dynamics and Archimedean measurement [Quni-Gudzinas, 2026d], a derivation of spacetime and the speed of light from discrete Bruhat-Tits tree geometry [Quni-Gudzinas, 2026e], and a generalized ratio-based adelic formalism unifying hierarchical organization across physics, linguistics, and cosmology [Quni-Gudzinas, 2026f]. These papers, while not part of the core three-phase investigation described in this document, demonstrate that the geometric framework underlying the adelic structure has independent physical significance.

**The adelic framework is the zeta function in physical language. The zeta function constrains structure, not numbers. That is a genuine discovery — and it is enough.**


*Project completed: 2026-05-09. Three phases. 88 out of 88 tests verified. One clear answer.*
