# HANDOFF -- A5: Hardware Pathway Visualizer

**Type:** Program→Project -- Interactive Artifact Build (D13)
**Sessions:** 1 | **Deploy:** QNFO.github.io/hardware-pathway/ | **Reference:** Symmetric Extension DOI: 10.5281/zenodo.20208437 §Hardware Specification

## What to Build
Interactive 3D (or 2.5D isometric) visualization of the 40-atom neutral atom layout. Visitor rotates, zooms, and explores the ternary Bruhat-Tits tree structure. Sees how Rydberg blockade gates map to tree vertices. Understands that "this is buildable today."

## Core Interaction
- **3D/isometric view of the tree:** 40 atoms arranged in a ternary tree of depth 3
- **Rotate/zoom:** Mouse drag to rotate, scroll to zoom
- **Click an atom:** Shows its role (leaf qubit, intermediate vertex, root), its error rate, its position in the tree
- **Toggle Rydberg gates:** Highlight the gate connections between atoms. Shows how the tree's edges map to physical Rydberg blockade interactions
- **"Buildable Today" panel:** Text explaining that 40 atoms is within demonstrated experimental capabilities (Harvard/Lukin, Caltech/Endres, PASQAL)

## Key Result to Demonstrate
"40 atoms. Ternary tree depth 3. Rydberg blockade gates. 4K operation. This is buildable with current neutral atom technology. No exotic hardware required."

## Technical
- Single HTML + CSS + vanilla JS + Three.js (or Canvas-based isometric)
- Fixed layout (40 positions are pre-computed from the tree geometry)
- Interactive rotation and zoom only -- no simulation, just visualization
- Three.js can be loaded from CDN for 3D; Canvas 2D isometric is simpler and faster

## Design
- Dark background. Atoms as glowing spheres at tree vertices
- Wireframe or translucent edges showing the tree structure
- "40 atoms" prominent
- Minimal UI -- just the tree and a few toggles

## DoD
WEB APP TASK gates per DEFINITION-OF-DONE.md
