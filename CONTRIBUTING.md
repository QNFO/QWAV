# CONTRIBUTING — 2026-05-23

## How to Work on This Project

### Agent Setup (New Session)
1. Read PROJECT STATE.md — understand current status
2. Read SPRINT.md — identify active task
3. Read LEARNINGS.md — avoid repeating mistakes
4. Read CHANGELOG.md (last entry) — know what just changed
5. Verify git branch with `git branch --show-current`
6. All work on feature/ branches per QWAV Git Protocol (§9)

### File Naming
- Project management files: fixed names (README.md, SPRINT.md, etc.)
- Content files: MAJOR.MINOR.ext versioning (§10)

### Git Discipline
- NEVER commit to main/master directly
- Feature branches: `feature/<description>`
- Commit format: `ACTION:[CREATE|EDIT|DELETE] FILE: <path> RATIONALE:<reason>`
- Full protocol: DEFAULT.md §9

### Development Environment
- Python: Standard library only unless specified
- Web: Single HTML file with inline CSS/JS (no build step)
- Git: Use `-C "<project_path>"` flag for project repos

### Quality Gates
- Before merge: All tests pass, git worktree clean
- Before deploy: Canvas renders, no JS errors, mobile check
- Before close-out: All tasks marked [x], docs updated, final audit

---

*QWAV Projects Agent workflow. See DEFAULT.md for full protocol.*
