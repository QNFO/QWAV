"""Experiment 0B: Energy Barrier Scaling with Tree Depth.

Tests the prediction that the energy barrier E_barrier protecting
logical states scales with tree depth.

Key insight: In the hierarchical majority-vote tree with tie_breaker=0:
  - A non-root node flips only if BOTH its children flip
  - The root flips if >= ceil((p+1)/2) of its children flip
  - This gives: E_barrier(d) = ceil((p+1)/2) * 2^(d-1) for p=2
  - Which is exponential in depth: E_barrier(d) = 2^d

For larger p (p > 2), the scaling is even stronger:
  - Non-root: need ceil(p/2) children to flip
  - Root: need ceil((p+1)/2) children to flip

The barrier grows exponentially with depth while the fraction of
leaves needed remains constant. This verifies the E_barrier ~ q^d
prediction with q = 2 for p=2.

For physical implementation: more tree depth = higher absolute energy
barrier protecting logical states from thermal noise at 4K.
"""

from __future__ import annotations
import math
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from btree import BruhatTitsTree
from plots import plot_energy_barrier, print_barrier_table


def compute_barrier_analytic(p: int, depth: int, tie_breaker: int = 0) -> dict:
    """Compute the energy barrier analytically from tree structure.

    For the majority-vote encoding with tie_breaker=0:
    - A node with k children needs ceil(k/2) children to flip to change
    - With tie_breaker=0 and even children: need ALL children to flip
    
    Args:
        p: Prime for p-adic tree
        depth: Tree depth
        tie_breaker: Tie-breaking value (0 = conservative, needs all children)

    Returns:
        dict with barrier analysis
    """
    # Root has p+1 children, non-root has p children
    root_branching = p + 1
    internal_branching = p

    if tie_breaker == 0:
        # Conservative: for even branching, need ALL children to flip
        root_required = root_branching  # All children must flip if even
        if root_branching % 2 == 1:
            root_required = (root_branching + 1) // 2  # Majority for odd

        internal_required = internal_branching  # All children if even
        if internal_branching % 2 == 1:
            internal_required = (internal_branching + 1) // 2
    else:
        # For tie_breaker=1: majority suffices (ceil(k/2))
        root_required = (root_branching + 1) // 2
        internal_required = (internal_branching + 1) // 2

    # Barrier: recursive product of requirements
    barrier = root_required * (internal_required ** (depth - 1)) if depth >= 1 else 1

    tree = BruhatTitsTree(p=p, depth=depth)
    n_leaves = tree.num_leaves

    return {
        "depth": depth,
        "p": p,
        "root_branching": root_branching,
        "root_required": root_required,
        "internal_branching": internal_branching,
        "internal_required": internal_required,
        "barrier": barrier,
        "n_leaves": n_leaves,
        "barrier_fraction": barrier / n_leaves if n_leaves > 0 else 0,
        "exponential_base": root_required ** (1/depth) * internal_required ** ((depth-1)/depth) if depth > 0 else 1,
    }


def verify_barrier_exhaustive(p: int, depth: int, max_depth: int = 3) -> dict | None:
    """Verify analytic barrier via exhaustive search (small depths only)."""
    if depth > max_depth:
        return None  # Skip for large depths

    import itertools
    tree = BruhatTitsTree(p=p, depth=depth)
    n_leaves = tree.num_leaves

    if n_leaves > 20:
        return None  # Too many leaves for exhaustive search

    analytic = compute_barrier_analytic(p, depth)

    # Try increasing numbers of flips
    for k in range(1, min(n_leaves + 1, 50)):
        for combo in itertools.combinations(range(n_leaves), k):
            # Reset all to 0
            for leaf in tree.leaves:
                leaf.value = 0
            # Flip selected leaves
            for idx in combo:
                tree.leaves[idx].value = 1
            # Propagate
            tree.propagate_up()
            if tree.root.value == 1:
                return {
                    "depth": depth,
                    "analytic_barrier": analytic["barrier"],
                    "measured_barrier": k,
                    "match": k == analytic["barrier"],
                    "n_leaves": n_leaves,
                }
    return None


def run_experiment_0b(
    p: int = 2,
    depths: list[int] | None = None,
    verify_small: bool = True,
    verbose: bool = True,
) -> dict:
    """Run the energy barrier scaling experiment (analytic + verification).

    Args:
        p: Prime for p-adic tree
        depths: Tree depths to test
        verify_small: Run exhaustive verification for small depths
        verbose: Print progress

    Returns:
        dict with barrier analysis
    """
    if depths is None:
        depths = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    results = {"p": p, "depths": depths, "barriers": {}}

    if verbose:
        print(f"\n{'='*60}")
        print(f"EXPERIMENT 0B: Energy Barrier Scaling")
        print(f"{'='*60}")
        print(f"  p = {p}")
        print(f"  tie_breaker = 0 (conservative: all children must flip for even branching)")
        print(f"  Method: analytic computation from tree structure")
        print()

    for depth in depths:
        analytic = compute_barrier_analytic(p, depth)

        # Optional exhaustive verification
        if verify_small and depth <= 3:
            verified = verify_barrier_exhaustive(p, depth)
            analytic["verified"] = verified is not None
            analytic["verified_match"] = verified["match"] if verified else None
            analytic["measured_barrier"] = verified["measured_barrier"] if verified else None

        results["barriers"][depth] = analytic

        if verbose:
            verified_str = ""
            if verify_small and depth <= 3:
                v = analytic.get("verified_match")
                verified_str = f" [VERIFIED: {v}]" if v is not None else " [NOT FOUND]"

            print(f"  depth={depth:2d}: barrier={analytic['barrier']:6d}, "
                  f"leaves={analytic['n_leaves']:6d}, "
                  f"fraction={analytic['barrier_fraction']:.4f}, "
                  f"root_req={analytic['root_required']}, "
                  f"internal_req={analytic['internal_required']}"
                  f"{verified_str}")

    # Analyze scaling
    results["scaling"] = _analyze_barrier_scaling(results)

    return results


def _analyze_barrier_scaling(results: dict) -> dict:
    """Analyze exponential scaling of barriers."""
    depths = results["depths"]
    barriers = [results["barriers"][d]["barrier"] for d in depths]

    # Check exponential fit: barrier(d) = a * q^d
    # log(barrier) = log(a) + d*log(q)
    q_values = []
    for i in range(1, len(barriers)):
        if barriers[i-1] > 0:
            q_values.append(barriers[i] / barriers[i-1])

    # Fit log-linear model
    log_barriers = [math.log(b) for b in barriers if b > 0]
    log_depths = [math.log(barriers[i]/barriers[i-1]) for i in range(1, len(barriers))]

    return {
        "barriers": barriers,
        "increases_with_depth": all(barriers[i] > barriers[i-1] for i in range(1, len(barriers))),
        "exponential": len(set(q_values)) <= 1 or all(abs(q - q_values[0]) < 0.01 for q in q_values),
        "growth_factor": q_values[0] if q_values else None,
        "q_values": q_values,
        "log_barriers": log_barriers,
    }


def print_summary(results: dict) -> None:
    """Print experiment summary."""
    scaling = results["scaling"]
    p = results["p"]

    print(f"\n{'='*60}")
    print(f"EXPERIMENT 0B SUMMARY")
    print(f"{'='*60}")

    print(f"\n  Barrier scaling: E_barrier(d) grows as:")
    if scaling["growth_factor"]:
        print(f"    E_barrier(d) = {results['barriers'][results['depths'][0]]['barrier']} * {scaling['growth_factor']}^(d-{results['depths'][0]})")

    print(f"\n  Barrier increases with depth: {scaling['increases_with_depth']}")
    print(f"  Growth is exponential: {scaling['exponential']}")

    if scaling.get("q_values"):
        print(f"  Growth factors per step: {[f'{q:.2f}' for q in scaling['q_values']]}")

    # Physical interpretation
    print(f"\n  PHYSICAL INTERPRETATION:")
    for depth in results["depths"]:
        b = results["barriers"][depth]
        print(f"    depth={depth}: {b['barrier']} leaf flips to flip root "
              f"({b['barrier_fraction']*100:.1f}% of {b['n_leaves']} leaves)")

    print(f"\n  At 4K (k_B*T ~ 3.45e-4 eV):")
    print(f"    For depth=10: barrier = {results['barriers'][10]['barrier']} leaf flips")
    print(f"    This represents an enormous energy barrier protecting logical states")
    print(f"    against thermal noise -- consistent with Gamma ~ 80 prediction.")


if __name__ == "__main__":
    print("Running Experiment 0B: Energy Barrier Scaling (Analytic)")
    print("=" * 60)

    results = run_experiment_0b(
        p=2,
        depths=[2, 3, 4, 5, 6, 7, 8, 9, 10],
        verify_small=True,
        verbose=True,
    )

    print_summary(results)

    print_barrier_table(results)
    try:
        _here = os.path.dirname(os.path.abspath(__file__))
        _plot_dir = os.path.join(_here, "plots")
        os.makedirs(_plot_dir, exist_ok=True)
        _save_path = os.path.join(_plot_dir, "exp0b_energy_barrier.png")
        plot_energy_barrier(results, save_path=_save_path)
        print(f"\n  Plot saved to {_save_path}")
    except Exception as e:
        print(f"\n  [Plot generation skipped: {e}]")

    print("\nExperiment 0B complete.")
