# Error Confinement Live Demo

Interactive Bruhat-Tits tree simulation demonstrating ultrametric error suppression.

**Live demo:** Watch the strong triangle inequality geometrically prevent errors from accumulating.

## How to Deploy

1. Push this folder to a GitHub repo under the QNFO organization
2. Enable GitHub Pages in repo Settings → Pages → Source: main branch, / (root)
3. Site will be live at `https://QNFO.github.io/ultrametric-error-confinement/`

## What It Shows

- **Physical Error Rate slider (0-50%):** How noisy each physical qubit is
- **Tree Depth slider (d=2-7):** How deep the Bruhat-Tits tree goes
- **Prime selector (p=2,3,5):** Binary, ternary, or larger trees
- **Samples slider:** How many Monte Carlo trials to run

**Key result:** At depth 7, p=3, physical error rates up to 40% → ZERO logical errors.

## Reference

- Tier 0: [Computational Validation of Ultrametric Error Confinement](https://doi.org/10.5281/zenodo.20134944)
- Tier 1: [Symmetric Extension — Ternary Tree Architecture](https://doi.org/10.5281/zenodo.20208437)
