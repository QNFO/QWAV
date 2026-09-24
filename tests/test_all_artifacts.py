"""QWAV structural artifact tests (unittest) -- CI-safe.

Rewritten 2026-09-24.  The previous suite read from `G:\\My Drive\\QWAV\\...`
and fetched dead qnfo.github.io URLs; both made CI red on every run.  This
suite validates the CHECKED-OUT repository only: any machine, no network.

Run:  python -m pytest tests/test_all_artifacts.py -q
      python -m unittest tests.test_all_artifacts
"""

import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE_DIRS = {".git", "node_modules", ".wrangler", "__pycache__"}


def _html_files():
    found = {}
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fn in files:
            if fn.endswith(".html"):
                abs_p = os.path.join(root, fn)
                found[os.path.relpath(abs_p, REPO_ROOT).replace(os.sep, "/")] = abs_p
    return found


HTML_FILES = _html_files()


class TestHTMLStructure(unittest.TestCase):
    """Every shipped HTML page is a well-formed document."""

    def test_html_files_exist(self):
        self.assertGreater(len(HTML_FILES), 0, "no .html files found in repo")

    def test_every_page_has_doctype(self):
        for rel, abs_p in HTML_FILES.items():
            with self.subTest(page=rel):
                text = open(abs_p, encoding="utf-8", errors="replace").read()
                self.assertRegex(
                    text[:400].lower(), r"<!doctype html>",
                    f"{rel} is missing <!DOCTYPE html>",
                )

    def test_every_page_has_title(self):
        for rel, abs_p in HTML_FILES.items():
            with self.subTest(page=rel):
                text = open(abs_p, encoding="utf-8", errors="replace").read()
                self.assertIsNotNone(
                    re.search(r"<title[^>]*>\s*\S", text, re.IGNORECASE),
                    f"{rel} has no non-empty <title>",
                )


class TestContentHonesty(unittest.TestCase):
    """No unrendered template output or placeholder text ships."""

    PLACEHOLDERS = ("{{", "}}", "TODO:", "FIXME:", "LOREM IPSUM", "[object Object]")

    def test_no_unrendered_placeholders(self):
        for rel, abs_p in HTML_FILES.items():
            text = open(abs_p, encoding="utf-8", errors="replace").read()
            for token in self.PLACEHOLDERS:
                with self.subTest(page=rel, token=token):
                    self.assertNotIn(
                        token, text,
                        f"{rel} contains unrendered placeholder {token!r}",
                    )


class TestRequiredFiles(unittest.TestCase):
    """Site entrypoint + machine-readability files are present."""

    REQUIRED = ("index.html", "robots.txt", "sitemap.xml", "llms.txt")

    def test_required_files_present(self):
        for name in self.REQUIRED:
            with self.subTest(file=name):
                self.assertTrue(
                    os.path.exists(os.path.join(REPO_ROOT, name)),
                    f"required site file {name} is missing",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
