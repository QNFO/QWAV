# AGENTS.md: universal instructions for every code agent

Read by Claude Code (via CLAUDE.md import), GitHub Copilot, Kimi, OpenAI Codex and any other agent.
No agent depends on another agent's chat history. GitHub is the shared memory.

## 1. Rules that never change
- Work from the repo, never from chat memory. If it is not in an issue, a PR or `docs/handoff/`, it did not happen.
- Never handle keys, passwords or tokens in output, commits or issues. Keep everything keyless.
- Published and sent content must be accurate and checked against sources. No invented facts.
- Cloudflare (D1, R2, KV) holds canonical runtime state. Nothing canonical lives in a chat or artifact.
- Follow the repo's CLAUDE.md lifecycle rules (SDLC-OWN-1) if present: define, research, design, build, test, deploy, verify, measure, iterate.

## 2. The handoff loop (how agents hand work to each other)
1. **Start**: read `docs/handoff/` (newest first) and the open issues labelled `agent-ready`. Pick one. Comment `claim: <agent> <date>` on the issue.
2. **Work on a branch** named `agent/<issue#>-<slug>`. Open a **draft PR** within the first few minutes.
3. **Checkpoint early and often**: after each stage (research, design, front end, back end, deploy) commit and update `docs/handoff/<slug>.md` from `docs/handoff/TEMPLATE.md`. Budget can run out at any time; an unpushed stage is a lost stage.
4. **Stop cleanly**: when budget is low, finish the current commit, update the handoff file (state, decisions, next step, how to verify), push, and comment on the issue `released: <agent>, next: <step>`.
5. **Finish**: tests green, live probe passes, handoff file marked `status: done`, PR marked ready, follow-up issues filed.

## 3. Issue format (any agent must be able to finish it cold)
Problem, context, files/paths, acceptance criteria, test plan, closing probe, size (`S`/`M`/`L`), `front:` and `back:` lines (both sides ship together, or the counterpart is its own issue).

## 4. Routing by plan (flat-fee plans run out; spread work, do not queue it)
| Work type | Preferred agent | Why |
|---|---|---|
| Large refactors, architecture, multi-file design | Claude Code | strongest planning; spend its budget here |
| Well-specified issues, small/medium features, tests | GitHub Copilot coding agent | assigned straight from an issue, produces draft PRs |
| Bulk edits, docs, boilerplate, long-context reading | Kimi | cheap, long context |
| Overflow and second opinions | OpenAI Codex (flat plan) | any `agent-ready` issue |
Rule: when one agent's budget is gone, the next agent picks up the same issue from its handoff file. Labels: `agent-ready`, `claimed`, `needs-review`, `blocked:<reason>`.

## 5. Velocity rule: features, not only fixes
Each repo keeps a roadmap issue ("Roadmap: next 5 features") with at most 5 items, each with goal, user, success metric. Agents pull from it before pulling bug fixes. At least 1 in 3 merged PRs per repo should be a user-visible feature. Every feature PR names its metric and how it will be measured.

## 6. Review and safety
- Agents do not review their own PRs. Copilot code review or a different agent checks `needs-review` PRs.
- CI must pass before merge. Auto-merge is allowed only for PRs whose checks are green.
- Each PR description ends with what was verified and the evidence.

## 7. Self-audit and no standalone documents (owner directive 2026-11-06)
- Before and after every delivery, audit the work against real output (run it, probe it). Name what you are not thinking about; fix it or file it as an issue with a closing probe. There is always room to improve.
- A document is never a deliverable on its own. Every output ships with running code, a PR, an issue or a roadmap entry. Existing write-ups that were never implemented become roadmap items with code.
- `scripts/audit.py` (run every 6h by `.github/workflows/fleet-audit.yml`) checks all active repos and files issues for gaps. Fix findings labelled `fleet-audit` before starting new work.
- Never stop at "waiting for the owner". If an action is reversible and in scope, do it; if it is truly blocked, file the blocker as an issue with an owner and a closing probe, then continue with other work.
