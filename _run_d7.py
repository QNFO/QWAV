"""
0.5_run_d7.py -- Run depth=7 experiment with 2000 trials.
d=7: 3^7 = 2187 leaves, barrier B=128.
Target: LER < 1e-3 at p_err=0.40.
"""
import sys, os, json, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import importlib.util
spec = importlib.util.spec_from_file_location("ultrametric",
    os.path.join(os.path.dirname(__file__), "0.1.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

p_err_list = [0.01, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
depth = 7
n_trials = 2000
base_seed = 42

all_results = {}

for bit in [0, 1]:
    key = f"d{depth}_bit{bit}"
    print(f"Running: depth={depth}, bit={bit} ... ", end="", flush=True)
    t0 = time.time()
    result = mod.run_experiment(depth, p_err_list,
                                n_trials=n_trials,
                                seed=base_seed,
                                logical_bit=bit)
    elapsed = time.time() - t0
    print(f"done in {elapsed:.1f}s", flush=True)

    for r in result["results"]:
        lo, hi = mod.wilson_ci(r["errors"], r["n_trials"])
        r["ci_lower"] = lo
        r["ci_upper"] = hi

    all_results[key] = result

# Merge with existing results
existing_path = os.path.join(os.path.dirname(__file__), "0.2_results.json")
with open(existing_path) as f:
    existing = json.load(f)
existing.update(all_results)

outpath = os.path.join(os.path.dirname(__file__), "0.2_results.json")
with open(outpath, "w") as f:
    json.dump(existing, f, indent=2)

print()
for bit in [0, 1]:
    key = f"d{depth}_bit{bit}"
    res = all_results[key]
    print(f"d={depth}, bit={bit}:")
    for r in res["results"]:
        print(f"  p_err={r['p_err']:.2f}: LER={r['ler']:.4f} "
              f"CI=[{r['ci_lower']:.4f}, {r['ci_upper']:.4f}] "
              f"({r['errors']}/{r['n_trials']})")

# Final: did we cross 1e-3 at p_err=0.40?
r40 = all_results[f"d{depth}_bit0"]["results"][-1]
print(f"\nAt p_err=0.40, d=7: LER={r40['ler']:.4f}, CI=[{r40['ci_lower']:.4f}, {r40['ci_upper']:.4f}]")
crossed = r40['ci_upper'] < 0.001 or r40['ler'] == 0
print(f"Crossed 1e-3 threshold: {'YES' if crossed else 'NOT YET (need more trials or depth)'}")

print(f"\nResults merged into {outpath}")
