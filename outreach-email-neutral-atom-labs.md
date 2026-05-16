# Outreach Email — Neutral Atom Labs (P32)

**Purpose:** Email 4 neutral atom quantum computing labs with the ultrametric hardware spec (40-atom $d=3$ ternary Bruhat–Tits tree). Each lab builds neutral atom platforms — the ideal audience to evaluate whether this architecture is buildable with existing hardware.

**Status:** ⏳ DRAFT — NOT YET SENT
**Depends on:** P31 (companion paper on Zenodo — DONE, DOI: 10.5281/zenodo.20208437)
**Supersedes:** P10 (generic cold outreach to NV center labs)

---

## Strategy

| Element | Rationale |
|:--------|:----------|
| **Target neutral atom labs only** | The 40-atom $d=3$ tree architecture maps directly to Rydberg atom arrays — the platform these labs already operate. No exotic hardware required. |
| **Each email references the lab's specific work** | Shows you've read their papers. Generic "Dear Professor" gets deleted. |
| **One specific, answerable question per email** | Binary or short-answer. Reply-able in 30 seconds. |
| **Two Zenodo DOIs as proof** | Computational validation (Tier 0) + symmetric extension (v2 companion). Tangible evidence. |
| **No overclaim** | "We've identified," "computational evidence suggests," "would you agree that" — all honest. |
| **Written-only** | No live pitches. No "let's hop on a call." Email → response → email. |

---

## Targets (4 Labs)

| # | Lab | PI / Contact | Platform | Why Them |
|:--|:----|:-------------|:---------|:---------|
| 1 | **Harvard** | Prof. Mikhail Lukin | Rydberg atom arrays, optical tweezers | Pioneered neutral atom QC. Published 256-atom programmable arrays (Nature 2021, 2022). The 40-atom tree is well within their demonstrated capabilities. |
| 2 | **Caltech** | Prof. Manuel Endres | Neutral atoms in optical tweezers, Rydberg gates | Demonstrated high-fidelity Rydberg blockade gates. Strong neutral atom program with quantum information focus. |
| 3 | **PASQAL** | Antoine Browaeys / Thierry Lahaye | Commercial neutral atom QC (Rydberg arrays) | Founded by Nobel laureate Alain Aspect. Already building neutral atom processors for customers. The 40-atom design maps to their existing hardware architecture. |
| 4 | **Innsbruck** | Institute for Quantum Optics and Quantum Information (IQOQI) / Institute for Experimental Physics, University of Innsbruck | Neutral atoms, optical lattices, quantum simulation | Strong neutral atom program. Multiple groups with optical tweezer capabilities. |

---

## Email 1 — Harvard (Mikhail Lukin)

**Email:** lukin@physics.harvard.edu *(verify before sending)*
**Subject:** A specific hardware design your 256-atom platform could test

Dear Professor Lukin,

Your group's work on programmable Rydberg atom arrays — particularly the 256-atom platform and the mid-circuit readout demonstration — sets the standard for what neutral atom quantum computing can achieve. I'm writing because we've identified a hardware architecture that your existing platform could test with minimal modification.

The design: a 40-atom ternary ($p=3$) Bruhat–Tits tree of depth 3, encoding logical states as majority-vote subtree patterns with Rydberg blockade gates. No active error correction. No repeated syndrome measurements. The tree geometry provides passive error suppression via the strong triangle inequality of ultrametric space.

**Computational evidence (published, open-access):**
- Tier 0 validation (DOI: [10.5281/zenodo.20134944](https://doi.org/10.5281/zenodo.20134944)): Binary Bruhat–Tits trees demonstrate error confinement with logical error rate of zero at depth 3+ for physical error rates up to 40%.
- Tier 1 symmetric extension (DOI: [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437)): Ternary ($p=3$) architecture shows ZERO logical errors at depth 7 (2,187 leaves, 36,000 trials), 48× LER reduction via $q$-ary scatter at zero additional qubit cost, and concatenation proven redundant.

**One question:** Does your group have capacity to evaluate whether the 40-atom $d=3$ ternary tree could be implemented on your existing 256-atom platform as a proof-of-concept demonstration? The architecture requires only standard Rydberg blockade gates on a static atom arrangement — no shuttling, no reconfiguration.

I'm an independent researcher — no institutional affiliation, no lab, no funding. Just computational evidence that the geometry works. Your group is uniquely positioned to test whether it works in hardware.

Thank you for considering this, and for the work that makes this question askable.

Best,
Rowan Brad Quni-Gudzinas
ORCID: [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)

---

## Email 2 — Caltech (Manuel Endres)

**Email:** mendres@caltech.edu *(verify before sending)*
**Subject:** An ultrametric tree architecture for neutral atom arrays

Dear Professor Endres,

Your group's work on high-fidelity Rydberg blockade gates in reconfigurable optical tweezer arrays is exactly the platform that could test an architecture we've been developing computationally.

The architecture: a static 40-atom ternary tree of depth 3 — no atom shuttling, no mid-circuit reconfiguration. Logical states are encoded as majority-vote patterns across subtrees, with the ultrametric geometry providing passive error suppression via the strong triangle inequality. No active QEC. The tree does the work.

**Computational evidence (open-access, published):**
- Tier 0 (DOI: [10.5281/zenodo.20134944](https://doi.org/10.5281/zenodo.20134944)): Binary Bruhat–Tits tree circuits show LER=0 at depth 3+ for physical error rates up to 40%.
- Tier 1 — symmetric extension (DOI: [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437)): Ternary ($p=3$) architecture yields ZERO logical errors at depth 7 across 36,000 trials. 48× LER reduction via $q$-ary scatter with zero additional qubits. Concatenation redundant.

**One question:** Your group has demonstrated repeated error detection (mid-circuit measurement and reuse) in neutral atom arrays. The ultrametric tree eliminates the need for repeated syndrome extraction entirely. Would you be interested in evaluating the computational evidence to assess whether a 40-atom static tree demonstration is within your platform's capability?

I'm independent — no lab, no funding, no institution. The computational evidence is all I can offer. But the neutral atom platform you've built is, as far as I can tell, the only hardware that can test this without modification.

Thank you for your time and for the rigorous experimental work that makes this evaluation possible.

Best,
Rowan Brad Quni-Gudzinas
ORCID: [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)

---

## Email 3 — PASQAL

**Email:** contact@pasqal.com OR antoine.browaeys@institutoptique.fr *(verify before sending)*
**Subject:** A static 40-atom architecture for neutral atom processors

Dear PASQAL team,

Your neutral atom quantum processors — built on the Rydberg atom array platform pioneered by your founders — are among the most advanced in the world. I'm writing because we've developed a computational architecture that maps directly to your existing hardware: a static 40-atom ternary ($p=3$) Bruhat–Tits tree of depth 3, requiring only standard Rydberg blockade gates on a fixed atom arrangement.

**Computational evidence (published, open-access):**
- Tier 0 paper (DOI: [10.5281/zenodo.20134944](https://doi.org/10.5281/zenodo.20134944)): Binary Bruhat–Tits tree circuits demonstrate passive error confinement — LER=0 at depth 3+ for physical error rates up to 40%. No active QEC.
- Tier 1 — symmetric extension (DOI: [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437)): Ternary architecture achieves ZERO logical errors at depth 7 (2,187 leaves, 36,000 trials), 48× error reduction via $q$-ary scatter at zero additional qubit cost, concatenation redundant.

The design operates at 4 K, uses no active syndrome extraction, and requires no atom shuttling or reconfiguration during computation. The tree geometry suppresses errors passively via the strong triangle inequality of ultrametric space.

**One question:** PASQAL's processors already support user-defined atom arrangements. Would the 40-atom $d=3$ ternary tree geometry be executable on your current-generation hardware as a proof-of-concept, or would it require hardware modifications?

I'm an independent researcher — no institution, no funding, no lab. I'm reaching out because PASQAL is one of the few organizations on the planet with neutral atom hardware capable of testing this architecture directly from computational specification.

Thank you for considering this, and for building the hardware that makes the question practical.

Best,
Rowan Brad Quni-Gudzinas
ORCID: [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)

---

## Email 4 — Innsbruck (IQOQI / University of Innsbruck)

**Email:** Contact IQOQI or Institute for Experimental Physics *(verify specific PI before sending)*
**Subject:** An ultrametric tree architecture for neutral atom arrays

Dear colleagues at Innsbruck,

The University of Innsbruck and IQOQI have built one of the world's leading programs in quantum simulation with ultracold atoms — from optical lattices to dipolar quantum gases. I'm writing because we've developed a computational architecture for neutral atom arrays that may align with your experimental capabilities.

The design: a static 40-atom ternary ($p=3$) Bruhat–Tits tree of depth 3. Logical states are encoded as majority-vote subtree patterns. The ultrametric (tree-based) geometry provides passive error suppression via the strong triangle inequality — no active error correction, no repeated syndrome measurements. Operation at 4 K. Standard Rydberg blockade gates on a fixed atom arrangement.

**Computational evidence (open-access, published):**
- Tier 0 (DOI: [10.5281/zenodo.20134944](https://doi.org/10.5281/zenodo.20134944)): Binary Bruhat–Tits tree circuits show LER=0 at depth 3+ for physical error rates up to 40%.
- Tier 1 — symmetric extension (DOI: [10.5281/zenodo.20208437](https://doi.org/10.5281/zenodo.20208437)): Ternary architecture — ZERO logical errors at depth 7 (2,187 leaves, 36,000 trials), 48× error reduction via $q$-ary scatter, concatenation proven redundant.

**One question:** Does any group at Innsbruck / IQOQI currently have the optical tweezer and Rydberg excitation capabilities to evaluate whether the 40-atom $d=3$ ternary tree could be implemented as a proof-of-concept demonstration?

I'm an independent researcher — no institution, no lab. The computational evidence is what I have. Innsbruck's experimental capabilities are what could test it.

Thank you for considering this.

Best,
Rowan Brad Quni-Gudzinas
ORCID: [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)

---

## Follow-Up Protocol

| Trigger | Action |
|:--------|:-------|
| **No response after 2 weeks** | Send ONE brief follow-up: "Just bumping my note from [date]. I know you're busy. The papers are open-access if you'd like to evaluate them on your own timeline. Thanks again." |
| **Still no response** | Move on. Not every door opens. These are busy people. You lose nothing. |
| **Positive response** | Prepare a 1-page technical briefing specific to their platform. Do NOT write it until you know what they need. |
| **Request for call** | Redirect: "I'm most effective in writing — happy to answer any technical questions by email. If a call is essential, I can make it work, but I find detailed written exchange produces better outcomes." |
| **Skeptical response** | Welcome it. Skepticism = engagement. Address each point directly from the computational evidence. Do not defend — explain and offer to provide more detail. |

---

## Alignment with QWAV Strategy

| Constraint | How This Respects It |
|:-----------|:---------------------|
| **Written-only** | All communication is email. No live pitching, no conferences, no networking events. |
| **Substance-first** | Each email references the lab's actual published work and provides DOIs as evidence. No credential positioning. |
| **No overclaim** | "We've identified," "computational evidence suggests," "would you evaluate" — all honest, all falsifiable. |
| **Low-friction** | One question per email. Answerable in under a minute. No attachments — hyperlinks to open-access DOIs instead. |
| **Zero downside** | A no-response or rejection costs nothing. These emails don't burn bridges — they inform people who might be interested. |

---

## Pre-Send Checklist

- [ ] Verify email addresses (check lab websites, recent papers, Google Scholar profiles)
- [ ] Confirm no major announcements from these labs in the past 2 weeks (don't email during a paper storm)
- [ ] Send on a Tuesday–Thursday morning (US/EU time)
- [ ] Test all DOI links
- [ ] Personalize any "Dear colleague" addresses to specific PIs where identifiable
- [ ] Set 2-week follow-up reminders
- [ ] Git commit all outreach documents before sending

---

*P32 — Neutral atom lab outreach. Draft complete. Ready for review and send.*
