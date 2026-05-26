# Handoff: Tier 1.5 Paper — Decoherence Validation

**Type:** Program→Project
**Date:** 2026-05-26
**Issuing Authority:** Program Agent v2.0
**Accepting Authority:** Projects Agent
**GitHub Issue:** [#53](https://github.com/QNFO/QWAV/issues/53)

## Scope

### Included
- Literature review of neutral atom decoherence mechanisms (Rydberg blockade, laser phase noise, atomic motion)
- Parameterized model mapping decoherence to ultrametric tree error suppression
- Quantitative validation: how tree geometry interacts with realistic decoherence
- Draft paper (8-12 pages) in QNFO research publication format
- All claims cited to peer-reviewed sources with DOIs

### Excluded
- New experimental data (simulation only)
- Hardware access or physical experiments
- Patent filing or IP strategy decisions (see IP-STRATEGY.md)
- Submission to specific journal (target: arXiv + eventual journal)

## Success Criteria

| # | Criterion | How Measured |
|:--|:----------|:-------------|
| 1 | Literature review complete with 15+ peer-reviewed sources | Bibliography with DOIs |
| 2 | Parameterized decoherence model documented | Mathematical formalism in paper |
| 3 | Quantitative validation results | Tables/figures with error rate comparisons |
| 4 | Draft paper (8-12 pages) | Word count, section completeness |
| 5 | Blind reader testing passed | §11.5 protocol — 2+ rounds |
| 6 | Published as GitHub Release | Release URL returns HTTP 200 |

## Constraints

| Constraint | Value |
|:-----------|:------|
| Budget | $0 (human attention hours only) |
| Sources | All quantitative claims must have peer-reviewed source with DOI |
| Format | QNFO research publication format (see prior releases) |
| Fabrication | ZERO tolerance — every claim traceable to source |
| Deadline | Sprint 25 (2 weeks) |

## Dependencies

| Dependency | Status | Blocking? |
|:-----------|:-------|:----------|
| strategy/mathematical-foundations.md | ✅ Complete | No |
| papers/index.md (prior publications catalog) | ✅ Complete | No |
| GitHub Releases (prior paper format) | ✅ Complete | No |
| Tier 0 paper (published) | ✅ Complete | Reference only |

## Research Trail

1. `strategy/mathematical-foundations.md` — Theoretical framework
2. `briefings/research/fqxi-briefing.md` — Prior grant application context
3. `briefings/research/src_fqxi_2026.md` — Source text from grant
4. `papers/index.md` — Prior publications catalog
5. GitHub Releases: QNFO/.github/releases/ — Prior paper format

## Acceptance Gate

- [ ] Re-read original handoff spec — each Success Criterion verified against deliverable
- [ ] Fabrication audit: every claim has source DOI
- [ ] Blind reader testing: §11.5 protocol, 2+ rounds, all blocking issues resolved
- [ ] Paper published as GitHub Release in QNFO/.github
- [ ] Papers catalog updated (papers/index.md)
- [ ] Issue #53 closed with deliverable reference

## Return Protocol

1. Publish paper as GitHub Release in QNFO/.github repository
2. Add entry to papers/index.md catalog
3. Close GitHub Issue #53 with comment: release URL + test results + paper DOI (once on arXiv)
4. Update roadmap #43 QEC Tiers status

---
*Program Agent → Projects Agent. Discover on startup by scanning for issues labeled `handoff`.*
