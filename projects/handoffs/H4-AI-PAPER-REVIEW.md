# Handoff H4: AI-Assisted Paper Review & Grading (Spinoff POC)

> **Type:** Program→Project | **Priority:** P1 | **Est. effort:** 8-12 hours
> **Depends on:** H1 (R2 pipeline) — papers must be in R2

## Problem

Early papers contain inaccuracies and myopic claims. They should be preserved for provenance but readers need honest AI-generated assessments to navigate shortcomings. This is also a POC for replacing human peer review with transparent, streamlined AI review — faster preprint→publication cycle with machine-generated rigor checks.

## Vision

```
paper.html?p=[slug]
    │
    ├── Full text rendering (existing)
    ├── Living Papers AI (existing)
    └── AI REVIEW PANEL ← THIS PROJECT
         ├── Accuracy score (1-10)
         ├── Methodology assessment
         ├── Clarity score (1-10)
         ├── Key shortcomings (bullet list)
         ├── Retraction/correction flag if warranted
         ├── "Reader's guide" — what to trust, what's outdated
         └── Collapsible section — doesn't interrupt reading
```

## Scope

### Included
- Workers AI model prompt for paper review
- Review generation pipeline (reads paper, generates assessment)
- Review storage (D1 or R2 alongside paper)
- Display component in `paper.html` (collapsible "AI Review" section)
- Rubric: accuracy, methodology, clarity, novelty, reproducibility
- Grading scale with explanations
- Retraction/correction flag logic
- "Reader's guide" — honest navigation aid

### Excluded
- Human-in-the-loop approval (future)
- Reviewer reputation system (future)
- Multi-model consensus (future — POC is single-model)
- Integration with external review platforms

## Technical Approach

### Review Generation
```
POST /api/review/generate
  Body: { slug: "autaxic-trilemma", paper_content: "..." }
  
Workers AI prompt:
  "You are a rigorous but fair research reviewer. Assess this paper on:
   1. Factual accuracy (1-10)
   2. Methodological soundness (1-10)  
   3. Clarity of exposition (1-10)
   4. Novelty of contribution (1-10)
   5. Reproducibility (1-10)
   
   For each criterion, provide a 2-3 sentence justification.
   List the top 3-5 shortcomings or inaccuracies.
   Flag if retraction or major correction is warranted.
   
   Be honest — early-career papers may score low. That's expected."
```

### Storage
- Reviews stored as JSON in R2: `qnfo/reviews/[slug].json`
- Or in D1: `reviews` table with `paper_slug`, `scores`, `shortcomings`, `generated_at`
- Cached — regenerate only on paper update or manual trigger

### Display
- New collapsible `<section id="ai-review">` in `paper.html`
- Shows overall grade (A-F or 1-10) prominently
- Expand to see detailed rubric with justifications
- "Reader's guide" at top: "⚠️ This 2024 paper contains claims about X that were superseded by Y (2025). Trust the methodology section but approach conclusions with caution."
- Color-coded: green (strong), yellow (mixed), red (problematic)

## Architecture Integration

```
paper.html loads
    │
    ├── fetch /api/paper/[slug] → render content
    └── fetch /api/review/[slug] → render review panel
              │
              ├── If review exists → return cached JSON
              └── If no review → return 404 (show "No review yet — request one")
```

## Success Criteria

| # | Criterion | Verification |
|:--|:----------|:-------------|
| 1 | AI generates review for any paper | Test on 5 papers across different years |
| 2 | Review scores correlate with paper quality | Spot-check: 2026 papers > 2024 papers |
| 3 | Shortcomings are specific and actionable | Each shortcoming references specific claims |
| 4 | Review panel renders collapsible in paper.html | Visual check on 3 papers |
| 5 | "Reader's guide" provides honest navigation | Check early papers get appropriate warnings |
| 6 | Review generation is idempotent | Re-running produces consistent results |
| 7 | Review cache invalidates on paper update | Upload new version, verify review regenerates |

## Dependencies

| Dependency | Status |
|:-----------|:-------|
| H1 (R2 pipeline) | Must complete first |
| Workers AI binding | Already configured on qwav project |
| Review storage (D1 or R2) | Needs creation |

## Acceptance Gate

- [ ] 7 success criteria verified
- [ ] Review panel renders on at least 3 papers
- [ ] Early paper (2024) gets lower scores than recent paper (2026)
- [ ] "Reader's guide" is honest and helpful, not defensive
- [ ] Collapsible — doesn't interrupt normal reading flow
