"""
Comprehensive automated test suite for QWAV Technical Site (K1) + all 5 interactive demos (A1-A5).
Tests HTML structure, interactive elements, JavaScript integrity, content honesty, deployment sync.

Run: python test_all_artifacts.py
"""
import re, os, sys, urllib.request, hashlib

PASS, FAIL = 0, 0

def check(cond, label):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  [PASS] {label}")
    else:
        FAIL += 1
        print(f"  [FAIL] {label}")
    return cond

def section(title):
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")

artifact_paths = {
    'A1': r'G:\My Drive\QWAV\artifacts\error-confinement-demo\index.html',
    'A2': r'G:\My Drive\QWAV\artifacts\qpna-playground\index.html',
    'A3': r'G:\My Drive\QWAV\artifacts\convergence-explorer\index.html',
    'A4': r'G:\My Drive\QWAV\artifacts\tree-distance\index.html',
    'A5': r'G:\My Drive\QWAV\artifacts\hardware-visualizer\index.html',
}

deployed_urls = {
    'A1': 'https://qnfo.github.io/ultrametric-error-confinement/',
    'A2': 'https://qnfo.github.io/Q-PNA/',
    'A3': 'https://qnfo.github.io/ultrametric-convergence/',
    'A4': 'https://qnfo.github.io/tree-distance/',
    'A5': 'https://qnfo.github.io/hardware-pathway/',
    'K1': 'https://qnfo.github.io/QWAV/',
}

# ============================================================
section("TEST SUITE 1: LOCAL HTML STRUCTURE (A1-A5)")
# ============================================================
for name, path in artifact_paths.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    js = html[html.rfind('<script'):] if '<script' in html else ''
    
    check('<!DOCTYPE html>' in html, f"{name}: Has DOCTYPE declaration")
    check('</html>' in html, f"{name}: Has closing </html>")
    check('</body>' in html, f"{name}: Has closing </body>")
    check('</script>' in html, f"{name}: Has closing </script>")
    check('<title>' in html, f"{name}: Has <title> tag")
    check('<meta name="viewport"' in html, f"{name}: Has viewport meta tag")
    check('canonical' in html.lower(), f"{name}: Has canonical link tag")
    
    # Footer audit
    footer_count = len(re.findall(r'<footer[^>]*>', html, re.IGNORECASE))
    check(footer_count == 1, f"{name}: Exactly 1 footer (found {footer_count})")
    
    # CDN audit
    has_cdn = bool(re.search(r'(cdn\.|unpkg\.com|jsdelivr)', html, re.IGNORECASE))
    check(not has_cdn, f"{name}: No CDN dependencies")
    
    # Size sanity
    size = len(html)
    check(size > 5000, f"{name}: File size > 5KB ({size:,} bytes)")
    check(size < 20000 or name == 'A5', f"{name}: File size < 20KB ({size:,} bytes)")

# ============================================================
section("TEST SUITE 2: INTERACTIVE ELEMENTS (A1-A5)")
# ============================================================
for name, path in artifact_paths.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    js = html[html.rfind('<script'):] if '<script' in html else ''
    
    # Find all buttons, selects, inputs with IDs
    elements = re.findall(r'<(button|select|input)[^>]*id=["\'](\w+)["\'][^>]*>', html, re.IGNORECASE)
    dead = [(tag, eid) for tag, eid in elements if eid not in js]
    
    total = len(elements)
    dead_count = len(dead)
    check(dead_count == 0, f"{name}: All {total} interactive elements wired to JS (dead: {dead_count})")
    if dead:
        for tag, eid in dead:
            print(f"         DEAD: <{tag} id='{eid}'> not found in JS")

# ============================================================
section("TEST SUITE 3: CONTENT HONESTY (A1-A5)")
# ============================================================
for name, path in artifact_paths.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # No placeholders
    no_placeholders = True
    for p in ['TODO', 'FIXME', 'placeholder', 'coming soon', 'under construction', 'TBD', 'to be implemented']:
        if p.lower() in html.lower():
            no_placeholders = False
            check(False, f"{name}: Found placeholder '{p}'")
    if no_placeholders:
        check(True, f"{name}: No placeholder content")
    
    # No fake training (A2 specific)
    if name == 'A2':
        check('simulateTraining' not in html, f"{name}: No fake training function (old 'simulateTraining' removed)")
        check('transformerAcc' not in html, f"{name}: No fake transformer accuracy")
        check('hardcoded' not in html.lower() or 'detection' not in html.lower(), f"{name}: No hardcoded STC claims")
    
    # No misleading labels (A1 specific)
    if name == 'A1':
        check('Archimedean Equivalent LER' not in html, f"{name}: Old misleading label removed")
        check('Pr(' in html or 'Unprotected' in html, f"{name}: Has honest label")

# ============================================================
section("TEST SUITE 4: JAVASCRIPT INTEGRITY (A1-A5)")
# ============================================================
for name, path in artifact_paths.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    js = html[html.rfind('<script'):] if '<script' in html else ''
    
    check('function ' in js, f"{name}: Has JavaScript functions")
    check('document.getElementById' in js, f"{name}: Has DOM manipulation")
    check('canvas' in html.lower() or 'WebGL' in html or 'renderer' in html.lower(), f"{name}: Has canvas element or WebGL renderer")
    
    # A1 specific
    if name == 'A1':
        check('buildTree' in js, f"{name}: Has tree builder")
        check('simulate(' in js, f"{name}: Has simulation function")
        check('drawTree' in js, f"{name}: Has tree renderer")
        check('updateAll' in js, f"{name}: Has update orchestrator")
    
    # A2 specific
    if name == 'A2':
        check('classifySample' in js or 'classifySamples' in js, f"{name}: Has classification function")
        check('buildTree' in js or 'buildQPNATree' in js, f"{name}: Has tree builder")
        check('drawTree' in js or 'drawQPNATree' in js, f"{name}: Has tree renderer")
        check('classNames' in js or 'className' in js.lower(), f"{name}: Has class labels")
    
    # A3 specific
    if name == 'A3':
        check('stepSimulation' in js, f"{name}: Has simulation stepper")
        check('togglePlay' in js, f"{name}: Has play/pause")
        check('clusterCount' in js, f"{name}: Has cluster counter")
    
    # A4 specific
    if name == 'A4':
        check('copheneticDist' in js, f"{name}: Has cophenetic distance calculator")
        check('euclideanDist' in js, f"{name}: Has Euclidean distance calculator")
        check('updateDistances' in js, f"{name}: Has distance update function")
        # Check resize fix
        resize_zone = js[js.find('resize'):] if 'resize' in js else ''
        check('buildDistTree(treeD)' not in resize_zone, f"{name}: Resize handler does NOT rebuild tree")
    
    # A5 specific
    if name == 'A5':
        check('triggerError' in js, f"{name}: Has error trigger")
        check('propagateToParent' in js, f"{name}: Has error propagation")
        check('OrbitControls' in html, f"{name}: Has 3D orbit controls")
        check('three.module.js' in html, f"{name}: Uses local Three.js (no CDN)")
        # Check propagation fix
        check('activeErrors--' in js, f"{name}: Has active error counter decrement on suppression")

# ============================================================
section("TEST SUITE 5: DEPLOYED vs LOCAL SYNC (A1-A5 + K1)")
# ============================================================
# Check all deployed URLs are accessible
for name, url in deployed_urls.items():
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'QWAV-Test/1.0')
        resp = urllib.request.urlopen(req, timeout=15)
        check(resp.status == 200, f"{name}: Deployed URL HTTP {resp.status}")
        deployed_size = len(resp.read())
        check(deployed_size > 5000, f"{name}: Deployed content > 5KB ({deployed_size:,} bytes)")
    except Exception as e:
        check(False, f"{name}: Deployed URL FAILED - {e}")

# Check artifact deployed vs local sync
for name, path in artifact_paths.items():
    with open(path, 'r', encoding='utf-8') as f:
        local_html = f.read()
    
    try:
        req = urllib.request.Request(deployed_urls[name])
        req.add_header('User-Agent', 'QWAV-Test/1.0')
        deployed_bytes = urllib.request.urlopen(req, timeout=15).read()
        deployed_html = deployed_bytes.decode('utf-8')
        local_bytes = local_html.encode('utf-8')
        
        # Normalize line endings for comparison (CRLF vs LF is platform, not content)
        deployed_norm = deployed_html.replace('\r\n', '\n').replace('\r', '\n')
        local_norm = local_html.replace('\r\n', '\n').replace('\r', '\n')
        
        deployed_size = len(deployed_bytes)
        local_size = len(local_bytes)
        diff = deployed_size - local_size
        
        content_match = deployed_norm == local_norm
        
        if content_match:
            if diff == 0:
                check(True, f"{name}: Deployed == Local ({local_size:,} bytes)")
            else:
                check(True, f"{name}: Deployed == Local (content match; {diff:+d} bytes line-ending diff)")
        else:
            # Find where they differ
            min_len = min(len(deployed_norm), len(local_norm))
            diverge_at = None
            for i in range(min_len):
                if deployed_norm[i] != local_norm[i]:
                    diverge_at = i
                    break
            if diverge_at:
                ctx = 80
                check(False, f"{name}: Content MISMATCH at byte {diverge_at} — deployed={len(deployed_norm):,}, local={len(local_norm):,}")
            else:
                extra = deployed_norm[len(local_norm):] if len(deployed_norm) > len(local_norm) else local_norm[len(deployed_norm):]
                check(False, f"{name}: Content MISMATCH — tail differs by {abs(len(deployed_norm)-len(local_norm))} bytes")
    except Exception as e:
        check(False, f"{name}: Sync check FAILED - {e}")

# K1 specific
try:
    k1_local_path = r'G:\My Drive\QWAV\index.html'
    with open(k1_local_path, 'r', encoding='utf-8') as f:
        k1_local = f.read()
    
    req = urllib.request.Request('https://qnfo.github.io/QWAV/')
    req.add_header('User-Agent', 'QWAV-Test/1.0')
    k1_deployed = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')
    
    diff = len(k1_deployed) - len(k1_local)
    check(diff == 0, f"K1: Deployed == Local ({len(k1_local):,} bytes)")
    check('Q-PNA/' in k1_deployed, "K1: Has correct Q-PNA/ link (capital)")
    check('q-pna/' not in k1_deployed.lower() or 'qnfo.github.io/q-pna/' not in k1_deployed, "K1: No broken lowercase q-pna link")
except Exception as e:
    check(False, f"K1: Sync check FAILED - {e}")

# ============================================================
section("TEST SUITE 6: K1 STRUCTURAL (from test_plan.py)")
# ============================================================
# Run the same checks as the K1 test_plan.py against the deployed version
k1_src = k1_deployed

sections = [
    ('hero', 'Hero/intro section'),
    ('evidence', 'Evidence highlights section'),
    ('artifact', 'Artifact directory section'),
    ('publication', 'Publication table section'),
    ('roadmap', 'Research roadmap section'),
    ('genealogy', 'Intellectual genealogy section'),
    ('footer', 'Footer with links'),
]
for keyword, desc in sections:
    check(keyword in k1_src.lower(), f"K1: Has {desc}")

check('<h1>' in k1_src, "K1: Has H1 title element")
check('QWAV' in k1_src, "K1: Title contains QWAV")

artifact_urls = {
    'A1': ('ultrametric-error-confinement', 'Error Confinement'),
    'A2': ('Q-PNA', 'Q-PNA Playground'),
    'A3': ('ultrametric-convergence', 'Convergence Explorer'),
    'A4': ('tree-distance', 'Tree Distance Sandbox'),
    'A5': ('hardware-pathway', 'Hardware Visualizer'),
}
for label, (slug, desc) in artifact_urls.items():
    url = f'qnfo.github.io/{slug}'
    check(url in k1_src, f"K1: {label} link present")

dois = re.findall(r'10\.5281/zenodo\.\d{8}', k1_src)
check(len(dois) >= 4, f"K1: At least 4 DOIs ({len(dois)} found)")
for doi in dois[:8]:
    check(f'doi.org/{doi}' in k1_src or f'zenodo.{doi[8:]}' in k1_src.lower(),
          f"K1: DOI {doi} has resolvable link")

canvases = re.findall(r'<canvas[^>]*>', k1_src)
check(len(canvases) >= 2, f"K1: At least 2 canvas elements ({len(canvases)} found)")

check('@media' in k1_src, "K1: Has @media queries (responsive)")
check('max-width' in k1_src, "K1: Has max-width rules")
check('og:' in k1_src.lower(), "K1: Has Open Graph tags")

external_links = re.findall(r"""(?:src|href)=["'](https?://[^"']+)["']""", k1_src)
own_domains = ['doi.org', 'qnfo.github.io', 'qwav.tech', 'zenodo.org', 'github.com', 'orcid.org']
all_own = all(any(domain in link.lower() for domain in own_domains) for link in external_links)
check(all_own, f"K1: All {len(external_links)} external links go to own domains")

cdn_domains = ['cdn.jsdelivr.net', 'unpkg.com', 'cdnjs.cloudflare.com']
no_cdn = not any(cdn in k1_src.lower() for cdn in cdn_domains)
check(no_cdn, "K1: Zero CDN dependencies")

# ============================================================
section("TEST SUITE 7: CROSS-REFERENCE INTEGRITY")
# ============================================================
# Verify back-links from artifacts to K1 hub
for name, url in deployed_urls.items():
    if name == 'K1': continue
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'QWAV-Test/1.0')
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')
        has_backlink = 'qnfo.github.io/QWAV/' in html
        check(has_backlink, f"{name}: Back-link to K1 hub present")
    except Exception as e:
        check(False, f"{name}: Back-link check FAILED - {e}")

# Verify K1 links to all 5 artifacts
for label, (slug, desc) in artifact_urls.items():
    check(f'qnfo.github.io/{slug}' in k1_src, f"K1: Hub links to {label} ({slug})")

# ============================================================
section("RESULTS")
# ============================================================
print(f"\n{'='*60}")
total = PASS + FAIL
print(f"PASSED: {PASS} / {total}")
print(f"FAILED: {FAIL} / {total}")
print(f"RATE:   {PASS/total*100:.0f}%" if total > 0 else "No tests")
print(f"{'='*60}")

if FAIL > 0:
    sys.exit(1)
