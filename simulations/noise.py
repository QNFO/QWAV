"""Error Models for Tree Circuit Simulation.

Implements noise channels that can be applied to leaf nodes of the
Bruhat-Tits tree or flat encodings. For Tier 0 (classical simulation),
we use bit-flip noise. Future extensions include depolarizing and
thermal noise models.
"""

from __future__ import annotations
import random
from btree import Node
from encoding import FlatEncoding


def bit_flip_noise(leaves: list[Node], error_rate: float,
                   rng: random.Random | None = None) -> None:
    """Apply independent bit-flip noise to each leaf.

    Each leaf's value is flipped (0<->1) with probability error_rate.

    Args:
        leaves: List of leaf nodes to apply noise to
        error_rate: Probability of flipping each bit (0.0 to 0.5)
        rng: Random number generator (uses fresh instance if None)
    """
    if rng is None:
        rng = random.Random()

    for leaf in leaves:
        if rng.random() < error_rate:
            leaf.value = 1 - leaf.value


def bit_flip_flat(encoding: FlatEncoding, error_rate: float,
                  rng: random.Random | None = None) -> None:
    """Apply bit-flip noise to a flat encoding."""
    encoding.apply_noise(error_rate, rng)


def correlated_noise(leaves: list[Node], error_rate: float,
                     correlation_length: int = 1,
                     rng: random.Random | None = None) -> None:
    """Apply spatially correlated noise to leaves.

    Flips a contiguous block of `correlation_length` leaves with
    probability `error_rate`. This models noise sources that affect
    multiple nearby qubits simultaneously.

    Args:
        leaves: Leaf nodes (ordered)
        error_rate: Probability of a correlated error event starting at each leaf
        correlation_length: Number of adjacent leaves affected per event
        rng: Random number generator
    """
    if rng is None:
        rng = random.Random()

    n = len(leaves)
    i = 0
    while i < n:
        if rng.random() < error_rate:
            for j in range(i, min(i + correlation_length, n)):
                leaves[j].value = 1 - leaves[j].value
            i += correlation_length
        else:
            i += 1


def targeted_subtree_noise(tree_root: Node, subtree_depth: int,
                           error_rate: float,
                           rng: random.Random | None = None) -> None:
    """Apply noise to leaves within a specific subtree.

    Useful for testing whether errors in one subtree propagate to the
    root or remain confined.

    Args:
        tree_root: Root of the full tree
        subtree_depth: Depth of the targeted subtree root (0 = tree root)
        error_rate: Bit-flip probability for each leaf in the subtree
        rng: Random number generator
    """
    if rng is None:
        rng = random.Random()

    # Find a node at the specified depth
    candidates = [n for n in _get_all_descendants(tree_root)
                  if n.depth == subtree_depth and not n.is_leaf()]
    if not candidates:
        return

    target = rng.choice(candidates)
    subtree_leaves = [n for n in _get_all_descendants(target) if n.is_leaf()]

    for leaf in subtree_leaves:
        if rng.random() < error_rate:
            leaf.value = 1 - leaf.value


def _get_all_descendants(node: Node) -> list[Node]:
    """Get all nodes in the subtree rooted at node."""
    result = [node]
    for child in node.children:
        result.extend(_get_all_descendants(child))
    return result
