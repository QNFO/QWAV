# QNFO/QWAV Decision Log

> Unified decision record for all QNFO and QWAV projects.
> Maintained by: github-sync Worker + agent session closeouts.
> Last updated: 2026-05-28 (Session: F12 Encoding Fix + Discovery Index Rebuild)

---

## 2026-05-28 — F12 Encoding Fix & Discovery Index Rebuild

### Decision: F12 wrangler encoding fix → shared utility module (RESOLVED)

**Status:** Implemented
**Context:** Decision log v1 documented F12 (wrangler Unicode box-drawing chars crash Python subprocess on Windows). Fix was known (`encoding='utf-8', errors='replace'`) but not centralized. H1 (R2 Content Pipeline) was blocked waiting for the fix.

**Implementation:**
- `G:/My Drive/QWAV/tools/wrangler_utils.py` — canonical wrangler subprocess wrapper with encoding fix built in. Provides `run_wrangler()`, `upload_to_r2()`, `get_r2_object()`.
- Shell=True on Windows for npx.cmd resolution.
- `--remote` flag confirmed STILL REQUIRED in wrangler v4.95+.
- cloudflare-deployer skill updated to v2.0 with F12 documentation.
- All 7 existing scripts audited — all already had the encoding fix applied individually. The utility ensures future scripts inherit it.
- qwav-papers state updated: blocker removed, H1 re-delegated with encoding fix available.

### Decision: Discovery Index rebuilt from filesystem

**Status:** Implemented
**Context:** On session startup, `qnfo/discovery/index.json` was empty (corrupted or never populated). R2 had zero audit objects.

**Implementation:**
- Scanned all 24 project directories + 9 archived projects from local filesystem
- Rebuilt index with topics mapping, git status, README presence
- Uploaded to R2 `qnfo/discovery/index.json`
- Bootstrapped R2 audit trail: `qnfo/audit/state/qwav-papers.json`, `qnfo/audit/decisions/DECISION-LOG.md`

**Key finding:** Obsidian releases directory only contains 1 file (not 650 as H1 states). The H1 handoff references `G:/My Drive/Obsidian/releases/` with 650 files, but the actual directory has been reduced/cleaned. H1 scope may need revision.

---

## 2026-05-27 â€” Cloudflare Audit Trail Implementation (Session 2)

### Decision: Build complete reusable automation layer for Cloudflare operations

**Status:** Implemented
**Context:** After building the R2 audit trail infrastructure and cron worker, the user requested reusable instructions/code/scripting that DeepChat agents can execute autonomously â€” "invisible to end user, always there."

**Implementation:**
- cloudflare-deployer skill v2.0: Complete rewrite (3,116 â†’ 16,054 bytes). Covers Workers (cron + HTTP), R2, Vectorize, secrets, DNS via REST API, bulk redirects. 10 failure modes documented. Python Worker quirks (Object.fromEntries, --remote flag, compatibility_flags).
- closeout-manager skill v2.0: Added mandatory R2 audit trail export + decision log update.
- REBUILD-FROM-SCRATCH.md (11,885 bytes): Idiot-proof crash recovery. Covers installation, authentication, cloning, deploying all workers, recreating R2 structure, verification.
- CLOUDFLARE-AUDIT-EXPORT template: Structured session export format for R2.
- DEFAULT.md Â§10: Closeout now references CLOUDFLARE-AUDIT-EXPORT template, cloudflare-deployer v2.0 skill, closeout-manager v2.0 skill, and REBUILD-FROM-SCRATCH.md.

### Decision: System reload required for new templates to activate

**Status:** Discovered (F11)
**Context:** CLOUDFLARE-AUDIT-EXPORT is correctly registered in prompts.json (29 entries, verified on disk) but `list_all_prompt_template_names()` does not include it. The runtime system caches the pre-rebuild template list.
**Impact:** Agents cannot use `fill_prompt_template("CLOUDFLARE-AUDIT-EXPORT")` until DeepChat restarts. Manual wrangler commands from DEFAULT.md Â§10 are the fallback.
**Mitigation:** Documented in REBUILD-FROM-SCRATCH.md (added after discovery).

### Decision: wrangler Unicode output crashes Python subprocess on Windows (F12)

**Status:** Discovered (2026-05-27)
**Context:** wrangler terminal output contains Unicode box-drawing characters (U+2500-U+257F) that cause UnicodeEncodeError when captured via Python subprocess with cp1252 encoding.
**Fix:** Use `encoding='utf-8', errors='replace'` or `text=False` + manual decode. Documented in cloudflare-deployer skill failure catalog.

### Decision: GitHub API returns HTTP 200 with empty array for flagged/blocked orgs (F13)

**Status:** Discovered (2026-05-27)
**Context:** qnfo/QWAV returns HTTP 200 with `[]` instead of an error when the QNFO org is flagged. Worker reports `count=0` which is indistinguishable from a repo with zero issues.
**Mitigation:** Documented as GitHub quirk. Worker handles gracefully.

---

## 2026-05-27 â€” Cloudflare Audit Trail Infrastructure (Session 1)

### Decision: Cloudflare is the distribution + survivability layer, not the development platform

**Status:** Accepted
**Context:** After completing Phase 1 Cloudflare migration (14 domains, 4 Pages sites, DNS, bulk redirects, $0/month), user requested migration of "everything" to Cloudflare. Full capability assessment performed.

**Rationale:**
- Cloudflare Workers cannot run git, provide a filesystem, or execute subprocesses
- Agent runtime requires local filesystem + git + Python with full stdlib
- Cloudflare Pages, R2, Vectorize, and Workers are ideal for: static hosting, DNS, object storage, semantic search, cron jobs, email processing
- GitHub remains the primary development platform (git, Issues, Projects, Wiki)
- Google Drive remains the working directory for agent runtime

**Architecture:**
- Cloudflare = Distribution layer (Pages, DNS, R2 archive, Workers, Vectorize)
- GitHub = Development layer (git, Issues, Projects, Wiki, Discussions)
- Local = Agent runtime (DeepChat, DeepSeek API, Python, git, PowerShell)

### Decision: Build unified audit trail on Cloudflare R2 + Vectorize

**Status:** Implemented (Phase 1)
**Context:** Need LLM-accessible documentation of every chat, project, decision, sprint, issue, backlog, and roadmap.

**Implementation:**
- R2 bucket (qnfo) with audit/ directory structure: conversations/, github/, decisions/, infrastructure/, wiki/
- github-sync Worker: daily cron (06:00 UTC) exports GitHub Issues to R2
- First export: rwnq8/prompts (33 issues, 151 KB)
- ask-qwav Worker: existing AI + Vectorize bindings, ready for semantic search
- Vectorize index (qwav-research): 768d cosine, ready for population

### Decision: Use gh auth token for Worker secrets

**Status:** Implemented
**Rationale:** Token has full scopes (repo, project, workflow, write:discussion). Set as Cloudflare secret via `wrangler secret put GITHUB_TOKEN`. Workers access via env.GITHUB_TOKEN.

### Decision: Python Workers require Object.fromEntries() for fetch options

**Status:** Discovered (2026-05-27)
**Context:** Initial worker code used Python dicts for fetch headers. This worked for the HTTP 200 response but R2 writes failed silently.
**Fix:** Use Object.fromEntries() to create JS objects from Python tuples for all fetch options and Response headers.

### Decision: wrangler r2 object commands default to local mode

**Status:** Discovered (2026-05-27)
**Context:** `wrangler r2 object get` without --remote returns "The specified key does not exist" even when files are present.
**Fix:** Always use --remote flag for R2 object get/delete operations. Put operations work in local mode but get/delete need --remote.

---

## 2026-05-27 â€” Phase 1 Cloudflare Migration (Earlier Session)

### Decision: qnfo.org is the platform root

**Status:** Accepted, partially implemented
**Source:** CLOUDFLARE-CLOSEOUT-2026-05-27.md

### Decision: No new domains â€” 14 existing sufficient

**Status:** Decided, no domains purchased
**Source:** CLOUDFLARE-CLOSEOUT-2026-05-27.md

### Decision: PM Strategy â€” Hybrid GitHub (live) + Cloudflare (mirror)

**Status:** Strategy decided, mirror partially built
**Source:** CLOUDFLARE-CLOSEOUT-2026-05-27.md

### Decision: rwnq8 repos stay on GitHub (for now)

**Status:** Accepted
**Source:** CLOUDFLARE-CLOSEOUT-2026-05-27.md

---

*Decision log format: ISO 8601 dates, status tracking, rationale, source traceability.*


---
## 2026-05-28 -- Deep-Dive Audit Remediation (QWAV Program Agent)

### ADR-002: Cloudflare-Native PM -- R2 State as PRIMARY, GitHub as FALLBACK
**Context:** QNFO org is flagged by GitHub. QWAV-DEFAULT.md had internal contradictions.
**Decision:** GitHub = source control + FALLBACK issue tracking. PRIMARY PM operations use R2 via wrangler per-object get/put/delete.
**Consequences:** All project state, backlogs, decisions, and deployments tracked in R2. GitHub Issues referenced only as fallback.

### ADR-003: wrangler v4.95+ Compatibility -- Per-Object Operations
**Context:** wrangler v4.95 removed r2 object list. QWAV-DEFAULT.md had 7 references to the removed command.
**Decision:** Replace all r2 object list with per-object get operations. Remove --remote flags.
**Consequences:** Startup checklist now uses per-project get commands. No enumeration until Worker deployed (P2.1).

### ADR-004: On-Demand Skills for Workflow Documentation
**Context:** DEFAULT.md trimmed from 177K to 13K by moving ~150K into on-demand skills, but the 7 skills were never created.
**Decision:** Create all 7 skills as SKILL.md files (~22K chars total). Each consolidates existing content from templates/, email/, and old DEFAULT.md.
**Consequences:** ~150K of operational knowledge restored with zero prompt bloat. Skills load on-demand via skill_view().

### ADR-005: Subagent v1.2 Files with v1.1 System Embeddings
**Context:** Subagent .md files are v1.2 (with DoD + Self-Verification gates) but subagent_orchestrator embeds v1.1 definitions.
**Decision:** Added slot IDs to DEFAULT.md section 5. Manual update required in DeepChat UI.
**Consequences:** Running subagents miss DoD + self-verification gates until UI updated. P1.2 pending item.

---

## 2026-05-28 — QWAV Directory Cleanup & Architecture (Session 2)

### ADR-006: QWAV as Pure Program Management Hub — Zero Project Content

**Status:** Implemented
**Context:** QWAV directory had 700+ files — project source code, paper HTML, build artifacts, personal documents — all mixed with program management files. LLM agents couldn't discover what existed.

**Decision:** QWAV directory contains ONLY program management files. All project code, content, build artifacts, and personal files evicted to dedicated repos or Cloudflare deployments.

**Result:** 700+ files → 214 files (69% reduction). 539 papers → rwnq8/qwav-papers. 5 demos → individual rwnq8/* repos. Every remaining file documented in FILE-MANAGEMENT-STRATEGY.md.

### ADR-007: llms.txt Hierarchy as Unified LLM Discovery Architecture

**Status:** Implemented
**Context:** LLM agents need to discover all program content without knowing what exists. User requirement: "UNIFIED WAY OF ACCESSING INFORMATION FOR LLM DUE-DILIGENCE/DISCOVERY."

**Decision:** Every content directory must contain an llms.txt file. Root llms.txt provides entry point. Auto-generated by enforce-structure.py --fix. 39 files deployed across all directories.

### ADR-008: Self-Enforcing File Management via Local Pre-Commit Hook

**Status:** Implemented
**Context:** Without enforcement, QWAV directory will become a dumping ground again. User requirement: "ENFORCEMENT WITHOUT MANUAL USER INTERVENTION."

**Decision:** 7-rule enforcement system runs on every git commit via local pre-commit hook. No GitHub Actions. Cloudflare-native. scripts/enforce-structure.py validates whitelist, extensions, llms.txt, sizes, links, orphans.

### Decision: GitHub Actions Fully Deprecated — Cloudflare-Native Only

**Status:** Implemented
**Context:** ADR-002 deprecated GitHub for non-git functions. GitHub Actions workflow deleted per user directive: "GITHUB IS DEPRECATED. USE CLOUDFLARE INSTEAD."

### Decision: All 16 Handoffs as Standalone Projects in projects/ Directory

**Status:** Implemented
**Context:** Handoff specs were buried in briefings/handoffs/. User required: "ALL HANDOFFS SHOULD BE SEPARATE PROJECTS IN PROJECTS DIRECTORY."

**Result:** 16 project directories (7 active Phase 3 + 9 legacy Phase 4/5), each with README.md + SPEC.md. briefings/handoffs/ deleted. HANDOFF-TRACKER.md at briefings/.

### Decision: Papers and Artifacts to Dedicated Repos, Not QWAV

**Status:** Implemented
**Context:** Papers (539 HTML) and artifacts (5 demos) had no defined home. User requirement: "EVERYTHING SHOULD HAVE A DEFINED HOME, PREFERABLY ON CLOUDFLARE."

**Result:** 6 repos created: rwnq8/qwav-papers + 5 rwnq8/artifact-* repos. All deployed/served from Cloudflare Pages.