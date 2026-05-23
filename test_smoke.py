"""
QWAV SMOKE TESTS — Browser-Level Functionality Checks
======================================================
Complements test_all_artifacts.py (structural tests) with
interactive functionality checks via HTTP + content heuristics.

What this tests that structural tests CANNOT:
- JavaScript presence and sanity (is there meaningful JS?)
- Button wiring (does each button have a corresponding function?)
- Canvas rendering (are canvases actually drawn to?)
- Content richness (is there substantive text, not just placeholders?)
- Interactive patterns (does the page have interaction logic?)
- DOM update mechanisms (does the page update after interaction?)
- No dead code / stale patterns

Run: python test_smoke.py
"""

import re, sys, urllib.request, json, io

PASS, FAIL = 0, 0
OUTPUT = []

def check(cond, label):
    global PASS, FAIL
    if cond:
        PASS += 1
        msg = f"  [PASS] {label}"
    else:
        FAIL += 1
        msg = f"  [FAIL] {label}"
    print(msg)
    OUTPUT.append(msg)
    return cond

def section(title):
    global OUTPUT
    sep = "=" * 60
    print(f"\n{sep}\n{title}\n{sep}")
    OUTPUT.append(f"\n{sep}")
    OUTPUT.append(title)
    OUTPUT.append(sep)

def fetch(url, timeout=15):
    """Fetch a URL and return (html, status_code) or (None, error)"""
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'QWAV-SmokeTest/1.0')
        resp = urllib.request.urlopen(req, timeout=timeout)
        html = resp.read().decode('utf-8', errors='replace')
        return html, resp.getcode()
    except urllib.error.HTTPError as e:
        return None, e.code
    except Exception as e:
        return None, str(e)

# Artifact map: name -> (local_path, live_url, expected_interactions)
artifacts = {
    'A1': {
        'local': r'G:\My Drive\QWAV\artifacts\error-confinement-demo\index.html',
        'live': 'https://qnfo.github.io/ultrametric-error-confinement/',
        'name': 'Error Confinement Demo',
        'expects': ['canvas', 'sliders', 'select', 'error_rate', 'simulation'],
    },
    'A2': {
        'local': r'G:\My Drive\QWAV\artifacts\qpna-playground\index.html',
        'live': 'https://qnfo.github.io/Q-PNA/',
        'name': 'Q-PNA Architecture Explorer',
        'expects': ['button', 'canvas', 'classify', 'tree', 'class regions'],
    },
    'A3': {
        'local': r'G:\My Drive\QWAV\artifacts\convergence-explorer\index.html',
        'live': 'https://qnfo.github.io/ultrametric-convergence/',
        'name': 'Convergence Explorer',
        'expects': ['canvas', 'play', 'reset', 'animation', 'clusters'],
    },
    'A4': {
        'local': r'G:\My Drive\QWAV\artifacts\tree-distance\index.html',
        'live': 'https://qnfo.github.io/tree-distance/',
        'name': 'Tree Distance Sandbox',
        'expects': ['canvas', 'click', 'distance', 'ultrametric', 'leaves'],
    },
    'A5': {
        'local': r'G:\My Drive\QWAV\artifacts\hardware-visualizer\index.html',
        'live': 'https://qnfo.github.io/hardware-pathway/',
        'name': 'Hardware Pathway',
        'expects': ['canvas', 'three.js', 'atoms', 'error', 'suppression'],
    },
    'K1': {
        'local': r'G:\My Drive\QWAV\site\index.html',
        'live': 'https://qnfo.github.io/QWAV/',
        'name': 'K1 Hub',
        'expects': ['links', 'demos', 'papers', 'navigation', 'resources'],
    },
}

# ============================================================
section("SUITE 1: LIVE AVAILABILITY (All Artifacts)")
# ============================================================
for key, art in artifacts.items():
    html, status = fetch(art['live'])
    if status == 200 and html:
        check(True, f"{key} ({art['name']}): Live (HTTP 200, {len(html):,} bytes)")
    else:
        check(False, f"{key} ({art['name']}): HTTP {status} — OFFLINE")

# ============================================================
section("SUITE 2: JAVASCRIPT EXECUTION CAPABILITY")
# ============================================================
for key, art in artifacts.items():
    if key == 'K1':
        continue  # K1 hub is navigation, not interactive JS
    html, status = fetch(art['live'])
    if not html:
        check(False, f"{key}: Cannot fetch for JS audit")
        continue
    
    # Find script blocks
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    inline_scripts = [s for s in scripts if s.strip() and 'src=' not in s]
    
    # Check for meaningful JS (not just boilerplate)
    total_js_chars = sum(len(s) for s in scripts)
    check(total_js_chars > 200, f"{key}: Has substantial JavaScript ({total_js_chars:,} chars)")
    
    # Check for event listeners or interaction patterns
    interaction_patterns = [
        r'addEventListener', r'onclick', r'onchange', r'oninput',
        r'\.click\(', r'querySelector', r'getElementById',
        r'requestAnimationFrame', r'setInterval', r'setTimeout',
        r'canvas', r'getContext', r'fillRect', r'stroke',
        r'THREE\.', r'WebGL', r'renderer',
    ]
    found_patterns = []
    for pat in interaction_patterns:
        if re.search(pat, '\n'.join(scripts), re.IGNORECASE):
            found_patterns.append(pat.replace(r'\\', ''))
    
    check(len(found_patterns) >= 3, 
          f"{key}: Has interaction logic ({len(found_patterns)} patterns: {', '.join(found_patterns[:5])}...)")

# ============================================================
section("SUITE 3: BUTTON -> FUNCTION WIRING")
# ============================================================
for key, art in artifacts.items():
    if key == 'K1':
        continue
    
    html, status = fetch(art['live'])
    if not html:
        check(False, f"{key}: Cannot fetch for button audit")
        continue
    
    # Extract all button IDs and onclick handlers
    buttons = re.findall(r'<button[^>]*>', html, re.IGNORECASE)
    button_ids = []
    for btn_html in buttons:
        id_match = re.search(r'id=["\'](\w+)["\']', btn_html)
        onclick_match = re.search(r'onclick=["\']([^"\']*)["\']', btn_html)
        if id_match:
            button_ids.append(('id', id_match.group(1)))
        if onclick_match:
            button_ids.append(('onclick', onclick_match.group(1)))
    
    # Extract all function definitions from JS
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    all_js = '\n'.join(scripts)
    functions = re.findall(r'function\s+(\w+)', all_js)
    arrow_funcs = re.findall(r'(?:const|let|var)\s+(\w+)\s*=\s*(?:\(|[a-zA-Z])', all_js)
    all_func_names = set(functions + arrow_funcs)
    
    # Check each button ID appears in JS
    dead_buttons = 0
    for btype, bid in button_ids:
        if btype == 'id' and bid not in all_js:
            dead_buttons += 1
            check(False, f"{key}: Button id='{bid}' NOT found in JS (dead button)")
    
    if button_ids:
        check(dead_buttons == 0, 
              f"{key}: All {len(button_ids)} button references wired to JS")
    else:
        # No buttons is OK for some artifacts (auto-initializing)
        check(True, f"{key}: No buttons (auto-initializing artifact)")

# ============================================================
section("SUITE 4: CANVAS RENDERING CAPABILITY")
# ============================================================
for key, art in artifacts.items():
    if key == 'K1':
        continue
    
    html, status = fetch(art['live'])
    if not html:
        check(False, f"{key}: Cannot fetch for canvas audit")
        continue
    
    canvases = re.findall(r'<canvas[^>]*>', html, re.IGNORECASE)
    # Note: A5 creates canvas dynamically via Three.js (verified via CDP),
    # so canvas count = 0 in source HTML is expected
    has_dynamic_canvas = bool(re.search(r'(THREE\.|WebGLRenderer|new\s+\w+Renderer)', 
                                        '\n'.join(re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)),
                                        re.IGNORECASE))
    
    if has_dynamic_canvas:
        check(True, f"{key}: Has dynamically-created canvas (Three.js/WebGL renderer)")
    else:
        check(len(canvases) >= 1, f"{key}: Has at least 1 canvas element (found {len(canvases)})")
    
    # Check that canvas is actually drawn to in JS
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    all_js = '\n'.join(scripts)
    
    canvas_draw_patterns = [
        r'getContext\([\'"]2d[\'"]\)', r'getContext\([\'"]webgl[\'"]\)', 
        r'fillRect', r'strokeRect', r'arc\(', r'fill\(', r'stroke\(',
        r'fillText', r'strokeText', r'beginPath', r'clearRect',
        r'THREE\.', r'WebGLRenderer', r'Scene\(', r'Camera\(',
        r'putImageData', r'drawImage', r'createImageData',
    ]
    found_draw = []
    for pat in canvas_draw_patterns:
        if re.search(pat, all_js, re.IGNORECASE):
            found_draw.append(pat.replace('\\', ''))
    
    check(len(found_draw) >= 2,
          f"{key}: Canvas has drawing logic ({len(found_draw)} patterns: {', '.join(found_draw[:4])})")

# ============================================================
section("SUITE 5: CONTENT RICHNESS (Not Just Placeholder)")
# ============================================================
for key, art in artifacts.items():
    html, status = fetch(art['live'])
    if not html:
        check(False, f"{key}: Cannot fetch for content audit")
        continue
    
    # Extract visible text (strip tags)
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Word count
    words = len(text.split())
    check(words >= 50, f"{key}: Has substantive text ({words} words)")
    
    # Check for specific domain terminology (proves it's not generic)
    domain_terms = {
        'A1': ['error', 'confinement', 'ultrametric', 'tree', 'suppression'],
        'A2': ['q-pna', 'tree', 'class', 'architecture', 'path'],
        'A3': ['convergence', 'ultrametric', 'euclidean', 'cluster', 'space'],
        'A4': ['distance', 'tree', 'ultrametric', 'cophenetic', 'leaf'],
        'A5': ['hardware', 'error', 'suppression', 'atom', 'rydberg'],
        'K1': ['qwav', 'ultrametric', 'quantum', 'computing', 'ai'],
    }
    
    if key in domain_terms:
        found_terms = [t for t in domain_terms[key] if t.lower() in text.lower()]
        check(len(found_terms) >= 3,
              f"{key}: Has domain terminology ({len(found_terms)}/{len(domain_terms[key])}: {', '.join(found_terms)})")

# ============================================================
section("SUITE 6: NO STALE / DEAD CODE PATTERNS")
# ============================================================
stale_patterns = {
    'simulateTraining': 'Old fake-training function',
    'hardcoded': 'Hardcoded/placeholder data',
    'transformerAcc': 'Old transformer accuracy claim',
    'TODO': 'Unfinished task marker',
    'FIXME': 'Bug marker left in code',
    'placeholder': 'Placeholder content',
    'coming soon': 'Vaporware marker',
    'under construction': 'Unfinished site marker',
    'TBD': 'To-be-determined (unresolved)',
}

for key, art in artifacts.items():
    html, status = fetch(art['live'])
    if not html:
        check(False, f"{key}: Cannot fetch for stale code audit")
        continue
    
    found_stale = []
    for pattern, desc in stale_patterns.items():
        if pattern.lower() in html.lower():
            found_stale.append(f"{pattern} ({desc})")
    
    check(len(found_stale) == 0,
          f"{key}: No stale/dead code patterns" + 
          (f" — FOUND: {', '.join(found_stale)}" if found_stale else ""))

# ============================================================
section("SUITE 7: K1 HUB SPECIFIC CHECKS")
# ============================================================
html, status = fetch(artifacts['K1']['live'])
if html:
    # Count navigation links
    links = re.findall(r'<a\s[^>]*href=["\'](https?://|/)[^"\']*["\'][^>]*>', html, re.IGNORECASE)
    check(len(links) >= 20, f"K1: Has substantial navigation ({len(links)} links)")
    
    # Check for artifact references
    for slug in ['ultrametric-error-confinement', 'Q-PNA', 'ultrametric-convergence', 
                 'tree-distance', 'hardware-pathway']:
        check(slug in html, f"K1: Links to {slug}")
    
    # Check for paper references
    check('zenodo' in html.lower(), "K1: References Zenodo/DOI records")
    check('10.5281' in html, "K1: Contains at least one DOI")
    
    # Check for demo section
    check('demo' in html.lower() or 'interactive' in html.lower(), 
          "K1: Has demo/interactive section")
else:
    check(False, "K1: Cannot fetch — critical failure")

# ============================================================
section("SUITE 8: RESPONSE TIME (Performance)")
# ============================================================
import time
for key, art in artifacts.items():
    start = time.time()
    html, status = fetch(art['live'], timeout=20)
    elapsed = time.time() - start
    if status == 200:
        check(elapsed < 5.0, f"{key}: Loads in <5s ({elapsed:.2f}s, {len(html):,} bytes)")
    else:
        check(False, f"{key}: Failed to load in {elapsed:.2f}s (HTTP {status})")

# ============================================================
section("SUITE 9: JAVASCRIPT ERROR-PATTERN DETECTION")
# ============================================================
error_patterns = {
    'console.error': (r'console\.error\(', 'Known-error logging in production code'),
    'eval': (r'\beval\(', 'eval() usage (security/stability risk)'),
    'document.write': (r'document\.write\(', 'document.write() (blocks rendering)'),
}

for key, art in artifacts.items():
    if key == 'K1':
        continue
    html, status = fetch(art['live'])
    if not html:
        check(False, f"{key}: Cannot fetch for error-pattern audit")
        continue
    
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
    all_js = '\n'.join(scripts)
    
    # Check for console.error (indicates known bugs logged to console)
    for pat_name, (pattern, desc) in error_patterns.items():
        count = len(re.findall(pattern, all_js, re.IGNORECASE))
        check(count == 0, f"{key}: No {pat_name}() calls ({desc})" + 
              (f" — found {count}" if count > 0 else ""))
    
    # Check for empty catch blocks (silent error swallowing)
    empty_catches = len(re.findall(r'catch\s*\([^)]*\)\s*\{\s*\}', all_js))
    check(empty_catches == 0, f"{key}: No empty catch blocks (silent error swallowing)" +
          (f" — found {empty_catches}" if empty_catches > 0 else ""))
    
    # Check innerHTML usage (risky for XSS, should prefer textContent)
    inner_html_count = len(re.findall(r'\.innerHTML\s*=', all_js))
    check(inner_html_count <= 3, f"{key}: innerHTML usage within limits ({inner_html_count}/3)" +
          ("" if inner_html_count <= 3 else f" — EXCESSIVE: {inner_html_count} uses"))
    
    # Check async operations have error handling
    fetch_calls = len(re.findall(r'fetch\(', all_js))
    catch_handlers = len(re.findall(r'\.catch\(', all_js))
    try_catch_blocks = len(re.findall(r'try\s*\{', all_js))
    
    if fetch_calls > 0:
        has_error_handling = catch_handlers > 0 or try_catch_blocks > 0
        check(has_error_handling, f"{key}: fetch() calls ({fetch_calls}) have error handling (catches: {catch_handlers}, try-blocks: {try_catch_blocks})")

# ============================================================
section("RESULTS")
# ============================================================
total = PASS + FAIL
result_lines = [
    f"SMOKE PASSED: {PASS} / {total}",
    f"SMOKE FAILED: {FAIL} / {total}",
    f"SMOKE RATE:   {PASS/total*100:.0f}%" if total > 0 else "No tests",
]
for line in result_lines:
    print(line)
    OUTPUT.append(line)
print(f"{'='*60}")
OUTPUT.append("="*60)

# Write output to file
out_path = r'G:\My Drive\QWAV\smoke_results.txt'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(OUTPUT))

if FAIL > 0:
    msg = f"\nWARNING: {FAIL} smoke test failure(s) detected."
    print(msg)
    OUTPUT.append(msg)
    msg = "These indicate issues that structural tests cannot catch."
    print(msg)
    OUTPUT.append(msg)
    sys.exit(1)
else:
    msg = "\nAll smoke tests passed. Basic interactive functionality verified."
    print(msg)
    OUTPUT.append(msg)
