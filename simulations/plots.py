"""Visualization Utilities for Tier 0 Experiments.

Generates plots (matplotlib) and ASCII tables for computational
validation results. Falls back gracefully to ASCII output when
matplotlib is not available.
"""

from __future__ import annotations
import math
import os

# Try importing matplotlib, fall back gracefully
try:
    import matplotlib
    matplotlib.use("Agg")  # Non-interactive backend
    import matplotlib.pyplot as plt
    HAS_MPL = True
except ImportError:
    HAS_MPL = False


# ---------------------------------------------------------------------------
# ASCII Table Output (always available)
# ---------------------------------------------------------------------------

def print_error_confinement_table(results: dict) -> None:
    """Print ASCII table of error confinement results."""
    print(f"\n{'='*80}")
    print("ERROR CONFINEMENT TABLE")
    print(f"{'='*80}")

    depths = results["depths"]
    error_rates = results["error_rates"]

    # Header
    header = f"{'p_err':>6s}"
    for d in depths:
        header += f" | {'tree_LER(d=' + str(d) + ')':>16s} {'flat_LER':>9s} {'R_prop':>7s} {'Supp':>6s}"
    print(header)
    print("-" * len(header))

    for i, err in enumerate(error_rates):
        row = f"{err:6.3f}"
        for d in depths:
            if d in results:
                tree_ler = results[d]["tree_ler"][i]
                flat_ler = results[d]["flat_ler"][i]
                r_prop = results[d]["r_prop"][i]
                supp = results[d]["suppression"][i]
                row += f" | {tree_ler:16.4f} {flat_ler:9.4f} {r_prop:7.3f} {supp:6.1f}"
        print(row)

    # Summary row
    print("-" * len(header))
    summary = f"{'MEAN':>6s}"
    for d in depths:
        if d in results:
            mean_tree = sum(results[d]["tree_ler"]) / len(results[d]["tree_ler"])
            mean_flat = sum(results[d]["flat_ler"]) / len(results[d]["flat_ler"])
            mean_r = sum(results[d]["r_prop"]) / len(results[d]["r_prop"])
            mean_s = sum(results[d]["suppression"]) / len(results[d]["suppression"])
            summary += f" | {mean_tree:16.4f} {mean_flat:9.4f} {mean_r:7.3f} {mean_s:6.1f}"
    print(summary)


def print_barrier_table(results: dict) -> None:
    """Print ASCII table of energy barrier results."""
    print(f"\n{'='*60}")
    print("ENERGY BARRIER TABLE")
    print(f"{'='*60}")
    print(f"{'Depth':>6s} | {'Leaves':>8s} | {'Min Flips':>10s} | {'Theoretical':>12s} | {'Fraction':>10s}")
    print("-" * 60)

    for depth in results["depths"]:
        b = results["barriers"][depth]
        # Support both analytic (barrier) and search-based (min_flips) keys
        flip_val = b.get("barrier", b.get("min_flips"))
        theo_val = b.get("barrier", b.get("theoretical", flip_val))
        flip_str = str(flip_val) if flip_val is not None else ">max"
        frac = b.get("barrier_fraction", b.get("fraction"))
        frac_str = f"{frac:.4f}" if frac is not None else "N/A"
        print(f"{depth:6d} | {b.get('n_leaves', 0):8d} | {flip_str:>10s} | "
              f"{theo_val:12d} | {frac_str:>10s}")

    # Scaling analysis
    scaling = results.get("scaling", {})
    if scaling.get("q_values"):
        print(f"\n  Growth factors q: {[f'{q:.2f}' for q in scaling['q_values']]}")
        if scaling.get("mean_q"):
            print(f"  Mean q: {scaling['mean_q']:.2f}")
    print(f"  Barrier increases with depth: {scaling.get('increases_with_depth', 'N/A')}")


# ---------------------------------------------------------------------------
# Matplotlib Plots (when available)
# ---------------------------------------------------------------------------

def plot_error_confinement(results: dict, save_path: str | None = None) -> None:
    """Plot error confinement: LER vs physical error rate for tree vs flat.

    Args:
        results: Results dict from experiment_0a.run_experiment_0a()
        save_path: If provided, save plot to this path
    """
    if not HAS_MPL:
        print("[matplotlib not available -- skipping plot]")
        return

    depths = results["depths"]
    error_rates = results["error_rates"]
    p = results.get("p", 2)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(f"Experiment 0A: Ultrametric Error Confinement (p={p})",
                 fontsize=14, fontweight="bold")

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    # Plot 1: Logical error rate vs physical error rate
    ax = axes[0]
    for i, depth in enumerate(depths):
        color = colors[i % len(colors)]
        ax.plot(error_rates, results[depth]["tree_ler"], "o-",
                color=color, label=f"Tree d={depth}", markersize=4)
        ax.plot(error_rates, results[depth]["flat_ler"], "s--",
                color=color, alpha=0.5, label=f"Flat d={depth}", markersize=3)
    ax.plot([0, 0.5], [0, 0.5], "k:", alpha=0.3, label="LER = p_err")
    ax.set_xlabel("Physical Error Rate (p_err)")
    ax.set_ylabel("Logical Error Rate (LER)")
    ax.set_title("Logical Error Rate: Tree vs Flat Encoding")
    ax.legend(fontsize=7, loc="upper left")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, max(error_rates) * 1.05)
    ax.set_ylim(0, 0.55)

    # Plot 2: Error propagation ratio R_prop
    ax = axes[1]
    for i, depth in enumerate(depths):
        color = colors[i % len(colors)]
        r_props = results[depth]["r_prop"]
        ax.plot(error_rates, r_props, "o-", color=color,
                label=f"d={depth}", markersize=4)
    ax.axhline(y=1.0, color="red", linestyle="--", alpha=0.5,
               label="R_prop = 1 (no advantage)")
    ax.set_xlabel("Physical Error Rate (p_err)")
    ax.set_ylabel("Error Propagation Ratio (R_prop)")
    ax.set_title("Error Propagation Ratio: R_prop = tree_LER / flat_LER")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, max(error_rates) * 1.05)

    # Plot 3: Suppression factor vs depth
    ax = axes[2]
    for i, err_rate in enumerate([0.05, 0.10, 0.20, 0.30]):
        if i >= len(error_rates):
            break
        sf_values = []
        for depth in depths:
            idx = error_rates.index(err_rate) if err_rate in error_rates else i
            if idx < len(results[depth]["suppression"]):
                sf_values.append(results[depth]["suppression"][idx])
            else:
                sf_values.append(1.0)
        ax.plot(depths, sf_values, "o-", label=f"p_err={err_rate:.2f}",
                markersize=6, linewidth=2)
    ax.axhline(y=1.0, color="red", linestyle="--", alpha=0.3)
    ax.set_xlabel("Tree Depth (d)")
    ax.set_ylabel("Error Suppression Factor")
    ax.set_title("Suppression vs Tree Depth")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  Plot saved: {save_path}")

    plt.close()


def plot_energy_barrier(results: dict, save_path: str | None = None) -> None:
    """Plot energy barrier scaling with tree depth.

    Args:
        results: Results dict from experiment_0b.run_experiment_0b()
        save_path: If provided, save plot to this path
    """
    if not HAS_MPL:
        print("[matplotlib not available -- skipping plot]")
        return

    depths = results["depths"]
    barriers = [results["barriers"][d]["min_flips"] for d in depths]
    theoretical = [results["theoretical"][d] for d in depths]
    leaves = [results["barriers"][d]["n_leaves"] for d in depths]
    p = results.get("p", 2)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(f"Experiment 0B: Energy Barrier Scaling (p={p})",
                 fontsize=14, fontweight="bold")

    # Plot 1: Barrier (linear scale)
    ax = axes[0]
    ax.plot(depths, barriers, "bo-", label="Measured", markersize=8, linewidth=2)
    ax.plot(depths, theoretical, "r^--", label="Theoretical", markersize=8, linewidth=2)
    ax.set_xlabel("Tree Depth (d)")
    ax.set_ylabel("Minimum Leaf Flips to Flip Root")
    ax.set_title("Energy Barrier: Linear Scale")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 2: Barrier (log scale) with exponential fit
    ax = axes[1]
    valid_data = [(d, b) for d, b in zip(depths, barriers) if b is not None]
    if valid_data:
        d_vals, b_vals = zip(*valid_data)
        ax.semilogy(d_vals, b_vals, "bo-", label="Measured", markersize=8, linewidth=2)
        ax.semilogy(depths, theoretical, "r^--", label="Theoretical",
                    markersize=8, linewidth=2)
    ax.set_xlabel("Tree Depth (d)")
    ax.set_ylabel("Minimum Leaf Flips (log scale)")
    ax.set_title("Energy Barrier: Log Scale (exponential scaling)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Add barrier fraction annotation
    if valid_data:
        for d, b, n in zip(depths, barriers, leaves):
            if b is not None:
                frac = b / n if n > 0 else 0
                ax.annotate(f"{frac:.3f}", (d, b),
                           textcoords="offset points", xytext=(0, 10),
                           fontsize=8, ha="center")

    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches="tight")
        print(f"  Plot saved: {save_path}")

    plt.close()


def plot_ultrametric_verification(tree_result: dict,
                                   save_path: str | None = None) -> None:
    """Plot strong triangle inequality verification results."""
    if not HAS_MPL:
        return

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(["Violations", "Correct"], 
           [tree_result["strong_triangle_violations"],
            tree_result["trials"] - tree_result["strong_triangle_violations"]],
           color=["red", "green"])
    ax.set_ylabel("Number of Trials")
    ax.set_title("Strong Triangle Inequality Verification")
    ax.text(0.5, 0.5,
            f"{tree_result['trials']} trials\n"
            f"{tree_result['strong_triangle_violations']} violations",
            transform=ax.transAxes, ha="center", fontsize=12)

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=150, bbox_inches="tight")

    plt.close()
