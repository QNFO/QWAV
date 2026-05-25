---
title: "Signal and Worker: How Proteins Activate Electrons"
authors: "Rowan Brad Quni-Gudzinas"
date: "2026-05-21"
doi: "10.5281/zenodo.20329448"
version: "v1.0"
abstract: >
  Proteins are the master choreographers of electron activation in biological systems. This document presents the Signal-Worker ontology — a framework in which bosons (photons/phonons) act as informational signals and fermions (electrons/excitons) perform chemical work — and shows how the protein scaffold functions as a programmable phonon source. Drawing on photosynthesis, respiration, oxidoreductases, and metalloproteins, we demonstrate that biological electron activation operates through Environment-Assisted Quantum Transport (ENAQT) and manifests an isomorphism with Floquet-engineered superconductivity. Design rules for bio-inspired room-temperature quantum metamaterials are derived from the analysis.
keywords: ["electron activation", "Signal-Worker ontology", "protein scaffold", "ENAQT", "phononic crystal", "bio-inspired metamaterials", "photosynthesis", "electron transport", "Floquet engineering", "CISS"]
license: "CC-BY-4.0"
modified: 2026-05-21T16:57:12Z
---

# Signal and Worker: How Proteins Activate Electrons

**Author**: [Rowan Brad Quni-Gudzinas](mailto://rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**DOI:** [10.5281/zenodo.20329448](https://doi.org/10.5281/zenodo.20329448)
**Date**: 2026-05-21

**Abstract**: Proteins are the master choreographers of electron activation in biological systems. This document presents the Signal-Worker ontology — a framework in which bosons (photons/phonons) act as informational signals and fermions (electrons/excitons) perform chemical work — and shows how the protein scaffold functions as a programmable phonon source. Drawing on photosynthesis, respiration, oxidoreductases, and metalloproteins, we demonstrate that biological electron activation operates through Environment-Assisted Quantum Transport (ENAQT) and manifests an isomorphism with Floquet-engineered superconductivity. Design rules for bio-inspired room-temperature quantum metamaterials are derived from the analysis.

## 1. What is Electron Activation?

The phrase “electron activation” refers to the process of raising an electron to a usable energy state — either by energetic excitation or by lowering the kinetic barrier to its transfer — so that it can perform chemical work. In biological systems, proteins are the master choreographers of this process. They do not merely house electron carriers; they actively generate the conditions under which electrons can be mobilised, directed, and delivered to their targets with extraordinary efficiency.

Two principal modes of electron activation operate in biology:

- **Photochemical activation.** A pigment molecule such as chlorophyll absorbs a photon, promoting an electron to a higher-energy orbital. The protein scaffold then separates the resulting charges so that the excited electron can enter a transport chain before it relaxes back to the ground state.
- **Redox activation.** An enzyme holds a substrate and an electron donor in precise mutual orientation, lowering the activation barrier for electron transfer. It may also stabilise radical intermediates that form after the electron arrives, enabling transformations that would be kinetically forbidden in free solution.

Both modes depend on the same underlying principle: the protein is not a passive container but an active participant in the physics of electron transfer. To understand how, we must first examine the ontology — the conceptual framework — that best captures what proteins actually do.

## 2. The Signal-Worker Ontology

### 2.1 Beyond Wave-Particle Duality

Standard quantum mechanics relies on wave-particle duality to describe energy transduction. While mathematically robust for isolated particles, this duality obscures the functional division of labour that operates in driven, non-equilibrium biological systems. A photosynthetic reaction centre at physiological temperature does not face an ambiguous quantum entity that is “both wave and particle.” It faces a **signal** — a structured bosonic field (photon or phonon) carrying energy and information — and a **worker** — a localised fermion (electron or exciton) that performs the chemical work.

The **Signal-Worker ontology**, introduced in the Bosonic Signal Hypothesis (Quni-Gudzinas, 2026), proposes a functional decomposition:

| Entity | Role | Physical Carrier | Biological Instantiation |
|:-------|:-----|:-----------------|:-------------------------|
| **Signal** | Carries energy + information; delocalised | Bosons (photons, phonons) | Sunlight, protein vibrational modes |
| **Worker** | Performs chemical work; localised | Fermions (electrons, excitons) | Chlorophyll excited electron, heme iron |

This decomposition is not merely semantic. It identifies a design principle that evolution has exploited for billions of years and that condensed-matter physicists are only beginning to replicate: **separate the signal source from the worker so that each can be optimised independently.**

### 2.2 Why the Distinction Matters

In conventional superconductors such as YBCO, the copper-oxide plane provides both the electrons for pairing and the phonons for binding. This inseparability — the “pigment and scaffold are the same atoms” — makes it extraordinarily difficult to engineer the system. Changing the electronic structure inevitably changes the phonon spectrum, and vice versa. Biology solved this problem by modularising the two functions: the pigment (worker) is a small molecule embedded within a protein polymer (scaffold/signal source). Evolution can tune the scaffold’s vibrational spectrum without altering the pigment’s electronic structure, achieving an engineering flexibility that crystal lattices lack — in a conventional superconductor, the same atoms that conduct electrons also generate the phonons that pair them, making the two functions inseparable.

This modularity is the deep reason why proteins are “poor electron conductors” — a phrase that undersells their design. By being electrically insulating, the protein scaffold isolates the signal-generation machinery (phonons) from the worker pathway (electrons), preventing cross-talk that would degrade both functions.

## 3. The Protein Scaffold as Programmable Phonon Source

### 3.1 From Passive Solvent to Active Signal Generator

Textbook biochemistry describes the protein environment as tuning redox potentials through hydrophobicity, hydrogen bonding, and electrostatic effects. While correct, this description is incomplete. A deeper analysis reveals that the protein scaffold functions as a **programmable phonon source** — a structured vibrational environment whose spectral density $J(\omega)$ has been shaped by evolution to match the energy gaps between electron donor and acceptor sites.

The key insight is that thermal motion in a protein is not random white noise. It is **coloured noise** — vibrations concentrated at specific frequencies determined by the amino acid sequence and three-dimensional fold. Where a generic solvent applies a featureless thermal background, a protein applies a vibrational spectrum tuned to the excitonic energy differences $\Delta E_{ij}$ between pigment sites $i$ and $j$. When $\hbar\omega \approx \Delta E_{ij}$, the phonon mode opens a channel for the electron to tunnel — the signal activates the worker.

### 3.2 The Phononic Crystal Analogy

In solid-state physics, a **phononic crystal** is a periodically structured material designed to control the propagation of mechanical vibrations. The protein scaffold can be understood as an aperiodic, evolutionarily optimised phononic crystal. Its vibrational band structure — determined by the masses of amino acid side chains, the stiffness of hydrogen bond networks, and the geometry of secondary structure elements — creates a density of states $g(\omega)$ that selectively enhances vibrations at the frequencies needed to bridge electronic energy gaps.

This framing upgrades the conventional language:

| Conventional Description | Signal-Worker Reframing |
|:-------------------------|:------------------------|
| “Protein tunes redox potential” | “Protein programs phonon spectrum to match electronic gaps” |
| “Aromatic residues provide tunnelling pathways” | “Vibrational modes of aromatic residues constitute the bosonic signal” |
| “Hydrophobic core excludes water” | “Low-dielectric interior prevents signal dissipation into solvent modes” |
| “Hydrogen bond network stabilises intermediate” | “Hydrogen bond network shapes $J(\omega)$ to amplify bridging frequencies” |

### 3.3 Mathematical Formalism

In the Frenkel exciton Hamiltonian that describes photosynthetic energy transfer, the protein contribution appears through the exciton-phonon coupling term:

$$H_{\text{bio}} = \sum_{i} \epsilon_i f^\dagger_i f_i + \sum_{i \neq j} J_{ij} f^\dagger_i f_j + \sum_{q} \hbar\omega_q b^\dagger_q b_q + \sum_{i,q} g_{iq} f^\dagger_i f_i (b^\dagger_q + b_q)$$

Here, $f^\dagger_i, f_i$ are the exciton (worker) creation and annihilation operators at site $i$, with site energies $\epsilon_i$ and inter-site couplings $J_{ij}$. The phonon (signal) modes are described by $b^\dagger_q, b_q$ with frequencies $\omega_q$, and $g_{iq}$ is the exciton-phonon coupling strength. The protein scaffold creates a non-zero, time-dependent expectation value for the phonon field $\langle b^\dagger_q + b_q \rangle$, acting as a local drive even in the absence of external light. This is the mathematical expression of the protein as a signal source.

## 4. How Signals Activate Workers: Environment-Assisted Quantum Transport

### 4.1 The ENAQT Mechanism

Environment-Assisted Quantum Transport (ENAQT) is the canonical example of the Signal-Worker mechanism in biological systems. The phenomenon was first recognised in theoretical studies of photosynthetic light-harvesting complexes, where it was observed that pure quantum coherence leads to destructive interference (Anderson localisation) in disordered energy landscapes, while pure classical diffusion is too slow. Optimal transport occurs in an **intermediate regime** where environmental noise — far from being a hindrance — actively assists the quantum walk.

In the Signal-Worker framework, this “noise” is reinterpreted as a functional signal. When the phonon energy $\hbar\omega$ matches the energy difference $\Delta E_{ij}$ between two pigment sites, the signal channel opens and the worker tunnels efficiently. The protein scaffold, by providing a structured vibrational spectrum rather than white noise, ensures that the noise is **constructive** — it contains the specific frequencies needed to bridge the gaps in the excitonic landscape.

### 4.2 Marcus Theory in the Signal-Worker Context

Conventional Marcus theory describes electron transfer rates in terms of three parameters: the electronic coupling $H_{AB}$, the reorganisation energy $\lambda$, and the driving force $\Delta G^0$. The rate is given by:

$$k_{ET} = \frac{2\pi}{\hbar} |H_{AB}|^2 \frac{1}{\sqrt{4\pi\lambda k_B T}} \exp\!\left(-\frac{(\Delta G^0 + \lambda)^2}{4\lambda k_B T}\right)$$

In the Signal-Worker reframing:

- $H_{AB}$ is the **worker coupling** — the quantum tunnelling matrix element between donor and acceptor, determined by distance and orientation.
- $\lambda$ is the **signal coupling** — the reorganisation energy, which measures how strongly the protein scaffold’s vibrational modes couple to the electron transfer coordinate.
- The exponential term describes the **resonance condition** — when the signal energy ($\lambda$) matches the work to be done ($\Delta G^0$), the transfer rate is maximised.

The protein’s role in Marcus theory is thus reframed: it does not merely “control the reorganisation energy” — it **programs the signal spectrum** so that the resonance condition is satisfied for the specific electron transfer step required.

### 4.3 The Photosynthesis-Superconductivity Isomorphism

A remarkable structural parallel exists between photosynthetic energy transduction and light-induced superconductivity, unified under the Signal-Worker Hamiltonian $H_{SW}$. In photosynthesis, the signal is a phonon from the protein scaffold; in a light-driven superconductor, the signal is a photon from a laser pulse. In both cases:

1. A bosonic signal (phonon or photon) supplies energy that matches an electronic gap.
2. This energy enables fermionic workers (excitons or Cooper pairs) to form and transport.
3. The stability of the resulting state depends on the signal’s spectral match to the worker’s energy landscape.

The Floquet engineering of superconductors — where periodic driving by light induces transient superconducting states — is the condensed-matter analogue of what photosynthetic proteins do continuously at ambient temperature. The difference is that biology uses a static, evolutionarily optimised phonon spectrum (the protein scaffold), while physicists use a dynamic, externally applied photon field (the laser). Both are instances of the same Signal-Worker dynamic.

With these theoretical tools in hand, we now turn to the experimental reality: how specific protein systems instantiate the Signal-Worker principle across the diversity of biological electron transfer. The systems examined below — photoreaction centres, respiratory complexes, oxidoreductases, and metalloproteins — each embody the same fundamental design: a modular separation of signal generation (the protein scaffold) from work execution (the cofactor), with evolutionarily optimised spectral matching between the two.

## 5. Key Protein Systems: Instantiations of the Signal-Worker Principle

### 5.1 Photoreaction Centres: Light-Driven Signal Capture

Photosystems II and I (PSII, PSI) are the entry points for light energy into the biosphere. When a chlorophyll molecule absorbs a photon, the excited electron must be separated from its “hole” before it relaxes — a process achieved within picoseconds by the protein scaffold.

In Signal-Worker terms:

- The **photon** is the primary signal, carrying energy from the sun.
- The **chlorophyll** is the worker, converting photonic signal into an excited electron.
- The **protein scaffold** provides the secondary signal — structured vibrations that stabilise charge separation and guide the electron down the transport chain.

The remarkable quantum efficiency of photosynthesis (approaching unity in low light) is a direct consequence of the protein scaffold’s spectral matching: the vibrational modes of the surrounding amino acids are tuned to the energy gaps between successive electron carriers, ensuring that the worker is handed off from site to site with minimal loss.

### 5.2 Respiratory Complexes: The Electron Transport Chain

Mitochondrial Complexes I, III, and IV transfer electrons from NADH to molecular oxygen, generating the proton gradient that drives ATP synthesis. Each complex employs a chain of redox cofactors (flavins, iron-sulfur clusters, hemes, copper centres) whose midpoint potentials are arranged in a descending staircase.

In Signal-Worker terms, each cofactor is a worker station, and the protein matrix between them provides the signal — vibrational modes that bridge the energy gaps between successive redox centres. The overall architecture is that of a **signal-guided assembly line**: electrons are not simply diffusing downhill in free energy; they are being actively channelled by the vibrational environment that the protein provides.

**Complex I** (NADH dehydrogenase) is particularly instructive. It contains a 45 $\mathring{\mathrm{A}}$ chain of eight iron-sulfur clusters connecting the NADH-binding site to the ubiquinone-binding site — a distance far too long for single-step electron tunnelling. The protein solves this by positioning the clusters at edge-to-edge distances of $< 14 \, \mathring{\mathrm{A}}$, with each inter-cluster gap spanned by structured protein vibrations that match the energy difference between the donor and acceptor clusters.

### 5.3 Oxidoreductases: Single-Electron Chemistry

Many enzymatic transformations — cleaving C–H bonds, reducing ribonucleotides to deoxyribonucleotides, activating molecular oxygen — require the transfer of single electrons, a process that would generate destructive free radicals if not carefully controlled. The protein scaffold solves this by:

1. **Generating the signal**: vibrational modes that lower the activation barrier for electron transfer.
2. **Stabilising the worker intermediate**: the protein pocket shields the radical species from solvent, preventing side reactions.
3. **Gating the transfer**: conformational changes ensure that electron transfer occurs only when the substrate is properly bound.

**Ribonucleotide reductase** exemplifies this strategy. A stable tyrosyl radical is generated and maintained within the protein interior, where it serves as a “parked” oxidising equivalent. When the substrate binds, a chain of conserved aromatic residues (tyrosine, tryptophan) transfers the radical character — effectively a single electron hole — over 35 $\mathring{\mathrm{A}}$ to the active site, where a cysteine residue is activated to abstract a hydrogen atom from the substrate. This long-range radical transfer is a prototypical Signal-Worker process: the protein’s vibrational and electronic structure provides both the pathway (signal) and the radical (worker).

**Cytochrome P450** illustrates a complementary strategy. The heme iron at the active site receives electrons from a redox partner (NADPH via a flavoprotein reductase), activating molecular oxygen to form a highly reactive oxo-iron(IV) porphyrin $\pi$-cation radical species (Compound I). This species then hydroxylates inert C–H bonds with remarkable regio- and stereoselectivity — chemistry that, without the protein scaffold’s control, would produce indiscriminate oxidation. The protein channels the electron to the heme, gates oxygen binding, and positions the substrate so that the activated oxygen attacks the correct C–H bond.

### 5.4 Metalloproteins and Chirality-Induced Spin Selectivity

Iron-sulfur clusters, blue copper proteins, and multi-heme cytochromes are versatile electron carriers whose redox potentials span nearly a volt, enabling them to connect diverse redox couples. The protein environment achieves this tuning through:

- **Dielectric modulation**: hydrophobic pockets raise potentials; charged residues lower them.
- **Hydrogen bonding to sulfur ligands**: modulates the electron density on the cluster.
- **Geometric constraint**: the “entatic state” — a strained geometry that poises the metal centre between oxidation states, lowering the reorganisation energy for electron transfer.

Beyond these well-known mechanisms, a more recent discovery adds a new dimension to protein electron transfer: **Chirality-Induced Spin Selectivity (CISS)**. All natural proteins are composed exclusively of L-amino acids, making them homochiral polymers. When electrons move through a chiral protein structure, the molecular handedness acts as a spin filter — preferentially transmitting electrons of one spin orientation while reflecting the other. This effect, well-characterised in electron transport through helical peptides and DNA, means that protein electron transfer is inherently **spin-polarised**.

The CISS effect connects protein biochemistry to the author’s work on chiral electron transport (Quni-Gudzinas, 2025), which demonstrated that structural chirality in crystalline materials induces asymmetric electronic responses. The same principle — that chirality breaks the symmetry between forward and reverse, or between spin-up and spin-down — operates in proteins at the molecular scale. In effect, the protein’s L-chirality adds a spin label to every electron it transports, providing an additional degree of control that achiral environments cannot offer.

## 6. Plastocyanin: A Case Study in Signal-Worker Design

The blue copper protein plastocyanin provides an elegant illustration of the Signal-Worker principle in a single molecule. Plastocyanin shuttles electrons between cytochrome $f$ (from the cytochrome $b_6f$ complex) and the photo-oxidised P700 reaction centre of Photosystem I.

### The Worker: A Type-1 Copper Centre

The copper ion is coordinated by two histidine nitrogens, a cysteine sulfur, and a methionine sulfur in a distorted tetrahedral geometry. This coordination environment is unusual: it is intermediate between the preferences of Cu(I) (tetrahedral) and Cu(II) (square planar). The protein forces the copper into a geometry that satisfies neither oxidation state perfectly — the **entatic state** — which has two crucial consequences:

1. **Low reorganisation energy.** Because the geometry does not need to rearrange significantly between Cu(I) and Cu(II), the reorganisation energy $\lambda$ for electron transfer is small ($\approx 0.6 \, \text{eV}$), enabling rapid transfer.
2. **High redox potential.** The highly covalent Cu–S(Cys) bond and the hydrophobic pocket raise the midpoint potential to approximately $+370 \, \text{mV}$, poised between the potentials of cytochrome $f$ ($+365 \, \text{mV}$) and P700 ($+430 \, \text{mV}$).

### The Signal: Protein Vibrations Tuned to the Copper

The protein scaffold around the copper site provides vibrational modes that match the energy of the electron transfer event. The cysteine thiolate ligand, with its relatively heavy sulfur atom, introduces low-frequency vibrational modes ($200$–$400 \, \text{cm}^{-1}$) that couple strongly to the copper redox state. These modes constitute the bosonic signal that activates the electron for transfer. The hydrophobic pocket surrounding the copper excludes water, preventing these tuned vibrations from dissipating into the solvent — a form of **phononic insulation**.

### The Design Principle

Plastocyanin embodies the modular Signal-Worker design: the copper (worker) performs the electron transfer, while the protein scaffold (signal source) provides the vibrational environment that makes the transfer fast and directional. The two functions are chemically and spatially separated, allowing each to be optimised independently — exactly the principle that bio-inspired materials engineering seeks to replicate.

The biological systems examined above do more than illustrate a physical principle — they constitute a design manual. Each system demonstrates a different aspect of the Signal-Worker architecture: spectral matching (photosynthesis), serial signal chaining (respiration), radical gating (oxidoreductases), spin filtering (chirality), and entatic state engineering (plastocyanin). We now translate these biological design rules into an engineering framework for synthetic quantum materials.

## 7. From Biology to Technology: Bio-Inspired Metamaterials

The Signal-Worker ontology is not merely a re-description of known biology; it is a **design manual** for engineering room-temperature quantum devices. Nature has demonstrated that stable, efficient quantum transport is possible at $300 \, \text{K}$ — the challenge is to translate the biological design rules into synthetic materials.

### 7.1 Design Rules from Photosynthesis

The Bosonic Signal Hypothesis extracts three engineering principles from photosynthetic proteins:

1. **Modularity.** Separate the worker (conductor) from the signal source (scaffold). In biology, the pigment and protein are chemically distinct; in a synthetic analogue, the conducting layer and the phononic scaffold should be independently tuneable.
2. **Resonance tuning.** The phonon spectrum of the scaffold must match the energy gaps of the electronic states. This requires “geometric doping” — designing the scaffold’s nanostructure to produce specific vibrational frequencies — rather than chemical doping of the conductor alone.
3. **Phononic insulation.** The scaffold must prevent signal dissipation. In biology, the hydrophobic protein core excludes water; in a synthetic system, acoustic impedance mismatches at interfaces can confine phonons to the scaffold.

### 7.2 The Proposed Metamaterial Architecture

A bio-inspired superconducting metamaterial would consist of:

- A **conducting layer** (the worker) — for example, graphene, monolayer FeSe, or a two-dimensional electron gas. These materials are adopted not as direct analogues of biological pigments but as well-characterised platforms where phonon engineering is experimentally feasible and electronic properties are independently tuneable — precisely the modularity that biology achieves with separate pigment and scaffold molecules.
- A **nanopatterned dielectric scaffold** (the signal source) — a phononic crystal with a lithographically defined band structure that mimics the vibrational spectral density $J(\omega)$ of a photosynthetic protein.
- An **acoustic isolation layer** — preventing phonon leakage into the substrate, analogous to the hydrophobic protein core.

The Hamiltonian for such a hybrid system takes the form:

$$H_{\text{hybrid}} = H_{\text{BCS}} + H_{\text{scaffold}}$$

where $H_{\text{BCS}}$ describes the superconducting state of the conducting layer (the workers: Cooper pairs) and $H_{\text{scaffold}}$ introduces the static, biologically-inspired phononic drive (the signal). Unlike a laser-driven superconductor, where the signal is externally applied and transient, a scaffolded superconductor would receive a continuous signal from its permanently structured environment — precisely as a photosynthetic protein does.

### 7.3 From Floquet Engineering to Static Design

Current approaches to light-induced superconductivity use Floquet engineering — periodic driving by an external laser — to create transient superconducting states. These states persist only as long as the laser is on. The biological insight is that a **static** phononic environment, permanently structured to provide the necessary spectral density, could achieve the same effect without external driving. The protein scaffold is, in essence, a room-temperature Floquet engineer that has been running continuously for 3.5 billion years. Replicating this in synthetic materials is the central challenge — and opportunity — of bio-inspired quantum engineering.

## 8. Conclusion

Proteins activate electrons by generating structured bosonic signals — phonons whose frequencies are tuned to the energy gaps between electronic states — that guide fermionic workers (electrons, excitons, radicals) through the steps of energy transduction and chemical transformation. The Signal-Worker ontology captures this functional division: the boson carries information, the fermion performs work, and the protein scaffold is the hardware that programs the signal.

This reframing resolves several puzzles at once:

- **Why is photosynthesis so efficient?** Because the protein scaffold provides a phonon spectrum matched to the excitonic landscape, enabling ENAQT to guide excitons to the reaction centre before they can decay.
- **Why are proteins modular?** Because separating the signal source (scaffold) from the worker (cofactor) allows each to be optimised independently — a design principle absent in conventional superconductors.
- **Why is biology homochiral?** Because chirality introduces spin selectivity into electron transport, adding a dimension of control — electron spin — that is unavailable in achiral environments.
- **What can engineers learn?** That room-temperature quantum devices may be achievable not by fighting thermal noise, but by structuring it — turning random vibrations into a programmed signal, exactly as proteins do.

The study of how proteins activate electrons is thus not only a question of biochemistry but a window into the design principles that nature has perfected for quantum engineering at ambient temperature.

---
## References

1. Quni-Gudzinas, R. B. (2026). The Bosonic Signal Hypothesis: Unifying Photosynthetic Energy Transduction and Ambient Superconductivity via a Non-Dualistic Signal-Worker Ontology. Zenodo. `[Obsidian\releases\2026\01\]`
2. Quni-Gudzinas, R. B. (2025). A Phenomenological Langevin Model for Asymmetric Electron Transport Arising from Intrinsic Structural Chirality. Zenodo. `[Obsidian\releases\2025\12\]`
3. Quni-Gudzinas, R. B. (2025). Particles, Proteins, and the Periodic Table: Peering into the Processes of the Physical World. QNFO. `[Archive\releases\]`
4. Quni-Gudzinas, R. B. (2025). Matter without Mass II-3: Geometric Electron. `[Obsidian\releases\2025\00\]`
5. Chen, M. et al. (2020). Vibrational spectral densities of photosynthetic proteins. *In preparation* (cited in Bosonic Signal Hypothesis).
6. Panitchayangkoon, G. et al. (2010). Long-lived quantum coherence in photosynthetic complexes at physiological temperature. *PNAS*, 107(29), 12766–12770.
7. O’Reilly, E. J. & Olaya-Castro, A. (2014). Non-classicality of the molecular vibrations assisting exciton energy transfer at room temperature. *Nature Communications*, 5, 3012.
8. Rebentrost, P. et al. (2009). Environment-assisted quantum transport. *New Journal of Physics*, 11, 033003.