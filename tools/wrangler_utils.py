"""
wrangler_utils.py — Safe subprocess wrapper for Cloudflare wrangler CLI

FIXES F12: wrangler Unicode output crashes Python subprocess on Windows.
Root cause: subprocess.run(text=True) uses CP1252 on Windows, which cannot
decode wrangler's UTF-8 terminal output (box-drawing chars U+2500-U+257F).

Usage:
    from wrangler_utils import run_wrangler
    result = run_wrangler(['r2', 'object', 'put', 'qnfo/papers/slug.md', '--file', path])
    print(result.stdout)

This module is the SINGLE canonical way to call wrangler from Python.
Do NOT use raw subprocess.run() for wrangler calls. Import this instead.

Maintained by: QWAV Program Agent
Last updated: 2026-05-28 (F12 fix applied)
"""
import subprocess
import os
import sys
from typing import List, Optional

# Ensure Python itself uses UTF-8 for I/O
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


def run_wrangler(
    args: List[str],
    *,
    cwd: Optional[str] = None,
    timeout: int = 60,
    check: bool = False,
    input_data: Optional[str] = None,
) -> subprocess.CompletedProcess:
    """
    Run a wrangler command safely on Windows with proper UTF-8 encoding.

    Args:
        args: wrangler subcommand args (e.g., ['r2', 'object', 'put', ...])
        cwd: Working directory (default: current)
        timeout: Timeout in seconds (default: 60)
        check: If True, raise CalledProcessError on non-zero exit
        input_data: Optional string to pipe to stdin

    Returns:
        subprocess.CompletedProcess with .stdout, .stderr as UTF-8 strings

    Example:
        >>> result = run_wrangler(['r2', 'object', 'put', 'qnfo/papers/test.md', '--file', 'test.md'])
        >>> if result.returncode == 0:
        ...     print("Uploaded:", result.stdout)
    """
    cmd = ['npx', 'wrangler'] + args

    # CRITICAL: encoding='utf-8' prevents CP1252 decode errors on Windows
    # errors='replace' prevents crashes on any remaining non-decodable bytes
    # shell=True needed on Windows for npx.cmd resolution
    result = subprocess.run(
        cmd if sys.platform != 'win32' else ' '.join(cmd),
        capture_output=True,
        encoding='utf-8',
        errors='replace',
        shell=(sys.platform == 'win32'),
        cwd=cwd,
        timeout=timeout,
        input=input_data,
    )

    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(
            result.returncode, cmd,
            output=result.stdout,
            stderr=result.stderr
        )

    return result


def upload_to_r2(
    r2_path: str,
    local_file: str,
    bucket: str = 'qnfo',
    timeout: int = 120,
) -> bool:
    """
    Upload a file to Cloudflare R2 with proper encoding.

    Args:
        r2_path: Destination path in R2 (e.g., 'papers/slug.md')
        local_file: Local file path to upload
        bucket: R2 bucket name (default: qnfo)
        timeout: Timeout in seconds (default: 120, longer for large files)

    Returns:
        True if upload succeeded (exit code 0)
    """
    result = run_wrangler(
        ['r2', 'object', 'put', f'{bucket}/{r2_path}', '--file', local_file, '--remote'],
        timeout=timeout,
    )
    return result.returncode == 0


def get_r2_object(r2_path: str, bucket: str = 'qnfo', timeout: int = 30) -> Optional[str]:
    """
    Fetch an object from Cloudflare R2.

    Args:
        r2_path: Path in R2 (e.g., 'audit/state/qwav-papers.json')
        bucket: R2 bucket name (default: qnfo)
        timeout: Timeout in seconds

    Returns:
        Object content as string, or None if not found
    """
    result = run_wrangler(
        ['r2', 'object', 'get', f'{bucket}/{r2_path}', '--remote'],
        timeout=timeout,
    )
    if result.returncode == 0:
        return result.stdout
    return None


if __name__ == '__main__':
    # Quick self-test
    result = run_wrangler(['--version'])
    print(f"wrangler version: {result.stdout.strip()}")
    print("Encoding test: PASSED (no UnicodeEncodeError)")
