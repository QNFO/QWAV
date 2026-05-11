"""Experiment 0A: Error Confinement in Ultrametric Circuits.

Tests the core claim: encoding quantum states on a Bruhat-Tits tree
suppresses error propagation compared to flat (Archimedean) encoding.

Method:
  1. Build Bruhat-Tits trees at varying depths (d=2,3,4,5)
  2. Encode logical 0 across all leaves
  3. Apply independent bit-flip noise at probability p_err
  4. Decode using hierarchical majority vote
  5. Compare logical error rate with flat encoding (same # of bits)
  6. Compute error propagation ratio R_prop = tree_LER / flat_LER

Expected: R_prop < 1 for all p_err, with stronger suppression at
          greater tree depths (the ultrametric error confinement property).

Falsification: R_prop >= 1 (no suppression) or no depth dependence.
"""

from __future__ import annotations
import random
import time
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from btree import BruhatTitsTree, FlatEncoding
from encoding import TreeEncoder, FlatEncoder
from noise import bit_flip_noise, bit_flip_flat
from metrics import (logical_error_rate, error_propagation_ratio,
                      error_suppression_factor, wilson_confidence_interval,
                      compute_depth_scaling, summarize_trial)
from plots import plot_error_confinement, print_error_confinement_table


def run_experiment_0a(
    p: int = 2,
    depths: list[int] | None = None,
    error_rates: list[float] | None = None,
    trials_per_point: int = 1000,
    seed: int = 42,
    verbose: bool = True,
) -> dict:
    """Run the error confinement experiment.

    Args:
        p: Prime for p-adic tree (default 2)
        depths: Tree depths to test (default [2,3,4,5])
        error_rates: Physical error rates to test (default 0.01 to 0.50)
        trials_per_point: Number of trials per (depth, error_rate) point
        seed: Random seed for reproducibility
        verbose: Print progress

    Returns:
        dict with all experimental results
    """
    if depths is None:
        depths = [2, 3, 4, 5]
    if error_rates is None:
        error_rates = [0.01, 0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50]

    rng = random.Random(seed)
    results = {"p": p, "depths": depths, "error_rates": error_rates,
               "trials_per_point": trials_per_point, "seed": seed}

    for depth in depths:
        if verbose:
            print(f"\n{'='*60}")
            print(f"Depth {depth}")
            print(f"{'='*60}")

        tree = BruhatTitsTree(p=p, depth=depth)
        encoder = TreeEncoder(tree)
        n_bits = tree.num_leaves
        flat = FlatEncoding(n_bits=n_bits)
        flat_encoder = FlatEncoder(flat)

        tree_lers = []
        flat_lers = []
        tree_cis = []
        flat_cis = []
        r_props = []
        s_factors = []

        for err_rate in error_rates:
            # Tree encoding trials
            tree_results = []
            for _ in range(trials_per_point):
                result = encoder.encode_decode_roundtrip(
                    0,
                    lambda leaves: bit_flip_noise(leaves, err_rate, rng)
                )
                tree_results.append(result)

            # Flat encoding trials
            flat_results = []
            for _ in range(trials_per_point):
                result = flat_encoder.encode_decode_roundtrip(
                    0,
                    lambda enc: bit_flip_flat(enc, err_rate, rng)
                )
                flat_results.append(result)

            tree_ler = logical_error_rate(tree_results)
            flat_ler = logical_error_rate(flat_results)
            r_prop = error_propagation_ratio(tree_ler, flat_ler)
            s_factor = error_suppression_factor(tree_ler, flat_ler)

            tree_lers.append(tree_ler)
            flat_lers.append(flat_ler)
            r_props.append(r_prop)
            s_factors.append(s_factor)

            # Confidence intervals
            tree_summary = summarize_trial(
                f"tree_d{depth}_err{err_rate:.2f}", tree_results)
            flat_summary = summarize_trial(
                f"flat_d{depth}_err{err_rate:.2f}", flat_results)
            tree_cis.append((tree_summary["ci_lower"], tree_summary["ci_upper"]))
            flat_cis.append((flat_summary["ci_lower"], flat_summary["ci_upper"]))

            if verbose:
                print(f"  p_err={err_rate:.2f}: tree_LER={tree_ler:.4f}, "
                      f"flat_LER={flat_ler:.4f}, R_prop={r_prop:.3f}, "
                      f"suppression={s_factor:.1f}x")

        results[depth] = {
            "tree_ler": tree_lers,
            "flat_ler": flat_lers,
            "r_prop": r_props,
            "suppression": s_factors,
            "tree_ci": tree_cis,
            "flat_ci": flat_cis,
            "n_leaves": n_bits,
        }

    # Compute scaling analysis
    results["scaling"] = compute_depth_scaling(depths, error_rates, results)

    return results


def print_summary(results: dict) -> None:
    """Print a summary of experiment results."""
    print(f"\n{'='*60}")
    print(f"EXPERIMENT 0A SUMMARY")
    print(f"{'='*60}")
    print(f"  p-adic prime: p = {results['p']}")
    print(f"  Depths tested: {results['depths']}")
    print(f"  Trials per point: {results['trials_per_point']}")
    print(f"  Random seed: {results['seed']}")

    print(f"\n  Mean Suppression Factors by Depth:")
    scaling = results.get("scaling", {})
    for depth in results["depths"]:
        sf = scaling.get("by_depth", {}).get(depth, {}).get("mean_suppression", "N/A")
        print(f"    depth={depth}: {sf:.1f}x" if isinstance(sf, float) else f"    depth={depth}: {sf}")

    # Check key prediction
    depth_increases = scaling.get("suppression_increases_with_depth", None)
    if depth_increases is True:
        print(f"\n  [PASS] PREDICTION CONFIRMED: Error suppression increases with tree depth")
    elif depth_increases is False:
        print(f"\n  [FAIL] PREDICTION FALSIFIED: Error suppression does NOT increase with depth")
    else:
        print(f"\n  ? Insufficient data to verify depth scaling")

    # Best-case suppression
    all_sf = []
    for depth in results["depths"]:
        all_sf.extend(results[depth]["suppression"])
    if all_sf:
        print(f"  Best suppression: {max(all_sf):.1f}x")
        print(f"  Worst suppression: {min(all_sf):.1f}x")

    print(f"\n  File output: See plots and tables below.")


if __name__ == "__main__":
    # Run with modest settings for quick testing
    print("Running Experiment 0A: Error Confinement")
    print("=" * 60)

    t0 = time.time()
    results = run_experiment_0a(
        p=2,
        depths=[2, 3, 4, 5],
        error_rates=[0.01, 0.02, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40],
        trials_per_point=500,
        seed=42,
        verbose=True,
    )
    elapsed = time.time() - t0

    print_summary(results)
    print(f"\n  Total runtime: {elapsed:.1f}s")

    # Generate plots and tables
    print_error_confinement_table(results)
    try:
        # Determine script directory for reliable save path
        _here = os.path.dirname(os.path.abspath(__file__))
        _plot_dir = os.path.join(_here, "plots")
        os.makedirs(_plot_dir, exist_ok=True)
        _save_path = os.path.join(_plot_dir, "exp0a_error_confinement.png")
        plot_error_confinement(results, save_path=_save_path)
        print(f"\n  Plot saved to {_save_path}")
    except Exception as e:
        print(f"\n  [Plot generation skipped: {e}]")
        print("  (Install matplotlib for graphical plots)")

    print("\nExperiment 0A complete.")
