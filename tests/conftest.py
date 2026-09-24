"""QWAV test fixtures -- CI-safe, repo-local.

Sprint 20 rewrote these to read files from the CHECKED-OUT REPOSITORY rather
than a developer's local `G:\\My Drive\\QWAV\\...` drive.  The previous
versions hard-coded Windows paths that never existed on a GitHub runner, so
every CI run failed with MODULE/FILE not found.  These fixtures work on any
machine and in CI.
"""

import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories that never contain site content.
EXCLUDE_DIRS = {".git", "node_modules", ".wrangler", "__pycache__"}


def _iter_html():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fn in files:
            if fn.endswith(".html"):
                abs_p = os.path.join(root, fn)
                yield os.path.relpath(abs_p, REPO_ROOT).replace(os.sep, "/"), abs_p


@pytest.fixture(scope="session")
def repo_root():
    return REPO_ROOT


@pytest.fixture(scope="session")
def html_paths():
    """Mapping of repo-relative path -> absolute path for every .html file."""
    return dict(_iter_html())


@pytest.fixture(scope="session")
def html_files(html_paths):
    """Mapping of repo-relative path -> file text (read once per session)."""
    out = {}
    for rel, abs_p in html_paths.items():
        with open(abs_p, encoding="utf-8", errors="replace") as fh:
            out[rel] = fh.read()
    return out


# Backwards-compatible alias used by test_all_artifacts_pytest.py.
@pytest.fixture(scope="session")
def artifact_html(html_files):
    return dict(html_files)


@pytest.fixture(scope="session")
def artifact_names(html_files):
    return sorted(html_files.keys())
