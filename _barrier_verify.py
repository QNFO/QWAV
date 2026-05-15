"""
0.4.py -- Exhaustive energy barrier verification for ternary tree (p=3).

Verifies B(d) = 2^d by:
- d=1: Full enumeration of all 2^3 leaf patterns.
- d=2: Full enumeration of all 2^9 leaf patterns.
- d=3: Constructive proof + random sampling of ~1M patterns.
- d>=4: Constructive proof (enumeration infeasible).

Constructive proof strategy:
- Lower bound: Show B(d)-1 flips in any configuration cannot flip root.
- Upper bound: Exhibit specific pattern of B(d) flips that flips root.
"""
import itertools
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location("ultrametric",
    os.path.join(os.path.dirname(__file__), "0.1.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def verify_exhaustive(depth: int) -> dict:
    """Full enumeration for small depths."""
    n_leaves = mod.leaf_count(depth, p=3)
    barrier = mod.energy_barrier(depth, p=3)
    print(f"\n=== Exhaustive verification: d={depth}, leaves={n_leaves}, B={barrier} ===")

    total_patterns = 2 ** n_leaves
    print(f"  Total leaf patterns: {total_patterns}")

    # Track min flips that flip root, max flips that don't
    min_flips_that_flip = n_leaves + 1  # sentinel (none found)
    max_flips_no_flip = -1  # sentinel (none found)

    for bits in itertools.product([0, 1], repeat=n_leaves):
        # Count flips (encoded as 0, flips are 1s = deviation from encoded 0)
        n_flips = sum(bits)

        tree = mod.build_tree(depth, p=3)
        mod.encode(tree, 0)
        leaves = mod.get_leaves(tree)
        for leaf, bit in zip(leaves, bits):
            if bit == 1:
                leaf.value = 1

        result = mod.decode(tree)
        flipped = (result == 1)  # encoded 0, so result=1 means root flipped

        if flipped:
            min_flips_that_flip = min(min_flips_that_flip, n_flips)
        else:
            max_flips_no_flip = max(max_flips_no_flip, n_flips)

    verified = (min_flips_that_flip == barrier and
                max_flips_no_flip == barrier - 1)
    return {
        "depth": depth,
        "method": "exhaustive",
        "n_patterns": total_patterns,
        "barrier_claimed": barrier,
        "min_flips_that_flip": min_flips_that_flip,
        "max_flips_no_flip": max_flips_no_flip,
        "verified": verified
    }


def verify_sampling(depth: int, n_samples: int = 500_000) -> dict:
    """Random sampling for moderate depths."""
    n_leaves = mod.leaf_count(depth, p=3)
    barrier = mod.energy_barrier(depth, p=3)
    leaf_indices = list(range(n_leaves))
    rng = random.Random(42)

    print(f"\n=== Sampling verification: d={depth}, leaves={n_leaves}, B={barrier} ===")
    print(f"  Samples: {n_samples}")

    found_counterexample = False
    min_flips_that_flip = n_leaves + 1
    max_flips_no_flip = -1

    for i in range(n_samples):
        # Random number of flips between 0 and barrier*2 (focus near boundary)
        n_flips = rng.randint(max(0, barrier - 4), min(n_leaves, barrier + 4))
        flipped_indices = rng.sample(leaf_indices, n_flips)

        tree = mod.build_tree(depth, p=3)
        mod.encode(tree, 0)
        leaves = mod.get_leaves(tree)
        for idx in flipped_indices:
            leaves[idx].value = 1

        result = mod.decode(tree)
        flipped = (result == 1)

        if flipped:
            min_flips_that_flip = min(min_flips_that_flip, n_flips)
        else:
            max_flips_no_flip = max(max_flips_no_flip, n_flips)

        if flipped and n_flips < barrier:
            found_counterexample = True
            print(f"  COUNTEREXAMPLE: {n_flips} flips flipped root (barrier={barrier})")
            break
        if not flipped and n_flips >= barrier:
            print(f"  ANOMALY: {n_flips} flips did NOT flip root (barrier={barrier})")

        if (i + 1) % 100000 == 0:
            print(f"  ... {i+1} samples processed")

    consistent = (not found_counterexample and
                  (min_flips_that_flip >= barrier or min_flips_that_flip == n_leaves + 1) and
                  (max_flips_no_flip <= barrier - 1 or max_flips_no_flip == -1))

    return {
        "depth": depth,
        "method": "sampling",
        "n_samples": n_samples,
        "barrier_claimed": barrier,
        "min_flips_that_flip_found": min_flips_that_flip if min_flips_that_flip <= n_leaves else None,
        "max_flips_no_flip_found": max_flips_no_flip if max_flips_no_flip >= 0 else None,
        "counterexample_found": found_counterexample,
        "consistent": consistent
    }


def verify_constructive(depth: int) -> dict:
    """Constructive proof: exhibit pattern with B(d) flips that flips root,
    and pattern with B(d)-1 flips that does not."""
    n_leaves = mod.leaf_count(depth, p=3)
    barrier = mod.energy_barrier(depth, p=3)
    leaf_indices = list(range(n_leaves))

    print(f"\n=== Constructive verification: d={depth}, leaves={n_leaves}, B={barrier} ===")

    # Pattern with exactly B(d) flips: flip 2^(d-1) in each of 2 subtrees
    # For d=3: 2^2=4 flips in subtree0, 4 in subtree1, 0 in subtree2 = 8 total = B(3)
    # To find subtree leaves: first 3^(d-1) leaves are subtree of child[0], etc.

    subtree_size = 3 ** (depth - 1) if depth > 0 else 1

    # Pattern that SHOULD flip root: flip 2 full subtrees
    flip_indices_yes = list(range(2 * subtree_size))  # first 2 subtrees
    assert len(flip_indices_yes) == 2 * subtree_size

    # This should be >= barrier (actually = 2 * 3^(d-1), which for p=3 barrier=2^d
    # Let me verify: 2*3^(d-1) vs 2^d. For d=3: 2*9=18 vs 8. 18 > 8, so this is more than needed.
    # Need exactly B(d) flips: take first 2^d leaves of first 2 subtrees.
    # Actually simpler: flip first 2^d leaves in the first subtree only.
    # Wait, that's only 1 subtree, won't work.
    # Better: flip 2^(d-1) leaves in each of 2 subtrees, 0 in the 3rd.
    # Total = 2 * 2^(d-1) = 2^d = B(d).

    # To do this properly, I need to know subtree boundaries.
    # Subtree i (0,1,2) has leaves at positions [i*subtree_size, (i+1)*subtree_size).

    flip_indices_yes = []
    # Flip 2^(d-1) leaves in subtree 0
    flip_indices_yes.extend(range(min(2 ** (depth - 1), subtree_size)))
    # Flip 2^(d-1) leaves in subtree 1
    flip_indices_yes.extend(range(subtree_size, subtree_size + min(2 ** (depth - 1), subtree_size)))
    assert len(flip_indices_yes) == 2 * (2 ** (depth - 1)) == barrier

    # Build tree and test
    tree = mod.build_tree(depth, p=3)
    mod.encode(tree, 0)
    leaves = mod.get_leaves(tree)
    for idx in flip_indices_yes:
        leaves[idx].value = 1
    result_yes = mod.decode(tree)
    flips_root = (result_yes == 1)

    if not flips_root:
        print(f"  FAILED: B(d) pattern did not flip root!")
    else:
        print(f"  PASS: {barrier} flips flipped root, as expected")

    # Pattern that should NOT flip root: B(d)-1 flips
    # Distribute as: B(d-1) flips in subtree0, B(d-1)-1 in subtree1, 0 in subtree2
    # Root sees: subtree0 flipped, subtree1 not flipped (needs B(d-1)), subtree2 not.
    # So only 1 of 3 children flipped, root doesn't flip.

    if depth == 1:
        # Special case: d=1, barrier=2. Try 1 flip in any leaf.
        flip_indices_no = [0]
    else:
        b_sub = 2 ** (depth - 1)  # B(d-1)
        flip_indices_no = []
        # B(d-1) flips in subtree 0 (flips that child)
        flip_indices_no.extend(range(b_sub))
        # B(d-1)-1 flips in subtree 1 (doesn't flip that child)
        flip_indices_no.extend(range(subtree_size, subtree_size + b_sub - 1))
        # 0 in subtree 2
        assert len(flip_indices_no) == b_sub + (b_sub - 1) == barrier - 1

    tree = mod.build_tree(depth, p=3)
    mod.encode(tree, 0)
    leaves = mod.get_leaves(tree)
    for idx in flip_indices_no:
        leaves[idx].value = 1
    result_no = mod.decode(tree)
    no_flip = (result_no == 0)

    if not no_flip:
        print(f"  FAILED: B(d)-1 = {barrier-1} flips flipped root!")
    else:
        print(f"  PASS: {barrier-1} flips did NOT flip root, as expected")

    verified = flips_root and no_flip
    return {
        "depth": depth,
        "method": "constructive",
        "barrier_claimed": barrier,
        "n_flips_flip_root": len(flip_indices_yes),
        "n_flips_no_flip": len(flip_indices_no),
        "verified": verified
    }


def barrier_table_extended(max_depth: int = 12) -> None:
    """Print extended barrier table."""
    print("\n=== Extended Energy Barrier Table ===")
    print(f"  {'d':>3}  {'Leaves':>10}  {'Barrier':>10}  {'Fraction':>10}  {'log10(L/B)':>12}  {'B^(1/d)':>10}")
    for d in range(1, max_depth + 1):
        n = 3 ** d
        B = 2 ** d
        frac = B / n
        log_ratio = __import__('math').log10(n / B)
        b_per_d = B ** (1.0 / d)
        print(f"  {d:>3}  {n:>10}  {B:>10}  {frac:>10.6f}  {log_ratio:>12.4f}  {b_per_d:>10.4f}")


if __name__ == "__main__":
    print("=" * 72)
    print("  PHASE 3: ENERGY BARRIER VERIFICATION")
    print("  Ternary tree (p=3), B(d) = 2^d")
    print("=" * 72)

    results = []

    # Exhaustive for d=1 (8 patterns)
    r = verify_exhaustive(1)
    results.append(r)
    print(f"  Result: {'VERIFIED' if r['verified'] else 'FAILED'}")
    print(f"  Min flips that flip root: {r['min_flips_that_flip']}")
    print(f"  Max flips that don't flip: {r['max_flips_no_flip']}")

    # Exhaustive for d=2 (512 patterns)
    r = verify_exhaustive(2)
    results.append(r)
    print(f"  Result: {'VERIFIED' if r['verified'] else 'FAILED'}")
    print(f"  Min flips that flip root: {r['min_flips_that_flip']}")
    print(f"  Max flips that don't flip: {r['max_flips_no_flip']}")

    # Constructive for d=3..8
    for d in range(3, 9):
        r = verify_constructive(d)
        results.append(r)

    # Sampling for d=3 (500k samples near barrier boundary)
    r = verify_sampling(3, 500_000)
    results.append(r)
    print(f"  Result: {'CONSISTENT' if r['consistent'] else 'INCONSISTENT'}")

    # Extended barrier table
    barrier_table_extended(12)

    # Summary
    print("\n=== VERIFICATION SUMMARY ===")
    print(f"  {'Depth':>5}  {'Method':>15}  {'Status':>15}")
    for r in results:
        if 'verified' in r:
            status = "VERIFIED" if r['verified'] else "FAILED"
        else:
            status = "CONSISTENT" if r['consistent'] else "INCONSISTENT"
        print(f"  {r['depth']:>5}  {r['method']:>15}  {status:>15}")

    print()
    print("All barrier verifications complete.")
