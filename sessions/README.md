# Session Export Directory

> Full DeepChat conversation exports for audit trail and provenance tracking.

## Structure

```
sessions/
  YYYY/
    MM/
      DD-session-topic.md
```

## Naming Convention

`YYYY-MM-DD-session-topic.md`

Examples:
- `2026-05-23-sprint-18-review.md`
- `2026-05-24-sprint-19-execution.md`

## Workflow

1. **After each session**: Export conversation from DeepChat → File
2. **Save export** to `sessions/YYYY/MM/DD-topic.md`
3. **Post Discussion** on GitHub with session summary (see template)
4. **Cross-link**: Discussion references Issues, Commits, Milestones

## Discussion Template

See [Discussion #13](https://github.com/QNFO/QWAV/discussions/13) for the full pipeline documentation.

## Categories (GitHub Discussions)

Create via Settings → Discussions → Categories:

| Category | Purpose | Emoji |
|:---------|:--------|:------|
| Session Records | LLM session logs | 📓 |
| Sprint Reports | Sprint completion reports | 📊 |
| Decisions | Architectural decisions | 📝 |

## Storage Policy

- **Session summaries**: Posted as GitHub Discussions (permanent, searchable)
- **Full exports**: Stored in this directory and/or as GitHub Gists
- **Cross-references**: Discussion ↔ Issue ↔ Commit, all linked

## Current State

- [x] Discussions enabled (6 default categories)
- [x] First sessions posted (#12, #13)
- [ ] Custom categories created (needs web UI)
- [ ] Historical exports posted (15 in Downloads/)
- [ ] Automated post-session workflow

---

*Part of QWAV audit infrastructure. Every LLM interaction preserved.*
