#!/usr/bin/env python3
"""
QWAV Structure Enforcement Script — v1.0

Automatically validates the QWAV directory structure against the rules defined in
briefings/FILE-MANAGEMENT-STRATEGY.md. Run as a pre-commit hook or manually.

Rules enforced:
  1. Top-level files: Only allowed whitelist
  2. Top-level directories: Only allowed whitelist
  3. Forbidden file types: No .pdf, no .docx (except briefings/research/), no loose .html
  4. Directory documentation: Every directory must have llms.txt
  5. File size limits: Files >1MB must be in .gitignore or explicitly allowed
  6. llms.txt consistency: All links must point to existing files
  7. No file left behind: Every file must be traceable through llms.txt hierarchy

Usage:
  python scripts/enforce-structure.py [--fix] [--report-only]
    --fix: Auto-fix simple issues (generate missing llms.txt, etc.)
    --report-only: Don't exit with error, just print report
"""

import os
import sys
import re
import argparse
from pathlib import Path
from collections import defaultdict

# Fix Windows encoding for emoji output
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ============================
# CONFIGURATION — EDIT CAREFULLY
# ============================

QWAV_ROOT = Path(__file__).resolve().parent.parent

# Top-level files that ARE allowed
ALLOWED_TOP_FILES = {
    '.gitignore',
    '.nojekyll',
    'CODE_OF_CONDUCT.md',
    'CONTRIBUTING.md',
    'index.html',
    'LICENSE',
    'llms.txt',
    'PROGRAM-STATE.md',
    'README.md',
    'robots.txt',
    'sitemap.xml',
}

# Top-level directories that ARE allowed
ALLOWED_TOP_DIRS = {
    '.github',
    '.githooks',
    '.wrangler',
    'briefings',
    'projects',
    'scripts',
    'sessions',
    'strategy',
}

# Directories that DON'T need llms.txt (tool/config dirs)
NO_LLMS_TXT_DIRS = {
    '.github',
    '.github/ISSUE_TEMPLATE',
    '.github/workflows',
    '.githooks',
    '.wrangler',
    '__pycache__',
    '.pytest_cache',
}

# File extensions that are FORBIDDEN everywhere (except where explicitly allowed)
FORBIDDEN_EXTENSIONS = {
    '.pdf': 'PDF files should be in R2 qnfo/releases/, not committed to git',
    '.exe': 'Executables should not be committed',
    '.dll': 'Binaries should not be committed',
    '.zip': 'Archives should be in R2, not git',
    '.tar.gz': 'Archives should be in R2, not git',
}

# File extensions forbidden except in specific directories
RESTRICTED_EXTENSIONS = {
    '.html': {'allowed_in': {'root'}, 'reason': 'Only index.html at root for landing page. Project HTML in dedicated repos.'},
    '.docx': {'allowed_in': {'briefings/research'}, 'reason': 'Only collaboration documents in briefings/research/. Others in dedicated repos.'},
    '.js': {'allowed_in': set(), 'reason': 'JavaScript belongs in dedicated project repos, not program directory.'},
    '.css': {'allowed_in': set(), 'reason': 'CSS belongs in dedicated project repos.'},
}

# Maximum file size in KB before triggering a warning (not error)
MAX_FILE_SIZE_KB = 1000  # 1MB

# Files explicitly allowed to exceed MAX_FILE_SIZE_KB
LARGE_FILE_EXEMPTIONS = {
    'sitemap.xml',  # 92KB, generated
}

# Files explicitly allowed despite restricted extension
HTML_EXEMPTIONS = {
    'index.html',             # Root landing page
    'projects\\index.html',   # Project catalog page (Cloudflare Pages)
}

DOCX_EXEMPTIONS = {
    # .docx files in briefings/research/ are already allowed by RESTRICTED_EXTENSIONS
}

# ============================
# VALIDATION FUNCTIONS
# ============================

class Violation:
    def __init__(self, path, rule, severity='error', fix_hint=None):
        self.path = path
        self.rule = rule
        self.severity = severity  # 'error' or 'warning'
        self.fix_hint = fix_hint

    def __str__(self):
        prefix = '⚠️ ' if self.severity == 'warning' else '❌ '
        result = f"{prefix}{self.path} — {self.rule}"
        if self.fix_hint:
            result += f"\n   💡 Fix: {self.fix_hint}"
        return result


def get_all_files(root):
    """Get all files recursively, excluding .git and __pycache__."""
    files = []
    for p in root.rglob('*'):
        if p.is_file():
            rel = p.relative_to(root)
            parts = rel.parts
            # Skip git, cache, and wrangler cache
            if parts[0] in ('.git', '__pycache__', '.pytest_cache'):
                continue
            if '.wrangler' in str(rel):
                continue
            if '/__pycache__/' in str(rel).replace('\\', '/'):
                continue
            files.append(rel)
    return files


def get_all_dirs(root):
    """Get all directories recursively."""
    dirs = []
    for p in root.rglob('*'):
        if p.is_dir():
            rel = p.relative_to(root)
            parts = rel.parts
            if parts[0] in ('.git', '__pycache__', '.pytest_cache', '.wrangler'):
                continue
            # Skip .wrangler subdirs
            if '.wrangler' in str(rel):
                continue
            dirs.append(rel)
    return dirs


def validate_top_level_files(files):
    """Rule 1: No unexpected files at the QWAV root."""
    violations = []
    for f in files:
        if len(f.parts) == 1 and f.name not in ALLOWED_TOP_FILES:
            violations.append(Violation(
                f, "Unexpected file at QWAV root",
                fix_hint=f"Move to appropriate subdirectory. Allowed files: {sorted(ALLOWED_TOP_FILES)}"
            ))
    return violations


def validate_top_level_dirs(dirs):
    """Rule 2: No unexpected directories at the QWAV root."""
    violations = []
    for d in dirs:
        if len(d.parts) == 1 and d.name not in ALLOWED_TOP_DIRS:
            violations.append(Violation(
                d, "Unexpected directory at QWAV root",
                fix_hint=f"Move to appropriate location or add to ALLOWED_TOP_DIRS in enforcement config. Allowed: {sorted(ALLOWED_TOP_DIRS)}"
            ))
    return violations


def validate_forbidden_extensions(files):
    """Rule 3: No forbidden file types anywhere."""
    violations = []
    for f in files:
        ext = f.suffix.lower()
        if ext in FORBIDDEN_EXTENSIONS:
            violations.append(Violation(
                f, FORBIDDEN_EXTENSIONS[ext],
                fix_hint="Move to R2 qnfo/releases/ or dedicated repo"
            ))
    return violations


def validate_restricted_extensions(files, root):
    """Rule 3b: Restricted file types only in allowed directories."""
    violations = []
    for f in files:
        ext = f.suffix.lower()
        if ext in RESTRICTED_EXTENSIONS:
            rule = RESTRICTED_EXTENSIONS[ext]
            allowed = rule['allowed_in']
            # Check if file is in an allowed directory
            parent_parts = list(f.parts[:-1]) if len(f.parts) > 1 else ['root']
            is_allowed = False
            for allowed_dir in allowed:
                allowed_parts = allowed_dir.replace('\\', '/').split('/')
                if allowed_dir == 'root' and len(f.parts) == 1:
                    is_allowed = True
                    break
                # Cross-platform path comparison
                if parent_parts == allowed_parts:
                    is_allowed = True
                    break
                # Check if file is in a subdirectory of allowed dir
                if len(parent_parts) >= len(allowed_parts):
                    if parent_parts[:len(allowed_parts)] == allowed_parts:
                        is_allowed = True
                        break
            if not is_allowed:
                # Check file-specific exemptions
                if ext == '.html' and str(f).replace('\\', '/') in HTML_EXEMPTIONS:
                    continue
                if f.name in HTML_EXEMPTIONS:
                    continue
                violations.append(Violation(
                    f, rule['reason'],
                    fix_hint=f"Move to dedicated project repo. Allowed locations: {allowed or 'nowhere'}"
                ))
    return violations


def _normalize_path(p):
    """Normalize a Path or string to use forward slashes for comparison."""
    return str(p).replace('\\', '/')


def validate_llms_txt_presence(dirs, files):
    """Rule 4: Every content directory must have llms.txt."""
    violations = []
    content_dirs = [d for d in dirs if _normalize_path(d) not in NO_LLMS_TXT_DIRS]
    for d in content_dirs:
        llms_path = d / 'llms.txt'
        if llms_path not in files:
            violations.append(Violation(
                d, f"Missing llms.txt — directory must have LLM discovery index",
                severity='warning',
                fix_hint="Run 'python scripts/enforce-structure.py --fix' to auto-generate"
            ))
    return violations


def validate_file_sizes(files, root):
    """Rule 5: No files larger than MAX_FILE_SIZE_KB without exemption."""
    violations = []
    for f in files:
        if f.name in LARGE_FILE_EXEMPTIONS:
            continue
        full_path = root / f
        try:
            size_kb = full_path.stat().st_size / 1024
            if size_kb > MAX_FILE_SIZE_KB:
                violations.append(Violation(
                    f, f"File too large ({size_kb:.0f}KB > {MAX_FILE_SIZE_KB}KB limit)",
                    severity='warning',
                    fix_hint="Move to R2 storage, dedicated repo, or add to LARGE_FILE_EXEMPTIONS"
                ))
        except OSError:
            pass
    return violations


def validate_llms_txt_links(files, dirs, root):
    """Rule 6: All links in llms.txt files must point to existing files/dirs."""
    violations = []
    for f in files:
        if f.name == 'llms.txt':
            full_path = root / f
            try:
                content = full_path.read_text(encoding='utf-8', errors='replace')
                # Find all markdown links: [text](url)
                links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', content)
                parent_dir = f.parent
                for link_text, link_url in links:
                    # Skip external URLs (http/https)
                    if link_url.startswith('http://') or link_url.startswith('https://'):
                        continue
                    # Skip anchor links
                    if link_url.startswith('#'):
                        continue
                    # Resolve relative path
                    target = (parent_dir / link_url).resolve().relative_to(root.resolve())
                    # Check if target exists (either as file or directory)
                    if target not in files and target not in dirs:
                        # Try with .md extension
                        target_md = target.with_suffix('.md')
                        if target_md not in files:
                            violations.append(Violation(
                                f"{f} → {link_url}",
                                f"Broken link: '{link_url}' does not exist",
                                severity='warning',
                                fix_hint=f"Update {f} to point to correct path or remove dead link"
                            ))
            except Exception as e:
                violations.append(Violation(
                    f, f"Error reading llms.txt: {e}",
                    severity='warning'
                ))
    return violations


def validate_no_orphaned_files(files, dirs, root):
    """Rule 7: Every file should be traceable through an llms.txt hierarchy."""
    # Build set of all files referenced in any llms.txt
    referenced = set()
    for f in files:
        if f.name == 'llms.txt':
            full_path = root / f
            try:
                content = full_path.read_text(encoding='utf-8', errors='replace')
                links = re.findall(r'\[([^\]]*)\]\(([^)]+)\)', content)
                parent_dir = f.parent
                for _, link_url in links:
                    if link_url.startswith('http://') or link_url.startswith('https://'):
                        continue
                    if link_url.startswith('#'):
                        continue
                    target = (parent_dir / link_url).resolve().relative_to(root.resolve())
                    referenced.add(target)
                    # Also add .md variant
                    referenced.add(target.with_suffix('.md'))
            except Exception:
                pass

    # Files that don't need to be in llms.txt (config, generated, etc.)
    EXEMPT_FILES = {
        Path('.gitignore'), Path('.nojekyll'), Path('llms.txt'),
        Path('index.html'), Path('robots.txt'), Path('sitemap.xml'),
        Path('CODE_OF_CONDUCT.md'), Path('CONTRIBUTING.md'), Path('LICENSE'),
    }
    # Directories whose contents are exempt
    EXEMPT_DIRS = {'.github', '.githooks', '.wrangler', '__pycache__'}

    violations = []
    for f in files:
        # Skip exempt files
        if f in EXEMPT_FILES:
            continue
        # Skip exempt directories
        if f.parts and f.parts[0] in EXEMPT_DIRS:
            continue
        # Skip llms.txt themselves
        if f.name == 'llms.txt':
            continue
        # Check if referenced
        if f not in referenced and f.with_suffix('.md') not in referenced:
            violations.append(Violation(
                f, "Orphaned file — not referenced in any llms.txt",
                severity='warning',
                fix_hint=f"Add to nearest llms.txt or move to appropriate directory"
            ))

    return violations


def auto_fix_llms_txt(dirs, files, root):
    """Auto-generate llms.txt for directories that are missing one."""
    created = []
    content_dirs = [d for d in dirs if _normalize_path(d) not in NO_LLMS_TXT_DIRS]
    for d in content_dirs:
        llms_path = d / 'llms.txt'
        if llms_path not in files:
            # Generate basic llms.txt
            dir_name = d.name.replace('-', ' ').replace('_', ' ').title()
            lines = [
                f"# QWAV {dir_name} — LLM Discovery Index",
                "",
                f"> Auto-generated index for {d}",
                "",
            ]
            # List files in this directory (not subdirectories)
            immediate_files = sorted([
                f for f in files
                if f.parent == d and f.name != 'llms.txt'
            ])
            if immediate_files:
                lines.append("## Files")
                lines.append("")
                for f in immediate_files:
                    lines.append(f"- [{f.name}](./{f.name})")
                lines.append("")

            # List subdirectories
            immediate_dirs = sorted([
                sd for sd in dirs
                if sd.parent == d
            ])
            if immediate_dirs:
                lines.append("## Subdirectories")
                lines.append("")
                for sd in immediate_dirs:
                    sd_name = sd.name.replace('-', ' ').title()
                    lines.append(f"- [{sd_name}/](./{sd.name}/)")
                    # Check if subdir has llms.txt
                    sub_llms = sd / 'llms.txt'
                    if sub_llms in files:
                        lines.append(f"  - [llms.txt](./{sd.name}/llms.txt)")
                lines.append("")

            lines.append("## Cross-Reference")
            lines.append(f"- Root index: [../llms.txt](../llms.txt)")
            lines.append(f"- Program State: [../PROGRAM-STATE.md](../PROGRAM-STATE.md)")

            full_path = root / llms_path
            full_path.write_text('\n'.join(lines), encoding='utf-8')
            created.append(str(llms_path))

    return created


# ============================
# MAIN
# ============================

def main():
    parser = argparse.ArgumentParser(description='Enforce QWAV directory structure rules')
    parser.add_argument('--fix', action='store_true', help='Auto-fix simple issues')
    parser.add_argument('--report-only', action='store_true', help='Print report without error exit')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    args = parser.parse_args()

    root = QWAV_ROOT
    files = get_all_files(root)
    dirs = get_all_dirs(root)

    if args.verbose:
        print(f"🔍 Scanning {len(files)} files in {len(dirs)} directories...")
        print(f"   Root: {root}")
        print()

    all_violations = []

    # Run all validations
    validations = [
        ("Top-level file whitelist", validate_top_level_files(files)),
        ("Top-level directory whitelist", validate_top_level_dirs(dirs)),
        ("Forbidden file extensions", validate_forbidden_extensions(files)),
        ("Restricted file extensions", validate_restricted_extensions(files, root)),
        ("llms.txt presence", validate_llms_txt_presence(dirs, files)),
        ("File size limits", validate_file_sizes(files, root)),
        ("llms.txt link validity", validate_llms_txt_links(files, dirs, root)),
        ("Orphaned file detection", validate_no_orphaned_files(files, dirs, root)),
    ]

    for name, violations in validations:
        if violations:
            all_violations.extend(violations)

    # Auto-fix if requested
    if args.fix:
        print("🔧 Auto-fixing...")
        created = auto_fix_llms_txt(dirs, files, root)
        if created:
            for c in created:
                print(f"   ✅ Created {c}")
        else:
            print("   Nothing to fix")

    # Report
    errors = [v for v in all_violations if v.severity == 'error']
    warnings = [v for v in all_violations if v.severity == 'warning']

    print()
    if errors or warnings:
        print(f"{'='*60}")
        print(f"STRUCTURE ENFORCEMENT REPORT")
        print(f"{'='*60}")
        print()

        if errors:
            print(f"❌ {len(errors)} ERROR(S) — must fix before merge:")
            print()
            for v in errors:
                print(f"   {v}")
                print()
        else:
            print("✅ No errors found.")

        if warnings:
            print(f"⚠️  {len(warnings)} WARNING(S):")
            print()
            for v in warnings:
                print(f"   {v}")
                print()
    else:
        print(f"{'='*60}")
        print("✅ ALL CHECKS PASSED — Directory structure is clean")
        print(f"{'='*60}")

    print(f"\n   Files scanned: {len(files)}")
    print(f"   Directories scanned: {len(dirs)}")

    if errors and not args.report_only:
        print(f"\n💡 Run with --fix to auto-fix simple issues.")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
