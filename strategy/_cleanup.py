"""
Brutal cleanup: collapse G:\My Drive\Patents\ from 6 confusing categories
down to ONLY what actually matters for QWAV IP.

Survivors: Only High-Temperature Topological Chiral (the one filing-ready package).
Everything else goes to Archive or gets deleted.
"""
import os, sys, shutil, subprocess

sys.stdout.reconfigure(line_buffering=True) if hasattr(sys.stdout, 'reconfigure') else None

PATENTS = r"G:\My Drive\Patents"
ARCHIVE = r"G:\My Drive\Archive\Patents"

def count_files(d):
    if not os.path.isdir(d): return 0
    return sum(1 for r,dd,f in os.walk(d) for _ in f)

def robocopy(src, dst):
    result = subprocess.run(
        ['robocopy', src, dst, '/E', '/COPY:DAT', '/R:0', '/W:0', '/NP', '/NFL', '/NDL'],
        capture_output=True, text=True, timeout=300
    )
    return result.returncode < 8

def archive_dir(src_name, archive_subdir, reason=""):
    """Move a directory from Patents to Archive."""
    src = os.path.join(PATENTS, src_name)
    dst = os.path.join(ARCHIVE, archive_subdir, src_name)
    if os.path.isdir(src):
        n = count_files(src)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if robocopy(src, dst):
            dst_n = count_files(dst)
            if dst_n >= n:
                shutil.rmtree(src)
                print(f"  MOVED: {src_name} -> Archive/{archive_subdir} ({n} files, {reason})")
            else:
                print(f"  PARTIAL: {src_name} ({dst_n}/{n} copied)")
        else:
            print(f"  COPY FAILED: {src_name}")
    else:
        print(f"  GONE: {src_name}")

print("=" * 60)
print("BRUTAL PATENTS CLEANUP")
print("=" * 60)
print()
print("KILL LIST:")
print("  02_DEVELOP/ — 348 files, no claims, not being developed")
print("  03_QWAV_FOUNDATIONS/ — wrong math (prime factorization, not p-adic)")
print("  04_TEMPLATES/ — USPTO garbage, not QWAV IP")
print("  05_REFERENCES/ — empty, useless")
print("  06_TBD/ — reference papers, not IP")
print()
print("SURVIVORS:")
print("  01_FILING_READY/High_Temperature_Topological_Chiral/ — 20 files")
print("  README.md")
print()

# Archive 02_DEVELOP contents
archive_dir("02_DEVELOP", "02_Former_Develop", "No claims, not being developed, not core QWAV IP")

# Archive 03_QWAV_FOUNDATIONS (Number-Theoretic = wrong math)
archive_dir("03_QWAV_FOUNDATIONS", "03_Former_Foundations", "Prime factorization math, not p-adic/ultrametric")

# Archive 04_TEMPLATES
archive_dir("04_TEMPLATES", "04_Former_Templates", "USPTO boilerplate, not QWAV IP")

# Archive 06_TBD (Bi-2212 papers)
archive_dir("06_TBD", "06_Former_TBD", "Reference papers, not IP")

# Remove empty dirs
for d in ["02_DEVELOP", "03_QWAV_FOUNDATIONS", "04_TEMPLATES", "05_REFERENCES", "06_TBD"]:
    dp = os.path.join(PATENTS, d)
    if os.path.isdir(dp):
        try:
            remaining = os.listdir(dp)
            if not remaining:
                os.rmdir(dp)
                print(f"  REMOVED DIR: {d}/")
            else:
                print(f"  DIR NOT EMPTY: {d}/ ({remaining})")
        except:
            pass

# Rename 01_FILING_READY to just the package name at root level
filing_ready = os.path.join(PATENTS, "01_FILING_READY")
if os.path.isdir(filing_ready):
    for item in os.listdir(filing_ready):
        src = os.path.join(filing_ready, item)
        dst = os.path.join(PATENTS, item)
        if os.path.isdir(src):
            if not os.path.exists(dst):
                shutil.move(src, dst)
                print(f"  MOVED TO ROOT: {item}/")
            else:
                print(f"  ALREADY EXISTS: {item}")
    # Remove empty 01_FILING_READY
    try:
        remaining = os.listdir(filing_ready)
        if not remaining:
            os.rmdir(filing_ready)
            print(f"  REMOVED DIR: 01_FILING_READY/")
    except:
        pass

# Write brutally honest README
readme = []
readme.append("# QWAV Patent Portfolio")
readme.append("")
readme.append("**One package. That's it.**")
readme.append("")
readme.append("## Active")
readme.append("")
readme.append("### High_Temperature_Topological_Chiral/")
readme.append("- **What:** $45^\\circ$ twisted Bi-2212 bilayer superconductor, chiral $d+id'$ phase, $\\Delta \\approx 25$ meV gap, Majorana zero modes, 4K operation.")
readme.append("- **Claims:** 12 drafted (apparatus: device, materials, tunnel barrier, substrate, seed layer)")
readme.append("- **QWAV match:** Exact — the Technical Deep-Dive predicts this specific hardware.")
readme.append("- **Filing cost:** ~$325 (US provisional, micro-entity)")
readme.append("- **Conversion probability:** 5.1% (depends entirely on VSD/FRO/EWOR)")
readme.append("- **Expected net value:** -$453 to +$59 (quantitative model)")
readme.append("- **Verdict:** File ONLY if $325 is disposable AND you need priority-date hedge.")
readme.append("")
readme.append("## Not Here (Archived)")
readme.append("")
readme.append("770 files across 15 categories archived to `G:\\My Drive\\Archive\\Patents\\`.")
readme.append("")
readme.append("| What Was Archived | Why |")
readme.append("|:-------------------|:----|")
readme.append("| Number-Theoretic Pattern Operations | Wrong math — prime factorization, not p-adic |")
readme.append("| Topological Computing Systems | Redundant with High-Temp, undeveloped Kitaev/FCI claims |")
readme.append("| 63940352 Quantum Computing | Mostly bio-inspired/liquid helium, twistronic sub-package has no claims |")
readme.append("| 2025-12-02 Quantum Info | Materials fabrication, not core QWAV IP |")
readme.append("| Photonic Computing (142 files) | Different paradigm entirely |")
readme.append("| QRC + QRC-PPA | Earlier concept, superseded |")
readme.append("| ~10 other packages | Dead, undeveloped, or off-path |")
readme.append("| Templates, guides, ADS generators | USPTO boilerplate — not QWAV IP |")
readme.append("| Bi-2212 reference papers | Reference materials, not patents |")
readme.append("")
readme.append("## Not Here (QWAV Project)")
readme.append("")
readme.append("| What | Where | Status |")
readme.append("|:-----|:------|:-------|")
readme.append("| Ultrametric Encoding Provisional | `QWAV/strategy/0.1.md` | 17 claims drafted. NOT FILED. No conversion plan. |")
readme.append("| Bruhat-Tits Processor files | `QWAV/` git repo | Recovered p-adic math. Research, not patents. |")
readme.append("| Morita Gamma, Invariant Geometric Structure | `QWAV/` git repo | Recovered research. Not patents. |")
readme.append("")
readme.append("## The Rule")
readme.append("")
readme.append("**DO NOT FILE unless you can answer \"How will I fund non-provisional conversion within 12 months?\" with a specific dollar amount and source.**")
readme.append("")
readme.append("This rule would have saved $6,000 on 18 expired provisionals with zero conversions.")

with open(os.path.join(PATENTS, "README.md"), 'w', encoding='utf-8') as f:
    f.write('\n'.join(readme))
print("  README written.")

# Final summary
print()
print("=" * 60)
print("CLEANUP COMPLETE")
print("=" * 60)
print()
print("SURVIVORS:")
for item in sorted(os.listdir(PATENTS)):
    ip = os.path.join(PATENTS, item)
    if os.path.isdir(ip) and item != '01_FILING_READY' and item != '02_DEVELOP':
        n = count_files(ip)
        print(f"  {item}/ — {n} files")
    elif not os.path.isdir(ip):
        print(f"  {item}")
print()
print("That's the QWAV patent portfolio. One package. File it or don't.")
