# QWAV Repo Cleanup Audit — 2026-05-26

**Auditor:** Program Agent v2.0  
**Trigger:** Root and subdirectories cluttered despite prior refactor (commit 006a55f)  
**Prior refactor scope:** Only removed 9 deprecated PM stub files (SPRINT, BACKLOG, CHARTER, etc.)  
**This audit scope:** Full structural cleanup across all 123 files

---

## ZONE 1: ROOT-LEVEL CLUTTER — 10 misplaced files

Root should contain ONLY: `.gitignore`, `.nojekyll`, `README.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `index.html`, and directories.

| # | File | Problem | Remediation |
|:--|:-----|:--------|:------------|
| 1 | `compile_audit.py` | Utility script at root | Move to `scripts/` |
| 2 | `conftest.py` | Pytest config at root | Move to `tests/` (new dir) |
| 3 | `test_all_artifacts.py` | Test at root | Move to `tests/` |
| 4 | `test_all_artifacts_pytest.py` | Test at root | Move to `tests/` |
| 5 | `test_browser_errors.py` | Test at root | Move to `tests/` |
| 6 | `test_plan.py` | Test at root | Move to `tests/` |
| 7 | `test_smoke.py` | Test at root | Move to `tests/` |
| 8 | `smoke_results.txt` | Test output at root | Move to `tests/` |
| 9 | `DEMO-AUDIT-REPORT.md` | Session artifact at root | Move to `sessions/2026/05/` |
| 10 | `FINAL_AUDIT_REPORT.md` | Session artifact at root | Move to `sessions/2026/05/` |

**Also:** `__pycache__/` and `.pytest_cache/` should be cleaned from disk (gitignored, but residual).

---

## ZONE 2: STRATEGY DIRECTORY — 29 files, severe version sprawl

### Versioned Drafts (14 files) — iterative refinement, now superseded by latest
| File | Estimated Status |
|:-----|:-----------------|
| `0.1.md` through `0.9.md` (9 files) | Early drafts — archive |
| `0.5.1.md`, `0.5.2.md` (2 files) | Point releases — archive |
| `0.4_linkedin.md`, `0.4_substack.md` (2 files) | Platform-specific variants of 0.4 — archive |
| `1.0.md`, `2.0.md`, `3.0.md` (3 files) | Major versions — keep 3.0.md as canonical |

### Named Strategy Documents (15 files) — mixed quality
| File | Category |
|:-----|:---------|
| `An Introvert's Deep-Tech Startup Path.md` | Personal narrative |
| `Experimental Validation Roadmap - Ultrametric Quantum Computing.md` | Technical strategy |
| `External Sources and Citation Map.md` | Reference |
| `Honest Investment Assessment - The 100K Question.md` | Fundraising strategy |
| `IP-Only Licensing Strategy - Strategy B CERN Model.md` | IP strategy |
| `ip-strategic-plan.md` | IP strategy (duplicate concern) |
| `mathematical-foundations.md` | Technical reference |
| `NEXT STEPS - From Library to Reality.md` | Action plan |
| `Pitch Deck - QWAV Ultrametric Computing.md` | Fundraising |
| `QA - Narrative Modules and Intellectual Defense.md` | Comms strategy |
| `src_fqxi_2026.md` | Grant application |
| `Technical Deep-Dive - Ultrametric Quantum Computing and AI.md` | Technical strategy |
| `VENUE-REGISTRY.md` | Reference |

**Remediation:** Archive all 0.x versions to `sessions/2026/05/strategy-archive/`. Keep 1.0–3.0 + named documents as active. Consider consolidating named documents into a canonical `STRATEGY.md`.

---

## ZONE 3: BRIEFINGS DIRECTORY — 34 files, 7+ categories mixed together

### Category Map

| Category | Files | Remediation |
|:---------|:------|:------------|
| **Handoffs (A1-A5)** | 5 files | Already completed — archive to `sessions/` |
| **Outreach Emails** | 9 files | Consolidate into `briefings/outreach/` subdir |
| **Platform/Docs** | 6 files (QNFO-README ×2, wiki-home, github-integration-plan, spinoff-registry, zenodo-crosslink) | Move to `briefings/platform/` |
| **Research Briefs** | 3 files (fqxi-briefing, sbir-phase1, P11*) | Move to `briefings/research/` |
| **Templates** | 3 files (lab-outreach-template, inbound-email-template, business-docs-template.tex) | Move to `briefings/templates/` |
| **Brand/Strategy** | 2 files (BRAND-STRATEGY, smoke-maintenance-protocol) | Keep in `briefings/` or move to `strategy/` |
| **Misc/Orphan** | 6 files (google-ai-studio-prompts, technical-site-sprint-plan, prior-work-catalog, release-v2.74-notes, rwnq8-profile-README, rwnq8-migrate-notice.b64.txt) | Categorize or archive |
| **Duplicate** | `QNFO-org-README.md` + `QNFO-org-README-v2.md` | Keep v2, archive v1 |

---

## ZONE 4: MINOR ISSUES

| Issue | Location | Remediation |
|:------|:---------|:------------|
| `site/__pycache__/` | `site/` | Clean from disk (gitignored) |
| `papers/QWAV System Instructions.txt` | `papers/` | Relocate or delete (not a paper) |
| `.nojekyll` at root | Root | Verify if needed (only if root is GitHub Pages source) |

---

## EXECUTION ORDER

1. **Root cleanup** (moves + cache purge) — SAFE, reversible via git
2. **Strategy archive** (move 0.x versions to sessions) — SAFE
3. **Briefings reorganization** (sort into subdirs) — requires file-by-file review
4. **Minor fixes** (papers txt, site cache)

**Total files affected:** ~55 moves/reorganizations across 123 total files.
