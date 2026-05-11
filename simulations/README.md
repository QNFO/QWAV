# Tier 0: Computational Validation Suite

Bruhat-Tits tree circuit simulator demonstrating ultrametric error
confinement, energy barrier scaling, and related properties.

## Quick Start

```bash
cd simulations/

# Run self-tests
python btree.py

# Run Experiment 0A (error confinement — the main experiment)
python experiment_0a.py

# Run Experiment 0B (energy barrier scaling)
python experiment_0b.py
```

## File Structure

```
simulations/
├── __init__.py          # Package init
├── btree.py             # Bruhat-Tits tree construction & traversal
├── encoding.py          # State encoding (tree + flat)
├── noise.py             # Error models (bit-flip, correlated)
├── metrics.py           # Measurement & analysis utilities
├── experiment_0a.py     # Experiment 0A: Error confinement
├── experiment_0b.py     # Experiment 0B: Energy barrier scaling
├── plots.py             # Visualization (matplotlib or ASCII)
├── plots/               # Generated plots (auto-created)
└── README.md            # This file
```

## Experiments

### Experiment 0A: Error Confinement
**Question:** Does encoding on a Bruhat-Tits tree suppress error
propagation compared to flat encoding?

**Method:** Build trees at depths d=2,3,4,5. Apply bit-flip noise at
varying rates. Compare logical error rates for tree vs. flat encoding.

**Key metric:** R_prop = tree_LER / flat_LER (< 1 means suppression)

### Experiment 0B: Energy Barrier Scaling
**Question:** Does the energy barrier protecting logical states scale
exponentially with tree depth?

**Method:** Find minimum leaf flips needed to change root value at
each depth. Verify exponential scaling.

## Requirements

- Python 3.8+
- Standard library only (no external dependencies required)
- matplotlib (optional, for graphical plots)

## Interpreting Results

**Success indicators:**
- R_prop < 1 for all depths and error rates (suppression exists)
- R_prop decreases with depth (deeper = better protection)
- Energy barrier increases with depth

**Falsification indicators:**
- R_prop ≈ 1 (no advantage over flat encoding)
- No depth dependence (deeper trees don't help)
- Energy barrier constant or decreasing with depth

## Output

ASCII tables are printed to stdout. Plots are saved to `plots/` if
matplotlib is available.

## Next Steps

After successful Tier 0 validation:
- Experiment 0C: Q-PNA tree walk speedup
- Experiment 0D: Token calculus confluence
- Open-source release on Zenodo
- Use results in applications (Emergent Ventures, Foresight)
