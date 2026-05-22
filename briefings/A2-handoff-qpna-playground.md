# HANDOFF — A2: Q-PNA Classifier Playground

**Type:** Program→Project — Interactive Artifact Build (D13)
**Sessions:** 2 | **Deploy:** QNFO.github.io/q-pna/ | **Reference:** Q-PNA v2.0 DOI: 10.5281/zenodo.20287742

## What to Build
Interactive web app where visitors explore glass-box AI. User selects a hierarchical classification problem (or uploads their own), watches LinMap + cophenetic loss train in real time, and explores the resulting decision tree to understand WHY each classification was made.

## Core Interaction
- **Demo datasets:** 3 pre-loaded (MNIST-ultrametric, synthetic hierarchy, custom CSV upload)
- **Training:** Click "Train" → watch accuracy climb over epochs. Compare against transformer baseline (pre-computed, shown as horizontal line)
- **Decision Explorer:** After training, click any classified sample → the Bruhat-Tits tree path lights up. Shows exactly which tree vertices contributed to the decision
- **Verification:** Toggle "STC Verification" → the Syntactic Token Calculus protocol runs and reports detection rate
- **Metrics display:** Test accuracy, training time, STC detection rate, false positive rate

## Key Result to Demonstrate
"Glass-box AI: Q-PNA beats transformer 6.6× on hierarchical classification with 100% verification detection."

## Technical
- Single HTML + CSS + vanilla JS
- Pre-compute model weights (use the existing Q-PNA Python code to generate JSON weight files)
- Client-side inference only (no backend training — pre-computed weights loaded from JSON)
- Decision tree rendered as interactive SVG

## Design
- Match technical site aesthetic (dark theme, indigo accent, geometric)
- Decision tree is the hero visual element
- Clean, accessible

## DoD
WEB APP TASK gates per DEFINITION-OF-DONE.md
