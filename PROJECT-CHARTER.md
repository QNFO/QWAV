# PROJECT CHARTER — QWAV Technical Site Hub

## Project Identity

| Field | Value |
|:------|:------|
| **Project Name** | qwav-technical-site |
| **Title** | QWAV Technical Site Hub |
| **Type** | QWAV Spinoff — Interactive Artifact (D13) |
| **Created** | 2026-05-22 |
| **Deployed** | 2026-05-23 |
| **Live URL** | https://qnfo.github.io/QWAV/ |
| **Repository** | QNFO/QWAV |
| **Parent Program** | QWAV — Ultrametric Quantum Computing & AI |

## Purpose & Thesis

Central hub site for the QWAV research program. Serves as the landing page linking all interactive demos, publications, evidence, and roadmap in one place.

## Technical Approach

Single HTML file, vanilla JavaScript, Canvas API for evidence deck charts. No dependencies.

## User Interaction

['T1: Landing page with hero, badges, and CTA links', 'T2: Artifact directory — 5 interactive demo cards with live status badges', 'T3: SEO metadata (OG tags, description, canonical)', 'T4: Evidence highlights — 4 evidence cards with key metrics', 'T5: Evidence Deck — scrollable Canvas charts (LER vs depth, error reduction, Q-PNA comparison) + STC verification table', 'T6: Expanded Research Roadmap — 4 phases with DOIs, [SPECULATIVE] flags on forward projections', 'T7: A1-A5 artifact links', 'T8: Intellectual Genealogy — 30 key publications in 4 threads (QEC, AI, Math, Strategy)', 'T9: Cross-link all artifacts — all 6 demos + Game of Life linked in footer', 'T12: Polish + audit — mobile responsive, canonical, OG image, accessibility audit']

## Evidence Contribution

Zero logical errors at depth 7. 48x error reduction. 40-atom hardware spec. 6.6x AI improvement. 5 interactive demos. 8+ publications with DOIs.

## Success Criteria

1. Interactive elements respond to user input (verified by automated canvas check)
2. Deployed and loading at https://qnfo.github.io/QWAV/
3. JavaScript executes without console errors
4. Cross-linked from QWAV Technical Site Hub
5. Demonstrates a specific, published QWAV result

## Constraints

- Zero external dependencies (no CDN, no npm)
- Single HTML file (inline CSS/JS)
- GitHub Pages deployment (no server)
- MIT licensed or equivalent open-source

## Relationship to QWAV Program

This project is one of 5 interactive artifacts (D13) that make QWAV's computational evidence tangible. Each demo demonstrates one key result:
- Error Confinement → strong triangle inequality visualization
- Q-PNA Playground → glass-box AI decision trees
- Convergence Explorer → ultrametric vs Euclidean comparison
- Tree Distance Sandbox → cophenetic distance computation
- Hardware Visualizer → neutral atom hardware mapping

Together, these 5 demos + the Technical Site Hub + the Virtual Qubit Showdown form the complete QWAV Gravity Portfolio.

---

*Project charter established 2026-05-22. Project completed 2026-05-23.*
