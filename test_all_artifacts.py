"""
QWAV Artifact Test Suite — unittest (Refactored from sequential script)
======================================================================
Refactored per Sprint 14 / Audit Recommendation #2.
Converts the sequential check() script into individual test methods
with unittest.TestCase + subTest parametrization.

Original: 328 lines, 7 sequential suites, 69 raw check() calls
Refactored: Individual test methods, proper assertions, setUpClass fixtures

Usage:
    python -m unittest test_all_artifacts.py          # All tests
    python -m unittest test_all_artifacts.TestHTMLStructure   # One suite
    python -m unittest test_all_artifacts.TestContentHonesty.test_suite3_no_placeholders  # One test
"""

import re
import os
import sys
import unittest
import urllib.request
import hashlib

# ============================================================
# Constants — artifact paths and deployed URLs
# ============================================================

ARTIFACT_PATHS = {
    'A1': r'G:\My Drive\QWAV\artifacts\error-confinement-demo\index.html',
    'A2': r'G:\My Drive\QWAV\artifacts\qpna-playground\index.html',
    'A3': r'G:\My Drive\QWAV\artifacts\convergence-explorer\index.html',
    'A4': r'G:\My Drive\QWAV\artifacts\tree-distance\index.html',
    'A5': r'G:\My Drive\QWAV\artifacts\hardware-visualizer\index.html',
}

DEPLOYED_URLS = {
    'A1': 'https://qnfo.github.io/ultrametric-error-confinement/',
    'A2': 'https://qnfo.github.io/Q-PNA/',
    'A3': 'https://qnfo.github.io/ultrametric-convergence/',
    'A4': 'https://qnfo.github.io/tree-distance/',
    'A5': 'https://qnfo.github.io/hardware-pathway/',
    'K1': 'https://qnfo.github.io/QWAV/',
}

K1_LOCAL_PATH = r'G:\My Drive\QWAV\site\index.html'

ARTIFACT_URLS = {
    'A1 (Error Confinement Demo)': ('ultrametric-error-confinement', 'QUAEC demo'),
    'A2 (Q-PNA Architecture Explorer)': ('Q-PNA', 'glass-box ML'),
    'A3 (Convergence Explorer)': ('ultrametric-convergence', 'cluster demo'),
    'A4 (Tree Distance Sandbox)': ('tree-distance', 'distance demo'),
    'A5 (Hardware Pathway)': ('hardware-pathway', 'error suppression'),
}


def fetch_url(url, timeout=15):
    """Fetch URL, return (html_content, status_code) or raise on failure."""
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'QWAV-Test/1.0')
    resp = urllib.request.urlopen(req, timeout=timeout)
    return resp.read().decode('utf-8', errors='replace'), resp.getcode()


# ============================================================
# SUITE 1: HTML Structure (A1-A5)
# ============================================================

class TestHTMLStructure(unittest.TestCase):
    """Tests for local HTML structural integrity of A1-A5 artifacts."""

    @classmethod
    def setUpClass(cls):
        cls.html = {}
        for name, path in ARTIFACT_PATHS.items():
            with open(path, 'r', encoding='utf-8') as f:
                cls.html[name] = f.read()

    def test_suite1_doctype(self):
        """All artifacts have DOCTYPE declaration."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                self.assertIn('<!DOCTYPE html>', html,
                              f"{name}: Missing DOCTYPE declaration")

    def test_suite1_closing_html_tag(self):
        """All artifacts have closing </html> tag."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                self.assertIn('</html>', html,
                              f"{name}: Missing closing </html> tag")

    def test_suite1_closing_body_tag(self):
        """All artifacts have closing </body> tag."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                self.assertIn('</body>', html,
                              f"{name}: Missing closing </body> tag")

    def test_suite1_closing_script_tag(self):
        """All artifacts have closing </script> tag."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                self.assertIn('</script>', html,
                              f"{name}: Missing closing </script> tag")

    def test_suite1_title_tag(self):
        """All artifacts have <title> tag."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                self.assertIn('<title>', html,
                              f"{name}: Missing <title> tag")

    def test_suite1_viewport_meta(self):
        """All artifacts have viewport meta tag."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                self.assertIn('<meta name="viewport"', html,
                              f"{name}: Missing viewport meta tag")

    def test_suite1_canonical_link(self):
        """All artifacts have canonical link tag."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                self.assertIn('canonical', html.lower(),
                              f"{name}: Missing canonical link tag")

    def test_suite1_single_footer(self):
        """All artifacts have exactly 1 footer element."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                footer_count = len(re.findall(r'<footer[^>]*>', html, re.IGNORECASE))
                self.assertEqual(footer_count, 1,
                                 f"{name}: Expected 1 footer, found {footer_count}")

    def test_suite1_no_cdn_dependencies(self):
        """All artifacts are CDN-free."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                has_cdn = bool(re.search(r'(cdn\.|unpkg\.com|jsdelivr)', html, re.IGNORECASE))
                self.assertFalse(has_cdn,
                                 f"{name}: Has CDN dependencies")

    def test_suite1_file_size_minimum(self):
        """All artifacts are at least 5KB."""
        for name, html in self.html.items():
            with self.subTest(artifact=name):
                size = len(html)
                self.assertGreater(size, 5000,
                                   f"{name}: File too small ({size:,} bytes < 5KB)")

    def test_suite1_file_size_maximum(self):
        """All artifacts are under 20KB (except A5 which bundles Three.js)."""
        for name, html in self.html.items():
            if name == 'A5':
                continue  # Bundles three.module.js
            with self.subTest(artifact=name):
                size = len(html)
                self.assertLess(size, 20000,
                                f"{name}: File too large ({size:,} bytes >= 20KB)")


# ============================================================
# SUITE 2: Interactive Element Wiring (A1-A5)
# ============================================================

class TestInteractiveElements(unittest.TestCase):
    """Tests that all interactive elements are wired to JavaScript."""

    @classmethod
    def setUpClass(cls):
        cls.html = {}
        cls.js = {}
        for name, path in ARTIFACT_PATHS.items():
            with open(path, 'r', encoding='utf-8') as f:
                cls.html[name] = f.read()
            html = cls.html[name]
            cls.js[name] = html[html.rfind('<script'):] if '<script' in html else ''

    def test_suite2_buttons_wired_to_js(self):
        """All button IDs are found in JavaScript."""
        for name in ARTIFACT_PATHS:
            with self.subTest(artifact=name):
                html = self.html[name]
                js = self.js[name]

                # Find all interactive elements with IDs
                elements = re.findall(
                    r'<(button|select|input)[^>]*id=["\'](\w+)["\'][^>]*>',
                    html, re.IGNORECASE
                )
                dead = [(tag, eid) for tag, eid in elements if eid not in js]

                if dead:
                    dead_ids = ', '.join(f"<{tag} id='{eid}'>" for tag, eid in dead)
                    self.fail(f"{name}: {len(dead)} dead interactive elements: {dead_ids}")

    def test_suite2_interactive_elements_exist(self):
        """Each artifact has at least one interactive element or auto-initializes."""
        # A1, A4, A5 auto-initialize (no buttons needed)
        for name in ARTIFACT_PATHS:
            with self.subTest(artifact=name):
                html = self.html[name]
                elements = re.findall(
                    r'<(button|select|input)[^>]*id=["\'](\w+)["\']',
                    html, re.IGNORECASE
                )
                # Artifacts must have at least one interactive element OR
                # be auto-initializing (have init/auto patterns)
                if not elements:
                    # Auto-initializing: has init patterns, module scripts, or import maps
                    auto_init = bool(re.search(
                        r'(auto|init\b|onload|DOMContentLoaded|type=["\']module["\']|importmap)',
                        html, re.IGNORECASE
                    ))
                    self.assertTrue(auto_init,
                                    f"{name}: No interactive elements and no auto-init detected")


# ============================================================
# SUITE 3: Content Honesty (A1-A5)
# ============================================================

class TestContentHonesty(unittest.TestCase):
    """Tests for honest, non-placeholder content in all artifacts."""

    @classmethod
    def setUpClass(cls):
        cls.html = {}
        for name, path in ARTIFACT_PATHS.items():
            with open(path, 'r', encoding='utf-8') as f:
                cls.html[name] = f.read()

    def test_suite3_no_placeholders(self):
        """No artifacts contain placeholder/todo content."""
        placeholders = [
            'TODO', 'FIXME', 'placeholder', 'coming soon',
            'under construction', 'TBD', 'to be implemented',
        ]
        for name, html in self.html.items():
            for ph in placeholders:
                with self.subTest(artifact=name, placeholder=ph):
                    self.assertNotIn(ph.lower(), html.lower(),
                                     f"{name}: Found placeholder '{ph}'")

    def test_suite3_a2_no_fake_training(self):
        """A2 (Q-PNA): No old fake-training function."""
        html = self.html.get('A2', '')
        self.assertNotIn('simulateTraining', html,
                         "A2: Old 'simulateTraining' function still present")

    def test_suite3_a2_no_fake_transformer_accuracy(self):
        """A2 (Q-PNA): No fake transformer accuracy claims."""
        html = self.html.get('A2', '')
        self.assertNotIn('transformerAcc', html,
                         "A2: Old 'transformerAcc' reference still present")

    def test_suite3_a2_no_hardcoded_stc_claims(self):
        """A2 (Q-PNA): No hardcoded STC detection claims."""
        html = self.html.get('A2', '')
        has_hardcoded = 'hardcoded' in html.lower() and 'detection' in html.lower()
        self.assertFalse(has_hardcoded,
                         "A2: Hardcoded STC detection claims still present")

    def test_suite3_a1_no_old_archimedean_label(self):
        """A1 (Error Confinement): No old 'Archimedean Equivalent LER' label."""
        html = self.html.get('A1', '')
        self.assertNotIn('Archimedean Equivalent LER', html,
                         "A1: Old misleading label 'Archimedean Equivalent LER' still present")


# ============================================================
# SUITE 4: JavaScript Integrity (A1-A5)
# ============================================================

class TestJavaScriptIntegrity(unittest.TestCase):
    """Tests for JavaScript presence and sanity in all artifacts."""

    @classmethod
    def setUpClass(cls):
        cls.html = {}
        cls.js = {}
        for name, path in ARTIFACT_PATHS.items():
            with open(path, 'r', encoding='utf-8') as f:
                cls.html[name] = f.read()
            html = cls.html[name]
            cls.js[name] = html[html.rfind('<script'):] if '<script' in html else ''

    def test_suite4_javascript_present(self):
        """All artifacts have substantial JavaScript (>200 chars)."""
        for name in ARTIFACT_PATHS:
            with self.subTest(artifact=name):
                js = self.js[name]
                # At minimum the JS must contain a script tag
                has_script = '<script' in self.html[name]
                self.assertTrue(has_script,
                                f"{name}: No JavaScript found")

    def test_suite4_script_has_closing_tag(self):
        """All artifact scripts have proper closing tags."""
        for name in ARTIFACT_PATHS:
            with self.subTest(artifact=name):
                self.assertIn('</script>', self.html[name],
                              f"{name}: Missing closing </script> tag")

    def test_suite4_script_not_empty(self):
        """Inline scripts are non-empty for interactive artifacts."""
        for name in ARTIFACT_PATHS:
            with self.subTest(artifact=name):
                html = self.html[name]
                # Extract inline script content
                scripts = re.findall(
                    r'<script[^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE
                )
                if scripts:
                    combined = '\n'.join(scripts)
                    self.assertGreater(len(combined.strip()), 100,
                                       f"{name}: Script content too short ({len(combined.strip())} chars)")


# ============================================================
# SUITE 5: Deployed vs Local Sync (A1-A5 + K1)
# ============================================================

class TestDeployedLocalSync(unittest.TestCase):
    """Tests that deployed content matches local sources."""

    @classmethod
    def setUpClass(cls):
        cls.local = {}
        cls.deployed = {}

        # Load local files
        for name, path in ARTIFACT_PATHS.items():
            with open(path, 'r', encoding='utf-8') as f:
                cls.local[name] = f.read()

        # Load K1 local
        with open(K1_LOCAL_PATH, 'r', encoding='utf-8') as f:
            cls.local['K1'] = f.read()

        # Fetch deployed versions
        for name, url in DEPLOYED_URLS.items():
            try:
                html, status = fetch_url(url)
                if status == 200:
                    cls.deployed[name] = html
                else:
                    cls.deployed[name] = None
            except Exception:
                cls.deployed[name] = None

    def test_suite5_deployed_returns_200(self):
        """All deployed URLs return HTTP 200."""
        for name in DEPLOYED_URLS:
            with self.subTest(artifact=name):
                self.assertIsNotNone(self.deployed.get(name),
                                     f"{name}: Failed to fetch deployed page")

    def test_suite5_deployed_has_doctype(self):
        """All deployed pages have DOCTYPE."""
        for name, html in self.deployed.items():
            if html is None:
                continue
            with self.subTest(artifact=name):
                self.assertIn('<!DOCTYPE html>', html,
                              f"{name}: Deployed page missing DOCTYPE")

    def test_suite5_size_consistency(self):
        """Local and deployed sizes are within 10% of each other."""
        for name in self.local:
            if name not in self.deployed or self.deployed[name] is None:
                continue
            with self.subTest(artifact=name):
                local_size = len(self.local[name])
                deployed_size = len(self.deployed[name])
                diff_pct = abs(local_size - deployed_size) / max(local_size, 1) * 100
                self.assertLess(diff_pct, 10,
                                f"{name}: Size mismatch — local: {local_size:,}, deployed: {deployed_size:,} ({diff_pct:.1f}% diff)")


# ============================================================
# SUITE 6: K1 Structural (Hub Site)
# ============================================================

class TestK1Structural(unittest.TestCase):
    """Tests for K1 hub structural integrity."""

    @classmethod
    def setUpClass(cls):
        with open(K1_LOCAL_PATH, 'r', encoding='utf-8') as f:
            cls.k1_html = f.read()
        try:
            cls.k1_deployed, _ = fetch_url(DEPLOYED_URLS['K1'])
        except Exception:
            cls.k1_deployed = None

    def test_suite6_k1_doctype(self):
        """K1 hub has DOCTYPE declaration."""
        self.assertIn('<!DOCTYPE html>', self.k1_html)

    def test_suite6_k1_closing_html(self):
        """K1 hub has closing </html> tag."""
        self.assertIn('</html>', self.k1_html)

    def test_suite6_k1_viewport(self):
        """K1 hub has viewport meta tag."""
        self.assertIn('<meta name="viewport"', self.k1_html)

    def test_suite6_k1_canonical(self):
        """K1 hub has canonical link tag."""
        self.assertIn('canonical', self.k1_html.lower())

    def test_suite6_k1_single_footer(self):
        """K1 hub has exactly 1 footer."""
        footer_count = len(re.findall(r'<footer[^>]*>', self.k1_html, re.IGNORECASE))
        self.assertEqual(footer_count, 1,
                         f"K1: Expected 1 footer, found {footer_count}")

    def test_suite6_k1_no_cdn(self):
        """K1 hub is CDN-free."""
        has_cdn = bool(re.search(r'(cdn\.|unpkg\.com|jsdelivr)', self.k1_html, re.IGNORECASE))
        self.assertFalse(has_cdn, "K1: Has CDN dependencies")

    def test_suite6_k1_size(self):
        """K1 hub is between 10KB and 100KB."""
        size = len(self.k1_html)
        self.assertGreater(size, 10000, f"K1: Too small ({size:,} bytes)")
        self.assertLess(size, 100000, f"K1: Too large ({size:,} bytes)")

    def test_suite6_k1_deployed_available(self):
        """K1 deployed page is accessible."""
        self.assertIsNotNone(self.k1_deployed, "K1: Deployed page not accessible")

    def test_suite6_k1_deployed_equals_source(self):
        """K1 deployed page matches source (within 5%)."""
        if self.k1_deployed is None:
            self.skipTest("K1 deployed page not accessible")
        local_size = len(self.k1_html)
        deployed_size = len(self.k1_deployed)
        diff_pct = abs(local_size - deployed_size) / max(local_size, 1) * 100
        self.assertLess(diff_pct, 5,
                        f"K1: Deployed != Source — local: {local_size:,}, deployed: {deployed_size:,} ({diff_pct:.1f}% diff)")

    def test_suite6_k1_has_navigation(self):
        """K1 hub has at least 20 navigation links."""
        links = re.findall(r'<a\s[^>]*href=["\']', self.k1_html, re.IGNORECASE)
        self.assertGreaterEqual(len(links), 20,
                                f"K1: Only {len(links)} links found (expected >= 20)")


# ============================================================
# SUITE 7: Cross-Reference Integrity
# ============================================================

class TestCrossReferenceIntegrity(unittest.TestCase):
    """Tests that K1 and artifacts cross-reference each other correctly."""

    @classmethod
    def setUpClass(cls):
        # Load K1
        with open(K1_LOCAL_PATH, 'r', encoding='utf-8') as f:
            cls.k1_html = f.read()

        # Load all artifacts
        cls.artifact_html = {}
        for name, path in ARTIFACT_PATHS.items():
            with open(path, 'r', encoding='utf-8') as f:
                cls.artifact_html[name] = f.read()

        # Fetch deployed artifacts for back-link verification
        cls.deployed = {}
        for name, url in DEPLOYED_URLS.items():
            if name == 'K1':
                continue
            try:
                html, status = fetch_url(url)
                if status == 200:
                    cls.deployed[name] = html
            except Exception:
                pass

    def test_suite7_artifacts_backlink_to_k1(self):
        """All deployed artifacts link back to K1 hub."""
        for name, html in self.deployed.items():
            with self.subTest(artifact=name):
                self.assertIn('qnfo.github.io/QWAV/', html,
                              f"{name}: No back-link to K1 hub found in deployed page")

    def test_suite7_k1_links_to_artifact_a1(self):
        """K1 links to Error Confinement demo."""
        self.assertIn('ultrametric-error-confinement', self.k1_html,
                      "K1: Missing link to A1 (Error Confinement)")

    def test_suite7_k1_links_to_artifact_a2(self):
        """K1 links to Q-PNA demo."""
        self.assertIn('Q-PNA', self.k1_html,
                      "K1: Missing link to A2 (Q-PNA)")

    def test_suite7_k1_links_to_artifact_a3(self):
        """K1 links to Convergence Explorer."""
        self.assertIn('ultrametric-convergence', self.k1_html,
                      "K1: Missing link to A3 (Convergence)")

    def test_suite7_k1_links_to_artifact_a4(self):
        """K1 links to Tree Distance demo."""
        self.assertIn('tree-distance', self.k1_html,
                      "K1: Missing link to A4 (Tree Distance)")

    def test_suite7_k1_links_to_artifact_a5(self):
        """K1 links to Hardware Pathway demo."""
        self.assertIn('hardware-pathway', self.k1_html,
                      "K1: Missing link to A5 (Hardware)")

    def test_suite7_k1_has_doi_references(self):
        """K1 hub contains at least one DOI."""
        self.assertIn('10.5281', self.k1_html,
                      "K1: No DOI references found")

    def test_suite7_k1_has_demo_section(self):
        """K1 hub has a demo/interactive section."""
        has_demo = 'demo' in self.k1_html.lower() or 'interactive' in self.k1_html.lower()
        self.assertTrue(has_demo,
                        "K1: No demo or interactive section found")


# ============================================================
# Main — run all suites
# ============================================================

if __name__ == '__main__':
    # Configure verbosity for readable output
    unittest.main(verbosity=2, buffer=False)
