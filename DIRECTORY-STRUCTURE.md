# QWAV Directory Structure — Reference

> **Last updated:** 2026-05-28 | **Purpose:** Navigation guide for agents and humans

---

## Top-Level Map

```
G:\My Drive\QWAV\
│
├── 📋 PROGRAM MANAGEMENT (this directory)
│   ├── README.md                 Portfolio identity, thesis, Cloudflare infrastructure
│   ├── PROGRAM-STATE.md          Canonical program state (20 sites, 6 phases)
│   ├── AUDIT-REPORT-2026-05-28.md Cleanup audit (this session)
│   ├── CODE_OF_CONDUCT.md        Community standards
│   ├── CONTRIBUTING.md           Contribution guidelines
│   └── LICENSE                   License
│
├── 🌐 STATIC WEB (deep.qwav.tech)
│   ├── index.html                Landing page
│   ├── llms.txt                  LLM-friendly site index
│   ├── robots.txt                SEO
│   └── sitemap.xml               SEO
│
├── 📁 DIRECTORIES
│   ├── .github/                  GitHub: issue templates, PR templates, CI workflows
│   ├── .wrangler/                Cloudflare wrangler state (DO NOT DELETE)
│   ├── briefings/                All briefings, handoffs, platform docs, templates
│   ├── strategy/                 Portfolio strategy (v1.0, v2.0, v3.0 + supporting docs)
│   ├── sessions/                 Session records (organized by year/month)
│   ├── scripts/                  Utility scripts (14 scripts + templates/)
│   ├── tests/                    Test suite (smoke tests, browser tests)
│   ├── artifacts/                Interactive demos (deployed to Cloudflare Pages)
│   ├── papers/                   HTML paper pages (served by deep.qwav.tech)
│   ├── projects/                 Project handoff workspace
│   └── archive/                  Archived session files
│
└── 🔧 CONFIG
    ├── .gitignore                Git ignore rules
    └── .nojekyll                 Cloudflare Pages config
```

---

## Directory Details

### `briefings/` — Program Briefings & Documentation

```
briefings/
├── HANDOFF-TRACKER.md            Program-level index of all 16 project handoffs
├── platform/                     Platform documentation
│   ├── cloudflare-comprehensive-audit-2026-05-28.md
│   ├── github-integration-plan.md
│   ├── QNFO-org-README-v2.md
│   ├── QWAV System Instructions.txt
│   ├── spinoff-registry-artifacts.md
│   ├── wiki-home.md
│   └── zenodo-crosslink-audit.md
├── research/                     Research-related briefings
│   ├── ewor-assessment.md
│   ├── fqxi-briefing.md
│   ├── P11 collaborator - Formal Verification Agenda (Shareable).docx
│   ├── P11 Formal Verification Collaboration Briefing.md
│   ├── sbir-phase1-briefing.md
│   └── src_fqxi_2026.md
├── templates/                    Document templates
│   ├── business-docs-template.tex
│   ├── inbound-email-template.md
│   └── lab-outreach-template.md
├── BRAND-STRATEGY.md
├── google-ai-studio-prompts-qwav-marquee.md
├── prior-work-catalog.md
├── smoke-maintenance-protocol.md
└── technical-site-sprint-plan.md
```

### `strategy/` — Portfolio Strategy

```
strategy/
├── 1.0.md                        Strategy v1.0
├── 2.0.md                        Strategy v2.0
├── 3.0.md                        Strategy v3.0 (includes §9 Cloudflare-Native Operations)
├── ACTION-PLAN.md
├── FUNDRAISING.md
├── IP-STRATEGY.md
├── MANUFACTURING-BLUEPRINT.md
├── VENUE-REGISTRY.md
├── External Sources and Citation Map.md
├── QA - Narrative Modules and Intellectual Defense.md
├── An Introvert's Deep-Tech Startup Path.md
├── Technical Deep-Dive - Ultrametric Quantum Computing and AI.md
└── mathematical-foundations.md
```

### `scripts/` — Utility Scripts

```
scripts/
├── build_pdf.py                  PDF builder
├── compile_audit.py              Audit compiler
├── convert_wikilinks.py          Wiki link converter
├── build-archive.py              Paper archive HTML builder
├── cf-create-token.py            Cloudflare API token creation
├── cf-dns-setup.py               Cloudflare DNS setup
├── cf-pages-domains.py           Cloudflare Pages domain config
├── fix-ids.py                    Paper ID fixer
├── ingest-full.py                Full paper ingestion
├── ingest-papers.py              Paper ingestion
├── ingest-v2.py                  Paper ingestion v2
├── test-r2-dl.py                 R2 download test
├── test-vectorize.py             Vectorize test
├── .cf-auth-config.ps1           Cloudflare auth helper (PowerShell)
└── templates/
    └── archive-template.html     Archive HTML template
```

### `sessions/` — Session Records

```
sessions/
├── README.md
└── 2026/
    └── 05/
        ├── cleanup-audit-2026-05-26.md
        ├── DEMO-AUDIT-REPORT.md
        ├── drafts-2026-05-26.md
        ├── FINAL_AUDIT_REPORT.md
        ├── outreach-atom-computing.md
        ├── outreach-email-david-wales.md
        ├── outreach-email-neutral-atom-labs.md
        ├── outreach-email-zuniga-galindo.md
        ├── outreach-infleqtion.md
        ├── outreach-pasqal.md
        ├── outreach-planqc.md
        ├── outreach-quera.md
        ├── QNFO-org-README.md
        ├── release-v2.74-notes.md
        ├── rwnq8-migrate-notice.b64.txt
        ├── rwnq8-profile-README.md
        ├── SESSION-HANDOFF-2026-05-27.md
        ├── SESSION-HANDOFF-2026-05-28.md
        ├── SESSION-CLOSEOUT-2026-05-28.md
        └── strategy-archive/     (v0.1-v0.9 + supporting docs)
```

### `artifacts/` — Interactive Demos (Cloudflare Pages)

```
artifacts/
├── convergence-explorer/         Interactive convergence demo
├── error-confinement-demo/       Error confinement visualization
├── hardware-visualizer/          Hardware visualizer (three.js)
├── qpna-playground/              QPNA playground
└── tree-distance/                Tree distance demo
```

### `papers/` — HTML Paper Pages (deep.qwav.tech)

~573 untracked HTML files serving as individual paper pages. Includes named papers (e.g., `10-architecture-of-order.html`), hash-named papers (e.g., `724026e3.html`), and year indexes (`2025.html`, `2026.html`).

---

## Evicted Files (Moved Out of QWAV)

| Original Location | New Location | Reason |
|:------------------|:-------------|:-------|
| `people/` | `G:\My Drive\personal\` | Personal resume, not program-related |
| `applications/` | `G:\My Drive\projects\applications\` | Grant applications, not portfolio management |
| `handoffs/` (#82-#90) | `briefings/handoffs/archive/phase-4-5-concept/` | Legacy handoffs, consolidated with active ones |

---

## Files Deleted

| File | Reason |
|:-----|:-------|
| `Bridging the Gap.md` | Empty file (0 bytes) |
| `.pytest_cache/` | Python test cache (added to .gitignore) |

---

*Reference document for QWAV program directory. Update when significant structural changes occur.*
