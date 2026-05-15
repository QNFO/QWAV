# Standalone barrier verification - no imports needed
import itertools, random, math
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

@dataclass
class Node:
    value: int = 0
    depth: int = 0
    children: List['Node'] = field(default_factory=list)
    parent: Optional['Node'] = None
    @property
    def is_leaf(self): return len(self.children) == 0

def build_tree(depth, p=3):
    if depth < 0: raise ValueError
    root = Node(depth=0)
    def _build(parent, rem):
        if rem == 0: return
        for _ in range(p):
            c = Node(depth=parent.depth + 1, parent=parent)
            parent.children.append(c)
            _build(c, rem - 1)
    _build(root, depth)
    return root

def get_leaves(root):
    leaves = []
    def collect(n):
        if n.is_leaf: leaves.append(n)
        else:
            for c in n.children: collect(c)
    collect(root)
    return leaves

def encode(root, bit):
    for leaf in get_leaves(root): leaf.value = bit

def decode(root):
    def _decode(n):
        if n.is_leaf: return n.value
        vals = [_decode(c) for c in n.children]
        r = 1 if sum(vals) > len(vals) - sum(vals) else 0
        n.value = r
        return r
    return _decode(root)

def build_barrier_pattern(depth, offset=0):
    if depth == 0: return []
    if depth == 1: return [offset, offset + 1]
    ss = 3 ** (depth - 1)
    p = []
    p.extend(build_barrier_pattern(depth - 1, offset))
    p.extend(build_barrier_pattern(depth - 1, offset + ss))
    return p

def build_non_flipping_pattern(depth, offset=0):
    if depth == 0: return []
    if depth == 1: return [offset]
    ss = 3 ** (depth - 1)
    p = []
    p.extend(build_barrier_pattern(depth - 1, offset))
    p.extend(build_non_flipping_pattern(depth - 1, offset + ss))
    return p

results = []

# Constructive d=1..15
print("Constructive proofs:")
for d in range(1, 16):
    B = 2**d
    py = build_barrier_pattern(d)
    pn = build_non_flipping_pattern(d)
    assert len(py) == B
    assert len(pn) == B - 1
    
    t = build_tree(d)
    encode(t, 0)
    for idx in py: get_leaves(t)[idx].value = 1
    ry = decode(t)
    
    t = build_tree(d)
    encode(t, 0)
    for idx in pn: get_leaves(t)[idx].value = 1
    rn = decode(t)
    
    ok = ry == 1 and rn == 0
    results.append(f"d={d:>2}  B={B:>6}  flip={ry} noflip={rn}  {'PASS' if ok else 'FAIL'}")

# Exhaustive d=1,2
print("Exhaustive verification:")
for d in [1, 2]:
    n = 3**d
    B = 2**d
    min_flip = n + 1
    for bits in itertools.product([0, 1], repeat=n):
        nf = sum(bits)
        t = build_tree(d)
        encode(t, 0)
        for i, b in enumerate(bits):
            if b: get_leaves(t)[i].value = 1
        if decode(t) == 1:
            min_flip = min(min_flip, nf)
    ok = min_flip >= B
    results.append(f"d={d}  exhaustive ({2**n} patterns)  min_flip={min_flip}  B={B}  {'VERIFIED' if ok else 'FAILED'}")

for r in results:
    print(r)

print(f"\nTotal tests: {len(results)}")
print("ALL PASSED" if all('PASS' in r or 'VERIFIED' in r for r in results) else "FAILURES DETECTED")
