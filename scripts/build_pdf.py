#!/usr/bin/env python3
"""
build_pdf.py -- Fully automated Markdown -> HTML -> PDF pipeline v3.0

Reusable CLI tool for DeepChat agent threads. Converts any Markdown file
(with optional YAML frontmatter) to a professional A4 PDF via HTML intermediate.

Pipeline:
  1. Parse YAML frontmatter -> styled author block
  2. Markdown -> HTML (code highlighting, tables, lists, math)
  3. MathJax 3 CDN for LaTeX rendering (unless --no-math)
  4. Edge/Chrome headless -> PDF with rendered JavaScript/MathJax

Usage:
  python build_pdf.py --input paper.md
  python build_pdf.py --input paper.md --output out.pdf
  python build_pdf.py --input paper.md --css custom.css --html-only
"""

import argparse
import datetime
import os
import re
import subprocess
import sys
import tempfile


# ---------------------------------------------------------------------------
# Embedded default CSS -- self-contained, no external CSS dependency
# Use --css to override with a custom stylesheet file.
# ---------------------------------------------------------------------------
EMBEDDED_CSS = r"""/* build_pdf.css v3.0 -- Embedded academic PDF stylesheet */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
:root{--text:#1a1a1a;--muted:#555;--border:#d0d0d0;--bg:#fafafa;--accent:#007acc;--title:24pt;--h1:18pt;--h2:15pt;--body:10.5pt}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"Inter","Segoe UI","Helvetica Neue",Arial,sans-serif;font-size:var(--body);line-height:1.6;color:var(--text);max-width:6.2in;margin:0 auto;padding:0;text-align:left;background:white}
h1.title{font-size:var(--title);font-weight:700;text-align:left;margin:0.8in 0 0.1in 0;line-height:1.1;color:var(--text);border-bottom:3px solid #000;padding-bottom:0.1in}
h1{font-size:var(--h1);font-weight:600;margin:0.6in 0 0.3in 0;line-height:1.2;color:var(--text);border-bottom:2px solid #333;padding-bottom:0.1in;page-break-before:always;page-break-after:avoid}
h2{font-size:var(--h2);font-weight:600;margin:1em 0 0.5em 0;color:var(--text);border-bottom:1px solid #ccc;padding-bottom:0.2em}
h3{font-size:13pt;font-weight:600;margin:0.9em 0 0.4em 0;color:#333}
p{margin:0 0 0.8em 0;line-height:1.6}
.author-block{margin:0.2in 0 0.3in 0;padding:0.15in 0.2in;background:#f9f9f9;border-left:3px solid #000;border-radius:0 4px 4px 0;font-size:9.5pt;line-height:1.5}
.author-block p{margin:0}.author-block strong{font-weight:600;color:var(--text)}
.author-block a{color:var(--accent);text-decoration:none;border-bottom:1px dotted var(--accent)}
.author-block .abstract-label{font-weight:700;display:block;margin-top:0.3em;font-size:10pt}
.author-block .abstract-text{margin-top:0.2em;font-style:normal;color:var(--muted)}
ul,ol{margin:0.8em 0;padding-left:2em}li{margin-bottom:0.4em;line-height:1.5}
ol{counter-reset:item;list-style-type:none}ol>li{counter-increment:item;position:relative;padding-left:2em}
ol>li::before{content:counter(item)".";font-weight:600;position:absolute;left:0;width:1.5em;text-align:right}
code{font-family:"JetBrains Mono",Consolas,monospace;font-size:0.85em;background:#f9f9f9;padding:0.1em 0.3em;border-radius:2px;border:1px solid #e0e0e0;color:#d63384}
pre{font-family:"JetBrains Mono",Consolas,monospace;background:#f9f9f9;padding:0.8em;margin:0.9em 0;border-radius:3px;overflow-x:auto;border:1px solid #e0e0e0;font-size:0.8em;line-height:1.5;border-left:3px solid #000;white-space:pre-wrap;word-break:break-word}
pre code{background:none;padding:0;border:none;color:inherit;font-size:inherit}
table{width:100%;border-collapse:collapse;margin:1.2em 0;font-size:0.95em;box-shadow:0 2px 4px rgba(0,0,0,0.05);border-radius:4px;overflow:hidden}
th{background:#f0f0f0;font-weight:600;padding:0.5em 0.6em;text-align:left;border:1px solid var(--border);border-top:2px solid #000}
td{background:#fff;padding:0.5em 0.6em;text-align:left;border:1px solid var(--border)}
tr:nth-child(even) td{background:#fafafa}tbody tr td:first-child{font-weight:600}
blockquote{border-left:3px solid #000;margin:1.2em 0;padding:0.5em 0 0.5em 0.9em;background:var(--bg);color:var(--muted);border-radius:0 2px 2px 0}
a{color:var(--accent);text-decoration:none;border-bottom:1px dotted var(--accent)}
mjx-container{overflow-x:auto;max-width:100%}mjx-container[display="true"]{display:block;margin:0.8em 0;text-align:left}
.c{color:#6a737d;font-style:italic}.k{color:#d73a49;font-weight:bold}.s{color:#032f62}.mi{color:#005cc5}.nf{color:#6f42c1}.nc{color:#6f42c1;font-weight:bold}
@media print{@page{size:A4;margin:0.75in 0.8in 0.75in 1.2in;@bottom-right{content:"Page "counter(page);font-family:"Inter",sans-serif;font-size:8pt;color:#666;padding:0.2in 0.4in 0 0}}body{padding:0;max-width:100%}.author-block{border:1px solid #000;border-left:3px solid #000}}
"""

MATHJAX_SCRIPT = """MathJax={tex:{inlineMath:[['$','$']],displayMath:[['$$','$$']],processEscapes:true,tags:'ams'},startup:{ready(){MathJax.startup.defaultReady();const n=document.querySelectorAll('mjx-container').length;console.log('MathJax ready: '+n+' expressions rendered')}}}"""

MATHJAX_CDN = '<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>'


# ---------------------------------------------------------------------------
# Utility functions
# ---------------------------------------------------------------------------

def find_browser():
    """Locate an installed Edge, Chrome, or Chromium browser for headless PDF rendering."""
    import shutil

    # 1. Try Windows paths (Edge, Chrome)
    for p in [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ]:
        if os.path.exists(p):
            return p

    # 2. Try Linux paths (Chromium, Google Chrome) via shutil.which
    for cmd in ["google-chrome-stable", "google-chrome", "chromium-browser", "chromium"]:
        path = shutil.which(cmd)
        if path and os.path.exists(path):
            return path

    # 3. Try macOS paths
    for p in [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]:
        if os.path.exists(p):
            return p

    return None


# CSS preset directory (relative to this script)
CSS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "css")

# Named style presets map to css/<name>.css files
STYLE_PRESETS = {
    "academic": os.path.join(CSS_DIR, "academic.css"),
    "modern": os.path.join(CSS_DIR, "modern.css"),
    "minimal": os.path.join(CSS_DIR, "minimal.css"),
}


def resolve_css(style=None, css_path=None):
    """Resolve CSS content from style preset, CSS file, or embedded default.

    Priority: --css overrides --style overrides embedded default.
    Returns (css_content, source_label) tuple.
    """
    # 1. Explicit CSS file (highest priority)
    if css_path:
        if not os.path.exists(css_path):
            raise FileNotFoundError(f"CSS file not found: {css_path}")
        with open(css_path, "r", encoding="utf-8") as f:
            return f.read(), css_path

    # 2. Named style preset
    if style and style in STYLE_PRESETS:
        preset_path = STYLE_PRESETS[style]
        if not os.path.exists(preset_path):
            print(f"WARNING: Style preset '{style}' not found at {preset_path}, falling back to embedded.", file=sys.stderr)
        else:
            with open(preset_path, "r", encoding="utf-8") as f:
                return f.read(), f"{style} (preset: {preset_path})"

    # 3. Embedded default (fallback)
    return EMBEDDED_CSS, "(embedded default)"


def parse_frontmatter(text):
    """Extract YAML frontmatter dict and body from markdown text."""
    meta, body = {}, text
    if not text.startswith("---"):
        return meta, body
    parts = text.split("---", 2)
    if len(parts) < 3:
        return meta, body
    body = parts[2]
    for line in parts[1].strip().split("\n"):
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip().strip('"')
        v = v.strip().strip('"').strip("'").strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip('"') for x in v[1:-1].split(",")]
        meta[k] = v
    return meta, body


def build_author_block(meta):
    """Build an HTML author+metadata block from frontmatter dict."""
    a = meta.get("authors", meta.get("author", ""))
    o = meta.get("orcid", "0009-0002-4317-5604")
    d = meta.get("doi", "")
    dt = meta.get("date", datetime.date.today().isoformat())
    ab = meta.get("abstract", "")
    lines = []
    if a:
        lines.append(f"<p><strong>Author:</strong> {a}</p>")
    lines.append(
        f'<p><strong>ORCID:</strong> <a href="https://orcid.org/{o}">{o}</a></p>'
    )
    if d and "zenodo" in d:
        lines.append(
            f'<p><strong>DOI:</strong> <a href="https://doi.org/{d}">{d}</a></p>'
        )
    lines.append(f"<p><strong>Date:</strong> {dt}</p>")
    if ab:
        lines.append(
            f'<p class="abstract-label">Abstract</p><p class="abstract-text">{ab}</p>'
        )
    return f'<div class="author-block">\n{"".join(lines)}\n</div>'


# ---------------------------------------------------------------------------
# Pipeline steps
# ---------------------------------------------------------------------------

def build_html(input_path, output_html, css_content, use_math=True, title_override=None):
    """Convert Markdown to standalone HTML with embedded CSS and MathJax.

    Args:
        input_path: Path to the Markdown (.md) source file.
        output_html: Path to write the generated HTML file.
        css_content: CSS string to embed (from file or default).
        use_math: Include MathJax CDN and config (default True).
        title_override: Override title from frontmatter (optional).

    Returns:
        (title, html_size) tuple.
    """
    import markdown

    with open(input_path, "r", encoding="utf-8") as f:
        raw = f.read()

    meta, body = parse_frontmatter(raw)
    author_html = build_author_block(meta)

    md = markdown.Markdown(extensions=["extra", "codehilite", "tables", "fenced_code"])
    html_body = md.convert(body)

    # Strip internal metadata lines that should not appear in publication PDFs
    html_body = re.sub(r"<p><strong>Version:</strong>.*?</p>", "", html_body)
    html_body = re.sub(r"<p><strong>Status:</strong>.*?</p>", "", html_body)

    title = title_override or meta.get("title", "Untitled")

    # Build HTML -- use string concat to avoid JS/CSS brace conflicts with f-strings
    parts = [
        '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>',
        title,
        "</title><style>",
        css_content,
        "</style>",
    ]
    if use_math:
        parts.append("<script>")
        parts.append(MATHJAX_SCRIPT)
        parts.append("</script>")
        parts.append(MATHJAX_CDN)
    parts.append("</head><body>")
    parts.append(f'<h1 class="title">{title}</h1>')
    parts.append(author_html)
    parts.append(html_body)
    parts.append("</body></html>")

    html = "".join(parts)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html)

    size = os.path.getsize(output_html)
    return title, size


def html_to_pdf(html_path, pdf_path, browser_path):
    """Convert HTML to PDF via headless browser (Edge/Chrome).

    Args:
        html_path: Path to the HTML file to render.
        pdf_path: Path for the output PDF.
        browser_path: Full path to msedge.exe or chrome.exe.

    Returns:
        PDF file size in bytes, or None on failure.
    """
    abs_html = os.path.abspath(html_path).replace("\\", "/")
    abs_pdf = os.path.abspath(pdf_path)

    cmd = [
        browser_path,
        "--headless",
        f"--print-to-pdf={abs_pdf}",
        "--no-pdf-header-footer",
        f"file:///{abs_html}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode == 0 and os.path.exists(abs_pdf):
        return os.path.getsize(abs_pdf)
    return None


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Markdown -> HTML -> PDF pipeline (v3.0)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_pdf.py --input paper.md
  python build_pdf.py --input paper.md --output out.pdf
  python build_pdf.py --input paper.md --style modern
  python build_pdf.py --input paper.md --style minimal --no-math
  python build_pdf.py --input paper.md --css custom.css
  python build_pdf.py --input paper.md --html-only
  python build_pdf.py --input paper.md --title "My Paper Title"
        """,
    )
    parser.add_argument(
        "--input", "-i", required=True, help="Input Markdown file (.md)"
    )
    parser.add_argument(
        "--output", "-o", default=None, help="Output PDF path (default: input name + .pdf)"
    )
    parser.add_argument(
        "--style", choices=["academic", "modern", "minimal"], default=None,
        help="CSS style preset: academic (default), modern, or minimal"
    )
    parser.add_argument(
        "--css", default=None, help="Custom CSS file (overrides --style)"
    )
    parser.add_argument(
        "--title", default=None, help="Override title from YAML frontmatter"
    )
    parser.add_argument(
        "--no-math", action="store_true", help="Skip MathJax/LaTeX rendering"
    )
    parser.add_argument(
        "--html-only", action="store_true", help="Stop after HTML generation (no PDF)"
    )
    parser.add_argument(
        "--working-dir", default=None,
        help="Directory for intermediate HTML file (default: output file directory)"
    )

    args = parser.parse_args()

    # Validate input exists
    if not os.path.exists(args.input):
        print(f"ERROR: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    # Determine output path
    if args.output:
        pdf_path = args.output
    else:
        base = os.path.splitext(os.path.basename(args.input))[0]
        pdf_path = os.path.join(os.path.dirname(args.input) or ".", f"{base}.pdf")

    pdf_dir = os.path.dirname(os.path.abspath(pdf_path))
    work_dir = args.working_dir or pdf_dir

    # Intermediate HTML: alongside PDF with same base name
    html_name = os.path.splitext(os.path.basename(pdf_path))[0] + ".html"
    html_path = os.path.join(work_dir, html_name)

    print("=" * 60)
    print("  Markdown -> HTML -> PDF Pipeline v3.0")
    print("=" * 60)
    print(f"  Input:     {args.input}")
    print(f"  Output:    {pdf_path}")

    # Step 1: Load CSS (style preset, custom file, or embedded default)
    try:
        css_content, css_source = resolve_css(style=args.style, css_path=args.css)
        print(f"  CSS:       {css_source}")
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)

    # Step 2: Markdown -> HTML
    try:
        title, html_size = build_html(
            args.input, html_path, css_content,
            use_math=not args.no_math,
            title_override=args.title,
        )
        print(f"  [1/2] HTML: {html_size:,} bytes -> {html_path}")
    except ImportError:
        print("ERROR: 'markdown' library not installed. Run: pip install markdown", file=sys.stderr)
        sys.exit(3)
    except Exception as e:
        print(f"ERROR: HTML build failed: {e}", file=sys.stderr)
        sys.exit(4)

    if args.html_only:
        print(f"  [DONE] HTML only (--html-only). No PDF generated.")
        print(f"  Title: {title}")
        return

    # Step 3: HTML -> PDF via headless browser
    browser = find_browser()
    if not browser:
        print("  [SKIP] No browser found for PDF step.")
        print(f"  Open {html_path} manually -> Ctrl+P -> Save as PDF")
        sys.exit(5)

    try:
        pdf_size = html_to_pdf(html_path, pdf_path, browser)
        if pdf_size:
            print(f"  [2/2] PDF:  {pdf_size:,} bytes -> {pdf_path}")
        else:
            print(f"  [FAIL] PDF step returned no output.")
            sys.exit(6)
    except subprocess.TimeoutExpired:
        print(f"  [FAIL] Browser PDF conversion timed out (30s).", file=sys.stderr)
        sys.exit(7)
    except Exception as e:
        print(f"  [FAIL] PDF conversion error: {e}", file=sys.stderr)
        sys.exit(8)

    print(f"  >> PIPELINE COMPLETE <<")


if __name__ == "__main__":
    main()
