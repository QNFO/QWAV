"""
Automated test suite for K1 -- QWAV Technical Site Hub.

Validates:
  TEST 1: Core sections present
  TEST 2: Artifact links correct (A1-A5 + GoL)
  TEST 3: DOI links resolve to correct Zenodo format
  TEST 4: Canvas chart elements present
  TEST 5: SEO meta tags
  TEST 6: Responsive design markers
  TEST 7: CDN dependency audit (count and document)

Run: python test_plan.py
"""
import sys, re

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

with open(r'G:\My Drive\QWAV\site\index.html', 'r', encoding='utf-8') as f:
    source = f.read()

# ============================================================
print("=" * 60)
print("TEST 1: Core Sections Present")
print("=" * 60)

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
    check(keyword in source.lower(), f"Has {desc}")

# Check for h1 title
check('<h1>' in source, "Has H1 title element")
check('QWAV' in source, "Title contains QWAV")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 2: Artifact Links")
print("=" * 60)

artifact_urls = {
    'A1': ('ultrametric-error-confinement', 'Error Confinement'),
    'A2': ('Q-PNA', 'Q-PNA Playground'),
    'A3': ('ultrametric-convergence', 'Convergence Explorer'),
    'A4': ('tree-distance', 'Tree Distance Sandbox'),
    'A5': ('hardware-pathway', 'Hardware Visualizer'),
}

for label, (slug, desc) in artifact_urls.items():
    url = f'qnfo.github.io/{slug}'
    check(url in source, f"{label} ({desc}): link to {url}")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 3: DOI Links -- Verified Format")
print("=" * 60)

dois = re.findall(r'10\.5281/zenodo\.\d{8}', source)
check(len(dois) >= 4, f"At least 4 unique DOIs found: {len(dois)}")
for doi in dois[:8]:
    check(f'doi.org/{doi}' in source or f'zenodo.{doi[8:]}' in source.lower(),
          f"DOI {doi} has resolvable link")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 4: Canvas Chart Elements")
print("=" * 60)

canvases = re.findall(r'<canvas[^>]*>', source)
check(len(canvases) >= 2, f"At least 2 canvas elements: found {len(canvases)}")

# Check for chart rendering JS
check('getContext' in source, "Has canvas getContext calls")
check('fillRect' in source or 'strokeRect' in source, "Has canvas drawing operations")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 5: SEO Meta Tags")
print("=" * 60)

check('<meta name="description"' in source, "Has meta description")
check('<meta name="viewport"' in source, "Has viewport meta")
check('<title>' in source, "Has title tag")
check('og:' in source.lower(), "Has Open Graph tags (og:)")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 6: Responsive Design Markers")
print("=" * 60)

check('@media' in source, "Has @media queries")
check('max-width' in source, "Has max-width responsive rules")
check('flex-wrap' in source or 'flex-direction' in source, "Has flexbox layout")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 7: External Dependency Audit")
print("=" * 60)

# Count all external URLs (src/href)
external_links = re.findall(r"""(?:src|href)=["'](https?://[^"']+)["']""", source)
check(len(external_links) > 0, f"Has external links: {len(external_links)} total")

# All external links should be to own domains: doi.org, qnfo.github.io, qwav.tech, zenodo.org, github.com/QNFO, orcid.org
own_domains = ['doi.org', 'qnfo.github.io', 'qwav.tech', 'zenodo.org', 'github.com', 'orcid.org']
all_own = all(any(domain in link.lower() for domain in own_domains) for link in external_links)
check(all_own, "All external links go to own domains (doi, qnfo, qwav, zenodo, github, orcid)")

# No CDN dependencies -- everything is inline/self-contained
cdn_domains = ['cdn.jsdelivr.net', 'unpkg.com', 'cdnjs.cloudflare.com', 'fonts.googleapis.com',
               'fonts.gstatic.com', 'cdn.jsdelivr.net', 'use.fontawesome.com']
no_cdn = not any(any(cdn in link for cdn in cdn_domains) for link in external_links)
check(no_cdn, "Zero third-party CDN dependencies (fully self-contained)")

# ============================================================
print(f"\n{'=' * 60}")
print("TEST 8: Cross-Link Structure")
print("=" * 60)

check('qnfo.github.io/QWAV' in source, "Self-references canonical URL")
check('qwav.tech' in source.lower(), "References qwav.tech domain")
check('github.com/QNFO' in source, "References GitHub org")

# ============================================================
print(f"\n{'=' * 60}")
print(f"RESULTS: {PASS} passed, {FAIL} failed, {PASS + FAIL} total")
print("=" * 60)

if __name__ == "__main__":
    sys.exit(0 if FAIL == 0 else 1)
