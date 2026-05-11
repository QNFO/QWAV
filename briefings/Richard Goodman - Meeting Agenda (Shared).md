# Meeting Agenda: QWAV × apoth3osis — Formal Verification Collaboration

**For:** Richard Goodman, Apoth3osis Labs
**From:** Rowan, QWAV
**Date:** May 2026
**Format:** Video call — open discussion, no slides, real conversation

---

## Why We're Here

Richard — thank you for reaching out through the QWAV website in April, and for the substantive six weeks of email exchange that followed. It's rare. Most people skim the abstract and move on. You engaged with the actual mathematics, asked hard questions, and proposed three concrete collaboration shapes. That kind of intellectual seriousness deserves a real conversation, so that's what this is.

This document is not a pitch deck. It's an agenda — a map of what I'd like to explore with you, what I'm bringing to the table, what I don't know yet, and where I think the honest tensions are. I'm sharing it ahead of time so you can come in knowing exactly where my head is at, and we can spend our time on the actual conversation rather than me monologuing context.

---

## 1. Meeting Goals

Three things I want to walk away with:

1. **A shared understanding** of what's worth formalizing and what's not ready
2. **A scoped first target** — probably the strong triangle inequality → error confinement chain, which I think is the right entry point
3. **Clarity on how we'd work together** — timeline, division of labor, IP boundaries

Everything else — the deeper ultrametric triangulation with Veselov's $\mathbb{F}_2^n$ work, the substrate-level questions, the hardware-vs-software debate — those are conversations to have, but not decisions to make in one call.

---

## 2. Running Agenda

| Time | Topic | What I Want to Cover |
|:-----|:------|:---------------------|
| 5 min | **Opening** | Thank you. The Veselov precedent. Why this matters to me. |
| 10 min | **What We've Built** | Tier 0 computational results: error confinement, barrier scaling, strong triangle inequality validation |
| 10 min | **The Core Theorem** | The threshold theorem concept — what's novel, what's formalizable, what's parameterizable with real data |
| 10 min | **The Ask** | Scope: start with strong triangle inequality → error confinement. Timeline. Division of labor. |
| 5 min | **The Honest Tension** | We disagree on hardware-vs-software. That's fine. Let's scope it out and focus on what we agree on. |
| 5 min | **Next Steps** | What I'll send you. What I need from you. When we talk next. |

**Total: ~45 minutes.** Flexible — if we go deep on one topic, the rest can wait.

---

## 3. What I'm Bringing

### Computational Results (Tier 0)

Since our email exchange, I've built a validation suite. Nothing peer-reviewed — this is Python code that anyone can run. Here's what it shows:

| Result | Method | Key Finding |
|:-------|:-------|:------------|
| **Strong triangle inequality** | 15,000 random trials across primes 2, 3, 5 | Zero violations. The inequality holds exactly — this is expected mathematically, but verifying it computationally matters for the formalization target |
| **Error confinement** | Bruhat-Tits tree encoding vs. flat encoding, variable physical error rates | Tree encoding: zero logical error at depth 3+ for physical error rates up to 40%. Flat encoding: LER up to 15.2%. The comparison makes the geometric advantage visible |
| **Energy barrier scaling** | Exhaustive verification for small depths | $E_{\text{barrier}}(d) = 2^d$ confirmed. This is the geometric protection mechanism |

The code is in Python (`simulations/experiment_0a.py`, `experiment_0b.py`, `btree.py`). I'll share the repository after the call — you can run it, inspect it, break it. That's the point.

### The Theorem I Want to Formalize

Here's the informal statement. I have a more formal \LaTeX version I'll send separately.

> **Threshold Theorem for Ultrametric QEC (informal):**
> In a Bruhat-Tits tree encoding of depth $d$ over $\mathbb{Q}_p$, with physical error rate $p_{\text{err}}$ per leaf qubit, the logical error rate at the root satisfies $p_{\text{logical}} \leq C \cdot p_{\text{err}}^{k \cdot d}$ for constants $C, k$ determined by the tree structure and error model.
>
> **Corollary:** There exists a threshold $p_{\text{thresh}}$ such that for all $p_{\text{err}} < p_{\text{thresh}}$, $p_{\text{logical}} \to 0$ as $d \to \infty$. This threshold is geometric — determined by the strong triangle inequality — not measurement-based.

**Why this theorem:**

- The mathematical objects (trees, probability bounds, ultrametric inequalities) are all definable in Lean 4
- It's parameterizable with real published data — plug in qubit error rates from Google, IBM, Rigetti; no new lab experiments needed
- It's analogous to the surface code threshold theorem (Kitaev, 1990s) — a known, respected class of results
- **It's publishable regardless of outcome.** If the bound doesn't hold, that's a valuable negative result. If it does, it's a new fault-tolerance mechanism
- The strong triangle inequality → error confinement chain is the right entry point: mathematically clean, computationally validated, and narrow enough to formalize in weeks rather than months

### Published Parameters We Can Use

I'm not asking anyone to run experiments. The conditional proof is what matters: **IF** physical error rates are below a threshold (using real published numbers), **THEN** the tree encoding provides fault tolerance.

| Source | Parameter | Value |
|:-------|:----------|:------|
| Google (2023) | Superconducting qubit $T_1, T_2$ | ~20–100 µs |
| IBM (2024) | Gate fidelity (Heron) | ~99.9% |
| Quantinuum (2024) | Trapped-ion 2-qubit gate fidelity | ~99.8% |
| Various | Cryogenic cooling limits at mK | ~50 µW at ~10 mK |
| Commercial | 4 K cryocooler cooling power | ~1 W |

### Documentation

| Asset | What It Contains |
|:------|:-----------------|
| UQC Release document | 57 numbered citations, full mathematical definitions, 6 testable predictions |
| Technical Deep-Dive | $\Gamma \approx 80$, $E \propto q^d$, Bi-2212 substrate, 5 falsifiable predictions |
| 300+ open-access papers | Zenodo, ResearchGate, SSRN — the full background corpus |

I'll share specific documents after the call based on what's most relevant to the formalization.

---

## 4. The Collaboration I'm Proposing

### Shape #1: Formalization Transport

Of the three collaboration shapes you proposed, **Shape #1 (formalization transport)** is the one I want to start with. Here's why:

- It has the lowest commitment and the most concrete output
- It builds the foundation for Shape #2 (ultrametric triangulation with Veselov's work)
- It produces a citable, verifiable artifact — a co-authored paper with a machine-checked repository
- If the formalization succeeds, the claims are stronger. If it reveals a problem, we find it early. Either outcome is a win.

### Proposed First Deliverable

**Working title:** *A Threshold Theorem for Ultrametric Quantum Error Correction: Formal Verification in Lean 4*

**Content:**
1. Formal definition of Bruhat-Tits tree encoding in Lean 4
2. Statement and proof of the strong triangle inequality for tree-encoded states
3. Derivation of error confinement: $p_{\text{logical}} \leq f(p_{\text{err}}, d)$
4. Proof of exponential suppression with tree depth
5. Parameterization with published experimental data from superconducting qubit platforms
6. Machine-verified repository (zero `sorry`)

**Output:** Co-authored paper + Lean repository, publishable on arXiv/Zenodo.

**Timeline:** Targeting 2–3 months for the first theorem. Incremental — each additional claim becomes a new module.

### How I See the Division of Labor

| Role | What |
|:-----|:-----|
| **My side (Rowan / QWAV)** | Provide the mathematical claims, formal theorem statements, tree structure definitions, error model specifications, and published experimental parameter references. Review the formalization as it develops. |
| **Your side (Richard / apoth3osis)** | Translate claims into Lean 4, prove them, build the verified repository using the HeytingLean infrastructure. |
| **Joint** | Write the paper. Agree on scope. Handle IP boundaries. |

This is a proposal, not a demand — I'm open to whatever division makes the work go fastest.

---

## 5. The Honest Tension

I don't want to pretend we agree on everything when we don't. Here's the elephant:

- Your HeytingLean stack is positioned as QEC verification for IBM — software-based quantum error correction on existing hardware
- My thesis is that software-based QEC is a thermodynamic dead end — the error rates scale wrong, and the cooling requirements become impossible at scale
- We disagree on this. Genuinely.

**Here's why I don't think it matters for this collaboration:**

The formalization transport (Shape #1) is about proving a mathematical claim about tree structures. We don't need to agree on IBM's trajectory to do that. If the ultrametric threshold theorem holds:

- **If hardware QEC works:** It strengthens your verification layer
- **If hardware QEC doesn't scale:** It provides an alternative geometric path
- **Either way:** The proof is useful, the paper is publishable, and the collaboration generates a concrete output

I also want to be honest about why I'm hopeful despite this disagreement:

You told me you were wrong about Veselov — you thought his approach wouldn't work for months, shelved it, then realized it just needed a new language. You changed your mind when the evidence changed. That's exactly the kind of intellectual honesty that makes me want to work with someone even when we disagree. I'm not asking you to change your mind about hardware-vs-software. I'm asking you to apply the same rigor to my tree-structure claims that you applied to Veselov's $\mathbb{F}_2^n$ constructions — and let the Lean proofs decide.

---

## 6. Questions I'd Like to Discuss

### Technical

1. What's the Lean 4 formalization of a tree data structure in HeytingLean? Is there a pre-existing `Tree` or `Graph` module I should be targeting?
2. How do you handle probabilistic claims in Lean? The threshold theorem involves bounds on error probabilities — is there established machinery for this in your stack?
3. What experimental parameters from the quantum computing literature have you already formalized? Qubit error rates, gate fidelities, etc. — I'd rather build on what exists than duplicate.
4. Vladimir's $\mathbb{F}_2^n$ ultrametric structures — how do they relate to Bruhat-Tits trees over $\mathbb{Q}_p$? Is there an existing formal connection, or is that something we'd need to build?

### Collaboration

5. The Veselov collaboration took about a year. What made it take that long, and what would make a QWAV formalization faster (or slower)?
6. You mentioned your other collaborator insisted on patents. How do you typically handle IP in these collaborations? I want to get this right from the start.
7. What's your co-authorship model? Does the Lean repository count as a publication in your view?

### Strategic

8. You were wrong about Veselov — you told me you thought his approach wouldn't work for months. What changed your mind? What should I show you that would change your mind about something you're currently skeptical of?
9. If the ultrametric threshold theorem formalizes, how would you see it fitting into your roadmap? As strengthening the QEC verification layer, or as an alternative path?

---

## 7. IP & Terms — What I Think We Should Discuss

I want to be upfront about IP because it's better to agree on principles before any code is written. Here's my starting position — but this is a discussion, not a demand:

```
Principles I'd propose:

1. Pre-existing IP: Each party retains all rights to their pre-existing
   intellectual property. QWAV's mathematical claims and published corpus
   remain QWAV's. HeytingLean infrastructure remains apoth3osis's.

2. Joint Work: Any new theorems, proofs, or methods discovered during the
   formalization process are jointly owned. Commercial use requires mutual
   agreement.

3. Publication: Co-authorship on the formalization paper. Rowan provides
   the mathematical claims and experimental parameter analysis. Richard
   provides the Lean 4 formalization and verification.

4. Patentable Methods: If the formalization produces patentable methods
   (implementation techniques, not mathematical theorems), the parties
   negotiate commercialization terms in good faith. Mathematical theorems
   per se are not patentable subject matter.

5. Open Access: The Lean repository and paper are published open-access
   (arXiv, Zenodo). The proofs are publicly verifiable.

6. Term: Initial collaboration for one formalization target (threshold
   theorem). Extendable by mutual agreement.
```

A simple email agreement or MOU capturing these principles is probably sufficient for a first project. I'm open to your preferred format.

---

## 8. Proposed Next Steps

| When | What |
|:-----|:-----|
| **After this call** | I send formal theorem statements (\LaTeX), tree structure definitions, error model specifications, and published parameter references |
| **Within 1 week** | We agree on IP terms (email or brief MOU) |
| **Within 2 weeks** | You provide initial assessment: is this formalizable in HeytingLean? What's the scope? |
| **Within 1 month** | First theorem statement checked in Lean (even if partial) |
| **2–3 months** | Target: first theorem fully formalized and verified |

These are targets, not deadlines. I'd rather do it right than do it fast.

---

## 9. What I'll Send After the Call

- Formal theorem statements (\LaTeX)
- UQC Release document (full 57-citation version)
- Tier 0 simulation code (Python — runnable, inspectable)
- Published experimental parameter references with citations
- This agenda document (for your reference)

---

## Appendix A: Who You're Talking To

I want to be transparent about where I'm coming from, because I think it matters for how we collaborate.

**What I am:** An independent researcher with 300+ self-published papers, a computational validation suite, and a mathematical program I believe in. I don't have an academic affiliation, a lab, or institutional backing. My work stands or falls on its substance.

**What I'm not:** I'm not asking you to validate my entire program. I'm not asking you to endorse my substrate-level claims or my philosophical framework. I'm asking you to formalize a specific, narrow, mathematically well-defined claim — the strong triangle inequality → error confinement chain — using your infrastructure and your standards.

**What I value:** Intellectual honesty over politeness. If something doesn't formalize, I want to know. If an axiom is missing, I want to identify it. If the claim is weaker than I think, I want to understand why. The Veselov precedent — where your formalization found and corrected a Table 1 error — is exactly what I want. That's not a risk; that's the point.

**What I bring:** Mathematical claims with computational evidence, a willingness to be wrong, and genuine respect for what you've built with HeytingLean.

---

## Appendix B: Key Technical References

| Asset | What It Contains |
|:------|:-----------------|
| UQC Release | 57 citations, full mathematical definitions, 6 testable predictions |
| Technical Deep-Dive | $\Gamma \approx 80$, $E \propto q^d$, Bi-2212 substrate |
| Tier 0 Simulation | Error confinement (experiment 0A), barrier scaling (experiment 0B), strong triangle inequality validation |
| Richard's polygraphic paper | ResearchGate: 404363291 |
| Richard's boundary draft | https://www.apoth3osis.io/boundary |
| Richard's p-adic page | https://www.apoth3osis.io/paper-proof-code/padic-functional-decoupling |

---

*Prepared May 2026. This is an agenda for our first conversation — not a final proposal. Everything in here is open to discussion, revision, or outright rejection. Let's talk.*
