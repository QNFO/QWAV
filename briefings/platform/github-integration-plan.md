# QWAV -- GITHUB INTEGRATION PLAN

**Status:** Comprehensive audit complete 2026-05-24. All org + repo settings documented.  
**Branch:** `feature/sprint-19-planning`  
**Next:** Import SPRINT.md → Issues. Create Project board. Init Wiki.

---

## 1. QNFO ORG AUDIT -- Full Settings (2026-05-24)

| Setting | Value | Notes |
|:--------|:------|:------|
| Plan | Free | 3 channel limit on Buffer |
| Members | rowan.quni (owner) | Solo org |
| 2FA Requirement | Not enforced | Recommended |
| Base Permissions | Read | Correct for public org |
| Repository Creation | All members | Only owner exists |
| Organization Projects | Enabled | Cross-repo boards possible |
| Repository Projects | Enabled | Per-repo boards |
| Copilot | Free tier | 2,000 completions/mo per user |
| Discussions (org-wide) | `.github` repo | https://github.com/QNFO/.github/discussions |
| IP Allow List | Not configured | Not needed for public org |

### 1.1 Security Features (Org-Level)

| Feature | Status | Detail |
|:--------|:------:|:-------|
| Dependabot Alerts | ✅ Enabled | All 7 repos |
| Dependabot Security Updates | ❌ Not enabled | Would require auto-PR capability |
| Secret Scanning | ✅ Enabled | Org-level |
| Push Protection | ✅ Enabled | Org-level |
| Code Scanning (CodeQL) | Setup available | Not yet configured |

---

## 2. QWAV REPO AUDIT -- `QNFO/QWAV`

| Setting | Value | URL |
|:--------|:------|:----|
| Visibility | Public | github.com/QNFO/QWAV |
| Default Branch | `main` | Branch protection active |
| Issues | ✅ Enabled | github.com/QNFO/QWAV/issues |
| Projects | ✅ Enabled | github.com/QNFO/QWAV/projects |
| Discussions | ✅ Enabled (6 categories) | github.com/QNFO/QWAV/discussions |
| Wiki | ✅ Enabled (needs 1st page) | github.com/QNFO/QWAV/wiki |
| Pages | ✅ Live | qnfo.github.io/QWAV |
| Actions | ✅ Enabled | Workflows functional |
| Branch Protection | ✅ Active on `main` | 1 approving review required |
| Merge Options | Squash + Rebase | No merge commits |
| Automated Deletions | ❌ Off | Head branches preserved |
| License | ❌ Not set | Previously claimed "MIT" -- WRONG |
| Description | QWAV Program -- Ultrametric Quantum Computing & AI | Added 2026-05-24 |
| Tags | ultrametric, quantum-computing, ai | Active |
| Social Preview | Not configured | Optional |
| CITATION.cff | Added | Placeholder -- needs DOI |


## 3. ARTIFACT REPO AUDIT (A1-A5)

| Repo | Description | Branch Protection |
|:-----|:------------|:----------------:|
| ultrametric-error-confinement | Tier 0: Bruhat-Tits tree error simulation | Not configured |
| Q-PNA | Quantum-Native p-Adic Neural Architecture v2.0 | Not configured |
| tree-distance | Tree Distance Sandbox -- interactive comparison | Not configured |
| ultrametric-convergence | Convergence Explorer -- ultrametric clustering | Not configured |
| hardware-pathway | Error suppression demo -- Three.js visualization | Not configured |

---

## 4. DEEPCHAT INTEGRATION PLAN -- Agent Workflow Mapping

### 4.1 Current State (File-Based)

| Doc | Purpose | Lines | Can Migrate To |
|:----|:--------|:------|:---------------|
| `SPRINT.md` | Active sprint tasks | ~900 | GitHub Issues + Project board |
| `BACKLOG.md` | Future work queue | ~200 | GitHub Issues (labeled `backlog`) |
| `PROJECT STATE.md` | Session handoff | ~400 | Wiki (or Issues with `handoff` label) |
| `LEARNINGS.md` | Kaizen engine | ~200 | Wiki |
| `DECISIONS.md` | Architecture decisions | ~50 | Wiki |
| `CHANGELOG.md` | Version history | ~1,300 | GitHub Releases |
| `FINAL_AUDIT_REPORT.md` | One-off report | ~340 | GitHub Issue |

### 4.2 Proposed Mapping

```
SPRINT.md tasks ──────► GitHub Issues (labeled: sprint, P0-P3)
BACKLOG.md items ─────► GitHub Issues (labeled: backlog, future)
PROJECT STATE.md ─────► Wiki "Session Handoff" page
LEARNINGS.md ─────────► Wiki "Learnings" page
DECISIONS.md ─────────► Wiki "Decisions" page
CHANGELOG.md ─────────► GitHub Releases (tag-based)
Sprint board ─────────► GitHub Projects (Kanban view)
Buffer queue ─────────► External -- not GitHub-managed
Test evidence ────────► GitHub Actions workflow output
```

### 4.3 GitHub API Access from DeepChat

The agent already has full GitHub access via `gh` CLI through `exec`:

```bash
# Issues
gh issue create --repo QNFO/QWAV --title "Task" --body "..." --label "sprint,P1"
gh issue list --repo QNFO/QWAV --label "sprint" --json number,title,state
gh issue close 1 --repo QNFO/QWAV

# Projects
gh project list --owner QNFO --format json
gh project item-list 1 --owner QNFO --format json

# Discussions
gh api graphql -f query='{repository(owner:"QNFO",name:"QWAV"){discussions(first:10){nodes{title url}}}}'

# Wiki (git-based)
git clone https://github.com/QNFO/QWAV.wiki.git

# Branch protection
gh api /repos/QNFO/QWAV/branches/main/protection

# GraphQL (complex queries)
gh api graphql -f query='{repository(owner:"QNFO",name:"QWAV"){...}}'
```

### 4.4 System Prompt Additions Needed

| Section | What to Add |
|:--------|:------------|
| **§0.7 Project Docs** | Add mapping: SPRINT.md → Issues, BACKLOG.md → Issues(backlog) |
| **§9 Git Protocol** | Add `gh issue` commands for sprint task opening/closing |
| **§11 Publication** | Add GitHub Release creation for CHANGELOG entries |
| **§11.5 Reader Testing** | Add Discussion creation for community feedback |
| **New section** | "GitHub Integration -- Issues/Projects/Wiki/Discussions" mapping |

### 4.5 Integration Depth -- Phased Approach

**Phase 1 (NOW): Dual Tracking**
- Keep SPRINT.md + BACKLOG.md as authoritative
- Mirror tasks to GitHub Issues (read-only from agent perspective)
- Agent: read SPRINT.md → update Issues → commit SPRINT.md

**Phase 2 (Next): Issues as Primary**
- GitHub Issues become the sprint task source of truth
- SPRINT.md auto-generated from `gh issue list` output
- Agent: create/update/close Issues directly, regenerate SPRINT.md

**Phase 3 (Future): Full GitHub-Native**
- All project management lives on GitHub
- SPRINT.md deprecated; replaced by Project board + Issues
- DeepChat agents use GitHub API exclusively for task management
- Wiki replaces PROJECT STATE.md handoff

---

## 5. IMMEDIATE FIXES -- Sprint 19 Tasks

| ID | Task | Est. | Priority |
|:---|:-----|:-----|:---------|
| S19.1 | Import 19 active BACKLOG items as GitHub Issues | 0.5h | P0 |
| S19.2 | Create "QWAV Sprint Board" Project with columns: Backlog → To Do → In Progress → Done | 0.5h | P0 |
| S19.3 | Initialize Wiki -- create Home page with program overview + links | 0.25h | P1 |
| S19.4 | Add Issue labels: `sprint`, `backlog`, `P0`, `P1`, `P2`, `P3`, `bug`, `enhancement`, `documentation` | 0.25h | P1 |
| S19.5 | Add Issue templates: Sprint Task, Bug Report, Feature Request | 0.5h | P2 |
| S19.6 | Enable Dependabot security updates on all 7 repos | 0.25h | P2 |
| S19.7 | Add real CITATION.cff with DOI to all repos | 0.5h | P2 |
| S19.8 | Write `docs/github-agent-workflow.md` -- the agent's reference for GitHub ops | 0.5h | P1 |
| S19.9 | Sprint close-out | 0.25h | P2 |

---

## 6. GITHUB REPOS -- COMPLETE INVENTORY

| # | Repo | Description | Pages | Branch Protection |
|:--|:-----|:------------|:-----:|:-----------------:|
| 1 | QWAV | Program overview | ✅ | ✅ Active |
| 2 | .github | Org profile README | -- | -- |
| 3 | ultrametric-error-confinement | Error simulation | ✅ | ❌ |
| 4 | Q-PNA | Neural architecture | ✅ | ❌ |
| 5 | tree-distance | Comparison sandbox | ✅ | ❌ |
| 6 | ultrametric-convergence | Clustering explorer | ✅ | ❌ |
| 7 | hardware-pathway | Error suppression demo | ✅ | ❌ |

---

## 7. HOW TO UPDATE THE SYSTEM PROMPT

The system prompt lives at `G:\My Drive\prompts\ARCHITECTURE.md` (or equivalent). Add this section after §9 (Git Workspace):

```markdown
### 9.9 GITHUB PROJECT MANAGEMENT -- Issues, Projects, Wiki, Discussions

#### Issues → Sprint Tasks
- Read SPRINT.md → for each `[ ]` task, create GitHub Issue with `gh issue create`
- Label: `sprint`, priority (`P0`-`P3`), domain
- On task completion: `gh issue close <num>` + mark SPRINT.md `[x]`

#### Projects → Kanban Board  
- `gh project list --owner QNFO` → find "QWAV Sprint Board"
- Issues auto-appear when added to project
- Manual status updates on the board

#### Wiki → Documentation
- Clone: `git clone https://github.com/QNFO/QWAV.wiki.git`
- Edit Home.md, Session-Handoff.md, Learnings.md
- Push: `git push origin master`

#### Discussions → Community
- Weekly: `gh api graphql` to fetch new discussions
- REVIEWER subagent scans for unanswered Q&A
- QWAV agent drafts responses, awaits founder approval

#### GraphQL Reference
```graphql
# Get repo ID
query { repository(owner:"QNFO", name:"QWAV") { id } }
# Get discussion categories
query { repository(owner:"QNFO", name:"QWAV") { discussionCategories(first:10) { nodes { id name } } } }
# Create discussion  
mutation { createDiscussion(input: {repositoryId:"REPO_ID", title:"TITLE", body:"BODY", categoryId:"CAT_ID"}) { discussion { url } } }
```
```

---

*Integration Plan v1.0 -- 2026-05-24. Sprint 19 will execute Phase 1 of this plan.*
