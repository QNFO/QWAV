"""QWAV pytest-style structural tests -- CI-safe.

Sprint 20 form (fixtures + parametrize + plain asserts), ported off the dead
local `G:\\` paths in 2026-09-24 so it runs in CI against the checkout.

Run:  python -m pytest tests/test_all_artifacts_pytest.py -q
"""

import re

import pytest


@pytest.mark.parametrize("page", ["index.html", "papers/index.html", "projects/index.html"])
def test_entry_pages_have_body(page, html_files):
    """Primary entry pages render a real <body> with text."""
    assert page in html_files, f"{page} not found in repo"
    html = html_files[page]
    assert re.search(r"<body[^>]*>", html, re.IGNORECASE), f"{page}: no <body>"


def test_pages_have_interactive_or_script_content(html_files):
    """At least the home page ships script/markup that can act."""
    html = html_files["index.html"]
    signals = [
        r"<script",
        r"addEventListener",
        r"<canvas",
        r"<a\s+href=",
        r"<button",
    ]
    total = sum(len(re.findall(p, html, re.IGNORECASE)) for p in signals)
    assert total > 0, "index.html has no interactive markup or scripts"


def test_index_has_substantive_text(html_files):
    """index.html is not an empty shell."""
    html = html_files["index.html"]
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    assert len(text) > 200, f"index.html visible text is only {len(text)} chars"


def test_no_secrets_committed(html_files):
    """High-confidence credential shapes must never ship in HTML."""
    patterns = {
        "cloudflare_token": r"[A-Za-z0-9_-]{40}\.[A-Za-z0-9_-]{40,}",
        "github_pat": r"gh[pousr]_[A-Za-z0-9]{36,}",
        "aws_key": r"AKIA[0-9A-Z]{16}",
    }
    for rel, html in html_files.items():
        for name, rx in patterns.items():
            for m in re.finditer(rx, html):
                ctx = html[max(0, m.start() - 20):m.start()]
                assert "REDACTED" in ctx, f"{rel}: possible {name} leaked"
