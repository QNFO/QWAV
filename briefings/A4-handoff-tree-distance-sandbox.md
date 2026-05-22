# HANDOFF — A4: Tree Distance Sandbox

**Type:** Program→Project — Interactive Artifact Build (D13)
**Sessions:** 1 | **Deploy:** QNFO.github.io/tree-distance/ | **Reference:** Tree Distance Cophenetic DOI: 10.5281/zenodo.20213043

## What to Build
Interactive comparison of three distance metrics: cophenetic, ultrametric, and Euclidean. Visitor picks two points on a tree (or enters coordinates) and instantly sees all three distances. Explores how "distance" means different things in different geometries — and why ultrametric distance matters for computation.

## Core Interaction
- **Tree display:** A small tree (depth 3-5) with labeled leaves
- **Click two leaves** → three distance values appear side by side:
  - Cophenetic distance (tree depth of common ancestor — the "tree" distance)
  - Ultrametric distance (strong triangle inequality version)
  - Euclidean distance (if the leaves were points in ℝ²)
- **Triadic rigidity demo:** Click three leaves → the three pairwise distances are displayed. In ultrametric space, the two largest distances are always equal. In Euclidean space, they vary. The visitor discovers the theorem by playing.
- **"Why this matters" panel:** Text explaining that ultrametric distances have special properties that Euclidean distances don't — and those properties are what enable passive error suppression.

## Key Result to Demonstrate
"In ultrametric space, of any three points, the two largest distances are equal. This property — triadic rigidity — geometrically prevents error accumulation."

## Technical
- Single HTML + CSS + vanilla JS
- Tree rendered as SVG
- Click handlers on leaf nodes
- Simple distance calculation in JS
- Fixed-depth tree (d=4, binary or ternary)

## Design
- Clean, minimal. Tree is centered. Distance cards on the right.
- "Click any two leaves" instruction visible
- Color-coded: cophenetic (green), ultrametric (blue), Euclidean (gray)

## DoD
WEB APP TASK gates per DEFINITION-OF-DONE.md
