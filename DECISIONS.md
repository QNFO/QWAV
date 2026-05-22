# DECISIONS — QWAV Technical Site Hub

Architecture and design decisions with rationale.

## ADR-1: Single HTML file, no dependencies
- **Date:** 2026-05-22
- **Status:** Accepted
- **Context:** QWAV interactive demos need to be deployable with zero build step.
- **Decision:** All CSS and JavaScript inlined in index.html. No npm, no webpack, no CDN.
- **Consequences:** File grows with complexity. Acceptable for demos under 100 KB. Not suitable for production applications.

## ADR-2: Canvas API over SVG for interactive visualization
- **Date:** 2026-05-22
- **Status:** Accepted
- **Context:** Need real-time visual feedback for user interactions.
- **Decision:** Use Canvas API for pixel-level control and fast redraws. SVG for static structural elements where interactivity is click-based.
- **Consequences:** Canvas has no DOM — custom hit-testing required for click interactions.

## ADR-3: GitHub Pages with .nojekyll for zero-config deploy
- **Date:** 2026-05-22
- **Status:** Accepted
- **Context:** Need public URL with zero server cost, zero configuration.
- **Decision:** Deploy to QNFO GitHub organization Pages. .nojekyll file prevents Jekyll processing. master branch, / (root) source.
- **Consequences:** No server-side logic. Static only. Acceptable for client-side demos.

## ADR-4: Verbatim published data, no simulation
- **Date:** 2026-05-22
- **Status:** Accepted
- **Context:** Demo should reflect published results, not generate new data.
- **Decision:** Hardcode verified research data from published papers. Interactive controls adjust parameters within validated range.
- **Consequences:** Demo shows what WAS validated, not predictions. Honest about scope.

---

*All decisions made during qwav-technical-site development.*
