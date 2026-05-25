---
title: "The Tree and Its Shadow: A Unified Phase Diagram of Ultrametric Organization and Resistance"
authors: "Rowan Brad Quni-Gudzinas"
date: "2026-05-23"
doi: "[10.5281/zenodo.20348370](https://doi.org/10.5281/zenodo.20348370)"
version: "1.0"
abstract: >
  Ultrametricity—the strong triangle condition, that for any three points the two largest distances are equal—is the mathematical signature of hierarchical branching. It appears wherever recursive distinction operates in isolation: in p-adic geometry, mean-field spin glasses, perturbative quantum field theory, clock-like phylogenetics, and core linguistic vocabulary. But isolation is rare. Most real systems resist tree organization through geometric embedding, lateral interaction, non-perturbative mixing, thermalization, or deliberate flat architecture. This paper catalogs the resistance mechanisms, maps the complete phase diagram from exact ultrametricity to pure chaos, and argues that the tree and its resistance form halves of a single generative logic. The tree is a conditional attractor—a limit approached only when isolation is nearly perfect. The resistance is the default. Five regimes, three dual operations, and four falsifiable predictions are proposed.
keywords: ["ultrametric", "strong triangle inequality", "hierarchical branching", "spin glasses", "phylogenetics", "renormalization group", "Zitterbewegung", "many-body localization", "small-world networks", "phase diagram", "resistance taxonomy"]
license: "CC-BY-4.0"
---

# The Tree and Its Shadow: A Unified Phase Diagram of Ultrametric Organization and Resistance

**Author:** [Rowan Brad Quni-Gudzinas](mailto://rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**DOI:** [10.5281/zenodo.20348370](https://doi.org/10.5281/zenodo.20348370)
**Date:** 2026-05-23

**Abstract:** Ultrametricity — the strong triangle condition, that for any three points the two largest distances are equal — is the mathematical signature of hierarchical branching. It appears wherever recursive distinction operates in isolation: in $p$-adic geometry, mean-field spin glasses, perturbative quantum field theory, clock-like phylogenetics, and core linguistic vocabulary. But isolation is rare. Most real systems resist tree organization through geometric embedding, lateral interaction, non-perturbative mixing, thermalization, or deliberate flat architecture. This paper catalogs the resistance mechanisms, maps the complete phase diagram from exact ultrametricity to pure chaos, and argues that the tree and its resistance form halves of a single generative logic. The tree is a conditional attractor — a limit approached only when isolation is nearly perfect. The resistance is the default. Five regimes, three dual operations, and four falsifiable predictions are proposed.

---

> ⚠️ **PROVENANCE NOTE.** This document proposes a unified framework for understanding where ultrametric organization appears and where it fails. The domain survey draws on published research (the author's prior corpus and standard scientific literature). The five-regime phase diagram, the three dual operations, and the falsifiable predictions are proposed — none have been empirically tested. The taxonomy of resistance mechanisms is a proposed classification, not an established one. Verify before citing.

---

## 1. Introduction

### 1.1 What Is Ultrametricity?

A metric $d$ on a set $X$ is ultrametric if, for any three points $x, y, z$, the two largest distances are equal:

$$d(x,z) = d(y,z) \geq d(x,y)$$

after reordering so that $d(x,y) \leq d(x,z) \leq d(y,z)$. This is the strong triangle condition — stronger than the ordinary triangle inequality $d(x,z) \leq d(x,y) + d(y,z)$. In an ultrametric space, every triangle is isosceles with a short base.

What kind of geometry satisfies this? Not Euclidean geometry. Pick any three points in $\mathbb{R}^3$ and the distances are almost never isosceles — and when they are, it's by accident, not by necessity. Ultrametricity requires a different kind of space: a rooted tree.

### 1.2 The Tree Connection

Consider a rooted tree — a branching structure with a single origin. Place items at the leaves. Define the distance between any two items as the depth of their lowest common ancestor — the point in the tree where their lineages diverged. This is called the cophenetic distance.

For any three leaves on a rooted tree, two will share a deeper common ancestor than either shares with the third. The two deeper siblings will be equally distant from the shallow sibling. Their cophenetic distances will satisfy the strong triangle condition — automatically, as a matter of geometry, not as an empirical discovery.

This is the central fact: **every rooted tree, when distance is measured as depth-to-common-ancestor, is ultrametric.** The tree and the strong triangle condition are equivalent. One implies the other.

### 1.3 The Generative Condition

When does a system organize as a rooted tree? When three conditions hold:

1. **Branching.** A process repeatedly splits one entity into sub-entities — "one becomes more." Recursive distinction generates a tree topology.

2. **Closure.** After splitting, sub-entities evolve independently. No lateral interaction, no cross-talk, no merging.

3. **Cophenetic distance.** The distance between two entities is measured as the number of operations (or time depth) since their common ancestor — not by an external metric like spatial separation.

When all three hold, edge-count distance on the resulting tree is automatically ultrametric. This is a theorem, not a hypothesis.

### 1.4 The Ubiquity Question

The ultrametric tree pattern has been identified across multiple scientific domains. It appears in:

- **$p$-adic geometry**, where the Bruhat-Tits tree is the canonical geometric realization of $\mathbb{Q}_p$ — every triangle is exactly isosceles by definition.
- **Mean-field spin glasses**, where Parisi's replica symmetry breaking solution revealed that the overlap matrix of pure states is organized as an ultrametric tree. Proven rigorously by Guerra (2003) and Talagrand (2006).
- **Perturbative quantum field theory**, where the renormalization group generates a tree of effective theories by integrating out short-wavelength degrees of freedom. Each effective theory is the "parent" of the finer-scale theories it coarse-grains over.
- **Clock-like phylogenetics**, where constant mutation rates produce cophenetic distances between species that satisfy the strong triangle condition. Core protein-coding genes often approximate a molecular clock.
- **Core linguistic vocabulary**, where the Swadesh list of basic words resists borrowing and preserves a tree-like signal of language descent.

But does this pattern represent a universal constraint on hierarchical systems, or is it an idealized limit approached only in special conditions? A comprehensive research program (Quni-Gudzinas, 2025–2026) has argued for the former — that ultrametricity is the signature of a deep generative logic operating across physics, biology, and cognition. This paper develops the complementary question: **where does the tree fail to form, and what do the failures reveal?**

---

## 2. Where the Tree Cannot Grow: A Taxonomy of Resistance

### 2.1 The Failure Modes

If the three generative conditions are sufficient for ultrametricity, then failure occurs when at least one condition is violated. The failure mode determines the category of resistance. Five broad categories emerge from a survey of systems across physics, biology, network science, and social organization:

| Category | What Fails | Signature | Example |
|:---------|:-----------|:----------|:--------|
| I. Geometric | Underlying space is non-tree | Equilateral triangles; all distances comparable | Euclidean space, small-world networks |
| II. Dynamical | Lateral interactions prevent closure | Cross-branch correlations; non-perturbative mixing | Many-body localization, strong-coupling QCD |
| III. Lateral Transfer | Information flows across branches | Phylogenetic networks; non-tree ancestry | Horizontal gene transfer, language contact |
| IV. Entropic | Noise or thermalization overwhelms hierarchy | Ergodicity; all states equally accessible | Thermal systems, turbulence, random matrices |
| V. Architectural | System designed without hierarchy | Flat topology; peer-to-peer connectivity | Peer-to-peer networks, distributed ledgers |

### 2.2 Category I: Geometric Resistance

The underlying space is not a tree. In Euclidean space $\mathbb{R}^n$, the strong triangle condition fails generically — equilateral triangles are possible, and for most triples the two largest distances are unequal. The author's prior work (Ultrametric Paradigm, 2026) contrasts Archimedean (additive, Euclidean) geometry with non-Archimedean (ultrametric) geometry, arguing that the Archimedean assumption underlying most of modern physics is an approximation valid only at coarse scales.

Small-world networks (Watts & Strogatz, 1998) combine local clustering with random long-range shortcuts. The resulting graph has high clustering (equilateral-like triangles among neighbors) and low diameter (shortcuts that bypass hierarchical structure). The cophenetic distance is undefined — there is no unique common ancestor in a small-world graph.

Scale-free networks with clustering (Barabási & Albert, 1999) have power-law degree distributions where hub nodes connect many leaves. Combined with triadic closure (friends of friends are friends), these networks resist tree organization because community structure overlaps in ways that cannot be represented by a single rooted tree.

### 2.3 Category II: Dynamical Resistance

The system's own dynamics introduce interactions that prevent branches from evolving independently. Closure fails because the physics generates cross-branch correlations.

In many-body localized (MBL) phases, disorder prevents thermalization. Each degree of freedom retains memory of its local initial conditions through an extensive set of local integrals of motion ("l-bits"). The l-bit structure is approximately hierarchical (each l-bit is dressed by interactions with faster l-bits), but spatial locality competes with tree depth — the distance between states depends on both their tree separation and their spatial proximity. The resulting metric is mixed, neither purely ultrametric nor purely Euclidean (Nandkishore & Huse, 2015).

In non-perturbative quantum field theory, the perturbative expansion fails. Feynman diagrams form trees at each order, but when the coupling is strong, all orders contribute equally. The tree of diagrams collapses. Hadronization in QCD — the process by which quarks and gluons become hadrons — is the canonical example of non-perturbative physics destroying tree structure. Color reconnection and multi-parton interactions further introduce lateral edges.

In finite-dimensional spin glasses, the Edwards-Anderson model in $d = 3$ has been debated for forty years between the replica symmetry breaking picture (ultrametric) and the droplet picture (non-ultrametric). In $d = 2$, $T_c = 0$ — no finite-temperature spin glass phase exists. The droplet picture (Fisher & Huse, 1986) proposes that low-energy excitations are compact clusters of flipped spins that do not form a hierarchical tree. Geometric locality breaks the mean-field ultrametricity.

### 2.4 Category III: Lateral Transfer Resistance

The system has a tree-like backbone (branching occurs), but information, genes, or traits move between branches after divergence. Closure fails through lateral edges.

In prokaryote evolution, horizontal gene transfer (HGT) is ubiquitous. Genes move between unrelated lineages through conjugation, transformation, and transduction. The "tree of life" becomes a "web of life" or phylogenetic network (Doolittle, 1999). Core genes (ribosomal RNA, essential enzymes) are rarely transferred and preserve a tree-like signal; accessory genes (antibiotic resistance, virulence factors) are frequently transferred and create lateral edges.

In historical linguistics, languages diverge by descent (the tree model), but contact introduces borrowing. English "beef" from French *boeuf* creates a lateral edge between Germanic and Romance branches. The Balkan sprachbund — Albanian, Romanian, Bulgarian, Greek — shares grammatical features without shared ancestry in those features. Creole languages, born from the merger of two or more languages, have mixed ancestry that cannot be represented as a tree.

In cognitive science, semantic memory is organized associatively, not hierarchically (Collins & Loftus, 1975). The spreading activation model proposes that concepts are connected by weighted edges. "Fire" connects to "hot," "danger," "camping," and "passion" — a network with lateral edges, not a tree. Analogical reasoning creates cross-links between separate concept domains.

### 2.5 Category IV: Entropic Resistance

Thermal fluctuations, noise, or mixing overwhelm the hierarchical signal. The system explores all accessible states so uniformly that no tree structure can be discerned.

In thermal systems above their critical temperature, all states at a given energy are equally accessible. The Boltzmann distribution becomes uniform as $T \to \infty$. In spin glasses, the Parisi ultrametric solution exists only below $T_c$; above $T_c$, the system is a paramagnet with no hierarchical state organization.

In fully developed turbulence, energy cascades from large to small scales (the Kolmogorov cascade). Superficially, this appears hierarchical — large eddies break into smaller ones. But intermittency (non-uniform energy dissipation), coherent structures that interact across scales, and chaotic sensitivity to initial conditions prevent clean tree organization. The scaling is multifractal, not single-exponent hierarchical.

In random matrix theory, the eigenvalues of Gaussian ensembles exhibit level repulsion — they avoid each other, producing a rigid spectrum with no hierarchical organization. The nearest-neighbor spacing follows the Wigner surmise, not the Poisson distribution that would indicate integrability and hierarchy.

### 2.6 Category V: Architectural Resistance

The system is deliberately designed or has evolved without hierarchical organization. Hierarchy was never present to be broken.

Peer-to-peer networks (BitTorrent, early Gnutella) have no root, no central authority, no hierarchy. Every node is both client and server. Routing is gossip-based or distributed-hash-table-based, not hierarchical.

Distributed ledgers (blockchains) are linear chains, not trees. Each block points to exactly one predecessor. Forks are resolved by the longest-chain rule. Consensus is achieved without hierarchical authority — no single node validates transactions.

Markets and price systems solve resource allocation without central planning (Hayek, 1945). Prices aggregate dispersed information. No single agent knows everything; no hierarchy of knowledge exists. The price vector is an emergent consensus, not a command.

---

## 3. The Complete Phase Diagram

### 3.1 Five Regimes of Organization

Ultrametric organization is not binary — a system is not simply "a tree" or "not a tree." Systems fall on a spectrum of five regimes, distinguished by which generative conditions are met and which resistance mechanisms are active:

| Regime | Conditions Met | Conditions Failed | Dominant Resistance | Domain Examples |
|:-------|:---------------|:------------------|:--------------------|:----------------|
| **I. Exact tree** | Branching, closure, cophenetic distance all hold | None | None | $p$-adic numbers; SK spin glass ($d = \infty$); perturbative RG; pure hierarchical taxonomies |
| **II. Approximate tree** | Branching holds; closure mostly holds | Cophenetic distance uses external metric (not operation count) | Category I (metric distortion) | Clock-like metazoan phylogeny; Swadesh vocabulary; $e^+e^-$ jets at LEP |
| **III. Tree + lateral edges** | Branching holds | Closure partially broken; cophenetic distance approximate | Category III (lateral transfer) | Prokaryote phylogeny with HGT; full lexicon with borrowing; $pp$ jets at LHC |
| **IV. Network with residual hierarchy** | Branching partially present (hubs, communities) | Closure broken; cophenetic distance undefined | Categories I + II (geometric + dynamical) | Social networks; semantic memory; AS-level internet; spin glasses at $d = 3$ |
| **V. Flat / non-hierarchical** | All three fail | Branching absent or scale-collapsed | Categories IV + V (entropic + architectural) | Thermal systems above $T_c$; CFT fixed points; random graphs; peer-to-peer networks |

### 3.2 Transitions Between Regimes

Systems do not stay fixed in one regime. Transitions occur when a control parameter — temperature, dimensionality, coupling strength, evolutionary time — crosses a threshold:

- **Temperature.** Spin glasses: $T < T_c$ → Regime I (RSB, ultrametric); $T > T_c$ → Regime V (paramagnetic, no tree).
- **Dimensionality.** Spin glasses: $d = \infty$ → Regime I; $d = 3$ → contested between I and IV; $d = 2$ → Regime V ($T_c = 0$, no spin glass phase).
- **Coupling strength.** QCD: weak coupling (high energy) → Regime II; strong coupling (low energy) → Regime IV–V (non-perturbative, hadronization).
- **Evolutionary time.** Networks: start tree-like (Regime II); accumulate lateral edges → Regime III; triadic closure dominates → Regime IV.
- **Measurement resolution.** Fine-grained measurement reveals tree structure (Regime II); coarse-grained measurement may only see Regime IV–V.

### 3.3 A Worked Example: Phylogenetics Across Regimes

Consider the evolutionary relationships among organisms. The domain illustrates how a single system can span multiple regimes depending on which organisms and which genes are examined:

- **Metazoan (animal) phylogeny with clock-like genes** sits in Regime II: sexual reproduction enforces vertical inheritance (branching holds, closure mostly holds), and clock-like genes evolve at approximately constant rates (cophenetic distance approximate).
- **Plant phylogeny** spans Regimes II–III: hybridization is common, introducing lateral edges. Phylogenetic networks with reticulation edges are needed to represent plant evolutionary history accurately.
- **Prokaryote phylogeny** (bacteria and archaea) sits in Regime III: horizontal gene transfer is ubiquitous. Core genes (ribosomal RNA) preserve a tree-like signal; accessory genes (antibiotic resistance, metabolic pathways) create extensive lateral edges. The "tree of life" concept has been largely abandoned for prokaryotes in favor of phylogenetic networks.
- **Endosymbiotic events** — such as the engulfment of an ancestral bacterium that became the mitochondrion — represent a transition toward Regime IV: two branches of the tree literally fuse. The eukaryotic cell has mixed ancestry (archaeal host + bacterial endosymbiont).

This example demonstrates that resistance is not an all-or-nothing property. It is graded, and the grade depends on which lineage and which genetic loci are examined.

### 3.4 The Fundamental Asymmetry

There is an asymmetry between the tree and its resistance:

- **The tree is unique.** There is exactly one way to be perfectly ultrametric: satisfy all three generative conditions. The resulting structure is rigid — all triangles are isosceles, all points at the same depth are equivalent.
- **Resistance is diverse.** There are many ways to NOT be ultrametric. The five categories represent different paths away from the tree, and a single system can exhibit multiple resistance mechanisms simultaneously.

This asymmetry reflects a deeper principle: **order is specific; disorder is generic.** The tree is an attractor not because most systems flow toward it, but because when systems do flow toward it, they all converge on the same structure. Most systems flow elsewhere — toward the diverse landscape of non-tree organization.

---

## 4. The Generative Logic and Its Shadow

### 4.1 Three Operations, Three Duals

The ultrametric tree arises from three operations:

1. **Recursive splitting** (branching): "One becomes more." A single entity splits into sub-entities, and the operation repeats on each sub-entity.
2. **Independent evolution** (closure): After splitting, sub-entities evolve without lateral interaction.
3. **Operation-count distance**: Distance between entities is measured as the count of splitting operations to their common ancestor.

Each operation has a counterpart that generates resistance instead of trees. This is a structural observation, not a formal theorem — the operations are described qualitatively:

| Attractor Operation | Resistance Counterpart | Effect on the System |
|:--------------------|:-----------------------|:---------------------|
| Recursive splitting | Accretion, merging, or flat growth | Structure built without branching — by adding parts, merging lineages, or simultaneous interaction |
| Independent evolution | Lateral interaction | Cross-branch edges (triadic closure, borrowing, HGT) are added after splitting |
| Operation-count distance | External metric or ergodic mixing | Distance is measured by spatial separation, similarity ratings, or all states become equally accessible |

A system dominated by the attractor operations will be ultrametric. A system dominated by the counterparts will resist tree organization. Most real systems lie between the extremes, with both sets of operations active to varying degrees.

### 4.2 Closure Is the Bottleneck

Of the three generative conditions, closure — the requirement that branches evolve independently after splitting — is the one most frequently broken. Branching is common across nature and culture: recursive splitting, nested categorization, hierarchical organization appear in many domains. Operation-count distance is a definitional choice — if we measure operation count, it holds; if we measure something else, it may not.

But closure fails almost everywhere. Lateral transfer (Category III: HGT, borrowing, analogy), triadic closure (Category I: social networks, semantic memory), non-perturbative mixing (Category II: strong-coupling QCD, MBL spatial locality), thermalization (Category IV), and deliberate flat architecture (Category V) all break the requirement that branches not interact after splitting.

The tree requires isolation. Nature rarely provides it.

### 4.3 The Tree as a Conditional Limit

This reframing resolves a tension in interpreting the cross-domain appearance of ultrametricity. The tree is not a property that systems "achieve" — it is a **conditional limit** that systems approach as isolation increases. The $p$-adic numbers are exactly ultrametric because they are pure mathematics, perfectly isolated by definition. The SK spin glass is exactly ultrametric because $d = \infty$ removes all geometry. Real systems, in finite dimensions with interactions, approach the tree to the degree that their isolation approaches perfection.

This means that the ultrametric pattern is both real and rare. It is real — the mathematical structure exists, and real systems approximate it. It is rare — perfect isolation is an idealized condition, and most real systems deviate from it. The cross-domain pattern exists not because the tree is a universal attractor, but because any system that approaches the isolated hierarchical limit will, necessarily, approach the ultrametric geometry. The approach is what matters; the limit is rarely reached.

### 4.4 What the Shadow Reveals

Cataloging systems that resist tree organization does more than list counterexamples. It reveals what the tree *is* by showing what happens when it *isn't*. Each category of resistance illuminates a specific generative condition:

- Geometric resistance shows what happens when the embedding space is not a tree — distances become equilateral, not isosceles.
- Dynamical resistance shows what happens when closure fails from within — the physics generates cross-branch correlations.
- Lateral transfer resistance shows what happens when closure fails from without — information moves across branches.
- Entropic resistance shows what happens when hierarchy is overwhelmed — all states become equivalent.
- Architectural resistance shows what happens when hierarchy is never present — organization without trees is possible.

The shadow defines the tree by negation. This is a deeper form of understanding than cataloging the tree alone. Together, the tree and its shadow form a complete picture of how hierarchical organization succeeds, fails, and transitions between regimes.

---

## 5. Falsifiable Predictions

The unified framework makes predictions that distinguish it from the null hypothesis that ultrametricity is merely an occasional pattern with no deeper significance.

**P1: Isolation drives ultrametricity.** In any system with recursive branching, increasing isolation (reducing lateral interaction) should increase the ultrametric signal. Decreasing isolation should degrade it.

*Test:* Compare phylogenetic tree signal for core genes (rarely transferred) versus accessory genes (frequently transferred) in bacterial genomes. Core genes should show stronger ultrametricity.

**P2: The phase transition is sharp.** As lateral edge density increases, the ultrametric signal should exhibit threshold behavior — remaining near the tree-like limit until a critical density, then dropping sharply toward the network regime.

*Test:* Construct synthetic networks on perfect trees, add random lateral edges with increasing probability, and measure the deviation from ultrametricity. The transition should show a characteristic sharp drop.

**P3: Resistance mechanisms compound.** Real systems often exhibit multiple resistance mechanisms simultaneously. A social network may show both geometric resistance (small-world shortcuts) and dynamical resistance (triadic closure). The combined effect should be stronger than either mechanism alone.

*Test:* Construct synthetic networks with controlled amounts of triadic closure AND random long-range edges. Measure the ultrametric deviation for each mechanism alone and in combination. If resistance compounds, the combined deviation should be greater than the sum of individual deviations.

**P4: MBL systems have a hidden tree.** Many-body localized phases should exhibit an approximate tree structure in their l-bit correlations, but the tree is distorted by spatial locality.

*Test:* Analyze l-bit correlation functions in numerical MBL simulations. Compare the degree to which correlations are organized by tree-distance versus spatial-distance.

**Status of predictions:** All four are proposed. None have been empirically tested.

---

## 6. Conclusion

This paper has argued that ultrametricity — the strong triangle condition — is the mathematical signature of isolated hierarchical branching. When recursive distinction operates without lateral interaction, and distance is measured as operation count to common ancestor, the result is necessarily, mathematically, an ultrametric tree.

But nature is rarely isolated. Five categories of resistance — geometric, dynamical, lateral transfer, entropic, and architectural — prevent or break tree organization across physics, biology, cognitive science, network theory, and social organization. The tree is a conditional attractor, approached only when isolation is nearly perfect. Resistance is the default.

The tree and its resistance form halves of a single generative logic. The tree shows what happens when branching, closure, and operation-count distance jointly hold. The resistance shows what happens when each condition fails, individually or in combination. Together, they map the full phase diagram of hierarchical organization in nature — from exact ultrametricity through approximate trees with lateral edges to flat, non-hierarchical architectures.

This framework generates testable predictions. The most fundamental: **isolation drives ultrametricity.** Systems with more lateral interaction should show weaker tree signals; systems with stronger isolation should approach the ultrametric limit. This prediction is falsifiable and has not been tested systematically across domains.

The tree at the bottom of thought has a shadow. Both are real. Both are informative. Neither alone tells the full story.

---

## References

### Author's Prior Corpus
- Quni-Gudzinas, R. B. (2026). *The Tree at the Bottom of Thought: A Synthesis of Ultrametric Branching*. DOI: 10.5281/zenodo.20329583.
- Quni-Gudzinas, R. B. (2026). *The Tree Is Real: Computational Validation of Ultrametric Convergence*. DOI: 10.5281/zenodo.20325850.
- Quni-Gudzinas, R. B. (2026). *Convergence, Consilience, and the Hierarchical Architecture of Reality*. DOI: 10.5281/zenodo.20302276.
- Quni-Gudzinas, R. B. (2025). *Treatise on Clocks and Taxonomies*. Unpublished manuscript.
- Quni-Gudzinas, R. B. (2025). *Nature of Zitterbewegung*. Unpublished manuscript.
- Quni-Gudzinas, R. B. (2025). *Resonant Complexity Framework*. Unpublished manuscript.

### External Literature
- Parisi, G. (1979). Infinite number of order parameters for spin-glasses. *Physical Review Letters*, 43(23), 1754.
- Guerra, F. (2003). Broken replica symmetry bounds in the mean field spin glass model. *Communications in Mathematical Physics*, 233(1), 1–12.
- Talagrand, M. (2006). The Parisi formula. *Annals of Mathematics*, 163(1), 221–263.
- Fisher, D. S., & Huse, D. A. (1986). Ordered phase of short-range Ising spin-glasses. *Physical Review Letters*, 56(15), 1601.
- Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393(6684), 440–442.
- Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509–512.
- Doolittle, W. F. (1999). Phylogenetic classification and the universal tree. *Science*, 284(5423), 2124–2128.
- Collins, A. M., & Loftus, E. F. (1975). A spreading-activation theory of semantic processing. *Psychological Review*, 82(6), 407.
- Nandkishore, R., & Huse, D. A. (2015). Many-body localization and thermalization in quantum statistical mechanics. *Annual Review of Condensed Matter Physics*, 6(1), 15–38.
- Hayek, F. A. (1945). The use of knowledge in society. *American Economic Review*, 35(4), 519–530.
- Schmidt, J. (1872). *Die Verwantschaftsverhältnisse der indogermanischen Sprachen*. Weimar: Böhlau.
