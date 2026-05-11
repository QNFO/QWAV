"""Bruhat-Tits Tree Construction and Traversal.

Implements a rooted tree approximating the Bruhat-Tits tree T_p for
prime p. The key property: the strong triangle inequality d(x,z) <=
max(d(x,y), d(y,z)) where distance is measured by the depth of the
lowest common ancestor.

For simulation purposes we use a complete k-ary tree where:
  - Root has (p+1) children (for p=2: 3 children)
  - All other non-leaf nodes have p children
  - Leaves are at the specified depth

The tree supports:
  - Construction to arbitrary depth
  - Node-level value storage (classical bits 0/1)
  - Hierarchical majority-vote propagation
  - Ultrametric distance computation between any two leaves
  - Subtree extraction for targeted noise injection
"""

from __future__ import annotations
import random
import math


class Node:
    """A node in the Bruhat-Tits tree.

    Attributes:
        value: Classical bit value (0 or 1)
        children: List of child nodes
        parent: Parent node (None for root)
        index: Unique index within the tree (assigned by Tree)
    """

    def __init__(self, value: int = 0):
        self.value = value
        self.children: list[Node] = []
        self.parent: Node | None = None
        self.index: int = -1

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def is_root(self) -> bool:
        return self.parent is None

    @property
    def depth(self) -> int:
        """Depth: 0 for root, increasing downward."""
        if self.is_root():
            return 0
        return self.parent.depth + 1

    def __repr__(self) -> str:
        kind = "root" if self.is_root() else ("leaf" if self.is_leaf() else "internal")
        return f"Node(idx={self.index}, depth={self.depth}, value={self.value}, {kind})"


class BruhatTitsTree:
    """A rooted Bruhat-Tits tree for p-adic simulation.

    For prime p:
      - Root has (p+1) children
      - All non-root non-leaf nodes have p children
      - Depth d means leaves are at level d (root at level 0)

    Args:
        p: Prime for the p-adic tree (default 2)
        depth: Number of levels below root (default 3)
    """

    def __init__(self, p: int = 2, depth: int = 3):
        if p < 2:
            raise ValueError(f"p must be >= 2, got {p}")
        if depth < 1:
            raise ValueError(f"depth must be >= 1, got {depth}")

        self.p = p
        self.depth = depth
        self.root: Node | None = None
        self.nodes: list[Node] = []
        self.leaves: list[Node] = []
        self._build()

    def _build(self) -> None:
        """Build the tree recursively."""
        self.root = Node()
        self.root.index = 0
        self.nodes = [self.root]
        self._build_subtree(self.root, self.p + 1, 0)

    def _build_subtree(self, node: Node, branching: int, current_depth: int) -> None:
        """Recursively build subtrees."""
        if current_depth >= self.depth:
            self.leaves.append(node)
            return

        for _ in range(branching):
            child = Node()
            child.index = len(self.nodes)
            child.parent = node
            node.children.append(child)
            self.nodes.append(child)
            # Non-root nodes have p children
            self._build_subtree(child, self.p, current_depth + 1)

    @property
    def num_nodes(self) -> int:
        return len(self.nodes)

    @property
    def num_leaves(self) -> int:
        return len(self.leaves)

    def get_nodes_at_depth(self, d: int) -> list[Node]:
        """Return all nodes at the given depth."""
        return [n for n in self.nodes if n.depth == d]

    def reset_values(self, value: int = 0) -> None:
        """Set all node values to the given value."""
        for node in self.nodes:
            node.value = value

    def propagate_up(self, tie_breaker: int = 0) -> None:
        """Propagate leaf values upward using majority vote.

        For each internal node (processed from leaves to root):
          - Count 0s and 1s among children
          - Set node value to majority
          - On tie, use tie_breaker

        Args:
            tie_breaker: Value to use when children are evenly split (default 0)
        """
        for d in range(self.depth - 1, -1, -1):
            for node in self.get_nodes_at_depth(d):
                if node.is_leaf():
                    continue
                ones = sum(c.value for c in node.children)
                zeros = len(node.children) - ones
                if ones > zeros:
                    node.value = 1
                elif zeros > ones:
                    node.value = 0
                else:
                    node.value = tie_breaker

    def lowest_common_ancestor(self, a: Node, b: Node) -> Node:
        """Find the lowest common ancestor of two nodes."""
        # Bring both to same depth
        while a.depth > b.depth:
            a = a.parent
        while b.depth > a.depth:
            b = b.parent
        # Walk up together
        while a is not b:
            a = a.parent
            b = b.parent
        return a

    def ultrametric_distance(self, a: Node, b: Node) -> int:
        """Ultrametric distance between two nodes.

        Distance = self.depth - depth(LCA(a,b))
        This satisfies the strong triangle inequality:
            d(x,z) <= max(d(x,y), d(y,z))

        Returns:
            int: Distance in tree levels (0 = same node, depth = in different
                 root-level subtrees)
        """
        lca = self.lowest_common_ancestor(a, b)
        return self.depth - lca.depth

    def verify_strong_triangle_inequality(self, trials: int = 1000) -> dict:
        """Verify the strong triangle inequality holds for random leaf triples.

        The strong triangle inequality: d(x,z) <= max(d(x,y), d(y,z))
        Also checks the isosceles property: two largest distances are equal.

        Returns:
            dict with verification statistics
        """
        violations = 0
        isosceles_violations = 0

        for _ in range(trials):
            x, y, z = random.sample(self.leaves, 3)
            d_xy = self.ultrametric_distance(x, y)
            d_yz = self.ultrametric_distance(y, z)
            d_xz = self.ultrametric_distance(x, z)

            # Strong triangle inequality
            if d_xz > max(d_xy, d_yz):
                violations += 1

            # Isosceles property: two largest distances should be equal
            dists = sorted([d_xy, d_yz, d_xz])
            if dists[2] != dists[1]:  # largest two not equal
                isosceles_violations += 1

        return {
            "trials": trials,
            "strong_triangle_violations": violations,
            "isosceles_violations": isosceles_violations,
            "strong_triangle_holds": violations == 0,
            "isosceles_holds": isosceles_violations == 0,
        }

    def get_subtree(self, node: Node) -> list[Node]:
        """Get all nodes in the subtree rooted at the given node."""
        result = [node]
        for child in node.children:
            result.extend(self.get_subtree(child))
        return result

    def print_tree(self, max_nodes: int = 40) -> str:
        """Return a string representation of the tree."""
        lines = []
        for d in range(self.depth + 1):
            nodes_at_d = self.get_nodes_at_depth(d)
            values = ",".join(str(n.value) for n in nodes_at_d[:max_nodes])
            lines.append(f"  depth {d} ({len(nodes_at_d)} nodes): [{values}]")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Flat (Archimedean) encoding for comparison
# ---------------------------------------------------------------------------

class FlatEncoding:
    """Flat (non-hierarchical) encoding for comparison with tree encoding.

    Simulates N independent bits with global majority vote. This represents
    the standard Archimedean approach: all bits are at the same level, no
    hierarchical error confinement.
    """

    def __init__(self, n_bits: int):
        if n_bits < 1:
            raise ValueError(f"n_bits must be >= 1, got {n_bits}")
        self.n_bits = n_bits
        self.bits: list[int] = []

    def reset(self, value: int = 0) -> None:
        """Set all bits to given value."""
        self.bits = [value] * self.n_bits

    def apply_noise(self, error_rate: float, rng: random.Random | None = None) -> None:
        """Flip each bit independently with probability error_rate."""
        if rng is None:
            rng = random.Random()
        for i in range(self.n_bits):
            if rng.random() < error_rate:
                self.bits[i] = 1 - self.bits[i]

    def majority_vote(self, tie_breaker: int = 0) -> int:
        """Return majority value of all bits."""
        ones = sum(self.bits)
        zeros = self.n_bits - ones
        if ones > zeros:
            return 1
        elif zeros > ones:
            return 0
        return tie_breaker

    @property
    def logical_value(self) -> int:
        """The decoded logical value (majority vote)."""
        return self.majority_vote()


# ---------------------------------------------------------------------------
# Convenience factory
# ---------------------------------------------------------------------------

def create_tree(p: int = 2, depth: int = 3) -> BruhatTitsTree:
    """Create a Bruhat-Tits tree for simulation."""
    return BruhatTitsTree(p=p, depth=depth)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Bruhat-Tits Tree Self-Test")
    print("=" * 60)

    for p in [2, 3]:
        for d in [2, 3, 4]:
            tree = BruhatTitsTree(p=p, depth=d)
            print(f"\np={p}, depth={d}: "
                  f"nodes={tree.num_nodes}, leaves={tree.num_leaves}")

    # Verify strong triangle inequality
    print("\n--- Strong Triangle Inequality Verification ---")
    for p in [2, 3, 5]:
        tree = BruhatTitsTree(p=p, depth=5)
        result = tree.verify_strong_triangle_inequality(trials=5000)
        status = "PASS" if result["strong_triangle_holds"] else "FAIL"
        isosceles = "PASS" if result["isosceles_holds"] else "FAIL"
        print(f"  p={p}: strong_triangle={status}, isosceles={isosceles} "
              f"(violations: {result['strong_triangle_violations']}, "
              f"{result['isosceles_violations']})")

    print("\n--- Majority Vote Propagation ---")
    tree = BruhatTitsTree(p=2, depth=3)
    print(f"  Tree: p=2, depth=3, leaves={tree.num_leaves}")

    # Set 70% of leaves to 1
    for i, leaf in enumerate(tree.leaves):
        leaf.value = 1 if i < 0.7 * tree.num_leaves else 0
    tree.propagate_up()
    print(f"  Root value with 70% ones: {tree.root.value}")

    # Set 30% to 1
    tree.reset_values(0)
    for i, leaf in enumerate(tree.leaves):
        leaf.value = 1 if i < 0.3 * tree.num_leaves else 0
    tree.propagate_up()
    print(f"  Root value with 30% ones: {tree.root.value}")

    print("\n--- Flat Encoding Self-Test ---")
    flat = FlatEncoding(n_bits=12)
    flat.reset(0)
    flat.bits = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]  # 7 ones, 5 zeros
    print(f"  Bits={flat.bits}, majority={flat.majority_vote()}")
    flat.bits = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]  # 5 ones, 7 zeros
    print(f"  Bits={flat.bits}, majority={flat.majority_vote()}")

    print("\nAll self-tests complete.")
