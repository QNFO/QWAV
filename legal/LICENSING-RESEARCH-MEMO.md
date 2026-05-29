# QWAV Licensing Research Memorandum — Best Practices & Recommendations

**Document Type:** Program-Level Research Memorandum  
**Date:** 2026-05-29  
**Author:** Program Agent (v3.4)  
**Status:** PENDING USER APPROVAL  
**Reference:** QWAV-ULA v2.0 (draft at `QWAV/legal/QWAV-UNIFIED-LICENSE-v2.0.md`)

---

## 1. Executive Summary

This memorandum presents research findings on licensing best practices for mixed-media research portfolios and provides concrete recommendations for the QWAV Unified License Agreement. **The core recommendation is CC BY-NC-SA 4.0 as the base license** (per your choice to retain ShareAlike), supplemented with QWAV-specific terms for prior art citation, liquidated damages, AI ethics, and international enforcement — drawing on best practices from Creative Commons, the RAIL Initiative, and established dual-licensing precedents.

---

## 2. Research Findings

### 2.1 Creative Commons License Selection for Research Organizations

**Source:** Creative Commons, SPARC, COAR, cOAlition S (Plan S), multiple university research guides.

| License | Strengths | Weaknesses | QWAV Fit |
|:--------|:----------|:-----------|:---------|
| **CC BY 4.0** | Gold standard for open access; Plan S compliant; maximum reuse | Allows full commercial exploitation; no copyleft | ❌ Too permissive — no commercial protection |
| **CC BY-NC 4.0** | Prevents commercial exploitation; common among researchers | No copyleft — derivatives can be made proprietary (just non-commercial); not OSI/FSF "open" for code | ⚠️ Weaker than desired |
| **CC BY-NC-SA 4.0** | Prevents commercial exploitation + copyleft; ecosystem stays open; used by major journals (PMC) | Less compatible with other licenses (SA requirement); not OSI/FSF "open" | ✅ **RECOMMENDED** — matches your "Keep ShareAlike" preference |
| **CC BY-SA 4.0** | Copyleft without NC; OSI-compatible | Allows commercial use | ❌ No commercial protection |
| **CC0** | Maximum reuse for data; recommended by Figshare, Dryad | No attribution requirement; no commercial restrictions | ❌ Too permissive |

**Key Finding:** CC BY-NC-SA 4.0 is the appropriate choice for a research portfolio that prioritizes non-commercial use with copyleft protection. It ensures that derivatives of QWAV work must also be non-commercial and share-alike, creating a self-reinforcing ecosystem.

**Important:** CC 4.0 licenses are designed to be **international** — they do not require porting to specific jurisdictions (unlike CC 3.0). This is critical for your international enforcement requirement.

### 2.2 ShareAlike (SA) — Practical Implications

**Source:** Creative Commons FAQ, Wikimedia Meta-Wiki, Reddit r/creativecommons, Utah State University LibGuide.

- **Without SA (CC BY-NC):** Someone can take QWAV work, modify it, and release the derivative under a different license — including one that allows commercial use by downstream parties (as long as the modifier themselves isn't commercial). This creates a "commercial laundering" risk.

- **With SA (CC BY-NC-SA):** Any derivative must use the same license (or a compatible one). The non-commercial restriction propagates through the derivative chain. This is stronger copyleft.

- **Academic impact:** SA is supported by major publishers (PMC uses CC BY-NC-SA 4.0). Researchers who build on SA-licensed work must share their derivatives under the same terms, which aligns with open science values.

- **Code impact:** NC+SA licenses are NOT considered "open source" by OSI/FSF. This means QWAV code won't be listed as "open source" on platforms that filter by OSI-approved licenses. **This is acceptable for QWAV's goals** — you're not seeking OSI approval; you're seeking non-commercial protection.

### 2.3 Liquidated Damages in IP Licenses — Enforceability

**Source:** Jacobsen v. Katzer (Fed. Cir. 2008), Artifex v. Hancom (N.D. Cal. 2017), MDY Industries v. Blizzard (9th Cir. 2011), National Law Review, Open Source Guides.

**Key precedents:**

| Case | Holding | Relevance to QWAV |
|:-----|:--------|:------------------|
| **Jacobsen v. Katzer** (2008) | Open source license terms are enforceable copyright **conditions**, not mere covenants. Violation = copyright infringement. | Supports enforceability of license conditions like NC and SA. |
| **Artifex v. Hancom** (2017) | GPL is an enforceable **contract**. Court recognized monetary damages for breach. | Supports liquidated damages as contractual remedy. |
| **MDY v. Blizzard** (2011) | Distinction between covenants (contract remedy) and conditions (copyright remedy). Money damages alone don't support copyright exclusion right. | Supports that liquidated damages are a contract remedy, while NC/SA are copyright conditions — dual enforcement paths. |

**Liquidated damages design principles:**
1. Must be a **reasonable pre-estimate** of actual damages, not a penalty
2. Actual damages must be **difficult to quantify** at the time of contracting
3. **85% of gross revenue** is aggressive but defensible if properly justified as a pre-estimate (the QNFO v1.1 and ASLA both use this figure with the "difficult to quantify" justification)
4. Courts in the US, UK, Switzerland, and most civil law jurisdictions enforce liquidated damages clauses that meet these criteria

**Recommendation:** Retain the 85% figure with the existing justification language. Add explicit language that this is a pre-estimate, not a penalty. The QNFO v1.1 already does this well.

### 2.4 Dual Licensing — Accepted Practice

**Source:** MySQL, Qt, MongoDB, national law review, Open Source Guides.

Dual licensing (base CC license + supplementary terms) is a well-established practice:
- **MySQL:** GPL + commercial license
- **Qt:** LGPL/GPL + commercial license
- **MongoDB:** SSPL (controversial but valid)
- **RAIL Initiative:** Base open license + behavioral-use restrictions

The QWAV approach of CC BY-NC-SA 4.0 + QWAV Supplemental Terms follows this established pattern. Courts have upheld dual-licensing structures. The key requirement is clarity about which terms apply and how they interact.

### 2.5 AI-Specific Behavioral Restrictions — RAIL Licenses

**Source:** RAIL Initiative (licenses.ai), BigScience OpenRAIL-M, Hugging Face, OECD.AI, Montreal AI Ethics Institute.

The **Responsible AI Licenses (RAIL)** represent best practice for AI-related content licensing in 2024-2026:

- **Behavioral-use clauses** restrict specific harmful uses (e.g., surveillance, criminal justice profiling, disinformation)
- **OpenRAIL** licenses are permissive but with use-restrictions
- **BigScience BLOOM RAIL v1.0** was the first major deployment
- RAIL licenses are gaining adoption in the ML community
- The OECD has endorsed RAIL as a practical tool for implementing AI ethics principles

**Relevance to QWAV:** The ASLA already includes an ethical preamble and restrictions on "restricting human invention, dignity, or well-being." This aligns with the RAIL approach. Consider adding explicit prohibited AI uses inspired by RAIL.

### 2.6 Prior Art Citation — Patent Law Basis

**Source:** 35 U.S.C. § 102, EPC Article 54, USPTO MPEP § 2001, Patent Law Article 22 (China), Patent Act Article 29 (Japan).

The prior art citation clause in QNFO v1.1 §4.2 has a solid legal foundation:

- **US:** 35 U.S.C. § 102 — prior art includes anything publicly available before the effective filing date. The duty of candor (37 CFR 1.56) already requires disclosure of known material prior art.
- **Europe:** EPC Article 54 — absolute novelty requirement. QWAV publications = prior art.
- **China:** Patent Law Article 22 — similar novelty standard.
- **Japan, Korea, India:** All have similar prior art definitions.

The QNFO clause **reinforces** existing legal obligations with a contractual requirement. Failure to cite = both patent invalidity risk AND breach of contract. This dual enforcement mechanism is sound.

### 2.7 Database Rights — EU Sui Generis Protection

**Source:** EU Database Directive 96/9/EC, Creative Commons Wiki on 4.0/Sui generis database rights.

- The EU Database Directive creates **sui generis database rights** (SGDRs) — separate from copyright — protecting substantial investment in database creation (15-year term)
- CC 4.0 licenses explicitly cover SGDRs (unlike CC 3.0, which excluded them)
- **QWAV data, glossaries, indices, and structured datasets** may qualify for SGDR protection in the EU
- The CC BY-NC-SA 4.0 license already covers these rights through its definition of "Licensed Rights"

**Recommendation:** The unified license should explicitly reference that it covers database rights, as CC 4.0 does. No additional clause needed beyond what CC 4.0 provides, but explicit mention is good practice.

### 2.8 International Enforcement — Swiss Law + ICC Arbitration

**Source:** New York Convention (1958), ICC Arbitration Rules, Swiss Private International Law Act.

| Element | Rationale |
|:--------|:----------|
| **Swiss governing law** | Neutral jurisdiction; strong IP tradition; not aligned with any major tech power; respected internationally |
| **ICC arbitration, Geneva** | ICC is the world's leading arbitral institution; Geneva is neutral; English language ensures accessibility |
| **New York Convention** | 170+ signatory nations must enforce arbitral awards; gives QWAV enforcement reach in virtually every jurisdiction |
| **CC 4.0 international design** | CC 4.0 is designed as a single, globally-applicable license (no porting needed) |

**This is robust.** The combination of Swiss law + ICC arbitration + New York Convention + CC 4.0's international design provides excellent international enforceability.

### 2.9 SPDX Identifier — Machine-Readable Licensing

**Source:** SPDX (Software Package Data Exchange), Linux Foundation, npm, PyPI.

SPDX identifiers enable automated license compliance checking:
- `CC-BY-NC-SA-4.0` is a standard SPDX identifier
- Package managers (npm, PyPI, cargo) use SPDX for license fields
- GitHub, GitLab auto-detect licenses via SPDX
- Custom licenses can register custom SPDX identifiers

**Recommendation:** Register `QWAV-ULA-2.0` as a custom SPDX identifier or use `LicenseRef-QWAV-ULA-2.0` in `package.json` files. Include the SPDX identifier in all code file headers.

---

## 3. Policy Recommendations — Specific Modifications

### 3.1 MODIFICATION 1: Add ShareAlike (CC BY-NC-SA 4.0)

**Change:** Replace "CC BY-NC 4.0" with "CC BY-NC-SA 4.0" throughout.

**Rationale:** Your explicit preference. SA prevents "commercial laundering" through derivative works. Derivatives must remain non-commercial and share-alike.

**Text change in §1.1:**
> ~~Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)~~
> **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**

### 3.2 MODIFICATION 2: Add AI Behavioral-Use Restrictions (RAIL-Inspired)

**New Section §2.2 — Prohibited AI Uses:**

Inspired by RAIL licenses and the ASLA preamble, add explicit prohibitions on:
- Using QWAV Content to train AI systems for surveillance, predictive policing, or criminal justice profiling
- Using QWAV Content to generate or disseminate disinformation at scale
- Using QWAV Content in autonomous weapons systems or military applications that violate international humanitarian law
- Using QWAV Content for mass psychological manipulation or exploitative behavioral engineering

**Rationale:** This aligns with the ASLA's ethical preamble and follows RAIL best practices for AI-related content. It gives the license "teeth" for ethical enforcement beyond general "ethical use" language.

### 3.3 MODIFICATION 3: Strengthen Database Rights Coverage

**New language in §1.1 or as §1.3:**

> "This license covers all rights in the Content, including but not limited to copyright, sui generis database rights (as defined in EU Directive 96/9/EC and equivalent protections worldwide), and any other intellectual property rights held by Licensor."

**Rationale:** CC 4.0 already covers SGDRs, but explicit mention ensures clarity for EU enforcement and signals awareness of database protections to potential licensees.

### 3.4 MODIFICATION 4: Add SPDX Identifier and Machine-Readable Provisions

**New Section §9.6 — Machine-Readable Licensing:**

> "The SPDX License Identifier for this Agreement is `LicenseRef-QWAV-ULA-2.0`. All code files governed by this Agreement should include the header:
> ```
> SPDX-License-Identifier: LicenseRef-QWAV-ULA-2.0
> Copyright (c) YYYY Rowan Brad Quni-Gudzinas
> ```
> This enables automated license compliance checking by package managers and development tools."

**Rationale:** Industry best practice for code licensing. Enables automated compliance.

### 3.5 MODIFICATION 5: Add License Compatibility Section

**New Section §9.7 — License Compatibility:**

> "The ShareAlike requirement of CC BY-NC-SA 4.0 means that derivative works must be licensed under CC BY-NC-SA 4.0, this Agreement, or a Creative Commons Compatible License as defined by Creative Commons. For purposes of this Agreement, CC BY-NC-SA 4.0 alone (without the QWAV Supplemental Terms) is considered a compatible license for the ShareAlike requirement. However, the Supplemental Terms apply only when this Agreement is the governing license."

**Rationale:** Clarifies what "compatible" means for SA purposes. Allows derivatives to use plain CC BY-NC-SA 4.0 without the supplemental terms (attribution still required, but liquidated damages and prior art clauses don't propagate to derivatives that don't use this Agreement).

Wait — this is actually a design question. Should the supplemental terms (liquidated damages, prior art) propagate with SA? Or only the CC part?

I recommend: The CC BY-NC-SA 4.0 portion propagates via SA (that's what SA does). The supplemental terms do NOT propagate — they only bind the original licensee. This is more defensible legally and more practical. Derivatives must use CC BY-NC-SA 4.0 (or this Agreement), but the damages clauses only apply to direct licensees of the original.

### 3.6 MODIFICATION 6: Add "Separate Commercial License" Framework

**Strengthen §9.5:**

Add explicit language:
> "Licensor may, at Licensor's sole discretion, grant separate commercial use licenses on a case-by-case basis. Such licenses will be documented in a separate written agreement. Nothing in this Agreement obligates Licensor to grant commercial licenses, and the availability of commercial licensing does not constitute a waiver of any rights under this Agreement."

**Rationale:** Standard dual-licensing practice (MySQL, Qt model). Provides a legal pathway for entities that want to use QWAV work commercially with permission, while maintaining the default NC restriction.

### 3.7 MODIFICATION 7: Explicit Reference to International Treaty Framework

**Strengthen §7.4:**

Add explicit references to specific treaty articles:
- Berne Convention Article 2 (protected works), Article 5 (national treatment)
- TRIPS Agreement Article 9-14 (copyright), Article 27-34 (patents)
- WIPO Copyright Treaty Article 4 (computer programs), Article 5 (databases)

**Rationale:** Strengthens international enforceability by anchoring to specific treaty provisions that signatory nations must implement domestically.

---

## 4. What NOT to Change (Why Existing Provisions Are Sound)

| Provision | Why Keep As-Is |
|:----------|:---------------|
| **85% liquidated damages** | Established in both ASLA and QNFO v1.1; courts enforce if characterized as reasonable pre-estimate; current justification language is adequate |
| **Swiss law + ICC Geneva** | Optimal neutral forum; New York Convention coverage is comprehensive; no reason to change |
| **Prior art patent citation (§4)** | Strong legal foundation in US, EU, CN, JP, KR, IN patent law; contractual reinforcement adds enforcement teeth |
| **$1 USD liability cap** | Standard limitation of liability; protects Licensor while not being unconscionable |
| **Indemnification (§8.3)** | Standard in IP licenses; protects Licensor from licensee misuse |
| **Ethical preamble** | From ASLA; aligns with RAIL best practices; sets interpretive context for the entire license |
| **Name clarification (§6.2)** | Important for chain of title; addresses prior name (Bradley James Gudzinas) for IP filed under either name |

---

## 5. Recommended Unified Text — Summary of Changes

| Section | Change | Source |
|:--------|:-------|:-------|
| §1.1 | CC BY-NC → CC BY-NC-SA | Your "Keep ShareAlike" preference |
| §1.3 (new) | Database rights explicit coverage | EU Database Directive 96/9/EC |
| §2.2 (new) | Prohibited AI uses (RAIL-inspired) | RAIL Initiative, ASLA preamble |
| §5.1 | Strengthen "reasonable pre-estimate" language | Jacobsen, Artifex precedents |
| §7.4 | Specific treaty article references | Berne, TRIPS, WCT |
| §9.5 | Separate commercial license framework | MySQL/Qt dual-licensing model |
| §9.6 (new) | SPDX identifier and machine-readable provisions | SPDX/Linux Foundation |
| §9.7 (new) | License compatibility clarification | CC SA compatibility rules |

---

## 6. Implementation — Recommended Order

1. **Approve modifications** → Update QWAV-ULA v2.0 text
2. **Deploy canonical text** to `https://qwav.tech/legal/license` (Cloudflare Pages)
3. **Register SPDX identifier** (optional, P3)
4. **Replace root LICENSE.md** with pointer
5. **Replace QWAV/LICENSE** with pointer
6. **Replace prompts/LICENSE** with pointer
7. **Update Discovery Index** with new license metadata
8. **Delegate per-project migration** to Projects Agent
9. **Update project initiation protocol** to automatically include new license
10. **Configure Kaizen audit** for license compliance checking

---

*End of Research Memorandum — Pending User Approval*
