# QNFO Strategic Research & Commercialization Framework

**Document Type:** Strategic Memorandum  
**Date:** 2026-05-29  
**Author:** Program Agent (v3.4)  
**Status:** FOR USER APPROVAL  
**Reference:** QNFO-ULA v2.0 at `QWAV/legal/QNFO-ULA-v2.0.md`

---

## 1. The Core Tension

QNFO faces a trilemma familiar to every research organization:

```
         PUBLIC GOOD RESEARCH
         (openness, accessibility, citation)
              /            \
             /              \
            /    TENSION     \
           /                  \
THOUGHT-LEADERSHIP          FUTURE COMMERCIALIZATION
(promotion, reputation,     (licensing, revenue,
 priority establishment)     partner agreements)
```

**The problem:** A maximally restrictive license (CC BY-NC-SA + 85% damages + AI prohibition) protects against exploitation but may deter legitimate engagement. A maximally permissive license (CC BY or CC0) maximizes reach but invites exploitation. Neither extreme serves all three goals.

**The solution:** A single, unified license with a **Licensor-reserved "Publication Exception"** — a mechanism that allows QNFO (and only QNFO) to designate specific content as freely shareable for thought-leadership purposes, while the default protection covers everything else.

---

## 2. Strategic Framework: The "Funnel" Model

```
                    ┌──────────────────────────────┐
                    │   TIER 1: THOUGHT-LEADERSHIP │
                    │   CC BY 4.0 (Publication     │
                    │   Exception content only)    │
                    │                              │
                    │   • Research papers          │
                    │   • Blog posts & articles    │
                    │   • Conference presentations │
                    │   • Educational materials    │
                    │   • High-level concept docs  │
                    │   • Press releases           │
                    │                              │
                    │   PURPOSE: Maximum reach,    │
                    │   citation, reputation,      │
                    │   prior art establishment    │
                    └──────────────┬───────────────┘
                                   │
                                   │ Attracts attention,
                                   │ establishes credibility
                                   ▼
                    ┌──────────────────────────────┐
                    │   TIER 2: PROTECTED CORE IP  │
                    │   QNFO-ULA v2.0 (default)    │
                    │                              │
                    │   • Source code              │
                    │   • Production systems       │
                    │   • Detailed formalisms      │
                    │   • Training data & models   │
                    │   • Datasets & databases     │
                    │   • Prompt templates         │
                    │   • Internal documentation   │
                    │                              │
                    │   PURPOSE: Protection from   │
                    │   exploitation, licensing    │
                    │   leverage, IP preservation  │
                    └──────────────┬───────────────┘
                                   │
                                   │ Serious adopters
                                   │ need to engage
                                   ▼
                    ┌──────────────────────────────┐
                    │   TIER 3: COMMERCIAL ACCESS  │
                    │   Separate Agreement (§10.7) │
                    │                              │
                    │   • Commercial licenses      │
                    │   • Research partnerships    │
                    │   • Revenue-share agreements │
                    │   • Public-benefit deals     │
                    │                              │
                    │   PURPOSE: Revenue, impact,  │
                    │   mission-aligned commercial │
                    │   deployment                 │
                    └──────────────────────────────┘
```

### How This Works in Practice

**Step 1 — QNFO publishes a paper** describing a new theory or framework.
- **License:** CC BY 4.0 (Publication Exception)
- **Effect:** Anyone can read, cite, share, build on the paper. Maximum academic reach. Establishes prior art. Builds QNFO's reputation.
- **Example:** "QNFO publishes 'Functional Topologic Computing: A New Paradigm' under CC BY on arXiv and qnfo.org."

**Step 2 — The paper references an implementation** available in QNFO's code repository.
- **License:** QNFO-ULA v2.0 (Protected Core)
- **Effect:** Researchers can use the code for non-commercial work. Companies wanting to commercialize must engage with QNFO.
- **Example:** "The reference implementation is available at github.com/QNFO/ftc-core under QNFO-ULA v2.0."

**Step 3 — A company wants to build a product** using QNFO's implementation.
- **Pathway:** §10.7 Commercial License Request
- **Effect:** QNFO negotiates a commercial agreement. Terms may include revenue sharing, public benefit commitments, or other conditions.
- **Example:** "Acme Corp licenses QNFO's FTC framework for their quantum simulation platform under a revenue-share agreement with open-source contribution commitments."

### Why This Works

| Goal | How It's Served |
|:-----|:----------------|
| **Public Good Research** | Tier 1 (CC BY) ensures maximum dissemination of ideas. Papers are freely accessible, citable, and buildable. |
| **Thought-Leadership** | Tier 1 content spreads widely. Attribution requirements ensure QNFO gets credit. Prior art is established. |
| **Protection from Exploitation** | Tier 2 (QNFO-ULA) prevents unauthorized commercial use of valuable IP. 85% damages deter violations. |
| **Future Commercialization** | Tier 3 (§10.7) provides a structured pathway for mission-aligned commercial partnerships. |
| **Unified Licensing** | ONE license governs everything. The Publication Exception is a RIGHT RESERVED BY LICENSOR, not a separate license regime. |

---

## 3. The "Publication Exception" — License Modification

### 3.1 Current Problem

The QNFO-ULA v2.0 applies uniformly to ALL Content. This means:
- A blog post about QNFO's research is under the same restrictive license as QNFO's production code
- A journalist wanting to quote QNFO's paper needs to navigate CC BY-NC-SA + supplemental terms
- A conference wanting to include QNFO's presentation in proceedings faces the same restrictions

This creates unnecessary friction for thought-leadership content that QNFO WANTS to spread widely.

### 3.2 Proposed Addition: Section 1.5 — Publication Exception

Add to the QNFO-ULA:

> **1.5 Publication Exception — Licensor-Designated Public Content**
>
> Notwithstanding any other provision of this Agreement, Licensor may, at Licensor's sole discretion, designate specific Content as **"Public Content"** subject to more permissive terms. Public Content shall be clearly marked as such through:
>
> (a) A prominent notice in the Content itself (e.g., "Licensed under CC BY 4.0 as QNFO Public Content");
> (b) A separate license file or metadata accompanying the Content; or
> (c) Publication on a QNFO website or platform with a clear designation of public content status.
>
> Public Content is licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)** only, without the QNFO Supplemental Terms. All other Content remains governed by this full Agreement.
>
> The following types of Content are presumptively eligible for designation as Public Content:
> - Research papers, preprints, and academic publications
> - Blog posts, articles, and public-facing educational materials
> - Conference presentations, posters, and talk materials
> - High-level concept descriptions, white papers, and vision documents
> - Press releases, announcements, and public communications
> - Educational tutorials and documentation intended for broad public dissemination
>
> The following types of Content are presumptively NOT eligible for Public Content designation (and remain governed by the full Agreement):
> - Source code, software, and production implementations
> - Detailed technical specifications, formalisms, and algorithms
> - Training data, model weights, and production AI/ML artifacts
> - Internal development documentation and agent configurations
> - Datasets and databases intended for research or commercial use
> - Prompt templates and AI system instructions
>
> Licensor may designate Public Content at any time, may revoke such designation for future versions of the Content (but not retroactively for copies already distributed), and may establish additional criteria for Public Content designation at Licensor's discretion. The absence of a Public Content designation on any particular Content shall mean such Content is governed by the full terms of this Agreement. This Section 1.5 does not create any obligation for Licensor to designate any Content as Public Content, nor does it create any expectation or entitlement to such designation.

### 3.3 Why This Works Within a Unified Framework

**Key principle:** This is NOT multiple licenses. This is a SINGLE license (QNFO-ULA v2.0) with a Licensor-reserved right to selectively apply more permissive terms to designated content.

- The DEFAULT is full QNFO-ULA protection
- Licensor can CHOOSE to release specific content under CC BY 4.0
- The choice is REVOCABLE for future versions (but not retroactive)
- Everything is still governed by ONE document
- There's no ambiguity about what license applies — Public Content is clearly marked

### 3.4 Comparison: Without vs. With Publication Exception

| Scenario | Without Exception | With Exception |
|:---------|:------------------|:---------------|
| Journalist wants to quote QNFO paper | Must comply with CC BY-NC-SA + supplemental terms | CC BY — free to quote with attribution |
| Researcher wants to build on QNFO theory | Must use SA-compatible license for derivatives | CC BY — free to build on with attribution |
| Company wants to use QNFO code | Must comply with QNFO-ULA or get commercial license | SAME — protected by QNFO-ULA |
| Conference includes QNFO talk in proceedings | Must negotiate license terms | CC BY — free to include |
| Textbook author references QNFO work | Must comply with NC restriction (textbook = commercial?) | CC BY — free to reference |
| AI company scrapes QNFO website | Protected by QNFO-ULA | SAME — website content is not necessarily Public Content |

---

## 4. Practical Implementation — "What QNFO Actually Does"

### 4.1 Content Classification Guide

**PUBLIC CONTENT (CC BY 4.0) — Publish freely, maximize reach:**

| Content Type | Rationale |
|:-------------|:----------|
| Research papers (arXiv, journals) | Academic dissemination; prior art establishment; citation building |
| Blog posts on qnfo.org | Thought-leadership; SEO; community building |
| Conference talks & slides | Promotion; networking; talent attraction |
| Whitepapers & vision documents | Industry positioning; partner attraction |
| Educational tutorials | Community building; lowering barriers to entry |
| Press releases | Media coverage; public awareness |

**PROTECTED CONTENT (QNFO-ULA v2.0) — Default protection:**

| Content Type | Rationale |
|:-------------|:----------|
| Source code in repositories | Core IP; licensing leverage |
| Production systems & tools | Commercial value; competitive advantage |
| Detailed technical specifications | Implementation IP; patent protection |
| Training data & model weights | Valuable asset; AI exploitation risk |
| Structured datasets | Database rights; research asset |
| Prompt templates & agent configs | Operational IP; system integrity |
| Internal documentation | Competitive sensitivity |

### 4.2 How to Mark Content

**For Public Content (CC BY 4.0):**

```markdown
> **License:** This document is QNFO Public Content, licensed under
> CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).
> You are free to share and adapt with attribution.
> This document is NOT subject to the full QNFO-ULA v2.0.
```

**For Protected Content (QNFO-ULA v2.0):**

```
SPDX-License-Identifier: LicenseRef-QNFO-ULA-2.0
Copyright (c) 2026 Rowan Brad Quni-Gudzinas
Licensed under QNFO-ULA v2.0: https://qnfo.org/legal/license
```

### 4.3 Website & Platform Strategy

**qnfo.org/public/** — Public Content directory
- Research papers, blog posts, talks, educational materials
- All under CC BY 4.0
- SEO-optimized, shareable, citable
- Clear "CC BY 4.0" badge on every page

**qnfo.org/research/** — Protected research assets
- Code repositories, datasets, detailed specifications
- All under QNFO-ULA v2.0
- Access may require acknowledgment of license terms
- Clear "QNFO-ULA v2.0" badge

**github.com/QNFO/** — Code repositories
- All under QNFO-ULA v2.0 by default
- README clearly states license
- SPDX headers in all files
- Commercial license inquiries directed to §10.7

---

## 5. Thought-Leadership Strategy — Specific Tactics

### 5.1 The "Cite the Paper, License the Code" Model

This is the core strategy used successfully by:
- **MongoDB:** SSPL for code, but extensive public documentation and blog posts
- **HashiCorp:** BSL for products, but Terraform Registry and docs are freely accessible
- **GitLab:** MIT for Community Edition, but enterprise features are proprietary
- **OpenAI:** Papers under permissive terms, but GPT models are proprietary

QNFO's version:
- **Paper/Theory:** CC BY 4.0 (Public Content) — "Here's what we discovered and how it works"
- **Code/Implementation:** QNFO-ULA v2.0 — "Here's the working system — non-commercial use is free; commercial use requires engagement"

### 5.2 Building a Community Around Public Content

The Public Content tier serves as a **community on-ramp**:
1. Someone discovers QNFO through a CC BY paper or blog post
2. They engage with the ideas, cite the work, build their own understanding
3. If they want to use the implementation commercially, they enter the commercial pathway
4. If they're an academic, they use the code under QNFO-ULA for research

### 5.3 The "Prior Art First" Strategy

Every Public Content release establishes prior art:
- Papers on arXiv → public disclosure date
- Blog posts on qnfo.org → public disclosure date
- Conference presentations → public disclosure date

This prevents others from patenting QNFO's ideas. Combined with the QNFO-ULA's prior art citation requirement (§5), this creates a strong IP protection framework.

### 5.4 The "Commercial Funnel"

```
Public Content (CC BY)
    │  10,000 readers
    │  1,000 citations
    │  100 active researchers
    ▼
Protected Core (QNFO-ULA)
    │  50 serious evaluators
    │  20 active non-commercial users
    │  5 commercial inquiries
    ▼
Commercial Agreements (§10.7)
    │  2-3 commercial partnerships
    │  Revenue / public benefit commitments
```

This is the standard open-core funnel used by successful research-to-commercial organizations.

---

## 6. Addressing Potential Objections

### "Doesn't this undermine the unified licensing goal?"

**No.** The unified license IS the QNFO-ULA v2.0. The Publication Exception is a feature OF that license, not a separate license. It's analogous to:

- Creative Commons' own "CC0" designation within their license framework
- The GPL's "classpath exception" — still GPL, but with a specific relaxation
- The LGPL's linking exception — still copyleft, but with a specific relaxation

One document. One framework. Licensor-controlled flexibility.

### "Won't people just use the Public Content and ignore the protected stuff?"

**That's the point.** Public Content is DESIGNED to be widely used. It serves the thought-leadership goal. The protected core is for those who need the actual implementation — and those are the people QNFO wants to engage with commercially.

### "Can't someone reconstruct the protected implementation from the Public Content?"

**In theory, yes** — if the Public Content describes the implementation in sufficient detail. This is a risk. Mitigation:
1. Public Content describes WHAT and WHY at a high level
2. Protected Content contains the HOW in detail
3. The implementation gap requires significant engineering investment
4. Most companies would rather license than reconstruct

### "What about AI companies training on Public Content?"

The QNFO-ULA's AI prohibitions (§2.1, §2.2(e)) apply to Protected Content. Public Content under CC BY 4.0 can be used for AI training (that's inherent in CC BY). However:
1. Public Content is high-level concepts, not training data
2. The valuable AI training data (code, datasets, models) is Protected Content
3. If AI training on Public Content becomes a concern, QNFO can revoke the Public Content designation for future versions

---

## 7. Recommended License Modification

Add to QNFO-ULA v2.0, after Section 1.4 (Database Rights) and before Section 2 (Permitted Uses):

**New Section 1.5 — Publication Exception:**

(Full text as drafted in Section 3.2 above)

---

## 8. Decision Required

| Question | Recommendation |
|:---------|:---------------|
| Add §1.5 Publication Exception to QNFO-ULA? | ✅ YES — Enables thought-leadership without undermining protection |
| Keep everything else as-is? | ✅ YES — No other changes needed |
| Apply all 6 legal research fixes from supplement? | Pending your review of LEGAL-RESEARCH-SUPPLEMENT.md |

---

## 9. Summary — The Unified Strategy

| Layer | Content | License | Purpose |
|:------|:--------|:--------|:--------|
| **Promotion** | Papers, blogs, talks | CC BY 4.0 (via §1.5) | Reach, reputation, prior art |
| **Protection** | Code, data, specs | QNFO-ULA v2.0 (default) | IP protection, licensing leverage |
| **Commercialization** | Partnerships | Separate agreement (§10.7) | Revenue, impact, mission alignment |

**One license. Three functions. Zero contradictions.**

---

*End of Strategic Framework — Pending User Approval*
