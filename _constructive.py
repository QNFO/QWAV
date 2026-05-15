"""Constructive barrier proof only (fast)."""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Node:
    value: int = 0
    depth: int = 0
    children: List = field(default_factory=list)
    parent: Optional['Node'] = None
    @property
    def is_leaf(self): return len(self.children) == 0

def build_tree(depth, p=3):
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

print("Constructive barrier proofs (d=1..10):")
all_ok = True
for d in range(1, 11):
    B = 2**d
    py = build_barrier_pattern(d)
    pn = build_non_flipping_pattern(d)
    assert len(py) == B, f"d={d}: pattern size {len(py)} != {B}"
    assert len(pn) == B - 1, f"d={d}: non-flip size {len(pn)} != {B-1}"
    
    t = build_tree(d)
    encode(t, 0)
    for idx in py: get_leaves(t)[idx].value = 1
    ry = decode(t)
    
    t = build_tree(d)
    encode(t, 0)
    for idx in pn: get_leaves(t)[idx].value = 1
    rn = decode(t)
    
    ok = (ry == 1 and rn == 0)
    all_ok = all_ok and ok
    status = "OK" if ok else "FAIL"
    print(f"  d={d:>2}  B={B:>6}  flip={ry} noflip={rn}  {status}")

print(f"\nOverall: {'ALL PASSED' if all_ok else 'FAILURES DETECTED'}")
