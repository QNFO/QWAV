# Technical Site Sprint Plan -- qnfo.github.io/QWAV/

**Date:** 2026-05-22
**From:** QWAV Strategy Program Manager
**To:** Projects Agent
**Priority:** 🔴 HIGH -- qwav.tech marquee now links here. Site must deliver on the promise.

---

## 0. THE PRESSURE POINT

The qwav.tech marquee page now prominently links to `qnfo.github.io/QWAV/` as "Technical Site & Interactive Demos." Visitors who click through are looking for depth. Currently the site is:

- ✅ Clean thesis and publication list (from README)
- ❌ Bare GitHub README rendering -- no design, no visual hierarchy
- ❌ No interactive artifact directory (A1-A5 don't exist yet, but there's no placeholder structure)
- ❌ No evidence deck (computational results are text-only, buried in paragraphs)
- ❌ No research roadmap
- ❌ No prior work catalog
- ❌ No SEO metadata (title tag is generic "QWAV -- Ultrametric Quantum Computing & AI | QWAV")
- ❌ No cross-links to sibling artifacts

**This sprint plan turns the README into a real technical hub.**

---

## 1. PHASED BUILD PLAN

### Phase 1: Foundation (Week 1 -- ~5 sessions)

| Task | ID | What | Sessions | Depends On |
|:-----|:--|:-----|:---------|:-----------|
| **Polished landing page** | T1 | Replace bare README rendering with a proper HTML/CSS landing page. Single page, clean design. Geometric aesthetic matching the marquee but lighter-weight. Static HTML + CSS -- no React, no framework. Everything in the QNFO/QWAV repo. | 2 | None |
| **Interactive artifact directory** | T2 | A section with cards for A1-A5. Each card: title, one-line description, status indicator (🔴 Coming Soon / 🟢 Live). Links to GitHub Pages URLs as artifacts deploy. Cards that aren't live yet are grayed out with "Coming June 2026." | 0.5 | T1 (needs the page structure) |
| **SEO metadata + analytics** | T3 | `<title>`, `<meta description>`, Open Graph tags, Schema.org `ScholarlyArticle` for each publication, sitemap.xml, robots.txt. Google Analytics or Plausible tag (founder decision). | 0.5 | T1 |
| **Evidence highlights section** | T4 | A visually distinct section pulling the key computational results out of paragraph text and into highlight cards: "Zero logical errors at depth 7," "48× error reduction at zero qubit cost," "40-atom neutral atom spec," "Q-PNA beats transformer 6.6×." Each card has a one-liner and links to the full paper DOI. | 1 | T1 |

### Phase 2: Depth (Week 2-3 -- ~5 sessions)

| Task | ID | What | Sessions | Depends On |
|:-----|:--|:-----|:---------|:-----------|
| **Evidence Deck (K3)** | T5 | Scrollable, visual summary of ALL computational results. LER vs. depth charts. Scatter reduction plots. Concatenation redundancy data. Q-PNA benchmarks. STC verification results. Each chart has a caption, source paper DOI, and "how to reproduce" link. | 2 | T1, ultrametric_v2 data |
| **Research Roadmap (K4)** | T6 | Public-facing forward agenda. What's being built now. What's next. Tier 2 computational validation (larger trees, more benchmarks). Q-PNA v3.0. New spinoffs. Timeline: NOW → Q3 2026 → Q4 2026 → 2027. Not a strategy document -- a "here's where we're going" page that builds anticipation. | 1 | T1 |
| **Link A1 live** | T7 | When A1 (Error Confinement Demo) deploys, update the artifact directory card from "Coming Soon" to "Live." Add the live URL. Update the evidence highlights if A1 produces new data. | 0.25 | A1 deployed |
| **Intellectual Genealogy (K2)** | T8 | Curated timeline of 30 key publications from the 673-release corpus. Each entry: title, date, DOI, one-line relevance to QWAV's thesis. Organized chronologically. Shows the intellectual evolution. Added as a dedicated page or a long scroll section. | 1.5 | T1, Obsidian corpus access |

### Phase 3: Integration (Week 4 -- ~3 sessions)

| Task | ID | What | Sessions | Depends On |
|:-----|:--|:-----|:---------|:-----------|
| **Cross-link all artifacts** | T9 | Each deployed artifact (A1-A5) links back to the technical site. The technical site links to each artifact. Navigation between artifacts. Unified visual identity across all GitHub Pages sites. | 1 | A1-A5 deploying |
| **Buffer campaign for technical site** | T10 | Social posts: "We rebuilt our technical site. Interactive demos, evidence deck, research roadmap. Explore → qnfo.github.io/QWAV/" Queue through Buffer. | 0.5 | T1-T6 deployed |
| **VENUE-REGISTRY update** | T11 | Update the QWAV venue registry with new technical site content, new artifact URLs, updated search baseline. | 0.25 | T1-T10 complete |
| **Polish + audit** | T12 | Full link check. Mobile responsiveness. Console audit (zero errors). Cross-browser screenshots. Accessibility check. All DoD gates passed. | 0.5 | All previous |

---

## 2. SESSION BUDGET

| Phase | Sessions | Key Output |
|:------|:---------|:-----------|
| Phase 1: Foundation | 4 | Polished landing page, artifact directory, SEO, evidence highlights |
| Phase 2: Depth | 4.75 | Evidence deck, research roadmap, A1 live link, intellectual genealogy |
| Phase 3: Integration | 2.25 | Cross-links, Buffer campaign, audit, polish |
| **Total** | **11** | **Complete technical site overhaul** |

At 1 session/day: 2 weeks. At 1 session/2 days: 3-4 weeks.

---

## 3. DEPENDENCY CHAIN

```
T1 (landing page) ─┬─ T2 (artifact directory)
                    ├─ T3 (SEO)
                    ├─ T4 (evidence highlights)
                    ├─ T5 (evidence deck)
                    ├─ T6 (research roadmap)
                    └─ T8 (intellectual genealogy)
                         │
                    A1 deployed ── T7 (link A1)
                         │
                    T1-T8 done ── T9 (cross-links)
                         │
                    T9 done ── T10 (Buffer campaign)
                         │
                    T10 done ── T11 (VENUE-REGISTRY update)
                         │
                    T11 done ── T12 (polish + audit)
```

---

## 4. DESIGN SPECIFICATIONS

### Visual Identity
- **Aesthetic:** Geometric, clean, evidence-first. Not corporate. Not academic-journal. Independent.
- **Color palette:** Match the qwav.tech marquee (dark indigo `#0A1128`, light text `#E5E5E5`, indigo accent `#818CF8`). The technical site should feel like it belongs to the same program.
- **Typography:** System font stack. No custom fonts (keeps it fast).
- **Layout:** Single-page scroll with clear sections. Sticky nav. Section anchors.
- **Hero element:** A Bruhat-Tits tree visualization (static SVG or canvas) -- simpler than the marquee's hero but visually connected.

### Technical Constraints
- **Static HTML + CSS + vanilla JS.** No React, no frameworks, no build step.
- **Deployed from `QNFO/QWAV` repo** -- the README.md becomes `index.html` (or the GitHub Pages config points to `docs/` or root).
- **All assets local** -- no CDN dependencies except maybe a Google Font or analytics tag.
- **`.nojekyll` file at root** -- GitHub Pages requirement.
- **Mobile responsive** -- must work on phones.
- **Loads in under 2 seconds.**
- **All links are absolute URLs** (DOIs, GitHub repos, artifact URLs).

### Content Rules
- **No investor language.** This is the technical site -- it's for researchers, developers, and people who clicked through from the marquee.
- **Every claim links to a DOI or GitHub repo.** No unsourced statements.
- **"Solo deep-tech research program"** -- correct framing. No "institute" cosplay.
- **All 5 current publications listed** with DOI links, one-line key results, and GitHub links where available.
- **"Coming Soon" cards are honest** -- grayed out, clear status indicator. Don't promise what isn't built.

---

## 5. HANDOFF SPECIFICATIONS -- Task-by-Task

### T1: Polished Landing Page

**Input:** Current `README.md` in `QNFO/QWAV` repo.
**Output:** `index.html` (or `docs/index.html`) with proper design.

**What to build:**
1. Replace the bare Markdown rendering with a designed HTML page.
2. Sections (in order):
   - **Hero:** "QWAV -- Ultrametric Quantum Computing & AI." One-paragraph thesis. Clean. Geometric SVG tree visual.
   - **Evidence Highlights:** 4 cards with key results (from T4 spec below).
   - **Publications:** Table/list with all 5 DOIs, dates, one-line key results, GitHub links.
   - **Interactive Artifacts:** Card grid -- 5 cards (A1-A5), grayed out with "Coming June 2026."
   - **Research Roadmap:** Forward-looking timeline (placeholder until T6).
   - **About:** Brief program description. Link to qwav.tech for full story.
   - **Footer:** GitHub, Zenodo, ORCID, contact, link back to qwav.tech.

3. **Design reference:** The qwav.tech marquee page. The technical site should feel like it belongs to the same program but be lighter-weight and more text/content-focused.

**Deliverable:** Single `index.html` file (with inline CSS -- no external stylesheets needed for a single page). Push to `QNFO/QWAV` repo. GitHub Pages auto-deploys.

### T2: Interactive Artifact Directory

**Output:** A `<section id="artifacts">` in `index.html`.

**Cards:**
```
┌─────────────────────────────────────┐
│ 🔴 Coming June 2026                 │
│                                     │
│ Error Confinement Live Demo         │
│ Watch ultrametric geometry suppress │
│ errors in real time. Adjust error   │
│ rates and tree depth with sliders.  │
│                                     │
│ [Coming Soon]                       │
└─────────────────────────────────────┘
```

Five cards:
1. Error Confinement Live Demo → `https://QNFO.github.io/ultrametric-error-confinement/`
2. Q-PNA Classifier Playground → `https://QNFO.github.io/q-pna/`
3. Ultrametric Convergence Explorer → `https://QNFO.github.io/ultrametric-convergence/`
4. Tree Distance Sandbox → `https://QNFO.github.io/tree-distance/`
5. Hardware Pathway Visualizer → `https://QNFO.github.io/hardware-pathway/`

When an artifact deploys, update the card: 🔴→🟢, "Coming Soon"→"Live -- Try It →", make the card clickable.

### T3: SEO Metadata

Add to `<head>`:
```html
<title>QWAV -- Ultrametric Quantum Computing & AI | Technical Site</title>
<meta name="description" content="Technical site for QWAV: computational evidence, interactive demos, and open-access publications on ultrametric quantum computing and glass-box AI. Zero logical errors at depth 7. 48× error reduction.">
<meta property="og:title" content="QWAV -- Ultrametric Quantum Computing & AI">
<meta property="og:description" content="Computational evidence, interactive demos, open-access publications.">
<meta property="og:url" content="https://qnfo.github.io/QWAV/">
<meta property="og:type" content="website">
```

Add `sitemap.xml` and `robots.txt` to the repo root.

Add Schema.org structured data for the program and each publication.

### T4: Evidence Highlights

Four cards in a visually distinct section:

| Card | Text | Links To |
|:-----|:-----|:---------|
| Zero Logical Errors | "At depth 7 (2,187 leaves), ternary Bruhat-Tits tree encoding produces zero logical errors at physical error rates up to 40%." | DOI: `10.5281/zenodo.20208437` |
| 48× Error Reduction | "Encoding one logical bit across q=128 leaves reduces logical error rate by 48× -- zero additional qubit cost. Achieved by exploiting existing hyperfine levels." | DOI: `10.5281/zenodo.20208437` |
| 40-Atom Hardware Spec | "Complete neutral atom hardware specification: ternary tree depth 3, Rydberg blockade gates, 4K operation. Within demonstrated experimental capabilities." | DOI: `10.5281/zenodo.20208437` |
| Glass-Box AI | "Q-PNA linear mapping + cophenetic loss beats transformer 6.6× on hierarchical classification. STC verification: 100% detection, 0 false positives." | DOI: `10.5281/zenodo.20287742`, GitHub: `QNFO/Q-PNA` |

### T5: Evidence Deck (K3)

A scrollable section with:
1. **LER vs. Depth chart** -- p=2,3,5 across depths d=2-7. Physical error rate 10%, 20%, 40%. Interactive or static image with caption.
2. **Scatter Reduction chart** -- LER vs. q (scatter factor) at fixed depth. Shows 48× drop.
3. **Concatenation Redundancy chart** -- LER with and without surface code / Steane code. Shows zero benefit.
4. **Q-PNA Benchmark table** -- Accuracy comparison: LinMap vs. transformer vs. baselines.
5. **STC Verification table** -- Detection rate, false positive rate.

Each chart/figure: caption, source paper DOI link, "how to reproduce" (link to GitHub code).

**Data source:** The `ultrametric_v2` project simulation outputs. The Projects agent can regenerate charts from the existing Python code.

### T6: Research Roadmap (K4)

Timeline section:

```
NOW (Q2 2026)
├─ Tier 0-1 computational validation: COMPLETE ✅
├─ Interactive artifacts deploying: A1-A5
└─ 6 applications pending

Q3 2026
├─ Tier 2 validation: larger trees (d=8-10), multi-prime benchmarks
├─ Q-PNA v2.1: new datasets, expanded STC validation
└─ First inbound contact milestone

Q4 2026
├─ Cross-Domain Synthesis v2: expanded domain coverage
├─ New spinoffs from backlog
└─ Strategy refresh (6-month review)

2027
├─ Experimental collaboration (if inbound contact converts)
├─ Entity formation (if funding triggers)
└─ Publication archive reaches 700+
```

Each item links to relevant DOI or GitHub repo. Honest about what's planned vs. what's speculative.

### T8: Intellectual Genealogy (K2)

A curated timeline of 30 key publications from the 673-release corpus. Each entry:

```
2024 -- Adelic Constraints on Quantum Field Theory (Phase 1-3)
  DOI: [doi]
  Relevance: First systematic application of p-adic mathematics to QFT. 
  Established the pattern: number-theoretic constraints on physical theory.

2025 -- Bruhat-Tits Quantum Processor
  DOI: 10.5281/zenodo.20109835
  Relevance: First explicit proposal for Bruhat-Tits tree as quantum 
  computing substrate. Precursor to Tier 0 validation.

[... 28 more entries ...]

2026 -- Symmetric Extension of Ultrametric Error Confinement
  DOI: 10.5281/zenodo.20208437
  Relevance: Tier 1 computational validation. Zero logical errors at 
  depth 7. Current state of the art for QWAV quantum computing.
```

The Projects agent should scan `Obsidian/releases/` for the 30 most QWAV-relevant publications. Selection criteria: (1) directly addresses ultrametric/p-adic quantum computing, (2) directly addresses Bruhat-Tits tree architectures, (3) directly addresses glass-box AI / Q-PNA, (4) represents a key intellectual turning point.

---

## 6. DO NOT

- Do NOT link to artifacts that don't exist yet with live-looking links. Use "Coming Soon" badges.
- Do NOT use the "institute" framing. "Solo deep-tech research program."
- Do NOT add investor pitch language or revenue model references. This is the technical site.
- Do NOT add collaborator recruitment language ("we need your expertise"). Inbound-only.
- Do NOT add framework dependencies (React, Vue, etc.). Static HTML + CSS only.
- Do NOT fabricate charts or data. All evidence must come from existing published results.
- Do NOT deploy without `.nojekyll` file. GitHub Pages requires it.

---

## 7. DEFINITION OF DONE (Per DEFINITION-OF-DONE.md)

### T1-T8: WEB APP TASK
- [ ] All interactive features verified working
- [ ] Error states handled
- [ ] Console audit: zero unexpected errors on page load
- [ ] Mobile responsiveness check OR "desktop-only" declaration
- [ ] Accessibility baseline: color contrast, keyboard-navigable, alt text
- [ ] All assets load from live URL (zero 404s)
- [ ] `<title>`, `<meta description>`, Open Graph tags present
- [ ] `.nojekyll` file at root
- [ ] Deployed and live at `https://qnfo.github.io/QWAV/`
- [ ] All links verified (no broken DOIs, no 404 GitHub links)

### T10: DOCUMENT TASK (Buffer campaign)
- [ ] All claims traceable to published DOIs
- [ ] Links point to interactive artifacts, not papers (D13)
- [ ] Campaign queued through Buffer

---

## 8. RETURN PROTOCOL

When each task completes:
1. Deploy to GitHub Pages (or push to QNFO/QWAV repo)
2. Verify live URL
3. Reply to QWAV Agent with: URL, commit hash, screenshot
4. QWAV Agent will: verify deployment, update VENUE-REGISTRY.md, update SPRINT.md, mark task complete

---

*QWAV Technical Site Sprint Plan v1.0. 2026-05-22.*
