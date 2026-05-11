"""Measurement and Analysis Utilities.

Computes performance metrics for tree vs. flat error correction:
  - Logical error rate: P(decoded != original)
  - Error propagation ratio: R_prop = logical_error_tree / logical_error_flat
  - Error suppression factor: 1 / R_prop
  - Energy barrier: minimum leaf flips to flip root
  - Confidence intervals via Wilson score
"""

from __future__ import annotations
import math
import random


def logical_error_rate(results: list[int]) -> float:
    """Logical error rate from binary trial results.

    Args:
        results: List of 0 (no error) or 1 (error) per trial

    Returns:
        float: p_L, the logical error rate (0.0 to 1.0)
    """
    if not results:
        return 0.0
    return sum(results) / len(results)


def error_propagation_ratio(tree_ler: float, flat_ler: float,
                            epsilon: float = 1e-10) -> float:
    """Ratio of tree logical error rate to flat logical error rate.

    R_prop < 1 means tree encoding suppresses errors.
    R_prop = 1 means no advantage.
    R_prop > 1 means tree encoding is worse.

    Returns:
        float: R_prop = tree_ler / flat_ler.
               Returns 1.0 when both are near zero (no advantage detected).
    """
    if tree_ler < epsilon and flat_ler < epsilon:
        return 1.0  # Both zero: no advantage detected
    denom = flat_ler if flat_ler > epsilon else epsilon
    return tree_ler / denom


def error_suppression_factor(tree_ler: float, flat_ler: float,
                              epsilon: float = 1e-10) -> float:
    """How many times fewer logical errors tree encoding produces.

    Returns:
        float: S = flat_ler / tree_ler.
               Returns 1.0 when both are near zero (no advantage detected).
               Returns large number when tree_ler ~ 0 but flat_ler > 0.
    """
    if tree_ler < epsilon and flat_ler < epsilon:
        return 1.0  # Both zero: no advantage detected
    if flat_ler < epsilon and tree_ler > epsilon:
        return 0.0  # Tree has errors but flat doesn't (bad for tree)
    denom = tree_ler if tree_ler > epsilon else epsilon
    return flat_ler / denom


def wilson_confidence_interval(successes: int, trials: int,
                                z: float = 1.96) -> tuple[float, float]:
    """Wilson score confidence interval for a proportion.

    More accurate than normal approximation for small n or p near 0/1.

    Args:
        successes: Number of successful trials
        trials: Total number of trials
        z: Z-score (1.96 for 95% CI)

    Returns:
        (lower_bound, upper_bound)
    """
    if trials == 0:
        return (0.0, 1.0)

    p_hat = successes / trials
    z2 = z * z
    n = trials

    denominator = 1 + z2 / n
    center = (p_hat + z2 / (2 * n)) / denominator
    margin = z * math.sqrt((p_hat * (1 - p_hat) + z2 / (4 * n)) / n) / denominator

    lower = max(0.0, center - margin)
    upper = min(1.0, center + margin)
    return (lower, upper)


def estimate_energy_barrier_min_flips(tree_oracle_fn, max_attempts: int = 1000
                                       ) -> int | None:
    """Estimate minimum number of leaf flips to change root value.

    Uses a simple hill-climbing search: start with all leaves at 0,
    flip random leaves, check if root changed.

    This is a lower-bound estimate of the effective energy barrier.

    Args:
        tree_oracle_fn: Function that takes a list of leaf indices to
                       flip and returns whether root value changed
        max_attempts: Maximum search attempts

    Returns:
        int or None: Estimated minimum flips to flip root
    """
    # Simple binary search on number of flips
    # Start with random flips and check threshold
    for k in range(1, max_attempts):
        for _ in range(100):
            leaf_indices = random.sample(range(max_attempts), k)
            if tree_oracle_fn(leaf_indices):
                return k
    return None


def compute_depth_scaling(depths: list[int],
                          error_rates: list[float],
                          results: dict) -> dict:
    """Analyze how error suppression scales with tree depth.

    For each depth, compute:
      - Mean logical error rate across physical error rates
      - Suppression factor at each physical error rate
      - Whether suppression increases with depth (it should)

    Returns:
        dict with scaling analysis
    """
    analysis = {"depths": depths, "by_depth": {}}

    for depth in depths:
        if depth not in results:
            continue
        tree_lers = results[depth]["tree_ler"]
        flat_lers = results[depth]["flat_ler"]

        suppression_factors = []
        for tree_ler, flat_ler, err in zip(tree_lers, flat_lers, error_rates):
            sf = error_suppression_factor(tree_ler, flat_ler)
            suppression_factors.append((err, sf))

        analysis["by_depth"][depth] = {
            "mean_tree_ler": sum(tree_lers) / len(tree_lers) if tree_lers else 0,
            "mean_flat_ler": sum(flat_lers) / len(flat_lers) if flat_lers else 0,
            "mean_suppression": (sum(s for _, s in suppression_factors) /
                                 len(suppression_factors) if suppression_factors else 1),
            "suppression_by_error_rate": suppression_factors,
        }

    # Check monotonicity: does suppression increase with depth?
    depths_sorted = sorted(analysis["by_depth"].keys())
    if len(depths_sorted) >= 2:
        sf_values = [analysis["by_depth"][d]["mean_suppression"]
                      for d in depths_sorted]
        analysis["suppression_increases_with_depth"] = all(
            sf_values[i] >= sf_values[i - 1] for i in range(1, len(sf_values))
        )

    return analysis


def summarize_trial(trial_name: str, results: list[int],
                    confidence: float = 0.95) -> dict:
    """Summarize a set of trial results.

    Args:
        trial_name: Name of the trial configuration
        results: List of 0/1 per trial
        confidence: Confidence level for intervals

    Returns:
        dict with LER, CI, and trial counts
    """
    n = len(results)
    successes = n - sum(results)
    ler = logical_error_rate(results)

    z = 1.96 if confidence == 0.95 else 1.645 if confidence == 0.90 else 1.0
    ci_low, ci_high = wilson_confidence_interval(successes, n, z)

    return {
        "name": trial_name,
        "trials": n,
        "logical_error_rate": ler,
        "ci_lower": ci_low,
        "ci_upper": ci_high,
        "confidence": confidence,
    }
