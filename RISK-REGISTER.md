---
template: RISK-REGISTER
version: "1.0"
---

# Risk Register — QWAV

**Last Reviewed:** 2026-05-22
**Review Cadence:** Per sprint

## Active Risks

| ID | Description | Likelihood | Impact | Mitigation | Owner | Review Date | Status |
|:---|:------------|:-----------|:-------|:-----------|:------|:------------|:-------|
| R1 | **Obscurity** — publications and artifacts exist but are never discovered by relevant readers | Medium | High — entire theory of change depends on discovery | Interactive artifacts lower engagement barrier (D13). Multi-channel social distribution. qwav.tech as discoverable web presence. | Founder | 2026-05-22 | Active |
| R2 | **Competitive emergence** — another group publishes on Bruhat-Tits QEC or ultrametric neural architectures | Low | Medium — QWAV has priority via 5 DOIs and 673-release corpus, but without institutional backing, priority claims have limited weight | Monitor arXiv for Bruhat-Tits + QEC keywords. Competitive landscape analysis (strategy/0.5.md) identifies zero direct competitors. | QWAV Agent | 2026-05-22 | Monitoring |
| R3 | **Technical obsolescence** — neutral atom hardware evolves incompatibly with the 40-atom d=3 spec, or a mathematical flaw is discovered | Low | High — would undermine core thesis | The 40-atom spec is minimum viable, not the only pathway. Geometric argument is hardware-independent. Re-validate computational results annually. | QWAV Agent | 2026-05-22 | Monitoring |
| R4 | **Application exhaustion** — all 6 pending applications return rejections, no new merit-based programs identified | Medium | Low — program costs nearly nothing to maintain | This is the baseline scenario. Strategy 3.0 builds endogenous momentum independent of application outcomes. | Founder | 2026-05-22 | Active |
| R5 | **Founder burnout** — solo founder reallocates attention or energy depletes | Unknown | High — program has no redundancy | Low-cost, low-intensity design mitigates burnout. Strategy 3.0 builds momentum in 30-day sprints with sustainable cadence afterward. Program can idle for months without damage. | Founder | 2026-05-22 | Monitoring |
| R6 | **Zero inbound contacts sustained** — 6+ months of artifacts and publications produce zero engagement | Medium | Medium — confirms discovery problem is deeper than presentation | Pivot to distribution strategy: bridge content, platform SEO, community engagement (within D3 written-only constraint). This is valuable diagnostic information, not failure. | QWAV Agent | 2026-05-22 | Monitoring |
| R7 | **Platform risk (Twitter/X)** — social distribution channel degrades or becomes inaccessible | Medium | Low — Mastodon and Bluesky provide redundancy | Multi-platform Buffer distribution. qwav.tech as owned channel (no platform dependency). | QWAV Agent | 2026-05-22 | Monitoring |
| R8 | **Build phase stalls** — interactive artifacts more complex than estimated, sessions take longer | Medium | Low — plan is modular; partial completion still produces value | Prioritize A1 + K1 as minimum viable gravity (3.5 sessions). Everything else is additive. | QWAV Agent | 2026-05-22 | Active |

## Pre-Populated Known Risks (from CPL)

| CPL Ref | Risk | Default Likelihood | Default Impact | Default Mitigation |
|:--------|:-----|:-------------------|:---------------|:-------------------|
| L1 | Git repository contamination — .git dirs in projects tree | Low | High | QWAV uses independent `.git/`. All git commands use `-C "G:\My Drive\QWAV"` flag. |
| L3/L6 | Unicode cp1252 console crash on Windows | High | Low | Rule 12: Pre-execution Unicode safety scan |
| L7 | Python -c string corruption on Windows (PowerShell) | High | Medium | Rule 13: HARD BLOCK — never inline Python through PowerShell; write scripts to files |
| L13 | Agent claims "committed" without git log verification | Medium | High | §9.3 Post-Work Checklist: `git log -1` after every commit |
| L14 | -ErrorAction SilentlyContinue masking critical failures | Medium | High | Forbidden in verification — use `Test-Path` or try/catch |
| L15/L17 | Write-then-verify gap — tool success $\neq$ file exists | Medium | High | `Test-Path` + `Get-Content` after every write/edit |
| L16 | temperature: 0.0 insufficient for fabrication prevention | Medium | High | Structural guardrails: Due Diligence §0.8, Pre-Send Checklist §E.5.1, git log verification §9 |
| L18/L40 | Write tool silent failure after multiple calls | Medium | High | Verify after every write; fall back to Python exec for batch ops |
| L19 | Git branch renamed by parallel process | Low | Medium | Check branch name before every commit against session-start recorded name |
| L20 | Branch reuse across projects — cross-contamination | Low | High | Never reuse branches — unique `feature/qwav-<name>-<date>` per session |
| L21 | Backlog drift — docs become stale when files deleted by parallel sessions | Low | Medium | Verify all Tier 1 docs at session start; audit against deleted files |
| L38 | Null-byte placeholder math fix corrupts files | Low | High | Use ASCII-safe markers only; Python scan for null bytes before file writes |
| L39 | Subagent output truncation at ~32K tokens | High | Medium | Break long-form generation into sections; parent completes truncated output |

## Resolved Risks

| ID | Description | Resolution Date | Resolution |
|:---|:------------|:----------------|:-----------|
| — | *None yet resolved* | — | — |

---
*Generated from RISK-REGISTER-TEMPLATE.md v1.0*
