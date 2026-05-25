#!/usr/bin/env python3
"""
Convert Obsidian wikilinks [[...]] to standard Markdown links.

Usage:
    python convert_wikilinks.py --releases-dir "G:\My Drive\Obsidian\releases" --dry-run
    python convert_wikilinks.py --releases-dir "G:\My Drive\Obsidian\releases" --output-dir "G:\My Drive\QWAV\publications"
"""

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|([^\]]+))?\]\]')

def slugify(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]+', '-', name).strip('-').lower()

def build_page_index(releases_dir: Path) -> dict:
    index = {}
    for md_file in releases_dir.rglob("*.md"):
        if md_file.name.startswith("_"):
            continue
        rel_path = md_file.relative_to(releases_dir)
        stem = md_file.stem
        clean_name = re.sub(r'^\d{4}-\d{2}-', '', stem)
        index[stem] = rel_path
        index[clean_name] = rel_path
        index[stem.lower()] = rel_path
        index[clean_name.lower()] = rel_path
    return index

def convert_wikilinks(content: str, page_index: dict, current_file: Path, releases_dir: Path):
    count = 0
    broken = []

    def replace_link(match):
        nonlocal count
        target = match.group(1).strip()
        section = match.group(2)
        alias = match.group(3)

        found_path = None
        for key in [target, re.sub(r'^\d{4}-\d{2}-', '', target),
                     target.lower(), re.sub(r'^\d{4}-\d{2}-', '', target).lower()]:
            if key in page_index:
                found_path = page_index[key]
                break

        if found_path is None:
            broken.append(target)
            return f'[BROKEN: {target}]({slugify(target)}.md)'

        current_dir = current_file.relative_to(releases_dir).parent
        try:
            rel_link = os.path.relpath(str(found_path), str(current_dir)).replace('\\', '/')
        except ValueError:
            rel_link = str(found_path).replace('\\', '/')

        display = alias if alias else target
        display = re.sub(r'^\d{4}-\d{2}-', '', display)

        if section:
            link = f'[{display}]({rel_link}#{slugify(section)})'
        else:
            link = f'[{display}]({rel_link})'

        count += 1
        return link

    new_content = WIKILINK_RE.sub(replace_link, content)
    return new_content, count, broken

def main():
    parser = argparse.ArgumentParser(description='Convert Obsidian wikilinks to standard Markdown links')
    parser.add_argument('--releases-dir', required=True, help='Path to Obsidian releases directory')
    parser.add_argument('--output-dir', help='Output directory for converted files')
    parser.add_argument('--dry-run', action='store_true', help='Preview only, no writes')
    args = parser.parse_args()

    releases_dir = Path(args.releases_dir)
    if not releases_dir.exists():
        print(f"ERROR: {releases_dir} not found", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output_dir) if args.output_dir else None
    dry_run = args.dry_run or output_dir is None

    if dry_run:
        print("=== DRY RUN ===\n")

    page_index = build_page_index(releases_dir)
    print(f"Indexed {len(page_index)} page-name entries\n")

    files_with_wikilinks = []
    for md_file in releases_dir.rglob("*.md"):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                if WIKILINK_RE.search(f.read()):
                    files_with_wikilinks.append(md_file)
        except:
            continue

    index_files = [f for f in files_with_wikilinks if f.name.startswith('_')]
    content_files = [f for f in files_with_wikilinks if not f.name.startswith('_')]

    total_conversions = 0
    all_broken = []

    for md_file in index_files + content_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except:
            continue

        new_content, count, broken = convert_wikilinks(content, page_index, md_file, releases_dir)
        total_conversions += count
        all_broken.extend(broken)

        if count > 0:
            status = "DRY-RUN" if dry_run else "CONVERTED"
            print(f"[{status}] {md_file.relative_to(releases_dir)}: {count} wikilinks")
            if broken:
                print(f"  BROKEN: {', '.join(broken)}")

        if not dry_run and count > 0 and output_dir:
            rel_path = md_file.relative_to(releases_dir)
            out_path = output_dir / rel_path
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

    if not dry_run and output_dir:
        copies = 0
        for md_file in releases_dir.rglob("*.md"):
            if md_file not in files_with_wikilinks:
                rel_path = md_file.relative_to(releases_dir)
                out_path = output_dir / rel_path
                out_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(md_file, out_path)
                copies += 1
        print(f"\nCopied {copies} non-wikilink files")

    unique_broken = sorted(set(all_broken))
    print(f"\n{'='*60}")
    print(f"Total wikilinks converted: {total_conversions}")
    print(f"Unique broken targets:     {len(unique_broken)}")
    if unique_broken:
        for t in unique_broken[:20]:
            print(f"  - [[{t}]]")
        if len(unique_broken) > 20:
            print(f"  ... and {len(unique_broken) - 20} more")

if __name__ == '__main__':
    main()
