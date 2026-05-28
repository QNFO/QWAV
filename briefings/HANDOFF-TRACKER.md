# QWAV Handoff Tracker — 2026-05-28

> **All 16 handoffs moved to `projects/` directories. Each project has `SPEC.md` (full handoff spec).**
> **7 active (Phase 3 infra) + 9 legacy (Phase 4/5 concepts).**

---

## Active Handoffs — Phase 3 Cloudflare Infrastructure (7)

| # | Issue | Project Directory | Repo | Priority | Sessions | Category |
|:--|:------|:------------------|:-----|:---------|:---------|:---------|
| 3 | [#93](https://github.com/QNFO/QWAV/issues/93) | `projects/ask-qwav-rag/` | — (modifies existing Worker) | 🔴 P0 | 2 | AI |
| 1 | [#94](https://github.com/QNFO/QWAV/issues/94) | `projects/sandbox-pdf-builder/` | [rwnq8/sandbox-pdf-builder](https://github.com/rwnq8/sandbox-pdf-builder) | 🔴 P0 | 1 | Compute |
| 2 | [#95](https://github.com/QNFO/QWAV/issues/95) | `projects/d1-citation-graph/` | [rwnq8/qwav-db](https://github.com/rwnq8/qwav-db) | 🔴 P0 | 1 | Storage |
| 4 | [#96](https://github.com/QNFO/QWAV/issues/96) | `projects/queues-browser-run/` | [rwnq8/qwav-research-pipeline](https://github.com/rwnq8/qwav-research-pipeline) | 🟡 P1 | 2 | Compute |
| 5 | [#97](https://github.com/QNFO/QWAV/issues/97) | `projects/email-service/` | [rwnq8/qwav-email](https://github.com/rwnq8/qwav-email) | 🟡 P1 | 1 | Network |
| 6 | [#98](https://github.com/QNFO/QWAV/issues/98) | `projects/ai-gateway/` | — (config only) | 🟡 P1 | 0.5 | AI |
| 7 | [#99](https://github.com/QNFO/QWAV/issues/99) | `projects/secrets-store/` | — (config only) | 🟡 P1 | 0.5 | Security |

## Legacy Handoffs — Phase 4/5 Concepts (9)

| # | Handoff | Project Directory | Phase | Superseded By |
|:--|:--------|:------------------|:------|:--------------|
| 82 | Living Paper | `projects/living-paper/` | P4 | — |
| 83 | QWAV Scan (arXiv Discovery) | `projects/qwav-scan/` | P4 | #96 Queues+Browser Run (scraping infra) |
| 84 | Cross-Paper Consistency Engine | `projects/consistency-engine/` | P5 | Needs #95 D1 first |
| 85 | Ultrametric Playground | `projects/ultrametric-playground/` | P4 | — |
| 86 | Concept Graph | `projects/concept-graph/` | P4 | Needs #95 D1 first |
| 87 | Reproducibility as Code | `projects/reproducibility-as-code/` | P5 | Needs #94 Sandbox first |
| 88 | Automated Peer Review | `projects/automated-peer-review/` | P5 | — |
| 89 | QWAV Compute Cloud | `projects/qwav-compute-cloud/` | P4 | Needs #94 Sandbox first |
| 90 | Agent Swarm | `projects/agent-swarm/` | P5 | — |

## Execution Order (Recommended)

```
BLOCKING (P0 — execute first):
  #3 Ask QWAV RAG (2 sessions)     ← SINGLE HIGHEST LEVERAGE MOVE
  #1 Sandbox PDF builder (1)       ← Unblocks PDF pipeline (GitHub Actions dead)
  #2 D1 citation graph (1)         ← Data foundation for all Phase 3+ features

NON-BLOCKING (P1 — execute after):
  #4 Queues + Browser Run (2)      ← Research pipeline backbone
  #5 Email Service (1)            ← Replaces Outlook COM
  #6 AI Gateway (0.5)             ← Quick win, cost control
  #7 Secrets Store (0.5)          ← Security foundation

Total: ~8 sessions across 7 active handoffs
```

## Handoff Status

| # | Status | Projects Agent | Started | Completed |
|:--|:-------|:---------------|:--------|:----------|
| 93 | ⬜ READY | — | — | — |
| 94 | ⬜ READY | — | — | — |
| 95 | ⬜ READY | — | — | — |
| 96 | ⬜ READY | — | — | — |
| 97 | ⬜ READY | — | — | — |
| 98 | ⬜ READY | — | — | — |
| 99 | ⬜ READY | — | — | — |

## Cross-Reference

- **Comprehensive Audit:** `briefings/platform/cloudflare-comprehensive-audit-2026-05-28.md`
- **Program State:** `PROGRAM-STATE.md` — Phase 3 status, infrastructure inventory
- **Strategy 3.0:** `strategy/3.0.md` — §9 Cloudflare-Native Operations appendix
- **Directory Structure:** `DIRECTORY-STRUCTURE.md`
- **Audit Report:** `AUDIT-REPORT-2026-05-28.md`

---

*All handoffs live in `projects/<name>/SPEC.md`. This tracker is the program-level index.*
