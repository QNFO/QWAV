# QWAV File Management Strategy — COMPREHENSIVE AUDIT 2026-05-28

> **Principle:** QWAV is the **Program Management Hub**. It coordinates. It does NOT store project code, build artifacts, content, or personal files. Every file must justify its presence by answering: "Does this serve program-level coordination, strategy, or identity?"

---

## FILE CLASSIFICATION LEGEND

| Tag | Meaning |
|:----|:--------|
| ✅ **KEEP** | Directly serves program management, strategy, identity, or landing page |
| ⚠️ **RELOCATE** | Useful but in wrong directory — move within QWAV to correct subdirectory |
| 🔄 **MIGRATE** | Belongs in a dedicated project repo, not QWAV program directory |
| 🗑️ **DELETE** | Redundant, obsolete, or one-off artifact no longer needed |
| ❓ **REVIEW** | Unclear purpose — needs human evaluation |

---

## 1. TOP-LEVEL FILES (13 files)

| File | Size | Classification | Rationale |
|:-----|:-----|:---------------|:----------|
| `.gitignore` | 0.3KB | ✅ KEEP | Git configuration for program repo |
| `.nojekyll` | 0KB | ✅ KEEP | Cloudflare Pages config — tells Pages this isn't Jekyll |
| `AUDIT-REPORT-2026-05-28.md` | 10KB | ⚠️ RELOCATE → `sessions/2026/05/` | Session output, not permanent program doc. Duplicates content in PROGRAM-STATE.md |
| `CODE_OF_CONDUCT.md` | 6KB | ✅ KEEP | Community governance — GitHub surfaces this |
| `CONTRIBUTING.md` | 3.6KB | ✅ KEEP | Contribution guidelines — GitHub surfaces this |
| `DIRECTORY-STRUCTURE.md` | 7.2KB | ⚠️ RELOCATE → `briefings/` | Reference doc for agents. Not needed at top level. README should summarize structure |
| `index.html` | 35KB | ✅ KEEP | Landing page for deep.qwav.tech — THE primary web asset |
| `LICENSE` | 9.9KB | ✅ KEEP | Legal — GitHub requires this |
| `llms.txt` | 2.4KB | ✅ KEEP | LLM-friendly site index — served by deep.qwav.tech for AI crawlers |
| `PROGRAM-STATE.md` | 8.5KB | ✅ KEEP | CANONICAL program state — THE most important file in this directory |
| `README.md` | 10.1KB | ✅ KEEP | Portfolio identity — GitHub surfaces this as repo homepage |
| `robots.txt` | 0.4KB | ✅ KEEP | SEO — served by deep.qwav.tech |
| `sitemap.xml` | 92.6KB | ✅ KEEP | SEO — served by deep.qwav.tech |

**Top-level verdict:** 9 keep, 2 relocate, 0 delete. Clean. The 2 audit/docs should move to subdirectories.

---

## 2. `.github/` (6 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `ISSUE_TEMPLATE/bug_report.md` | ✅ KEEP | GitHub standard — program repo needs issue templates |
| `ISSUE_TEMPLATE/feature_request.md` | ✅ KEEP | GitHub standard |
| `ISSUE_TEMPLATE/research_proposal.md` | ✅ KEEP | GitHub standard |
| `PULL_REQUEST_TEMPLATE.md` | ✅ KEEP | GitHub standard |
| `workflows/build-pdfs.yml` | ❓ REVIEW | GitHub Actions workflow to build PDFs. Is this still active since GitHub Actions is deprecated in favor of Sandboxes? (#94) |
| `workflows/smoke-tests.yml` | ❓ REVIEW | Tests artifacts/ — if artifacts/ migrates out, this workflow should migrate with it |

**GitHub verdict:** 4 keep, 2 review. Workflows may be obsolete or tied to migrating content.

---

## 3. `archive/` (5 files — 740KB total)

| File | Size | Classification | Rationale |
|:-----|:-----|:---------------|:----------|
| `cloudflare-blue-sky-blueprint-2026-05-27.md` | 25.5KB | ⚠️ RELOCATE → `sessions/2026/05/` | Session output from Cloudflare strategy session. Belongs with other session records. |
| `cloudflare-closeout-2026-05-27.md` | 11.7KB | ⚠️ RELOCATE → `sessions/2026/05/` | Session closeout. |
| `cloudflare-master-strategy-2026-05-27.md` | 11.6KB | ⚠️ RELOCATE → `strategy/` or `sessions/2026/05/` | Strategy document. If canonical, belongs in strategy/. If session notes, in sessions/. |
| `cloudflare-poc-full-session-2026-05-27.md` | 658.7KB | ⚠️ RELOCATE → `sessions/2026/05/` | MASSIVE session log. Should be in sessions/, not consuming 659KB in a separate archive. |
| `cloudflare-poc-session-2026-05-27.md` | 30KB | ⚠️ RELOCATE → `sessions/2026/05/` | Session log. |

**Archive verdict:** 0 keep, 5 relocate. The entire `archive/` directory is redundant — these are session records that should live in `sessions/2026/05/`. After relocation, DELETE the `archive/` directory.

---

## 4. `artifacts/` (12 files — 5 Cloudflare Pages interactive demos)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `convergence-explorer/index.html` (7.5KB) + `.nojekyll` | 🔄 MIGRATE → own repo | Project source code, not program management. Should be in `qnfo/convergence-explorer` repo deployed to Cloudflare Pages. |
| `error-confinement-demo/index.html` (10.4KB) + `.nojekyll` | 🔄 MIGRATE → own repo | Same — `qnfo/error-confinement-demo` |
| `hardware-visualizer/index.html` (11.3KB) + `.nojekyll` + `three.module.js` + `controls/OrbitControls.js` (31KB) | 🔄 MIGRATE → own repo | Same — `qnfo/hardware-visualizer`. Has external dependency (three.js) |
| `qpna-playground/index.html` + `.nojekyll` | 🔄 MIGRATE → own repo | Same — `qnfo/qpna-playground` |
| `tree-distance/index.html` + `.nojekyll` | 🔄 MIGRATE → own repo | Same — `qnfo/tree-distance` |

**Artifacts verdict:** 0 keep, 5 migrate. These are PROJECT source code. QWAV is not a code repository. Each demo should be in its own `qnfo/<name>` repo with its own Cloudflare Pages deployment. The QWAV program directory should contain a REFERENCE to these repos, not their source code. **This is ~60KB of project code wrongly stored in the program directory.**

---

## 5. `papers/` (539 files — paper HTML pages)

| Count | Classification | Rationale |
|:------|:---------------|:----------|
| 539 HTML files | 🔄 MIGRATE → dedicated repo | These are CONTENT, not program management. They serve as paper pages on deep.qwav.tech/papers/. Two possibilities: (1) They are BUILD OUTPUT from paper ingestion scripts — if so, `.gitignore` them and deploy to Cloudflare Pages separately. (2) They are SOURCE CONTENT — if so, they belong in a dedicated `qnfo/qwav-papers` content repo. Either way, 539 HTML files do NOT belong in the program management directory. **This is the #1 bloat problem — the bulk of the 573 untracked files.** |

**Papers verdict:** 0 keep, 539 migrate. This is a content warehouse, not program management.

---

## 6. `projects/` (33 files — 16 handoff project specs)

| File(s) | Classification | Rationale |
|:--------|:---------------|:----------|
| `index.html` | ✅ KEEP | Project index page |
| 16 × `README.md` + 16 × `SPEC.md` | ✅ KEEP (for now) | Handoff specifications. These are program-level coordination documents — they tell Projects Agent what to build. When each project is initialized as a proper GitHub repo (per §0.9.1), the SPEC.md becomes the canonical source in that repo and the QWAV copy can be archived. |

**Projects verdict:** 33 keep. These ARE program management — they define what projects exist and what they should build. But the end-state is proper repo initialization, not perpetual storage in QWAV.

---

## 7. `strategy/` (13 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `1.0.md`, `2.0.md`, `3.0.md` | ✅ KEEP | Core strategy versions |
| `ACTION-PLAN.md` | ✅ KEEP | Program-level action plan |
| `FUNDRAISING.md` | ✅ KEEP | Fundraising strategy |
| `IP-STRATEGY.md` | ✅ KEEP | IP strategy |
| `VENUE-REGISTRY.md` | ✅ KEEP | Publication venue tracking |
| `External Sources and Citation Map.md` | ⚠️ RELOCATE → `briefings/research/` | Research artifact, not strategy |
| `QA - Narrative Modules and Intellectual Defense.md` | ✅ KEEP | Strategic Q&A |
| `MANUFACTURING-BLUEPRINT.md` | ❓ REVIEW | Is this strategy or a research deliverable? |
| `mathematical-foundations.md` | ⚠️ RELOCATE → `briefings/research/` | Research content, not strategy |
| `An Introvert's Deep-Tech Startup Path.md` | ❓ REVIEW | Personal essay — strategy or personal? |
| `Technical Deep-Dive - Ultrametric Quantum Computing and AI.md` | ⚠️ RELOCATE → `briefings/research/` | Research content, not strategy |

**Strategy verdict:** 6 keep, 3 relocate, 2 review. The strategy directory has become a catch-all for long-form documents. Pure strategy stays; research content moves to `briefings/research/`.

---

## 8. `briefings/` (22 files)

### Root-level briefings (6 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `HANDOFF-TRACKER.md` | ✅ KEEP | Program-level index of all 16 handoffs — essential |
| `BRAND-STRATEGY.md` | ⚠️ RELOCATE → `strategy/` | This is strategy, not a briefing |
| `google-ai-studio-prompts-qwav-marquee.md` | ❓ REVIEW | AI prompts. Program configuration or research? |
| `prior-work-catalog.md` | ✅ KEEP | Research reference catalog |
| `smoke-maintenance-protocol.md` | ⚠️ RELOCATE → `scripts/` or `briefings/platform/` | Operational, not briefing |
| `technical-site-sprint-plan.md` | ✅ KEEP | Sprint planning document |

### `briefings/platform/` (7 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `cloudflare-comprehensive-audit-2026-05-28.md` | ⚠️ RELOCATE → `sessions/2026/05/` | Session output, not permanent platform doc |
| `github-integration-plan.md` | ✅ KEEP | Platform documentation |
| `QNFO-org-README-v2.md` | ❓ REVIEW | Org-level documentation. Should this be in a qnfo/.github repo instead of QWAV? |
| `QWAV System Instructions.txt` | ❓ REVIEW | Unclear — system prompt? Agent instructions? |
| `spinoff-registry-artifacts.md` | ✅ KEEP | Platform documentation |
| `wiki-home.md` | ❓ REVIEW | Wiki content — should be in GitHub wiki, not briefings |
| `zenodo-crosslink-audit.md` | ⚠️ RELOCATE → `sessions/` | Session output |

### `briefings/research/` (6 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `ewor-assessment.md` | ✅ KEEP | Research assessment |
| `fqxi-briefing.md` | ✅ KEEP | Research briefing |
| `sbir-phase1-briefing.md` | ✅ KEEP | Research briefing |
| `src_fqxi_2026.md` | ✅ KEEP | Research source document |
| `P11 collaborator - Formal Verification Agenda (Shareable).docx` | ❓ REVIEW | Binary file. Should this be in a project repo? Also: .docx in a markdown repo is unusual. |
| `P11 Formal Verification Collaboration Briefing.md` | ✅ KEEP | Collaboration briefing |

### `briefings/templates/` (3 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `business-docs-template.tex` | ✅ KEEP | Document template |
| `inbound-email-template.md` | ✅ KEEP | Email template |
| `lab-outreach-template.md` | ✅ KEEP | Outreach template |

**Briefings verdict:** 14 keep, 4 relocate, 4 review. Briefings has accumulated session outputs and misplaced documents.

---

## 9. `scripts/` (15 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| `build_pdf.py` | ✅ KEEP | PDF builder — core program utility |
| `compile_audit.py` | ✅ KEEP | Audit compiler — program utility |
| `convert_wikilinks.py` | ✅ KEEP | Wiki link converter — program utility |
| `.cf-auth-config.ps1` | ✅ KEEP | Cloudflare auth helper |
| `cf-create-token.py` | ✅ KEEP | Cloudflare utility |
| `cf-dns-setup.py` | ✅ KEEP | Cloudflare utility |
| `cf-pages-domains.py` | ✅ KEEP | Cloudflare utility |
| `build-archive.py` | 🔄 MIGRATE — with papers/ | Tied to papers/ archive. If papers/ migrates out, this script goes with it. |
| `fix-ids.py` | 🔄 MIGRATE — with papers/ | Paper ID fixer. Tied to papers/. |
| `ingest-full.py` | 🔄 MIGRATE — with papers/ | Paper ingestion. Tied to papers/. |
| `ingest-papers.py` | 🔄 MIGRATE — with papers/ | Paper ingestion. Tied to papers/. |
| `ingest-v2.py` | 🔄 MIGRATE — with papers/ | Paper ingestion v2. Tied to papers/. |
| `test-r2-dl.py` | 🗑️ DELETE | One-off test. Already verified. |
| `test-vectorize.py` | 🗑️ DELETE | One-off test. Already verified. |
| `templates/archive-template.html` | 🔄 MIGRATE — with papers/ | Paper archive template. Tied to papers/. |

**Scripts verdict:** 7 keep, 6 migrate (tied to papers/), 2 delete. Scripts directory is cluttered with paper-ingestion utilities that belong with the papers content.

---

## 10. `sessions/` (37 files)

| File(s) | Classification | Rationale |
|:--------|:---------------|:----------|
| `README.md` | ✅ KEEP | Session directory documentation |
| `SESSION-HANDOFF-2026-05-27.md`, `SESSION-HANDOFF-2026-05-28.md`, `SESSION-CLOSEOUT-2026-05-28.md` | ✅ KEEP | Session handoff/closeout records |
| `cleanup-audit-2026-05-26.md` | ✅ KEEP | Session audit |
| `drafts-2026-05-26.md` | ✅ KEEP | Session drafts |
| `release-v2.74-notes.md` | ✅ KEEP | Release notes |
| `DEMO-AUDIT-REPORT.md` | ❓ REVIEW | Generic name. What demo? |
| `FINAL_AUDIT_REPORT.md` | ❓ REVIEW | Generic name. What audit? Rename descriptively. |
| `outreach-*.md` (7 files) | ⚠️ REVIEW | Outreach emails — contain PII (names, emails, institutions). Should these be in .gitignore? Some may already be. Need to verify. |
| `QNFO-org-README.md` | ❓ REVIEW | Duplicate of `briefings/platform/QNFO-org-README-v2.md`? |
| `rwnq8-migrate-notice.b64.txt` | 🗑️ DELETE | One-off migration artifact |
| `rwnq8-profile-README.md` | ❓ REVIEW | Personal profile — belongs in personal directory, not program |
| `strategy-archive/` (17 files: v0.1-v0.9 + pitch deck, investment assessment, etc.) | ⚠️ RELOCATE → `strategy/archive/` | Strategy drafts belong with strategy, not buried in sessions |

**Sessions verdict:** 12 keep, 7 review, 1 delete, 17 relocate. Sessions directory has accumulated non-session content.

---

## 11. `tests/` (9 files)

| File | Classification | Rationale |
|:-----|:---------------|:----------|
| All 6 test .py files + conftest + smoke_results.txt + __pycache__ | 🔄 MIGRATE — with artifacts/ | These test the 5 interactive demos in `artifacts/`. They are PROJECT tests, not program management tests. If artifacts/ migrates to dedicated repos, tests migrate with them. |

**Tests verdict:** 0 keep, 9 migrate. These test project code, not program management.

---

## SUMMARY — What Should Leave QWAV

| Category | Files | Action |
|:---------|:------|:-------|
| **papers/** | 539 HTML files | 🔄 Migrate to dedicated `qnfo/qwav-papers` repo or .gitignore as build output |
| **artifacts/** | 12 files (5 demos) | 🔄 Migrate each to own `qnfo/<name>` repo |
| **tests/** | 9 files | 🔄 Migrate with artifacts/ to respective project repos |
| **Paper scripts** | 6 files (build-archive, fix-ids, ingest-*, archive-template) | 🔄 Migrate with papers/ to dedicated repo |
| **archive/** | 5 files (740KB) | ⚠️ Relocate to sessions/2026/05/, then delete archive/ |
| **One-off scripts** | 2 files (test-r2-dl, test-vectorize) | 🗑️ Delete |
| **Session misc** | rwnq8-migrate-notice.b64.txt | 🗑️ Delete |
| **Strategy archive** | 17 files in sessions/ | ⚠️ Relocate to strategy/archive/ |

**Total to evict/migrate:** ~575 files (~568 from papers/ + artifacts + tests + scripts)
**Total to remain:** ~130 files (core program management)

---

## PROPOSED FILE MANAGEMENT STRATEGY

### QWAV's Role
QWAV is the **program management hub** for the QNFO research portfolio. It is NOT:
- ❌ A project code repository
- ❌ A content warehouse (papers)
- ❌ A build artifact store
- ❌ A personal filing cabinet

### What QWAV Contains
1. **IDENTITY** — README, LICENSE, CODE_OF_CONDUCT, CONTRIBUTING
2. **STATE** — PROGRAM-STATE.md (canonical)
3. **STRATEGY** — strategy/* (portfolio-level strategy + archive)
4. **BRIEFINGS** — briefings/* (research, platform docs, templates)
5. **COORDINATION** — HANDOFF-TRACKER.md, projects/* (handoff specs)
6. **HISTORY** — sessions/* (program agent session records)
7. **TOOLS** — scripts/* (program-level utilities only, not project-specific)
8. **WEB** — index.html, robots.txt, sitemap.xml, llms.txt (landing page)
9. **CONFIG** — .github/, .wrangler/, .gitignore, .nojekyll

### What Goes Elsewhere
| Content | Destination |
|:--------|:------------|
| Project source code | `qnfo/<project-name>` GitHub repo |
| Interactive demos (artifacts/) | Each in own `qnfo/<name>` repo → Cloudflare Pages |
| Paper HTML pages (papers/) | `qnfo/qwav-papers` repo → Cloudflare Pages |
| Project tests (tests/) | In respective project repos |
| Paper ingestion scripts | In `qnfo/qwav-papers` repo |
| Personal documents | `G:\My Drive\personal\` |
| Grant applications | `G:\My Drive\projects\applications\` |
| Outreach emails (PII) | .gitignored or in sessions/ with PII redacted |

### Directory Discipline Rules
1. **No loose files at top level** — everything in subdirectories (except required GitHub files)
2. **No project code in program directory** — projects get their own repos
3. **No build artifacts committed** — deployed to Cloudflare Pages/R2, not git
4. **Session outputs in sessions/** — not archive/, not briefings/, not top-level
5. **Strategy documents in strategy/** — not briefings/, not sessions/
6. **Research briefings in briefings/research/** — not strategy/
7. **Templates in briefings/templates/** — not scattered around
8. **One-off scripts deleted after use** — not accumulating in scripts/
