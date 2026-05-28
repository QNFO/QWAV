# QNFO/QWAV Cloudflare Migration — Master Program Strategy

> **Status:** ACTIVE | **Priority:** P0 (risk mitigation for QNFO flagging) | **Cost:** $0/month  
> **Parent Trigger:** QNFO/QWAV#62 — QNFO Organization Flagged (240+ hours offline)  
> **PoC:** QNFO/QWAV#63 — Complete, Phase 1+2 partial deployment proven  
> **Last Updated:** 2026-05-27

---

## PROGRAM OVERVIEW

The QNFO organization was flagged by GitHub on 2026-05-27, removing all 24 QNFO repos from public view and blocking GitHub Pages for 240+ hours. This demonstrated that GitHub is a **single point of failure** for QWAV's public-facing research. Cloudflare already hosts QWAV's DNS — this program migrates hosting, storage, compute, and communication to Cloudflare's platform, eliminating the flagging risk while adding AI-native capabilities at zero marginal cost.

### Architecture

```
CLOUDFLARE (hosting/storage/compute/email/AI)       GITHUB (git remote/source of truth)
├── Pages: 4 sites live, 9 more planned             ├── rwnq8: 29 repos (git remote, not flagged)
├── Workers: 1 AI endpoint deployed                 ├── QNFO: 24 repos (flagged, source preserved)
├── Vectorize: 768-dim index ready                  └── Issues/Projects/Wiki: Program management
├── R2: 15 repos archived, ~85 MB
├── DNS: 10 zones, 6 bulk redirects
├── Email: 2 addresses routing
└── AI: Workers AI available, unused

PLATFORM ROOT: qnfo.org (research institute portal)
PROGRAM DOMAIN: qwav.tech (computing program, unchanged)
```

---

## PHASE STRUCTURE

### Phase 1: Foundation & Immediate Risk Mitigation ✅ COMPLETE

| # | Task | Status | Evidence |
|:--|:-----|:------|:---------|
| P1.1 | Deploy 1 Pages site (PoC) | ✅ | primer.qwav.tech |
| P1.2 | Deploy QWAV Knowledge Base | ✅ | deep.qwav.tech — was offline 240h |
| P1.3 | Archive QNFO repos to R2 | ✅ | 15 repos, ~85 MB |
| P1.4 | Fix 4 NXDOMAIN domains | ✅ | qnfo.net/uk, qwav.net/uk |
| P1.5 | Create bulk redirect rules | ✅ | 6 domains, 754 visitors/month rescued |
| P1.6 | Deploy AI Worker + Vectorize | ✅ | ask-qwav.q08.workers.dev |
| P1.7 | Enable Email Routing | ✅ | papers@qnfo.org, collab@qnfo.org |
| P1.8 | Document 6 failures | ✅ | CLOUDFLARE-DEPLOYMENT v2.0 |
| P1.9 | Create closeout document | ✅ | archive/cloudflare-closeout-2026-05-27.md |

### Phase 2: Consolidation — Migrate Everything Still on GitHub ⬜ PLANNED

**Goal:** Move all remaining GitHub-dependent assets to Cloudflare, making the QNFO flagging a non-event for public access.

| # | Task | Depends On | Effort | Priority |
|:--|:-----|:----------|:-------|:---------|
| P2.1 | **Migrate 9 rwnq8 GitHub Pages sites** | P1 complete | 3 sessions | 🔴 HIGH |
| P2.2 | **Archive full QNFO/QWAV issue list** → archive.qnfo.org | QNFO unflag or API workaround | 2 sessions | 🔴 HIGH |
| P2.3 | **Fix Google Site broken links** (qwav.tech, qnfo.org, q08.org) | P2.1 | 2 sessions | 🟡 MED |
| P2.4 | **Complete DNS redirect chain** (all domains → canonical) | P1.5 | 1 session | 🟡 MED |
| P2.5 | **Configure security headers** (all Pages sites) | P2.1 | 1 session | 🟡 MED |
| P2.6 | **Deploy custom 404 pages** (all Pages sites) | P2.1 | 1 session | 🟢 LOW |
| P2.7 | **Domain expiry WHOIS audit** (all 14 domains) | None | 1 session | 🟢 LOW |
| P2.8 | **R2 bucket inventory** (0pus, mail) | None | 1 session | 🟢 LOW |
| P2.9 | **Email routing destination verification** | None | 1 session | 🟢 LOW |
| P2.10 | **Template registration** (CLOUDFLARE-DEPLOYMENT in fill system) | System reload | 1 session | 🟢 LOW |
| P2.11 | **Close QNFO/QWAV#63** — investigation complete | All P2 | 0 | Admin |

#### P2.1: 9 GitHub Pages Sites to Migrate

| # | Repo | Current URL | Proposed Domain | Branch | Content |
|:--|:-----|:-----------|:----------------|:-------|:--------|
| 1 | qlof-primer | rwnq8.github.io/qlof-primer | **primer.qwav.tech** ✅ DONE | master | HTML |
| 2 | quantum-laws-of-form | rwnq8.github.io/quantum-laws-of-form | **laws.qnfo.org** | main | HTML |
| 3 | ultrametric-paradigm | rwnq8.github.io/ultrametric-paradigm | **paradigm.qnfo.org** | master | HTML |
| 4 | hierarchical-universe | rwnq8.github.io/hierarchical-universe | **hierarchy.qnfo.org** | master | HTML |
| 5 | different-physics | rwnq8.github.io/different-physics | **different.qnfo.org** | master | HTML |
| 6 | two-ways-of-measuring | rwnq8.github.io/two-ways-of-measuring | **measure.qnfo.org** | master | HTML |
| 7 | unity-of-ultrametric-physics | rwnq8.github.io/unity-of-ultrametric-physics | **unity.qnfo.org** | master | HTML |
| 8 | ultrametric-quantum | rwnq8.github.io/ultrametric-quantum | **quantum.qnfo.org** | master | HTML |
| 9 | ultrametric-ai-poc | rwnq8.github.io/ultrametric-ai-poc | **ai-poc.qnfo.org** | master | HTML |

**Procedure:** 1. Create CNAME FIRST → 2. Create Pages project → 3. Deploy → 4. Add domain → 5. Verify → 6. Disable GitHub Pages after 24h verification

### Phase 3: Enhancement — AI-Native Research Platform ⬜ PLANNED

**Goal:** Transform QWAV from static publications into an interactive, AI-augmented research platform.

| # | Task | Depends On | Effort | Priority |
|:--|:-----|:----------|:-------|:---------|
| P3.1 | **Index all 29 QWAV papers in Vectorize** | P2.1 | 4 sessions | 🔴 HIGH |
| P3.2 | **Deploy "Ask QWAV" research oracle** (RAG + Workers AI) | P3.1 | 3 sessions | 🔴 HIGH |
| P3.3 | **Email Workers — native email processing** (QNFO/QWAV#65) | P2.9 | 3 sessions | 🟡 MED |
| P3.4 | **Interactive Living Paper template** (one paper first) | P2.1 | 3 sessions | 🟡 MED |
| P3.5 | **Ultrametric Playground** (interactive tools) | P3.2 | 3 sessions | 🟡 MED |
| P3.6 | **Autonomous Research Pipeline** (arXiv scraper → classifier) | P3.2 | 4 sessions | 🟢 LOW |
| P3.7 | **QWAV Agent Swarm** (Explorer → Synthesizer → Verifier) | P3.6 | 5 sessions | 🟢 LOW |
| P3.8 | **Concept Graph** (living knowledge graph) | P3.1 | 4 sessions | 🟢 LOW |
| P3.9 | **Reproducibility as Code** (Sandbox verification) | P2.1 | 3 sessions | 🟢 LOW |
| P3.10 | **qwav.ai or qnfo.org unified platform** | All above | 5 sessions | 🟢 LOW |

### Phase 4: Monitoring & Audit (Continuous) 🔄 ONGOING

| # | Task | Frequency | Automation |
|:--|:-----|:----------|:-----------|
| P4.1 | **Pages health check** (all sites return 200) | Weekly | Workers cron trigger → smoke test |
| P4.2 | **DNS resolution audit** (all 10 zones) | Monthly | Workers → dig equivalent |
| P4.3 | **R2 storage audit** (size, cost projection) | Monthly | wrangler r2 object list --json |
| P4.4 | **Vectorize index health** (dim count, freshness) | Weekly | API query |
| P4.5 | **Worker health check** (AI endpoint responds) | Daily | curl + cron |
| P4.6 | **Cost gate check** (free tier thresholds) | Monthly | Compare usage vs limits |
| P4.7 | **Domain expiry audit** (14 domains) | Quarterly | WHOIS check |
| P4.8 | **Bulk redirect verification** (6 rules active) | Monthly | curl each source → verify 301 |
| P4.9 | **GitHub Pages sync check** (original sites still work) | Weekly | curl github.io URLs |
| P4.10 | **Security scan** (SSL certs, headers) | Monthly | curl -sI + validation |

---

## DEPENDENCY GRAPH

```
P1 ✅ → P2.1 (9 Pages sites) ────→ P2.3 (Google Site fixes)
              │                    → P2.5 (security headers)
              │                    → P2.6 (custom 404s)
              │                    → P3.1 (Vectorize indexing)
              │                    → P3.4 (Living Paper)
              │                    → P3.9 (Reproducibility)
              │
P2.2 (QNFO archive) ← blocked by QNFO flagging (#62)
              │
P2.4 (DNS redirects) ← independent
              │
P3.1 (Vectorize) → P3.2 (Ask QWAV) → P3.5 (Playground) → P3.8 (Concept Graph)
                                    → P3.6 (Pipeline) → P3.7 (Agent Swarm)
              │
P2.9 (Email verify) → P3.3 (Email Workers)
              │
P3.10 (Unified platform) ← ALL above complete
```

---

## COST PROJECTION (Updated with Actuals)

| Service | Free Limit | Current Usage | % Used | Monthly Cost |
|:--------|:-----------|:--------------|:-------|:-------------|
| Pages builds | 500/mo | ~15 builds | 3% | $0 |
| Pages bandwidth | Unlimited | Low | — | $0 |
| Workers requests | 100k/day | 0 (not yet serving) | 0% | $0 |
| Workers AI | Included | 0 (not yet called) | 0% | $0 |
| R2 storage | 10 GB | ~85 MB | 0.85% | $0 |
| R2 egress | Free | N/A | — | $0 |
| Vectorize | Free tier | 1 index, empty | ~0% | $0 |
| D1 | 5 GB | Not yet used | 0% | $0 |
| Email Routing | Free | 2 addresses | — | $0 |
| DNS zones | Free | 10 zones | — | $0 |
| Bulk Redirects | Free | 6 rules | — | $0 |
| **TOTAL** | | | | **$0/mo** |

**Projected at Phase 3 completion:** $0–$5/mo (Workers AI usage, Sandbox compute minutes)

---

## RISK REGISTER

| Risk | Severity | Phase | Mitigation | Contingency |
|:-----|:---------|:------|:-----------|:------------|
| GitHub flags rwnq8 account | 🔴 CRITICAL | All | Maintain Cloudflare mirror of all repos; archive Issues to R2 weekly | Full cutover to Cloudflare + GitLab mirror |
| Cloudflare free tier changes | 🟡 MEDIUM | All | Monitor pricing page; Pro plan ($20/mo) as fallback | Budget $20/mo if needed |
| wrangler CLI breaking changes | 🟡 MEDIUM | P2/P3 | Pin version in CI; catalog failures in template | Roll back wrangler version |
| QNFO flagging unresolved | 🔴 ACTIVE | P2.2 | Use API workarounds; archive from local clones | Wait for support ticket resolution |
| Domain registration lapse | 🟢 LOW | P4.7 | Quarterly WHOIS audit with 90-day warning | Auto-renew via registrar |
| Vectorize index corruption | 🟢 LOW | P3.1 | Backup embeddings to R2; idempotent rebuild pipeline | Rebuild from source papers |

---

## SUCCESS METRICS

| Metric | Current | Phase 2 Target | Phase 3 Target |
|:-------|:--------|:---------------|:---------------|
| GitHub Pages sites on Cloudflare | 2 of 11 | 11 of 11 | 11 of 11 |
| Domains resolving correctly | 10 of 10 | 10 of 10 | 10 of 10 |
| Visitors rescued (redirects) | 754/mo | All domain leakage captured | All leakage captured |
| QNFO repo survivability | R2 mirror (partial) | R2 mirror (full) | R2 mirror + live archive |
| AI research capability | 0 | 0 | "Ask QWAV" live, indexed |
| Platform cost | $0/mo | $0/mo | $0–$5/mo |
| Flagging impact | QNFO offline 240h+ | QNFO offline, public sites online | Zero impact |

---

## COORDINATION

### GitHub Issues (this repo)

| # | Title | Phase | Status |
|:--|:------|:------|:------|
| #62 | QNFO Organization Flagged | Trigger | 🔴 OPEN |
| #63 | Cloudflare Migration Investigation | PoC | ✅ Complete |
| #64 | MASTER STRATEGY (this issue) | All | 🟡 ACTIVE |
| #65 | Email Workers Investigation | P3 | 🔶 BACKLOG |
| #66–#76 | Phase 2 sub-tasks (to be created) | P2 | ⬜ PLANNED |

### Program Board

All Cloudflare issues tracked on QWAV Program Management board (qnfo board #1) with labels `cloudflare-p1`, `cloudflare-p2`, `cloudflare-p3`, `cloudflare-monitor`.

### Execution Model

- **Program Agent** (this thread): Strategy, planning, quality-gate, cross-issue coordination
- **Projects Agent** (separate threads): Execution via handoffs — build, deploy, verify, report
- **Template:** `fill_prompt_template("CLOUDFLARE-DEPLOYMENT")` for all deployment operations

---

*This is a living document. Updated as phases complete, risks evolve, and new Cloudflare capabilities launch.*
