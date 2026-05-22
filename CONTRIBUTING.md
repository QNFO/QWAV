---
template: CONTRIBUTING
version: "1.0"
---

# CONTRIBUTING.md — QWAV

How agents work in this project. Inherits all rules from `prompts/CONTRIBUTING.md`.
This file adds project-specific additions.

## Project-Specific Definition of Done

See `DEFINITION-OF-DONE.md` for the complete task completion criteria. QWAV-specific additions:

- **Strategy Document Task:** Cross-reference against all prior strategy versions. Verify no D1-D13 violations. Consult all L1-L23 learnings. Update PROJECT STATE, SPRINT, CHANGELOG.
- **Spinoff Handoff Task:** Handoff document with research trail + expected output + return protocol. Scaffold project directory with 7 mandatory docs. Update spinoff registry.

## Project-Specific Verification Gates

### Pre-Work Gates (Every Session)
1. **Git Identity:** `git branch --show-current` — must be on `feature/qwav-*`. Never on `main`.
2. **CROSS-PROJECT-LEARNINGS:** Read `G:\My Drive\projects\_shared\CROSS-PROJECT-LEARNINGS.md` for relevant lessons.
3. **Due Diligence (§0.8):** Search Archive, Obsidian/releases, and sibling projects for prior work before writing substantive content.
4. **Documentation Audit:** All 7 core docs exist and are non-empty. Read PROJECT STATE.md first.

### Post-Work Gates (Every Session)
1. **Git Audit:** `git log -1 --oneline` confirms all changes committed. `git status --short` is clean.
2. **Documentation Sync:** PROJECT STATE.md, SPRINT.md, CHANGELOG.md updated with session summary.
3. **Learnings Capture:** Any new lessons added to LEARNINGS.md in L<N> format.
4. **Math Format Scan:** All output scanned for bare Unicode math characters (Rule 6).

### Pre-Publication Gates
1. **Publication Language Gate (§11.7):** Zero internal project language in external-facing documents.
2. **Reader Testing (§11.5):** Minimum 2 rounds for publication documents.
3. **Curly Quotes Scan:** Python verification of typographic quotes throughout.
4. **DOI Verification:** No placeholder DOIs (`########`). Real DOI or `[DOI-PENDING]`.

## Project-Specific Risks

See `RISK-REGISTER.md` for the complete risk inventory. Key QWAV-specific risks:

- **R1: Obscurity** — primary strategic risk. Mitigated by interactive artifacts (D13) and qwav.tech site.
- **R4: Application exhaustion** — baseline scenario. Mitigated by strategy/3.0 endogenous momentum.
- **R5: Founder burnout** — mitigated by sustainable cadence and low-intensity design.

## Domain Rules

### QWAV-Only Rules
- **Geometry precision:** Always distinguish Archimedean ($\mathbb{R}^n$, continuous) from ultrametric ($p$-adic, tree-based) geometry. Never conflate them.
- **Thesis consistency:** Every publication must trace back to the core thesis: replacing continuous geometry with ultrametric geometry solves QC fault tolerance and AI explainability.
- **Evidence standard:** All quantitative claims about error rates, benchmarks, or computational results must be `[CODE-EXECUTED]` — traceable to specific Python scripts with re-executable output.
- **Citation traceability:** Every external reference must have a verifiable source file in the project directory or Obsidian/releases. No fabricated citations.
- **D13 compliance:** Every spinoff must produce an interactive public artifact. The paper is archival backstop, not primary output.
- **Constraint discipline:** Before any action, verify it does not violate D1-D13. If uncertain, DON'T.

### Writing Standards for External Documents
- **No internal project language:** Strategy documents and handoff protocols stay in QWAV repo. External publications use standalone, accessible language.
- **No credential claims:** The work speaks for itself. No institutional name-dropping, no PhD equivalency claims, no "as seen in" references.
- **Evidence-first framing:** "Here's what we found. Here's how we tested it. Here's the code so you can verify." Not: "Here's why we're credible."

## Git Conventions

- Branch prefix: `feature/qwav-<description>-<YYYY-MM-DD>`
- No branch reuse across projects (CPL L20)
- All git commands use `-C "G:\My Drive\QWAV"` flag
- Commit format: `ACTION:[CREATE|EDIT|DELETE] FILE: <relative-path> RATIONALE:<brief-reason>`
- Never commit to `main` (CPL L1)

## Escalation

If blocked:
1. Check RISK-REGISTER.md for known mitigations
2. Check CROSS-PROJECT-LEARNINGS.md for applicable lessons
3. Check QWAV LEARNINGS.md for project-specific lessons (L1-L23)
4. Report blocking condition to human with: what was tried, what failed, alternatives

## Agent Workflow

### QWAV Agent (This Repository)
- **Scope:** Strategy, documentation, portfolio coordination, publication management, social distribution, application pipeline, spinoff initiation and handoff
- **Does NOT:** Execute computational work, write production code, perform deep research requiring extended Archive exploration

### Projects Agent (Project Repositories)
- **Scope:** Computational simulation, code implementation, data analysis, deep research, prototype and PoC development
- **Receives:** Handoff documents from QWAV Agent with research trail, expected output, return protocol
- **Returns:** Completed deliverables to `Obsidian/releases/YYYY/MM/`

### Boundary Rule
When the next task is project execution (computation, deep research, implementation):
1. QWAV Agent creates a clear handoff document
2. Updates SPRINT.md to reflect delegation
3. PAUSES — waits for Projects Agent to complete the work
4. On return: reviews deliverable, updates documentation, coordinates next steps

---
*Generated from CONTRIBUTING-TEMPLATE.md v1.0*
