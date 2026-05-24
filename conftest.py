"""
QWAV Pytest Fixtures -- Shared test infrastructure for pytest-style test suite.

Replaces the repetitive setUpClass pattern in test_all_artifacts.py
with reusable fixtures that pytest auto-discovers via conftest.py.

Usage:
    def test_something(artifact_html, artifact_names):
        for name in artifact_names:
            assert '<!DOCTYPE html>' in artifact_html[name]

Sprint 20: Refactored from unittest.TestCase setUpClass pattern.
"""

import pytest
import os

# --- Artifact paths ---
ARTIFACT_PATHS = {
    'A1': r'G:\My Drive\QWAV\artifacts\error-confinement-demo\index.html',
    'A2': r'G:\My Drive\QWAV\artifacts\qpna-playground\index.html',
    'A3': r'G:\My Drive\QWAV\artifacts\convergence-explorer\index.html',
    'A4': r'G:\My Drive\QWAV\artifacts\tree-distance\index.html',
    'A5': r'G:\My Drive\QWAV\artifacts\hardware-visualizer\index.html',
}

K1_PATH = r'G:\My Drive\QWAV\site\index.html'

DEPLOYED_URLS = {
    'A1': 'https://qnfo.github.io/ultrametric-error-confinement/',
    'A2': 'https://qnfo.github.io/Q-PNA/',
    'A3': 'https://qnfo.github.io/ultrametric-convergence/',
    'A4': 'https://qnfo.github.io/tree-distance/',
    'A5': 'https://qnfo.github.io/hardware-pathway/',
    'K1': 'https://qnfo.github.io/QWAV/',
}


# ============================================================================
# Fixtures
# ============================================================================

@pytest.fixture(scope="session")
def artifact_paths():
    """Dict mapping artifact name → local file path."""
    return dict(ARTIFACT_PATHS)


@pytest.fixture(scope="session")
def artifact_names():
    """List of artifact names: ['A1', 'A2', 'A3', 'A4', 'A5']."""
    return list(ARTIFACT_PATHS.keys())


@pytest.fixture(scope="session")
def artifact_html(artifact_paths):
    """Dict mapping artifact name → full HTML source (session-scoped, loaded once)."""
    html = {}
    for name, path in artifact_paths.items():
        if not os.path.exists(path):
            html[name] = None
            continue
        with open(path, 'r', encoding='utf-8') as f:
            html[name] = f.read()
    return html


@pytest.fixture(scope="session")
def k1_html():
    """K1 hub HTML source (session-scoped, loaded once)."""
    if not os.path.exists(K1_PATH):
        return None
    with open(K1_PATH, 'r', encoding='utf-8') as f:
        return f.read()


@pytest.fixture(scope="session")
def deployed_urls():
    """Dict mapping artifact name → deployed URL."""
    return dict(DEPLOYED_URLS)
