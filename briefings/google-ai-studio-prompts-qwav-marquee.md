# Google AI Studio App Builder Prompts — qwav.tech Marquee Page Update

**Date:** 2026-05-22
**Purpose:** Minimal updates to the qwav.tech marquee page. The page is strong overall. These prompts only fix what's outdated and add cross-links to the technical site.
**How to use:** Copy each prompt into Google AI Studio's app builder chat. Apply one at a time. Preview after each.

---

## What's Changing — Summary

| Change | Why |
|:-------|:----|
| Add 3 key publications | The marquee shows 6 older papers but MISSING your best work: Symmetric Extension (zero errors at depth 7), Foundations (credential doc), Q-PNA v2.0 (glass-box AI) |
| Add "Technical Site" link | Bridge from marquee (discovery) to technical site (depth + interactive demos). Currently no way to get from qwav.tech to qnfo.github.io/QWAV/ |
| Add "Interactive Demos" teaser section | A1-A5 coming June 2026. The marquee should tell visitors these are on the way. Builds anticipation. |
| Update meta description | Current meta: "Applied research institute..." Add computational evidence keywords for SEO. |
| Add footer links | Zenodo community, GitHub org. Currently no links to where the actual work lives. |

## What's NOT Changing

- "Applied research institute" framing — KEEP. It's marquee positioning.
- "For Investors" section — KEEP. The marquee's purpose includes investor discovery.
- "For Researchers" section — KEEP. Same reason.
- Revenue model references — KEEP.
- "18+ Provisional Patents" — KEEP.
- Generational Scaling Roadmap — KEEP. Forward-looking vision is what marquees do.
- "This is not an engineering problem. It is a geometry problem." — KEEP. Strong headline.
- Dark theme, design, layout — KEEP. The site looks good.

---

## PROMPT 1: Add Missing Key Publications

```
In the Publications / Open-Access Research section, ADD these 3 publications AFTER the existing ones. Keep all 6 existing publications — just append these at the end:

7. Symmetric Extension of Ultrametric Error Confinement — Ternary Tree Architecture
   DOI: 10.5281/zenodo.20208437
   Date: 2026-05-16
   Key result: Zero logical errors at depth 7. 48x error reduction via scatter at zero qubit cost.

8. Ultrametric Quantum Computing Foundations
   DOI: 10.5281/zenodo.20154557
   Date: 2026-05-15
   Key result: 3,700-word accessible overview. 5 pre-registered falsifiable predictions.

9. Q-PNA: Quantum-Native p-Adic Neural Architecture — Research Specification v2.0
   DOI: 10.5281/zenodo.20287742
   Date: 2026-05-19
   Key result: Glass-box AI. Linear mapping beats transformer 6.6x on hierarchical classification. 100% verification detection.
   GitHub: github.com/QNFO/Q-PNA

Each publication entry should follow the same format as the existing ones: title, DOI link, date, and a one-line key result. Keep all styling consistent with the existing publication cards.
```

---

## PROMPT 2: Add Cross-Link to Technical Site

```
Add a new section or banner between the header/nav and the first content section (or as the last nav item, or as a small banner at the top of the page):

"Technical Site & Interactive Demos → qnfo.github.io/QWAV/"

Design: Subtle but clickable. A small pill/badge style, matching the existing color scheme (indigo/white). Not a full-width banner — something compact.

Also add the same link in the footer.

This is the bridge from the marquee page (discovery/SEO) to the technical site where all publications, code, and interactive demos live. The marquee page gets people interested. The technical site gives them everything.
```

---

## PROMPT 3: Add Interactive Demos Teaser

```
Add a new section called "Interactive Demos" (or "Coming Soon") that shows what's being built. Place it after the Technology section or after Publications.

Use card-style layout matching the existing design. Three cards, each with a title and one-line description:

1. Error Confinement Live Demo — Watch ultrametric geometry suppress errors in real time. Adjust error rates and tree depth with sliders. (Coming June 2026)

2. Q-PNA Classifier Playground — Explore glass-box AI decision trees. Train on sample problems. See WHY a classification was made. (Coming June 2026)

3. Ultrametric Convergence Explorer — Watch hierarchical dynamics in action. See why diversity collapses into uniformity — not by design but by geometry. (Coming June 2026)

Each card should link to: qnfo.github.io/QWAV/

Design: Cards should be visually distinct from the publication cards — maybe with a subtle "coming soon" badge or slightly different background. The section communicates: "Don't just read about it. Soon you'll be able to watch it happen."
```

---

## PROMPT 4: Update Meta Description (SEO)

```
Update the page's meta description tag to:

"QWAV replaces the continuous-geometry assumption underlying quantum computing with ultrametric geometry. Computational evidence: zero logical errors at depth 7, 48x error reduction. Glass-box AI. 5+ open-access Zenodo publications."

Current meta description is: "Applied research institute focusing on non-Archimedean quantum computing architectures and geometrically interpretable AI via Bruhat-Tits tree topologies."

The new version adds key search terms: "zero logical errors," "48x error reduction," "glass-box AI," "computational evidence." These are the terms people searching for QWAV's thesis would use.
```

---

## PROMPT 5: Add Footer Links

```
In the page footer, ADD these links alongside the existing footer content:

- GitHub: github.com/QNFO
- Zenodo: zenodo.org/communities/qwav/
- ORCID: orcid.org/0009-0002-4317-5604

These give visitors (and search crawlers) direct paths to where the actual work, code, and publication archive live. Keep styling consistent with existing footer links.
```

---

## OPTIONAL PROMPT 6: Update "The Evidence" Section with v2 Results

```
In "The Evidence" section, update the "Computational Validation" card/subsection:

CURRENT text mentions: "Zero errors at 40% physical gate failure rate."

UPDATE to: "Zero logical errors at depth 7 (2,187 leaves). Validated at physical error rates up to 40%. Ternary (p=3) symmetric architecture. 48x error reduction via q-ary scatter at zero additional qubit cost. 40-atom neutral atom hardware specification published. Concatenation of active QEC proven redundant — the tree already provides geometric suppression that standard error correction cannot improve upon."

The current text is from the May 12 Tier 0 paper. The Symmetric Extension (May 16) produced much stronger results. Update the evidence claims to reflect the strongest available data.
```

---

## Sequence Recommendation

Apply in this order:
1. PROMPT 1 (add publications) — most important, fixes staleness
2. PROMPT 6 (update evidence) — optional but high impact, updates claims to strongest data
3. PROMPT 2 (cross-link) — connects marquee to technical site
4. PROMPT 3 (demos teaser) — builds anticipation
5. PROMPT 4 (meta description) — SEO improvement
6. PROMPT 5 (footer links) — SEO + navigation

Preview the page after each prompt to confirm the AI Studio app builder applied the change correctly.

---

## After Applying — Verify

1. Load qwav.tech in browser
2. Check: Publications section now has 9 entries (6 original + 3 new)
3. Check: "Technical Site" link visible and points to qnfo.github.io/QWAV/
4. Check: Interactive Demos section visible with 3 cards
5. Check: Footer has GitHub, Zenodo, ORCID links
6. View page source: meta description updated
7. Test all links work

---

*Generated 2026-05-22. Apply via Google AI Studio app builder chat.*
