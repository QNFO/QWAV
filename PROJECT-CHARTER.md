# PROJECT CHARTER — QWAV Technical Site Hub

## 1. PROJECT IDENTITY

| Field | Value |
|:------|:------|
| **Project Name** | `qwav-technical-site` |
| **Title** | QWAV Technical Site Hub |
| **Type** | QWAV Spinoff — Central Hub (K1) |
| **QWAV Strategy Reference** | `strategy/3.0.md` — Build Gravity, Tier 2 |
| **Created** | 2026-05-22 |
| **Repository** | `QNFO/QWAV` |
| **Live Target** | `https://qnfo.github.io/QWAV/` |
| **Parent Program** | QWAV — Ultrametric Quantum Computing & AI |

## 2. RAISON D'ÊTRE — QWAV STRATEGY NEXUS

**This project exists because six separate interactive demos scattered across GitHub Pages are not a program — they need a single destination that tells the complete story.**

Strategy 3.0 defines Tier 2 as the "Technical Site Hub" — the aggregation point for all evidence, artifacts, publications, and the research roadmap. It is the single URL shared in every application, bio, and outreach email. If Tier 1 artifacts are the gravity wells, the hub is the gravity center — the nexus where all paths converge.

**Strategic contribution:**
- Provides one canonical URL for all QWAV evidence
- Aggregates publications (8+ DOIs), artifacts (A1-A5), roadmap, and intellectual genealogy
- Serves as the "deep dive" destination for serious evaluators
- Links TO every artifact and FROM every artifact (cross-linked portfolio)

**Without this project, QWAV is six disconnected demos with no unifying narrative.**

## 3. SCOPE

### In Scope (Built)
- Hero section with thesis statement
- Evidence highlights (4 cards: error confinement, glass-box AI, convergence, hardware)
- Interactive artifact directory (A1-A5 cards with links)
- Publication table (8+ DOIs with links to Zenodo)
- Research roadmap timeline
- Intellectual genealogy (30+ publications)
- Canvas-based evidence deck charts (LER, Error Reduction, Q-PNA performance)

### In Scope (Not Yet Built)
- Cross-links FROM each artifact back to the hub
- Mobile-optimized layout (current version works but needs testing)
- Offline fallback for CDN resources
- Search engine optimization meta tags

## 4. CURRENT STATUS (2026-05-23)

**Phase:** FUNCTIONAL — Most complete artifact in the portfolio

**What exists:** A 31 KB `index.html` with 7 commits of real development, including bug fixes. All sections present. Canvas charts render. Publication table complete. Artifact directory links functional.

**What's missing:**
- **58 external CDN dependencies** (fonts, icons, analytics) — fragile, breaks if any CDN is down
- **No offline fallback.** Site requires internet for fonts/icons.
- **No mobile testing.** Responsive design implemented but not verified on real devices.
- **No test suite.** Charts render but accuracy of displayed data not verified.
- **Missing back-links from A1-A5 artifacts.**

## 5. DELIVERABLES

| # | Deliverable | Status |
|:--|:------------|:------|
| T1-T4 | Core hub structure (hero, evidence, artifacts, roadmap) | ✅ BUILT |
| T5 | Evidence Deck (Canvas charts) | ✅ BUILT (bug fixed) |
| T6 | Expanded roadmap with DOIs | ✅ BUILT |
| T7 | Publication table (8+ DOIs) | ✅ BUILT |
| T8 | Intellectual Genealogy (30 publications) | ✅ BUILT |
| T9 | Cross-links to all artifacts + Game of Life | ✅ BUILT |
| T10 | Mobile optimization | NOT TESTED |
| T11 | Offline fallback (self-host fonts) | NOT BUILT |
| T12 | SEO meta tags | NOT BUILT |

---

*Updated: 2026-05-23 | QWAV Strategy: Build Gravity v3.0 | Tier 2 — Hub*
