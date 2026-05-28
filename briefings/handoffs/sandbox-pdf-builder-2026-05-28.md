# HANDOFF: Cloudflare Sandbox PDF Builder — Replace GitHub Actions

> **Type:** Program → Project  
> **Date:** 2026-05-28  
> **Priority:** 🔴 P0 — GitHub Actions blocked by QNFO flagging. No PDF builds possible.  
> **Sessions:** 1  
> **Phase:** 3 (Enhancement) — P3.3  
> **Cross-Reference:** Cloudflare Audit §1.1 (C3: Sandboxes), §7 Action #1; Master Strategy P3.3

---

## SCOPE

GitHub Actions can no longer build PDFs from QWAV's LaTeX papers because the QNFO organization is flagged. Cloudflare Sandboxes (GA since April 2026) provide persistent Linux VMs that can run `pdflatex`, `bibtex`, and any build toolchain. This handoff creates a Sandbox-based PDF build pipeline that replaces the blocked GitHub Actions.

**What the Projects Agent should produce:**

1. A Cloudflare Sandbox configured with:
   - Full TeX Live installation (`apt install texlive-full` or minimal `texlive-latex-base texlive-latex-recommended texlive-latex-extra`)
   - Git installed
   - Python 3 + any QWAV build scripts
   - A build script (`build.sh`) that:
     - Clones the target repo from GitHub (rwnq8/ or QNFO/)
     - Runs `pdflatex` + `bibtex` + `pdflatex` × 2
     - Uploads the resulting PDF to R2 (`qnfo/releases/<paper-name>.pdf`)
     - Reports success/failure

2. A trigger mechanism (one of):
   - **Option A (recommended):** A Worker endpoint that accepts a webhook → triggers Sandbox build via API
   - **Option B:** Manual trigger via `wrangler sandbox exec`
   - **Option C:** Cron-based periodic rebuild of all papers

3. Documentation: README.md in the Sandbox or a `build-pdf` repo explaining:
   - How to trigger a build
   - How to add a new paper to the build list
   - How to check build status
   - Cost estimate (Sandbox minutes per build)

## SUCCESS CRITERIA

- [ ] Sandbox created and accessible via `wrangler sandbox list`
- [ ] TeX Live installed and `pdflatex --version` works
- [ ] At least ONE QWAV paper builds successfully from source → PDF produced
- [ ] PDF uploaded to R2 `qnfo/releases/` and verified via `wrangler r2 object get`
- [ ] Build completes in < 5 minutes per paper
- [ ] Build script is idempotent (running twice produces same result)
- [ ] Cost per build < $0.02 (Sandbox at $0.002/min × ~10 min max)

## CONSTRAINTS

- **Sandbox GA (free quota):** Use the free tier Sandbox quota first. Monitor minutes.
- **R2 bucket:** Use existing `qnfo` bucket, path `qnfo/releases/`. Do NOT create a new bucket.
- **No GitHub Actions dependency:** The Sandbox must clone from git (GitHub) but NOT depend on GitHub Actions for anything.
- **Git hygiene:** Store build scripts in a repo (`rwnq8/pdf-builder` or similar). Not just in the Sandbox filesystem.
- **Reproducibility:** Builds must be deterministic. Pin TeX Live version if possible.

## RESEARCH TRAIL

| File / Resource | Purpose |
|:----------------|:--------|
| `G:\My Drive\QWAV\briefings\platform\cloudflare-comprehensive-audit-2026-05-28.md` §1.1 C3 | Sandboxes capability, pricing, use cases |
| `G:\My Drive\QWAV\archive\cloudflare-master-strategy-2026-05-27.md` P3.3 | Original spec for PDF builder |
| `G:\My Drive\QWAV\PROGRAM-STATE.md` | Current infrastructure state, Sandboxes section |
| Cloudflare Docs: [Sandboxes](https://developers.cloudflare.com/sandboxes/) | API reference, wrangler commands |
| `wrangler sandbox list` | Check if any sandboxes already exist |
| `wrangler r2 object list qnfo/releases/ --remote` | Check existing release PDFs |
| GitHub: QNFO org repos | Source LaTeX files for papers (may need rwnq8/ mirrors if QNFO is flagged) |

### Key wrangler Commands

```bash
# Create sandbox
npx wrangler sandbox create pdf-builder --image ubuntu-22.04

# Execute commands
npx wrangler sandbox exec pdf-builder -- "apt-get update && apt-get install -y texlive-latex-base texlive-latex-recommended texlive-latex-extra git"

# Run build script
npx wrangler sandbox exec pdf-builder -- "bash /build.sh"

# List sandboxes
npx wrangler sandbox list

# Check status
npx wrangler sandbox exec pdf-builder -- "ls -la /output/"
```

## RETURN PROTOCOL

1. Sandbox created and configured → `wrangler sandbox list` evidence
2. At least one paper built → PDF uploaded to R2 → `wrangler r2 object get qnfo/releases/<paper>.pdf --remote` evidence
3. Build script committed to git repo
4. Cost report: minutes used per build, projected monthly cost
5. Report back to Program Agent with: Sandbox name, build script repo, test results, any issues
6. Update PROGRAM-STATE.md Sandboxes row: `pdf-builder: ⬜ → ✅`

---

*Projects Agent: This unblocks the PDF pipeline that was killed by GitHub flagging. Every QWAV paper needs PDF builds for Zenodo DOI registration. This is the foundation for all future publication workflows.*
