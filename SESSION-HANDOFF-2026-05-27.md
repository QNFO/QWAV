# Session Handoff — QWAV Cloudflare Migration Program

> **From:** Program Manager session 2026-05-27  
> **To:** Incoming Program Manager or Projects Agent  
> **Status:** Operational — 6 gaps to fix, then Phase 2 dispatch  
> **Read Time:** 5 minutes

---

## 0. CONTEXT — What Happened This Session

The QNFO organization was flagged by GitHub (QNFO/QWAV#62) — all 24 repos hidden, GitHub Pages blocked. We built a complete Cloudflare migration as risk mitigation. A Projects Agent proved Cloudflare viable by deploying 4 Pages sites, 1 Worker, 1 Vectorize index, and an R2 archive — all at $0/month. The full program strategy (Phases 1-4) is planned across 20 GitHub Issues.

### What's LIVE ($0/month)

| Asset | URL |
|:------|:----|
| Pages | primer.qwav.tech · deep.qwav.tech · archive.qnfo.org · veritatum.pages.dev |
| Worker | ask-qwav.q08.workers.dev (AI + Vectorize bindings) |
| Vectorize | qwav-research (768-dim, cosine, bge-base-en-v1.5 — ready, empty) |
| R2 | qnfo bucket (15 QNFO repos, ~85 MB) |
| DNS | 10 zones, 6 bulk redirects (754 visitors/month rescued) |
| Email | papers@qnfo.org · collab@qnfo.org |

### Architecture Decision

```
Platform root: qnfo.org (the research institute portal)
Program domain: qwav.tech (computing program, existing, unchanged)
14 domains owned — ZERO new domains needed. All on Cloudflare.
```

---

## 1. CRITICAL — Fix These TWO Gaps First (30 min)

The ecosystem was designed but the agent prompt files don't reflect it yet. A Projects agent starting up today CANNOT deploy to Cloudflare because the prompt doesn't know Cloudflare exists.

### GAP 1: PROJECTS-AGENT.md — Add Cloudflare Deployment Section

**File:** `G:\My Drive\prompts\agents\PROJECTS-AGENT.md`

**Current state:** §PUBLICATION only knows GitHub Pages + GitHub Releases. Zero Cloudflare awareness.

**Action:** Add a new section `§CLOUDFLARE-DEPLOYMENT` after the GitHub deployment section. The section must include:

1. **CLI reference:** `wrangler` commands (pages deploy, r2 object put, workers deploy, sandbox exec)
2. **Startup checklist:** `wrangler --version`, `wrangler whoami`, `wrangler pages project list`
3. **CNAME FIRST rule (BOLD):** Create CNAME DNS record BEFORE adding domain to Pages. Failure = HTTP 522. See failures F2/F3 catalogued in CLOUDFLARE-DEPLOYMENT v2.1.
4. **Cost gate:** Pages (500 builds/mo), R2 (10 GB), Workers (100k req/day), Sandboxes ($0.002/min)
5. **Deployment evidence:** After every deploy, log URL + cost to parent GitHub Issue via `gh issue comment`
6. **Failure catalog reference:** 6 documented failures with resolutions in `CLOUDFLARE-DEPLOYMENT.md`

**Template for the deployment section (paste into agent prompts):**
```
### §CLOUDFLARE-DEPLOYMENT — Cloudflare-Native Deployment & Hosting

Cloudflare is the PRIMARY deployment platform for all QWAV public-facing assets.
GitHub remains the git remote. All deployment uses `wrangler` CLI v3.0+.

Prerequisites (run at startup):
  wrangler --version              # Must be v3.0+
  wrangler whoami                 # Must be authenticated (CLOUDFLARE_API_TOKEN)
  wrangler pages project list     # Active deployments

Core commands:
  wrangler pages deploy --project-name <name> --branch main
  wrangler r2 object put <bucket>/path --file ./local/file.pdf
  wrangler deploy --name <worker-name>
  wrangler sandbox exec <name> -- "<command>"

⚠️ CNAME FIRST: Create CNAME DNS record before adding domain to Pages.
   Adding domain before CNAME → verification failure → HTTP 522.

Cost gate (free tier):
  Pages: 500 builds/mo | R2: 10 GB | Workers: 100k req/day | Sandboxes: $0.002/min

After every deployment, post evidence to parent GitHub Issue:
  gh issue comment <num> --repo QNFO/QWAV --body "## 🌐 Cloudflare Deploy
  | Field | Value | ..."

For full procedures (migration, bulk redirects, email routing, rollback):
  fill_prompt_template("CLOUDFLARE-DEPLOYMENT")

Reference: QNFO/QWAV#66 (Master Strategy) · CLOUDFLARE-DEPLOYMENT v2.1
  (rwnq8/prompts:templates/CLOUDFLARE-DEPLOYMENT.md)
```

### GAP 2: QWAV-DEFAULT.md — Add Master Strategy Reference

**File:** `G:\My Drive\prompts\QWAV-DEFAULT.md`

**Current state:** §0.6.7 (Cloudflare-Native Deployment) exists with auth fix, but NO reference to the Master Strategy.

**Action:** Add to §0.6.7, after "Deployable Template" line:

```
**Master Strategy:** QNFO/QWAV#66 — full Phase 1-4 plan with dependency graph,
monitoring framework, and cost projections. All Cloudflare sub-tasks (#67-#84)
are children of this issue. Coordinate deployments through #66.
```

Add to §H.1 (Semi-Autonomous Progression), after "Check GitHub Issues/Projects":

```
3.6. **Cloudflare health check:** `wrangler pages project list` + 
     `gh issue list --repo QNFO/QWAV --label "cloudflare-monitor"` for Phase 4 audit items
```

---

## 2. MEDIUM — Spin-Off Project Scaffolding (20 min)

Issues #81-#84 exist on GitHub but the local project directories with handoff files were never created on disk. A Projects agent can't discover the work without them.

**Create these directories with README.md + HANDOFF.md:**

| Issue | Directory | Content |
|:------|:----------|:--------|
| QNFO/QWAV#83 | `G:\My Drive\projects\google-site-auditor\` | Handoff: Audit qwav.tech, qnfo.org, q08.org for broken `qnfo.github.io` links. Report replacements. |
| QNFO/QWAV#84 | `G:\My Drive\projects\cf-dns-validator\` | Handoff: Verify 10 DNS zones resolve, 6 bulk redirects active, HTTPS on all Pages. |
| QNFO/QWAV#81 | `G:\My Drive\projects\cloudflare-pages-migration\` | Handoff: Migrate 8 remaining Pages sites (#67-#74). CNAME FIRST every time. |
| QNFO/QWAV#82 | `G:\My Drive\projects\pm-mirror-builder\` | Handoff: Archive full QNFO/QWAV issue list to archive.qnfo.org. Blocked by QNFO flagging. |

**Handoff template** (use for each directory):
```
# PROJECT HANDOFF: [Name]

Type: Program→Project
Parent: QNFO/QWAV#[num]
Status: Ready (or Blocked — explain)

## Scope
[What the Projects agent should produce]

## Success Criteria
1. [Measurable outcome]
2. [Measurable outcome]

## Constraints
- Cloudflare free tier only
- CNAME DNS record FIRST before adding domain to Pages (prevents HTTP 522)
- Do NOT delete original GitHub Pages until 24h after Cloudflare is verified

## Research Trail
- Read parent issue QNFO/QWAV#[num] for full context
- Read QNFO/QWAV#66 for master strategy
- Template: fill_prompt_template("CLOUDFLARE-DEPLOYMENT")

## Return Protocol
- Post deployment evidence (URL, status, cost) to parent issue
- Update this directory's STATE.md with completion status
```

---

## 3. FIRST EXECUTION — What to Do After Gaps Are Fixed

### Next Action: Dispatch Google Site Auditor (S3)

**Why this first:** Fixes broken links for 8,111 visitors/month across 3 Google Sites. No Cloudflare deployment needed — pure HTML audit. Lowest risk, highest immediate visitor impact.

**How:** Create a handoff from the HANDOFF.md in `G:\My Drive\projects\google-site-auditor\` (after creating the directory in GAP 3). The Projects agent will:
1. Audit qwav.tech for `qnfo.github.io/*` links (2 found: QWAV/ and QWAV/papers)
2. Audit qnfo.org for broken links (5,590 visitors — high priority)
3. Audit q08.org for broken links (2,280 visitors)
4. Report replacement URLs: `qnfo.github.io/X` → `deep.qwav.tech/X` or `archive.qnfo.org/X`
5. Post findings to QNFO/QWAV#77

### After That: Phase 2 Pages Migration

Once GAP 1 is fixed (Projects agent knows Cloudflare exists), migrate the 8 remaining GitHub Pages sites to `*.qnfo.org` subdomains using Issues #67-#74. Procedure per site:
1. Create CNAME FIRST (e.g., `laws.qnfo.org` → `quantum-laws-of-form.pages.dev`)
2. `wrangler pages project create` / `wrangler pages deploy`
3. Add domain via Cloudflare REST API (not wrangler CLI — bug in v4.95.0)
4. Verify `curl -sI https://laws.qnfo.org` → 200
5. Wait 24h, then disable GitHub Pages

---

## 4. DEFERRED — Don't Start These Yet

| Item | Why Deferred |
|:-----|:-------------|
| Phase 3 (Vectorize indexing, Ask QWAV, Email Workers) | Needs Phase 2 complete |
| Phase 4 (Monitoring framework) | #80 created, needs Worker scaffold |
| Subagent prompt updates (EXPLORER/IMPLEMENTER/REVIEWER) | Low impact — text-only agents |
| cloudflare-deploy.md issue template | Nice-to-have — manual creation works |
| 9 rwnq8 Pages sites → Cloudflare | User said "on hold" |

---

## 5. KEY FILES — Everything You Need

| File | Purpose |
|:-----|:--------|
| `G:\My Drive\prompts\agents\PROJECTS-AGENT.md` | **FIX THIS** — add §CLOUDFLARE-DEPLOYMENT |
| `G:\My Drive\prompts\QWAV-DEFAULT.md` | **FIX THIS** — add #66 reference to §0.6.7 + §H.1 |
| `G:\My Drive\prompts\templates\CLOUDFLARE-DEPLOYMENT.md` | Reference — v2.1 with 7 ops + 6 failures |
| `G:\My Drive\QWAV\archive\cloudflare-master-strategy-2026-05-27.md` | Full Phase 1-4 plan |
| `G:\My Drive\QWAV\archive\cloudflare-closeout-2026-05-27.md` | Deployment session closeout |
| `G:\My Drive\QWAV\archive\cloudflare-blue-sky-blueprint-2026-05-27.md` | 12-vision Cloudflare × QWAV |
| `G:\My Drive\QWAV\archive\cloudflare-poc-full-session-2026-05-27.md` | Full PoC execution trace (API keys redacted) |
| GitHub: QNFO/QWAV#66 | Master Strategy (parent of all Cloudflare issues) |
| GitHub: QNFO/QWAV#62 | QNFO Org Flagged (root cause trigger) |

---

## 6. AGENT INSTRUCTIONS — Paste This Into the New Session

```
You are the QWAV Program Manager. The Cloudflare migration program is LIVE:
4 Pages sites, 1 Worker, 1 Vectorize index, R2 archive. $0/month.

FIRST: Fix 2 critical gaps in the agent prompts:
1. G:\My Drive\prompts\agents\PROJECTS-AGENT.md — missing Cloudflare deployment
   section. Add §CLOUDFLARE-DEPLOYMENT (template in the handoff document).
2. G:\My Drive\prompts\QWAV-DEFAULT.md — add Master Strategy reference
   to §0.6.7 and §H.1.

SECOND: Create 4 spin-off project directories with handoff files:
   G:\My Drive\projects\google-site-auditor\
   G:\My Drive\projects\cf-dns-validator\
   G:\My Drive\projects\cloudflare-pages-migration\
   G:\My Drive\projects\pm-mirror-builder\

THIRD: Dispatch the Google Site Auditor (lowest risk, highest visitor impact).
   Create a Program→Project handoff for QNFO/QWAV#83.

Master Strategy: QNFO/QWAV#66. All sub-tasks: #67-#84.
Template: fill_prompt_template("CLOUDFLARE-DEPLOYMENT")
```

---

*Handoff generated 2026-05-27. 20 issues created. 6 gaps catalogued. Infrastructure live at $0/month.*
