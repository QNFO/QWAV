---
template: DEFINITION-OF-DONE
version: "1.0"
---

# Definition of Done — QWAV

A task is NOT complete until ALL applicable criteria are met. DoD is verified by the human orchestrator per the Force-Multiplier Protocol, not self-assessed by the agent.

## CODE TASK

- [ ] File passes pre-execution Unicode safety scan (Rule 12)
- [ ] File executes without errors on first run
- [ ] Output verified against expected results
- [ ] No `python -c` used (Rule 13: HARD BLOCK)
- [ ] File committed with format: `ACTION:[CREATE|EDIT] FILE: path RATIONALE:reason`
- [ ] `git log -1 --oneline` confirms commit exists

## CODE TEST TASK

- [ ] ALL test files for this module executed — verified by re-execution (NOT by checking file existence)
- [ ] Test suite output: [N] passed, [0] failed, [K] skipped
- [ ] Edge cases covered: empty input, boundary values, error conditions
- [ ] Test evidence saved via `fill_prompt_template("TEST-EVIDENCE-TEMPLATE")`
- [ ] If any tests failed: root cause documented, fix applied, re-executed to zero failures
- [ ] Regression check: re-ran ALL related test files after fix — no new failures

## DOCUMENT TASK

- [ ] Document passes Publication Language Gate (§11.7) — zero internal project language
- [ ] Curly quotes throughout body text (Python scan confirmation)
- [ ] YAML frontmatter present and valid
- [ ] Reader testing: minimum 1 round (2 rounds for publication documents per §11.5)
- [ ] All `[BLOCKING]` and `[MAJOR]` reader testing issues resolved
- [ ] File committed with format
- [ ] If replacing prior version: old version deleted per File Replacement Protocol (§10.5)

## PUBLICATION TASK

- [ ] Publication Language Gate (§11.7): zero internal language hits
- [ ] Standalone Publication Requirement (§11.8): zero project references
- [ ] Reader testing: 2 rounds minimum, no truncation gaps (§3.1)
- [ ] Curly quotes, YAML, author block per §11
- [ ] `[DOI-PENDING]` replaced with actual DOI
- [ ] Copy to `G:\My Drive\Obsidian\releases\YYYY\MM\` verified with Test-Path
- [ ] Human review (G4) completed
- [ ] File committed

## ANALYSIS TASK

- [ ] All quantitative claims verified via Python (re-executed, output matches)
- [ ] All citations traceable to source files or labeled `[UNVERIFIED-LLM]`
- [ ] Limit checks performed on derivations
- [ ] Web-retrieved claims verified per §0.8.6 Web Research Protocol
- [ ] Results saved in structured format (JSON/CSV)

## ANALYSIS TEST TASK

- [ ] ALL analysis scripts re-executed — verified output matches claimed results
- [ ] Reproducibility confirmed: same input $\to$ same output (seed-controlled)
- [ ] Limit/boundary checks performed and documented
- [ ] Test evidence saved via `fill_prompt_template("TEST-EVIDENCE-TEMPLATE")`
- [ ] Discrepancies between claimed and re-executed results documented with rationale

## WEB APP TASK

- [ ] All interactive features verified working — click every button, test every input, confirm every mode
- [ ] Error states handled: empty config, broken JSON, missing DOM elements show user-facing messages (not console errors)
- [ ] Cross-browser screenshots captured: Chrome + Firefox (minimum)
- [ ] Console audit: zero unexpected errors on page load and during ALL interaction paths
- [ ] Mobile responsiveness check OR explicit "desktop-only" declaration visible in UI
- [ ] Accessibility baseline: color contrast ratios pass WCAG AA, keyboard-navigable, alt text on key visuals
- [ ] All assets load from live URL (zero 404s on JS/CSS/images — verify with browser network tab)
- [ ] `<title>`, `<meta description>`, and Open Graph tags present in `<head>`
- [ ] `.nojekyll` file present at root (GitHub Pages requirement)
- [ ] Test suite executed with zero failures — verified by re-execution, NOT by checking file existence
- [ ] LEARNINGS.md updated with any issues found during testing
- [ ] BACKLOG.md: all P1 items triaged (complete, migrate to next sprint, or explicitly defer with rationale)
- [ ] File committed with format: `ACTION:[CREATE|EDIT] FILE: path RATIONALE:reason`
- [ ] `git log -1 --oneline` confirms commit exists

## QWAV-Specific Additions

### Strategy Document Task (beyond DOCUMENT)

- [ ] Cross-referenced against all prior strategy documents (0.1 through current version)
- [ ] All 13 D-constraints (D1-D13) verified not violated
- [ ] All 23 L-lessons (L1-L23) consulted for relevant prevention rules
- [ ] PROJECT STATE.md, SPRINT.md, CHANGELOG.md updated to reflect new strategy posture

### Spinoff Handoff Task

- [ ] Handoff document written with research trail, expected output, return protocol
- [ ] Project directory scaffolded with 7 mandatory docs + initial SPRINT.md
- [ ] PROJECT STATE.md spinoff registry updated
- [ ] BACKLOG.md spinoff item status updated

---
*Generated from DEFINITION-OF-DONE-TEMPLATE.md v1.0*
