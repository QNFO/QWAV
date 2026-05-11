"""State Encoding on Bruhat-Tits Trees.

Defines how logical quantum states are encoded onto tree structures.
For Tier 0 (classical simulation), this uses repetition-like encoding:
each leaf carries a copy of the logical bit, and the tree structure
provides hierarchical majority-vote decoding.

For quantum simulation (future), this would encode qubit states using
tree-path superpositions with ultrametric error protection.
"""

from __future__ import annotations
from btree import BruhatTitsTree, FlatEncoding, Node


class TreeEncoder:
    """Repetition encoder on a Bruhat-Tits tree.

    Encodes a single classical bit (the logical value) across all leaf
    nodes of the tree. Decoding uses hierarchical majority vote which
    exploits the ultrametric structure for error suppression.

    Args:
        tree: The Bruhat-Tits tree to encode onto
    """

    def __init__(self, tree: BruhatTitsTree):
        self.tree = tree

    def encode(self, logical_value: int) -> None:
        """Encode logical_value (0 or 1) across all leaves."""
        if logical_value not in (0, 1):
            raise ValueError(f"logical_value must be 0 or 1, got {logical_value}")
        for leaf in self.tree.leaves:
            leaf.value = logical_value

    def decode(self, tie_breaker: int = 0) -> int:
        """Decode the logical value from leaf states.

        Propagates leaf values up the tree using majority vote at each
        level. The ultrametric structure means errors confined to
        individual subtrees are filtered before reaching the root.

        Returns:
            int: The decoded logical value (0 or 1)
        """
        self.tree.propagate_up(tie_breaker=tie_breaker)
        return self.tree.root.value

    def encode_decode_roundtrip(self, logical_value: int,
                                 noise_fn, tie_breaker: int = 0) -> int:
        """Encode, apply noise, then decode.

        Args:
            logical_value: The original logical bit (0 or 1)
            noise_fn: Function that applies noise to leaves
            tie_breaker: Value for tie-breaking in majority vote

        Returns:
            int: 1 if logical error occurred (decoded != original), 0 otherwise
        """
        self.encode(logical_value)
        noise_fn(self.tree.leaves)
        decoded = self.decode(tie_breaker=tie_breaker)
        return 1 if decoded != logical_value else 0


class FlatEncoder:
    """Repetition encoder for flat (non-hierarchical) comparison.

    Same number of bits as tree leaves, but no hierarchical structure.
    Uses global majority vote for decoding.
    """

    def __init__(self, encoding: FlatEncoding):
        self.encoding = encoding

    def encode(self, logical_value: int) -> None:
        """Set all bits to logical_value."""
        self.encoding.reset(logical_value)

    def decode(self, tie_breaker: int = 0) -> int:
        """Global majority vote."""
        return self.encoding.majority_vote(tie_breaker=tie_breaker)

    def encode_decode_roundtrip(self, logical_value: int,
                                 noise_fn, tie_breaker: int = 0) -> int:
        """Encode, apply noise, decode."""
        self.encode(logical_value)
        noise_fn(self.encoding)
        decoded = self.decode(tie_breaker=tie_breaker)
        return 1 if decoded != logical_value else 0
