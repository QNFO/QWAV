"""Write barrier verification results to file (avoids output buffering)."""
import sys, os, itertools

sys.path.insert(0, r'G:\My Drive\projects\ultrametric_v2')

# Import 0.1.py module-level code only (skip __main__ block)
source = open(r'G:\My Drive\projects\ultrametric_v2\0.1.py', 'rb').read().decode()
source_mainless = source.split("if __name__")[0]
exec(source_mainless)

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

out = []

# Constructive d=1..12
for d in range(1, 13):
    B = 2**d
    py = build_barrier_pattern(d)
    pn = build_non_flipping_pattern(d)
    assert len(py) == B, f"d={d}: size mismatch {len(py)} vs {B}"
    assert len(pn) == B - 1, f"d={d}: size mismatch {len(pn)} vs {B-1}"
    
    t = build_tree(d, p=3)
    encode(t, 0)
    for idx in py:
        get_leaves(t)[idx].value = 1
    ry = decode(t)
    
    t = build_tree(d, p=3)
    encode(t, 0)
    for idx in pn:
        get_leaves(t)[idx].value = 1
    rn = decode(t)
    
    ps = "PASS" if (ry == 1 and rn == 0) else "FAIL"
    out.append(f"d={d:>2}: B={B:>5}, constructive: {ps} (flip={ry}, noflip={rn})")

# Exhaustive d=1,2
for d in [1, 2]:
    n = 3**d
    B = 2**d
    nf_min = n + 1
    for bits in itertools.product([0, 1], repeat=n):
        nf = sum(bits)
        t = build_tree(d, p=3)
        encode(t, 0)
        for i, b in enumerate(bits):
            if b:
                get_leaves(t)[i].value = 1
        if decode(t) == 1:
            nf_min = min(nf_min, nf)
    ok = nf_min >= B
    out.append(f"d={d}: exhaustive ({2**n} patterns), min_flip={nf_min}, barrier={B}: {'VERIFIED' if ok else 'FAILED'}")

with open(r'G:\My Drive\projects\ultrametric_v2\_barrier_results.txt', 'w') as f:
    f.write('\n'.join(out) + '\n')

print(f'Wrote {len(out)} lines to _barrier_results.txt')
