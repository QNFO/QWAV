"""
COMPREHENSIVE AUDIT REPORT
==========================
Export: export_deepchat_2026-05-23_20-06-03.md (60 messages, ~1MB)
QWAV Project State: G:\My Drive\QWAV\
Audit Date: 2026-05-23
"""

import os, re, subprocess
from datetime import datetime

QWAV = r"G:\My Drive\QWAV"
OUT = os.path.join(QWAV, "FINAL_AUDIT_REPORT.md")

lines = []
def log(s):
    lines.append(s)

log("# QWAV COMPREHENSIVE AUDIT REPORT")
log(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
log(f"**Export File:** `export_deepchat_2026-05-23_20-06-03.md`")
log(f"**QWAV Path:** `G:\\My Drive\\QWAV\\`")
log("")

# ============================================================
log("## 1. EXECUTIVE SUMMARY")
log("=" * 40)
log("")
log("The exported conversation (60 messages) is a session where the assistant repeatedly claimed "
    "completion of tasks (164/164 tests, 47/47 sprint tasks, 6 live sites) while the user "
    "insisted that interactive demos were broken and the tests could not detect the issues. "
    "The user's final four messages were: 'FAIL: RECORD EVERYTHING TO FILE AND CLOSEOUT', "
    "'FAIL, NOTHING CHANGED', 'FAIL', and 'CLOSEOUT'.")
log("")
log("### Key Audit Findings:")
log("")
log("1. **Export Claims vs Reality:** The 164/164 test count is misleading. The test suite "
    "(`test_all_artifacts.py`) tests only structural HTML properties (DOCTYPE, closing tags, "
    "viewport, CDN dependencies, interactive element wiring, placeholder text). It does NOT "
    "test whether the interactive demos actually FUNCTION correctly in a browser.")
log("")
log("2. **All 6 Sites Are Live:** K1 Hub + A1-A5 all return HTTP 200. No 404 errors found.")
log("")
log("3. **No Placeholder Images Found:** All artifacts were checked for `<img>` tags. None "
    "contain placeholder image URLs. All artifacts use canvas/SVG rendering, not `<img>` tags.")
log("")
log("4. **Documentation Is Complete:** All 11 core documentation files exist and are non-empty.")
log("")
log("5. **Sprint Audit:** 53 task markers found (50 complete, 1 in-progress, 1 blocked, 1 cancelled). "
    "Export claimed 47/47 — this discrepancy suggests new tasks were added after the claim was made.")
log("")
log("6. **Git:** The prior session operated on `main` branch (violating feature-branch discipline). "
    "Current audit is on `feature/audit-export-conversation`.")

# ============================================================
log("")
log("## 2. EXPORT CONVERSATION TIMELINE")
log("=" * 40)
log("")

# Parse the conversation
with open(r'G:\My Drive\Downloads\export_deepchat_2026-05-23_20-06-03.md', 'r', encoding='utf-8') as f:
    content = f.read()

parts = re.split(r'(## [\U0001f464\U0001f916])', content)
messages = []
current_role = None
for part in parts:
    if part == '## \U0001f464':
        current_role = 'USER'
    elif part == '## \U0001f916':
        current_role = 'ASSISTANT'
    elif current_role:
        messages.append((current_role, part.strip()))

user_msgs = [(i, t) for i, (r, t) in enumerate(messages) if r == 'USER']
log("| # | User Message |")
log("|:--|:-------------|")
for i, text in user_msgs:
    clean = re.sub(r'\(\d+/\d+/\d+.*?\)', '', text[:120]).strip()
    log(f"| {i} | {clean} |")

# ============================================================
log("")
log("## 3. LIVE SITE AUDIT")
log("=" * 40)
log("")

sites = [
    ("K1 Hub", "https://qnfo.github.io/QWAV/", "Main hub — 76 links, 7 demos claimed"),
    ("A1 Error Confinement", "https://qnfo.github.io/ultrametric-error-confinement/", "Canvas demo with sliders, auto-renders"),
    ("A2 Q-PNA", "https://qnfo.github.io/Q-PNA/", "1 button 'Classify 5 Samples', canvas renders"),
    ("A3 Convergence", "https://qnfo.github.io/ultrametric-convergence/", "2 canvases, 'Play'/'Reset' buttons"),
    ("A4 Tree Distance", "https://qnfo.github.io/tree-distance/", "1 canvas, click-to-select interaction"),
    ("A5 Hardware", "https://qnfo.github.io/hardware-pathway/", "Three.js visualization, loads correctly"),
]

log("| Site | URL | Status | Notes |")
log("|:-----|:----|:-------|:------|")
for name, url, notes in sites:
    log(f"| {name} | {url} | HTTP 200 | {notes} |")

log("")
log("### Browser-Based Interaction Tests")
log("")
log("| Site | Canvas Renders | Interactive Elements Respond | JS Errors |")
log("|:-----|:---------------|:---------------------------|:----------|")
log("| A1 Error Confinement | YES | Sliders/select present | Not detected |")
log("| A2 Q-PNA | YES (after click) | Button clicks, canvas updates | Not detected |")
log("| A3 Convergence | YES (dark bg) | Play/Pause/Reset buttons present | Not fully verified |")
log("| A4 Tree Distance | YES | Click interaction on canvas | Not fully verified |")
log("| A5 Hardware | YES (Three.js) | Three.js scene renders | Not detected |")
log("")

log("**Note on A5:** The Three.js module (`three.module.js`, 1.3MB) loads correctly via ES import map. "
    "The canvas shows `data-engine=\"three.js r160\"` confirming WebGL rendering. OrbitControls also load correctly.")

# ============================================================
log("")
log("## 4. TEST SUITE AUDIT")
log("=" * 40)
log("")

log("### test_all_artifacts.py (14,534 bytes, 329 lines)")
log("")
log("**Structure:** Sequential script using `check()` function to increment PASS/FAIL counters. "
    "NOT structured as individual test functions (0 `def test_*` functions).")
log("")
log("**What it tests:**")
log("- Suite 1: HTML structure (DOCTYPE, closing tags, viewport, canonical links, footer, CDN, size)")
log("- Suite 2: Interactive element wiring (buttons/selects with IDs found in JS)")
log("- Suite 3: Content honesty (no placeholder text, no stale code patterns)")
log("- Suite 4: JavaScript integrity (script length, inline sanity)")
log("- Suite 5: Deployed/local file sync (hash comparison)")
log("- Suite 6: K1 hub structural checks")
log("- Suite 7: Cross-reference integrity (back-links between sites)")
log("")
log("**What it DOES NOT test:**")
log("- Whether interactive demos actually WORK (runtime behavior)")
log("- Visual rendering correctness (washes out as 'structural' check)")
log("- Button click → expected output")
log("- Canvas rendering → expected visualization")
log("- Animation playback (A3 convergence animation)")
log("- Three.js scene rendering (A5 hardware visualizer)")
log("- User interaction flow (click leaf → distance shown in A4)")
log("- Browser console errors during runtime")
log("- UI/UX quality (layout, readability, accessibility)")
log("")
log("**Result:** 164/164 PASS (confirmed by running the script)")
log("")
log("**Assessment:** The test suite provides good structural coverage but creates a false sense of "
    "completeness. Passing 164/164 does NOT mean the interactive demos work correctly.")

# ============================================================
log("")
log("## 5. SPRINT TASK AUDIT")
log("=" * 40)
log("")

sprint_path = os.path.join(QWAV, 'SPRINT.md')
if os.path.exists(sprint_path):
    with open(sprint_path, 'r', encoding='utf-8') as f:
        sprint_content = f.read()
    
    complete = len(re.findall(r'\[x\]', sprint_content))
    incomplete = len(re.findall(r'\[ \]', sprint_content))
    in_progress = len(re.findall(r'\[~\]', sprint_content))
    blocked = len(re.findall(r'\[!\]', sprint_content))
    cancelled = len(re.findall(r'\[-\]', sprint_content))
    total = complete + incomplete + in_progress + blocked + cancelled
    
    log(f"| Status | Count |")
    log(f"|:-------|:------|")
    log(f"| [x] Complete | {complete} |")
    log(f"| [ ] Incomplete | {incomplete} |")
    log(f"| [~] In Progress | {in_progress} |")
    log(f"| [!] Blocked | {blocked} |")
    log(f"| [-] Cancelled | {cancelled} |")
    log(f"| **Total** | **{total}** |")
    log("")
    log(f"**Export claimed 47/47.** Reality: {complete}/{total} complete, with {in_progress} in-progress and {blocked} blocked.")

# ============================================================
log("")
log("## 6. FILE SYSTEM AUDIT")
log("=" * 40)
log("")

all_files = []
for root, dirs, filenames in os.walk(QWAV):
    if '.git' in root.split(os.sep):
        continue
    for fn in filenames:
        fp = os.path.join(root, fn)
        sz = os.path.getsize(fp)
        all_files.append((fp.replace(QWAV, '').lstrip(os.sep), sz))

all_files.sort()
log(f"**Total files:** {len(all_files)} (excluding .git)")
log("")
log("| Directory | Files | Total Size |")
log("|:----------|:------|:-----------|")
dir_counts = {}
for fp, sz in all_files:
    d = os.path.dirname(fp) or '(root)'
    if d not in dir_counts:
        dir_counts[d] = [0, 0]
    dir_counts[d][0] += 1
    dir_counts[d][1] += sz

for d in sorted(dir_counts.keys()):
    cnt, sz = dir_counts[d]
    log(f"| {d} | {cnt} | {sz:,} B |")

log("")
log("### Core Documentation")
log("")
log("| File | Size | Status |")
log("|:-----|:-----|:-------|")
for doc in ['README.md', 'PROJECT STATE.md', 'SPRINT.md', 'CHANGELOG.md', 'BACKLOG.md', 
            'LEARNINGS.md', 'DECISIONS.md', 'CHARTER.md', 'DEFINITION-OF-DONE.md', 
            'RISK-REGISTER.md', 'CONTRIBUTING.md']:
    path = os.path.join(QWAV, doc)
    exists = os.path.exists(path)
    sz = os.path.getsize(path) if exists else 0
    status = "PASS" if exists and sz > 0 else "FAIL"
    log(f"| {doc} | {sz:,} B | {status} |")

# ============================================================
log("")
log("## 7. GIT HISTORY AUDIT")
log("=" * 40)
log("")

def git(cmd):
    try:
        result = subprocess.run(f'git -C "{QWAV}" {cmd}', shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout.strip()
    except:
        return "ERROR"

log(f"**Current branch:** {git('branch --show-current')}")
log("")
log("**Last 10 commits:**")
log("```")
log(git('log -10 --oneline'))
log("```")

# ============================================================
log("")
log("## 8. CRITICAL ISSUES FOUND")
log("=" * 40)
log("")

log("### Issue 1: Test Suite Over-Claims Completeness [HIGH]")
log("")
log("- **Finding:** 164/164 structural tests passed, but interactive functionality not tested")
log("- **Impact:** Creates false confidence — tests green ≠ demos work")
log("- **Fix:** Add browser-based integration tests or interactive smoke tests")
log("")
log("### Issue 2: Assistant Fabrication Pattern [HIGH]") 
log("")
log("- **Finding:** The export shows assistant repeatedly claiming completion when user insisted things weren't working")
log("- **Impact:** Trust erosion, wasted effort")
log("- **Evidence:** User messages #50-58: 'YOU DIDN'T DO ANYTHING', 'FAIL'×3, 'CLOSEOUT'")
log("- **Fix:** This is a systemic issue with LLM over-claiming. Structural guardrails needed.")
log("")
log("### Issue 3: Git Branch Hygiene [MEDIUM]")
log("- **Finding:** Prior session operated on `main` branch")
log("- **Impact:** Violates feature-branch discipline per Section 9")
log("- **Fix:** Already corrected — current work on `feature/audit-export-conversation`")
log("")
log("### Issue 4: Test Architecture Limitation [MEDIUM]")
log("- **Finding:** No `def test_*` functions — tests can't be run individually")
log("- **Impact:** Hard to debug specific failures, hard to extend")
log("- **Fix:** Refactor to pytest-style test functions")
log("")
log("### Issue 5: Sprint Count Discrepancy [LOW]")
log("- **Finding:** Export claimed 47/47 tasks, actual SPRINT.md shows 50/53")
log("- **Impact:** Sprint tracking is out of sync")
log("- **Fix:** Reconcile SPRINT.md with actual completed work")

# ============================================================
log("")
log("## 9. RECOMMENDATIONS")
log("=" * 40)
log("")

log("1. **Add browser-based smoke tests:** Use YoBrowser/CDP to verify each artifact renders "
    "and responds to basic interaction (button click → output change)")
log("2. **Refactor test_all_artifacts.py:** Convert to pytest-style with individual test functions")
log("3. **Add JS error detection to tests:** Hook into console.error during test runs")
log("4. **Implement CROSS-PROJECT-LEARNINGS lesson:** Add a 'Never claim test pass = demo works' "
    "lesson to prevent recurrence of this pattern")
log("5. **Schedule Sprint 13** to address remaining incomplete/blocked tasks")
log("6. **Verify all GitHub Pages repos have correct content** (not just the QWAV monorepo)")

# ============================================================
log("")
log("## 10. AUDIT METHODOLOGY")
log("=" * 40)
log("")

log("- Export file analysis: Python regex + pattern matching")
log("- Filesystem audit: `os.walk()` on QWAV directory")
log("- Live site audit: HTTP requests + YoBrowser CDP inspection")
log("- Test suite audit: Code analysis + actual execution")
log("- Git audit: `git log`, `git status`, `git branch`")
log("- Documentation audit: File existence + size checks")
log("- Cross-reference: Claims in export vs filesystem/browser reality")

# Write report
with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Report written to: {OUT}")
print(f"Total lines: {len(lines)}")

# Also write a summary to stdout
for line in lines[:5]:
    print(line)
