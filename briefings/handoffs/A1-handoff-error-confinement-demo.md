# HANDOFF -- A1: Error Confinement Live Demo

**From:** QWAV Strategy Program Manager
**To:** Projects Agent
**Date:** 2026-05-22
**Type:** Program→Project -- Interactive Artifact Build (D13)

---

## What to Build

An interactive Bruhat-Tits tree error simulation deployed on GitHub Pages. A visitor adjusts parameters with sliders and watches logical error rates change in real time. This is the "30-second demo" that replaces "please read my 30-page paper."

**Deploy target:** `https://QNFO.github.io/ultrametric-error-confinement/`
**Source repo:** Create in `G:\My Drive\projects\ultrametric-error-confinement-demo\`

---

## Core Interaction

### Slider 1: Physical Error Rate (0-50%)
- Single qubit/gate error probability
- Default: 10%
- Real-time update: as slider moves, the tree visualization updates and LER recalculates

### Selector 1: Tree Depth (d = 2, 3, 4, 5, 6, 7)
- Controls how many levels of Bruhat-Tits tree
- Default: d=4
- d=2: 9 leaves (ternary) or 4 (binary)
- d=7: 2,187 leaves (ternary) -- the depth where zero logical errors were demonstrated

### Selector 2: Prime (p = 2, 3, 5)
- p=2: binary tree (asymmetric -- bit 0 protected, bit 1 not)
- p=3: ternary tree (symmetric -- goldilocks)
- p=5: larger tree (validated but grows faster)
- Default: p=3

### Visualization
- The Bruhat-Tits tree drawn on screen
- Leaves color-coded: green = correct logical state, red = error
- Error propagation visibly climbs the tree or gets geometrically suppressed
- When p=3, depth=7, error rate <40%: observe ZERO logical errors -- the marquee result

### Metrics Display
- Logical Error Rate (LER): updated in real time
- Physical Error Rate: mirroring the slider
- Comparison: "Archimedean equivalent would have LER of X%" (calculated)
- Note: "At p=2, bit 0 is protected but bit 1 isn't -- this is the asymmetry that p=3 fixes"

---

## Design Requirements

### Aesthetic
- Dark background, geometric tree in ultrametric-inspired colors
- Clean, no clutter. The tree is the hero.
- QWAV branding minimal -- small "QWAV" text link in corner
- "This is what ultrametric geometry does. Watch."

### Technical
- Single HTML file + CSS + vanilla JS (no framework needed)
- All simulation happens client-side -- no backend
- GitHub Pages deployment
- `.nojekyll` file at root
- Mobile: works but shows "best viewed on desktop" note
- Loads in under 2 seconds

### DO NOT
- No login, no accounts, no data collection
- No external API calls
- No framework dependencies (React, Vue, etc.) -- keep it deployable by dropping one folder into GitHub Pages
- No paper download required -- the demo IS the experience

---

## Reference Materials

### The Math (what to simulate)
The Bruhat-Tits tree for prime $p$ is a $(p+1)$-regular infinite tree. Vertices represent $p$-adic balls. For computation:
- **Encoding:** Each logical bit is represented by a path from root to leaf. For $q$-ary scatter, one logical bit maps to $q$ leaves.
- **Error model:** Each physical qubit (leaf or edge) flips with probability $p_{\text{phys}}$.
- **Decoding:** Majority vote across the $q$ leaves determines the logical bit. The strong triangle inequality $d(x,z) \leq \max\{d(x,y), d(y,z)\}$ geometrically suppresses errors -- errors on nearby leaves are correlated in a way that majority vote exploits.

### Prior Code
- `G:\My Drive\projects\ultrametric_v2\` -- 7 sprints of Python simulation. Key files contain the error model, tree construction, and LER calculation logic. Read these for the math before coding.
- `github.com/QNFO/ultrametric-error-confinement` -- the Tier 0 paper repo. Contains Python code for the binary case.

### Published Papers (for reference values)
- Tier 0: DOI `10.5281/zenodo.20134944` -- binary tree results
- Tier 1: DOI `10.5281/zenodo.20208437` -- ternary tree, 48× scatter, concatenation redundancy

### Design References
- Bruhat-Tits tree visualizations: search the 673-release corpus for tree diagrams
- Geometric aesthetic: think clean, mathematical, evidence-driven -- not corporate, not academic

---

## Success Criteria (DoD -- WEB APP TASK)

- [ ] All interactive features verified working
- [ ] Error states handled (empty config, broken JSON, missing DOM elements)
- [ ] Console audit: zero unexpected errors
- [ ] Mobile responsiveness check OR "desktop-only" declaration
- [ ] Accessibility baseline: color contrast, keyboard-navigable, alt text
- [ ] All assets load from live URL (zero 404s)
- [ ] `<title>`, `<meta description>`, Open Graph tags present
- [ ] `.nojekyll` file at root
- [ ] Deployed and live at `https://QNFO.github.io/ultrametric-error-confinement/`
- [ ] LER = 0 at d=7, p=3, error rate up to 40% (matches published result)

---

## Return Protocol

When complete:
1. Deploy to GitHub Pages
2. Verify live URL
3. Reply to QWAV Agent with: URL, commit hash, screenshot
4. QWAV Agent will: verify deployment, update PROJECT STATE.md, create Buffer campaign, update qwav.tech artifact directory

---

## Session Budget

**Estimated:** 2 sessions (3-4 hours each)
- Session 1: Tree simulation logic + basic visualization
- Session 2: Polish, sliders, deployment, testing

---

## Constraints (D1-D13 -- All Apply)

- All code completable in single LLM thread (D12)
- No external APIs, no backends, no databases
- MIT license
- Open-source under QNFO GitHub org

---

*QWAV Handoff -- A1 Error Confinement Live Demo. 2026-05-22.*
