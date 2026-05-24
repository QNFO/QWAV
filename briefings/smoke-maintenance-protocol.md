# Smoke Test Maintenance Protocol

> **Purpose:** Scheduled verification that all QWAV artifacts remain functional.
> **Last verified:** 2026-05-24 — 102/102 PASS
> **Sprint:** 22 (automation)

---

## Test Suites

| Suite | Tests | Type | Command |
|:------|:------|:-----|:--------|
| Structural | 42 | unittest (via pytest) | `python -m pytest test_all_artifacts.py -q` |
| Parametrized | 60 | pytest | `python -m pytest test_all_artifacts_pytest.py -q` |
| Browser Smoke | CDP | Python script | `python test_smoke.py` |

**Total:** 102 structural + browser smoke tests.

## Schedule

### Automated (GitHub Actions)

- **Workflow:** `.github/workflows/smoke-tests.yml`
- **Schedule:** Every Monday at 09:00 UTC
- **Manual trigger:** `gh workflow run smoke-tests.yml --repo QNFO/QWAV`
- **On push:** Can be added if needed

### Manual Protocol (if needed)

```bash
cd "G:\My Drive\QWAV"
python -m pytest test_all_artifacts.py test_all_artifacts_pytest.py -q
python test_smoke.py
```

## What to Check

1. **All 102 tests pass** — no regressions
2. **No JavaScript errors** — browser console clean
3. **All artifact URLs resolve** — GitHub Pages healthy
4. **No CDN dependencies** — all artifacts self-contained

## Failure Response

| Severity | Action |
|:---------|:-------|
| Test failure | Create GitHub Issue with `bug` label, assign to current sprint |
| URL down | Check GitHub Pages status → re-trigger deploy if needed |
| JS error | Check `test_browser_errors.py` output → fix source artifact |

## History

| Date | Result | Notes |
|:-----|:-------|:------|
| 2026-05-24 | 102/102 PASS | Sprint 22 — automation implemented |
