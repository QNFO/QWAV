#!/usr/bin/env python
"""
QWAV SMOKE TESTS -- structural + integrity checks, CI-safe
===========================================================
Standalone (stdlib only, no network). Rewritten 2026-09-24 from a version that
read `G:\\My Drive\\QWAV\\...` and fetched dead qnfo.github.io URLs, which made
the weekly CI job red on every run.

What it checks that unit tests do NOT cover:
  - site structure: every HTML page is a well-formed document
  - required machine-readability files exist
  - internal links resolve to files that actually exist in the repo
  - no unrendered template placeholders ship
  - NO COMMITTED SECRETS (regression guard for the 2026-09-24 credential leak)

Run: python tests/test_smoke.py          (exit 0 = pass, 1 = fail)
"""

import os
import re
import sys
import urllib.parse

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE_DIRS = {".git", "node_modules", ".wrangler", "__pycache__"}

PASS = 0
FAIL = 0


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
    print(f"\n{'=' * 60}\n{title}\n{'=' * 60}")


def walk_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fn in files:
            yield os.path.relpath(os.path.join(root, fn), REPO_ROOT).replace(os.sep, "/")


def html_files():
    return [p for p in walk_files() if p.endswith(".html")]


# ----------------------------------------------------------------------
# Section 1: document structure
# ----------------------------------------------------------------------
section("1. Every HTML page is well-formed")
pages = html_files()
check(len(pages) > 0, f"found {len(pages)} HTML page(s)")
for rel in pages:
    text = open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace").read()
    check("<!doctype html>" in text[:400].lower(), f"{rel}: has <!DOCTYPE html>")
    check(bool(re.search(r"<title[^>]*>\s*\S", text, re.IGNORECASE)), f"{rel}: has non-empty <title>")

# ----------------------------------------------------------------------
# Section 2: required files
# ----------------------------------------------------------------------
section("2. Required site files present")
for name in ("index.html", "robots.txt", "sitemap.xml", "llms.txt"):
    check(os.path.exists(os.path.join(REPO_ROOT, name)), f"{name} exists")

# ----------------------------------------------------------------------
# Section 3: no unrendered placeholders
# ----------------------------------------------------------------------
section("3. No unrendered placeholders")
PLACEHOLDERS = ("{{", "}}", "TODO:", "FIXME:", "LOREM IPSUM", "[object Object]")
for rel in pages:
    text = open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace").read()
    for token in PLACEHOLDERS:
        check(token not in text, f"{rel}: no {token!r}")

# ----------------------------------------------------------------------
# Section 4: internal links resolve
# ----------------------------------------------------------------------
section("4. Internal links resolve to real files")
LINK_RE = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.IGNORECASE)
# Prefixes that only resolve on the deployed host (the QWAV site is mounted
# under /QWAV/ on Pages); they are not verifiable from the repo checkout.
DEPLOY_PREFIXES = ("/QWAV/",)
checked = 0
for rel in pages:
    text = open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace").read()
    page_dir = os.path.dirname(rel)
    for raw in LINK_RE.findall(text):
        target = urllib.parse.urlparse(raw)
        if target.scheme or raw.startswith(("//", "#", "mailto:", "data:", "javascript:")):
            continue
        path = urllib.parse.unquote(target.path)
        if not path:
            continue
        if any(path.startswith(pre) for pre in DEPLOY_PREFIXES):
            continue  # deploy-mount link, not repo-verifiable
        is_dir_link = path.endswith("/")
        if path.startswith("/"):
            resolved = os.path.normpath(path.lstrip("/"))
        else:
            resolved = os.path.normpath(os.path.join(page_dir, path))
        if resolved.startswith("..") or resolved.startswith("/"):
            continue
        abs_target = os.path.join(REPO_ROOT, resolved)
        checked += 1
        ok = os.path.isdir(abs_target) if is_dir_link else os.path.exists(abs_target)
        check(ok, f"{rel}: link '{raw}' resolves")
print(f"  ({checked} internal links checked)")

# ----------------------------------------------------------------------
# Section 5: committed-secret guard
# ----------------------------------------------------------------------
section("5. No committed secrets (recurrence guard)")
SECRET_PATTERNS = {
    "cloudflare_token": r"[A-Za-z0-9_-]{40}\.[A-Za-z0-9_-]{40,}",
    "github_pat": r"gh[pousr]_[A-Za-z0-9]{36,}",
    "aws_key": r"AKIA[0-9A-Z]{16}",
    "private_key": r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "slack_token": r"xox[baprs]-[A-Za-z0-9-]{10,}",
}
scan_exts = (".py", ".js", ".html", ".json", ".ps1", ".sh", ".yml", ".yaml", ".txt", ".md")
secret_hits = 0
for rel in walk_files():
    if not rel.endswith(scan_exts):
        continue
    text = open(os.path.join(REPO_ROOT, rel), encoding="utf-8", errors="replace").read()
    for name, rx in SECRET_PATTERNS.items():
        for m in re.finditer(rx, text):
            if "REDACTED" in text[max(0, m.start() - 20):m.start()]:
                continue
            secret_hits += 1
            print(f"  [FAIL] {rel}: possible {name} -> {m.group(0)[:16]}...")
check(secret_hits == 0, "no high-confidence secrets committed")

# ----------------------------------------------------------------------
print(f"\n{'=' * 60}")
print(f"{PASS} passed, {FAIL} failed")
print("=" * 60)
sys.exit(0 if FAIL == 0 else 1)
