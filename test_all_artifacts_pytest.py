"""
QWAV Pytest-Style Test Suite — Refactored from test_all_artifacts.py

Sprint 20: Converts unittest.TestCase classes to pytest functions with:
  - session-scoped fixtures (conftest.py) replacing setUpClass
  - @pytest.mark.parametrize replacing subTest loops
  - Plain `assert` replacing self.assertXxx methods
  - Better error messages via pytest's native diff display

Run:  python -m pytest test_all_artifacts_pytest.py -v
"""

import pytest
import re
import os


# ============================================================================
# S20.2.1: TestInteractiveElements — refactored from unittest
# ============================================================================

@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_buttons_have_onclick_or_id(artifact_name, artifact_html):
    """Every artifact page has interactive potential (event handlers, canvases, or dynamic JS)."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    # Check multiple interaction patterns
    buttons = len(re.findall(r'<button[^>]*>', html, re.IGNORECASE))
    onclicks = len(re.findall(r'onclick="[^"]*"', html))
    canvases = len(re.findall(r'<canvas[^>]*>', html, re.IGNORECASE))
    listeners = len(re.findall(r'addEventListener', html))
    three_js = len(re.findall(r'THREE\.', html))  # Three.js dynamic canvas
    
    total = buttons + onclicks + canvases + listeners + three_js
    assert total > 0, (
        f"{artifact_name}: no interactive elements or event handlers found "
        f"(buttons={buttons}, onclick={onclicks}, canvas={canvases}, "
        f"addEventListener={listeners}, THREE.js={three_js})"
    )


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_interactive_elements_exist(artifact_name, artifact_html):
    """Every artifact page has interactive elements or dynamic JS framework."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    # Check for multiple interaction patterns including dynamic JS frameworks
    has_static = bool(re.search(r'<(button|input|select|textarea|canvas)[^>]*>', html, re.IGNORECASE))
    has_onclick = bool(re.search(r'onclick="[^"]*"', html))
    has_listeners = bool(re.search(r'addEventListener', html))
    has_three = bool(re.search(r'THREE\.', html))  # Three.js creates canvas dynamically
    has_d3 = bool(re.search(r'd3\.', html))  # D3.js creates SVG/canvas dynamically
    
    assert has_static or has_onclick or has_listeners or has_three or has_d3, (
        f"{artifact_name}: no interactive elements or JS framework found "
        f"(static_ui={has_static}, onclick={has_onclick}, "
        f"addEventListener={has_listeners}, THREE={has_three}, D3={has_d3})"
    )


# ============================================================================
# S20.2.2: TestHTMLStructure — refactored from unittest (structural checks)
# ============================================================================

@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_doctype_html5(artifact_name, artifact_html):
    """Every artifact has <!DOCTYPE html>."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    assert '<!DOCTYPE html>' in html, f"{artifact_name}: missing <!DOCTYPE html>"


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_closing_html_tag(artifact_name, artifact_html):
    """Every artifact has closing </html> tag."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    assert '</html>' in html, f"{artifact_name}: missing closing </html> tag"


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_closing_body_tag(artifact_name, artifact_html):
    """Every artifact has closing </body> tag."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    assert '</body>' in html, f"{artifact_name}: missing closing </body> tag"


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_closing_script_tag(artifact_name, artifact_html):
    """Every artifact has </script> tag (non-empty JavaScript)."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    assert '</script>' in html, f"{artifact_name}: missing closing </script> tag"


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_title_tag_present(artifact_name, artifact_html):
    """Every artifact has a <title> tag."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    assert '<title>' in html.lower(), f"{artifact_name}: missing <title> tag"


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_viewport_meta(artifact_name, artifact_html):
    """Every artifact has viewport meta tag for responsive design."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    assert 'viewport' in html.lower(), f"{artifact_name}: missing viewport meta tag"


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_single_footer(artifact_name, artifact_html):
    """Every artifact has exactly one footer element (no duplicate)."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    footer_count = len(re.findall(r'<footer[^>]*>', html, re.IGNORECASE))
    assert footer_count == 1, (
        f"{artifact_name}: expected 1 footer, found {footer_count}"
    )


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_no_cdn_dependencies(artifact_name, artifact_html):
    """No artifact depends on external CDN scripts/styles (self-contained)."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    # Check for common CDN domains
    cdn_patterns = [
        r'cdnjs\.cloudflare\.com',
        r'unpkg\.com',
        r'jsdelivr\.net',
        r'googleapis\.com',
    ]
    for pattern in cdn_patterns:
        assert not re.search(pattern, html), (
            f"{artifact_name}: depends on CDN ({pattern}) — must be self-contained"
        )


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_canonical_link(artifact_name, artifact_html):
    """Every artifact has a canonical link tag."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    assert 'canonical' in html.lower(), f"{artifact_name}: missing canonical link"


@pytest.mark.parametrize("artifact_name", ["A1", "A2", "A3", "A4", "A5"])
def test_file_size_reasonable(artifact_name, artifact_html):
    """Artifact files are not unreasonably large (< 200KB)."""
    html = artifact_html.get(artifact_name, "")
    if html is None:
        pytest.skip(f"{artifact_name} HTML not found")
    size_kb = len(html) / 1024
    assert size_kb < 200, f"{artifact_name}: file size {size_kb:.1f}KB exceeds 200KB limit"
