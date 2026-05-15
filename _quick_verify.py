"""Quick barrier verification - avoids PowerShell escaping issues."""
import sys, os, itertools
sys.path.insert(0, r'G:\My Drive\projects\ultrametric_v2')
import importlib.util
spec = importlib.util.spec_from_file_location('m', r'G:\My Drive\projects\ultrametric_v2\0.1.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

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

# Constructive verification d=1..12
for d in range(1, 13):
    B = 2**d
    py = build_barrier_pattern(d)
    pn = build_non_flipping_pattern(d)
    assert len(py) == B
    assert len(pn) == B - 1
    
    t = mod.build_tree(d, p=3)
    mod.encode(t, 0)
    for idx in py:
        mod.get_leaves(t)[idx].value = 1
    ry = mod.decode(t)
    assert ry == 1, f"d={d}: barrier pattern FAILED"
    
    t = mod.build_tree(d, p=3)
    mod.encode(t, 0)
    for idx in pn:
        mod.get_leaves(t)[idx].value = 1
    rn = mod.decode(t)
    assert rn == 0, f"d={d}: non-flip pattern FAILED"
    
    print(f"d={d:>2}: B={B:>5}, constructive proof: PASS")

# Exhaustive d=1-2
for d in [1, 2]:
    n = 3**d
    B = 2**d
    nf_min = n + 1
    n_total = 2**n
    for bits in itertools.product([0, 1], repeat=n):
        nf = sum(bits)
        t = mod.build_tree(d, p=3)
        mod.encode(t, 0)
        for i, b in enumerate(bits):
            if b:
                mod.get_leaves(t)[i].value = 1
        if mod.decode(t) == 1:
            nf_min = min(nf_min, nf)
    ok = (nf_min >= B)
    status = "VERIFIED" if ok else "FAILED"
    print(f"d={d}: exhaustive ({n_total} patterns), min flip={nf_min}, barrier={B}: {status}")

print()
print("All complete.")
