# QWAV PROGRAM LEARNINGS

> **Purpose:** Program-level lessons discovered during execution. Machine-readable format for kaizen (continuous improvement). Read this before starting new work to avoid repeating mistakes.

**Last updated:** 2026-05-23 | **Status:** 27 lessons (L1-L27). L18 archived. L18 archived (CLOSED). L24 (Build gravity, don't wait for permission — endogenous momentum > exogenous validation) added as direct result of strategy reframe confirmed by founder.

---

### L25: All deliverables MUST have a detailed, executed test plan — "Deployed" is not "Done," "Clicked the slider" is not "Tested"

- **Category:** METHODOLOGY
- **Issue:** The 2026-05-23 cross-project audit revealed that 6 of 8 active projects (A1-A5 + K1 — the entire Build Phase portfolio) have ZERO automated tests. Their "test" consists of a single checkbox: "Verify live URL." The Definition of Done files contained checkbox theater — `[x]` marks next to claims like "tested: slider movement → canvas redraw" with no test script, no test log, no screenshot, and no automated verification. One project (A2) contains hardcoded fake accuracy numbers that were never validated against any dataset. Only one project (Game of Life) has an actual executed test suite — and it found 7 real failures (46/53 pass).

The pattern is systemic: deliverables are declared "complete" and "deployed" the moment a URL loads, with zero verification that the code actually works, the math is correct, or the claims match reality. This produces a portfolio of untested prototypes masquerading as finished products.

- **Solution:** Every deliverable — code, document, or artifact — must include:
  1. **A test plan file** (`test_plan.py` or equivalent) with specific, executable test cases and expected results, written BEFORE the deliverable is declared complete.
  2. **Execution evidence** — a test log, screenshot, or terminal output showing tests were run and results recorded.
  3. **Pass/fail accounting** — honest reporting of what passed and what failed, with documented explanations for failures.
  4. **The test plan is part of the Definition of Done** — a deliverable CANNOT be marked `[x]` complete until its test plan is written AND executed.

  The Game of Life project (46/53 pass, 7 documented failures) is the model. Every other project should match this standard.

- **Prevention:** 
  - Add "Test Plan Executed" as a mandatory gate in every DEFINITION-OF-DONE.md template.
  - The SPRINT.md "Verify live URL" task must be replaced with "Execute test plan: N/N pass" as the completion condition.
  - No deliverable may be marked DEPLOYED or COMPLETE in PROJECT STATE.md until test results are committed.
  - Audit question for every project review: "Show me the test plan. Show me the test results."

- **Cross-Project:** YES — This applies to all projects. The checkbox-theater pattern was found across every Build Phase artifact. Any future project spun off from QWAV or initiated independently must have test plans as a Definition of Done prerequisite.


### L26: Email outreach must be high-impact and targeted — no booster language, just the work

- **Category:** METHODOLOGY — OUTREACH
- **Issue:** Outreach templates drafted in the 2026-05-23 session used booster language ("48x error reduction," "zero errors at depth 7," "groundbreaking," "the hardware story") in cold emails. This language is marketing copy that undermines credibility. The same templates were aimed at generic corporate addresses (info@company.com) rather than specific named individuals with relevant expertise. Cold emailing generic addresses has near-zero success probability and wastes time.
- **Solution:** Every outreach email must follow these rules:
  1. **No booster language.** Strip "demonstrate," "proves," "48x," "breakthrough," "groundbreaking." Replace with "explores," "suggests," "indicates."
  2. **One link, one paragraph.** Body less than or equal to 8 sentences. A single link to the technical hub or a specific artifact. Let the recipient decide if they're interested.
  3. **Specific named individuals only.** No info@company.com. No C-level executives without a warm introduction. Target: arXiv authors who published on the exact topic, postdocs at relevant labs, conference attendees with shared research interests.
  4. **Affirmative opt-in before sending.** Drafts are saved for review. Never send without explicit user "yes" confirmation.
  5. **"Explore" not "demonstrate."** Honest uncertainty is more credible than false certainty.
- **Prevention:** The QWAV agent must not draft outreach emails unless the user initiates the request. Drafts must be reviewed against a checklist: (a) booster language stripped? (b) specific named recipient? (c) less than or equal to 8 sentences? (d) single link? (e) user approved? If any check fails, BLOCK the send.
- **Cross-Project:** YES — applies to all projects. The booster-language antipattern appeared across all 5 lab outreach templates and the summer school application.

### L27: Cold outreach is antithetical to the introvert path — the founder finds it draining

- **Category:** METHODOLOGY — FOUNDER CONSTRAINT
- **Issue:** The 2026-05-23 session drifted from the written-first strategy into cold outreach mode: drafting lab emails, searching LinkedIn for contacts, preparing templates for unsolicited messages. This violates Strategy 3.0's core constraint: "The introvert path is the path. No networking, no live pitching, no conference schmoozing. All communication is written." Cold email outreach — even well-crafted — is the written equivalent of networking. It drains the founder and has low expected return.
- **Solution:** The QWAV agent must default to introvert-compatible actions:
  1. **Conference abstract submissions** — write once, submit, the committee decides. No personal outreach required.
  2. **Publication pipeline** — Zenodo DOIs, cross-links, SEO. The work finds its audience organically.
  3. **Scheduled social media** — Buffer posts. No personal interaction required.
  4. **Archiving and documenting** — lessons, charters, test plans. Building the asset base that speaks for itself.
  Cold email outreach is permitted ONLY when the founder explicitly requests it for a specific named individual with a warm introduction or shared context.
- **Prevention:** The QWAV agent must not draft cold outreach emails unless: (a) the user initiates the request, (b) a specific named individual is identified, (c) there is a warm connection or shared context, (d) the email is reviewed and approved by the user before sending. If the user says "no cold emails" or "this is draining," the agent stops immediately and pivots to introvert-compatible actions.
- **Cross-Project:** YES — applies to all projects. The written-first, introvert-path constraint is a non-negotiable design decision per Strategy 3.0.


## Active Learnings

### L1: Computational validation is the highest-leverage evidence generator
- **Category:** METHODOLOGY
- **Issue:** Without a lab or experimental collaborator, QWAV had zero empirical evidence despite 300+ publications and a sound mathematical thesis.
- **Solution:** The Tier 0 Python simulation (Bruhat-Tits tree circuits, error injection, metrics) produces reproducible, shareable, citable data without any physical equipment. Experiment 0A demonstrated LER=0 at depth 3+ for physical error rates up to 40% — a result that generates its own credibility.
- **Prevention:** When blocked on physical experiments, always ask: "Can this be simulated computationally?" If yes, simulation is faster, cheaper, and fully under your control.
- **Cross-Project:** YES — any deep-tech venture facing experimental bottlenecks should consider computational validation as a legitimate first step.

### L2: The library-based writing strategy works
- **Category:** METHODOLOGY
- **Issue:** Writing bespoke applications from scratch for each opportunity is unsustainable for a solo founder. The founder had 300+ papers but no modular way to assemble them into applications.
- **Solution:** The M1–M12 narrative module library enables rapid application assembly: grab relevant modules, customize the framing, submit. Three applications submitted in May 2026 with minimal friction.
- **Prevention:** For any project requiring repeated written submissions (grants, fellowships, proposals), invest upfront in modular content libraries. Reuse over rewrite.
- **Cross-Project:** YES — applicable to any solo founder or small team doing repeated written outreach.

### L3: Volume alone doesn't convert — evidence does
- **Category:** METHODOLOGY
- **Issue:** 300+ open-access publications over years did not organically attract experimental collaborators, funding, or institutional support. "Publish and hope" failed.
- **Solution:** Active outreach (written applications to specific programs) + computational evidence (Tier 0 simulation) + targeted collaboration (P11 collaborator for Lean formalization) replaced passive publishing. The 301st paper won't do what the first 300 didn't — a different approach is needed.
- **Prevention:** If a strategy hasn't produced results after significant investment (300 papers), don't double down — change the strategy.
- **Cross-Project:** YES

### L4: Patent filing without a conversion plan is pure cost
- **Category:** METHODOLOGY
- **Issue:** Estimated 18 previous provisional patents were filed (~$6,000 total spend), and zero converted to PCT or utility patents. No licensing revenue. No strategic value realized.
- **Solution:** Quantitative EV analysis (`strategy/0.1.md` internal cost-benefit): conversion probability ~5%, licensing probability ~0.26%, expected net value negative in all scenarios. New rule: FILE ONLY IF a specific, funded 12-month conversion plan exists.
- **Prevention:** Before any patent filing, run a cost-benefit model. If expected net value is negative, don't file — wait until circumstances change.
- **Cross-Project:** YES — applicable to any IP-heavy venture.

### L5: The introvert path is not a limitation — it's a filter
- **Category:** METHODOLOGY
- **Issue:** Traditional startup advice demands networking, live pitching, conference attendance — all draining for an introvert founder. Felt like a deficit.
- **Solution:** Reframed introversion as a strategic filter: written-only communication selects for audiences that evaluate substance over presentation. Programs like Emergent Ventures, Foresight Institute, and EWOR explicitly evaluate ideas on merit. The path is sustainable and energizing rather than draining.
- **Prevention:** Design workflows around founder energy patterns, not around external expectations. A sustainable path beats an ambitious burnout path.
- **Cross-Project:** YES

### L6: Git branch discipline prevents context loss
- **Category:** GIT
- **Issue:** Working directly on `main`/`master` makes it impossible to isolate experiments, track parallel workstreams, or recover from mistakes. Multiple sessions on `main` created ambiguity about what changed when.
- **Solution:** All work now happens on `feature/<name>` branches. `main` is protected — receives only completed, reviewed work. Each meaningful change gets its own commit with descriptive messages.
- **Prevention:** Never work on `main`. Always create a feature branch before any file operation.
- **Cross-Project:** YES

### L7: Open-access publishing bypasses gatekeepers but doesn't bypass the evidence gap
- **Category:** METHODOLOGY
- **Issue:** The founder correctly identified peer review as a gatekeeping mechanism and built a 300+ publication corpus through open-access channels (Zenodo, ResearchGate, SSRN). However, open-access alone didn't close the credibility gap — readers still needed computational or experimental evidence.
- **Solution:** Tier 0 simulation + Lean 4 formal verification (via P11 formal verification collaboration) provide the evidence layer. Open-access ensures the evidence is accessible; the evidence itself must exist first.
- **Prevention:** Publishing strategy and evidence strategy are separate concerns. Open-access solves distribution, not credibility. Credibility comes from falsifiable, reproducible results.
- **Cross-Project:** YES

---

### L8: Computational validation produced first published evidence for the thesis
- **Category:** METHODOLOGY
- **Issue:** The QWAV thesis lacked any published, reproducible, citable evidence. Without a lab or collaborator, the evidence gap seemed insurmountable.
- **Solution:** The Tier 0 Python simulation produced quantitative, reproducible results (LER=0 at depth 3+ for error rates up to 40%; energy barrier exponential in tree depth) that were packaged into a formal paper and published on Zenodo (DOI: 10.5281/zenodo.20134944). The entire pipeline — code, experiments, paper — was executed solo with zero external dependencies. The publication now serves as citable, verifiable evidence for applications.
- **Prevention:** When blocked on physical experiments, computational validation is not a "consolation prize" — it is a legitimate, publication-worthy path in its own right. The paper is the evidence.
- **Cross-Project:** YES — any deep-tech venture facing experimental bottlenecks should treat computational validation as a primary publication strategy.

---

### L9: LLM-hostile programs are structurally incompatible with QWAV's workflow
- **Category:** METHODOLOGY
- **Issue:** VSD explicitly prohibits LLM-generated submissions and disqualifies applicants who use them. It also prohibits applicants from developing existing ideas/IP — a direct conflict with QWAV, which IS an existing body of work refined through iterative LLM-augmented sessions. These policies are not quirks — they are structural hostility to the solo-founder-with-AI-tools methodology that makes QWAV possible.
- **Solution:** Before applying to any program, audit for LLM policies and "existing IP" clauses. Programs that ban AI tools are incompatible with the QWAV workflow regardless of how strong the application is. The rejection confirms a known filter: some programs want blank-slate students, not founders with existing research programs. That's fine — it's a mismatch, not a failure.
- **Prevention:** Add "LLM policy audit" and "existing IP clause check" to the pre-application checklist. Any program with explicit LLM bans or "no existing IP" clauses should be skipped. The filter works in both directions.
- **Cross-Project:** YES — any venture that relies on AI-augmented workflows must screen for these policies before investing application effort.

---

### L10: Technical objections can be competitive positioning disguised as rigor
- **Category:** METHODOLOGY
- **Issue:** A potential collaborator raised detailed technical objections to the Tier 0 paper. On inspection, every objection — if sustained — would protect the objector's own commercial positioning (software-based QEC verification) while undermining the paper's thesis (hardware-based passive fault tolerance). The objections were real enough to require answers, but their function was competitive defense, not collaborative rigor. Additionally, the objector disclosed their own competing work ("I have been and am actively working in similar directions") only AFTER extracting detailed technical information about the paper's decoder design, error model, and formalization goals — reversing the proper order of disclosure.
- **Solution:** (1) Identify the objector's commercial positioning. If their business model conflicts with your thesis, treat their "technical feedback" as competitive intelligence, not collaboration scoping. (2) Apply the symmetry test: does the objection apply equally to the objector's own work? ("Classical decoder therefore not quantum" applies to ALL decoder verification, including theirs.) If it does and they didn't mention it, the objection is selective — a gatekeeping word, not a technical standard. (3) Disclose competing work BEFORE asking for technical detail, not after. If someone reverses that order, they're extracting information, not building trust. (4) The "classical vs. quantum" decoder objection is structurally invalid: every QEC decoder is classical by architecture — syndrome extraction (quantum) → classical decoder → correction (quantum). Calling a decoder "classical" is describing what a decoder IS, not identifying a flaw.
- **Prevention:** Before sharing detailed technical information with a potential collaborator, audit their commercial positioning. If it conflicts with yours, treat every "technical question" as also a competitive move. Share only what you'd be comfortable publishing. Get competing-work disclosure upfront.
- **Cross-Project:** YES — any deep-tech venture seeking collaborators must recognize that "collaboration scoping" and "competitive intelligence gathering" look identical in early email exchanges.

**Technical reference — the QEC decoder rebuttal:** *A QEC decoder is a classical algorithm processing classical syndrome bits. The quantum hardware first extracts the syndrome, then the decoder runs, then the hardware applies the correction. Attempting to distinguish a "classical" decoder points out nothing unusual — they all are. Every surface code decoder, every color code decoder, every tree code decoder is classical by architecture. The quantum operations are syndrome extraction and correction application; the decoder sits between them and is classical by design. Anyone who uses "classical" as an objection to a decoder either does not understand the standard QEC architecture or is using it as a rhetorical gatekeeping word.*

### L11: Low-friction email outreach is the highest-leverage written-first networking tool
- **Category:** METHODOLOGY
- **Issue:** The founder had zero active connections to key researchers in ultrametric/p-adic fields despite 300+ publications and a validated computational thesis. "Publish and hope" (L3) didn't build relationships. Traditional networking (conferences, live pitches) violates the Introvert's Path constraint.
- **Solution:** A targeted, low-friction email to a single gatekeeper (W.A. Zuniga-Galindo, organizer of the First International Conference on Models of Complex Hierarchic Systems) opens a door without requiring live interaction. The email asks only binary questions (conference date? unaffiliated researchers welcome?) — answerable in 30 seconds. It references a Zenodo DOI as tangible evidence of substance. It positions the founder as a peer, not a supplicant. Email IS written communication — fully consistent with the Introvert's Path.
- **Prevention:** When blocked on connections, identify the single most relevant gatekeeper in the field. Draft a 5-sentence email that (a) shows you know their work, (b) references your own tangible output, (c) asks one or two binary questions. Do not pitch. Do not overclaim. Do not ask for favors. Low friction wins.
- **Cross-Project:** YES — any solo founder or independent researcher facing the "credential gap" can use this pattern. The key insight: email outreach IS written-first when done right. Conference abstract submission is a viable "back door" (peer-reviewed but not a full paper).

### L12: Ternary ($p=3$) is the definitive sweet spot — validated across general $p$
- **Category:** METHODOLOGY
- **Issue:** The original Tier 0 paper used binary ($p=2$) Bruhat-Tits trees. These showed excellent error protection but had a hidden asymmetry: bit 0 was protected (LER exponentially decaying), but bit 1 had constant error at all depths. A symmetric architecture was needed for real computation.
- **Solution:** ultrametric_v2 (7 sprints, 2026-05-16) validated the full prime family: $p=2$ (asymmetric — deprecated), $p=3$ (symmetric AND compact — adopted), $p=5$ (symmetric, validated — but trees grow as $5^d$), $p=7$ (symmetric, validated — but trees grow as $7^d$). Ternary $p=3$ provides identical protection for both logical states with the smallest tree size among symmetric options.
- **Prevention:** Before publishing architecture claims, validate symmetry across all logical states, not just one. Binary encoding masks a fundamental defect that ternary reveals.
- **Cross-Project:** YES — any ultrametric/tree-based encoding should validate general-p before settling on a prime.

### L13: Concatenation of active QEC on ultrametric trees is redundant
- **Category:** METHODOLOGY
- **Issue:** Quantum computing orthodoxy says "error correction is necessary." The natural question: should we add standard QEC on top of the tree? The intuitive answer was "yes — layering protection can only help."
- **Solution:** Sprint 6 simulated concatenation (surface code, Steane code) on ternary trees of depths 2-5. Result: LER with concatenation = LER without concatenation at all tested points. Adding active QEC adds 2-7× qubit overhead with ZERO benefit. The strong triangle inequality provides geometric suppression that standard QEC cannot improve upon — the tree already does what active QEC would do, passively.
- **Prevention:** "Layering protection" is not always additive — sometimes the structural protection is already complete. Before adding QEC to a novel architecture, prove it helps.
- **Cross-Project:** YES — any geometric error suppression architecture should be tested for QEC redundancy before committing to the overhead.

### L14: 48× LER reduction via scatter with zero extra qubits
- **Category:** METHODOLOGY
- **Issue:** Can we reduce error further without adding more qubits?
- **Solution:** Sprint 4 generalized from binary leaf states to $q$-ary leaf states (scatter: encoding one logical bit across $q$ leaves rather than 2). At $q=128$, LER drops by approximately $48\times$ compared to $q=2$ at the same depth and physical error rate — with ZERO additional physical qubits. The strong triangle inequality amplifies protection as logical states spread across more leaves.
- **Prevention:** When a geometric protection mechanism exists, investigate "scatter" (spreading logical states across more structural positions) before adding physical resources.
- **Cross-Project:** YES — scatter/generalization is a design pattern applicable to any tree-based encoding.

### L15: 40-atom neutral atom $d=3$ hardware is a viable minimum implementation
- **Category:** METHODOLOGY
- **Issue:** The tree architecture seemed abstract — was there a real physical platform that could implement it?
- **Solution:** Sprint 7 designed a complete hardware specification: 40 atoms in a ternary tree of depth 3, neutral atom platform (reconfigurable arrays), Rydberg blockade gates for tree-vertex operations, 4 K operation. 40 atoms is within demonstrated experimental capabilities. The design is concrete enough to hand to an experimental group.
- **Prevention:** When proposing a novel computing architecture, always specify at least one concrete physical implementation pathway — even if it's not the final platform. This transforms the architecture from "mathematical possibility" to "engineering specification."
- **Cross-Project:** YES — every theoretical computing architecture should include a minimum viable hardware spec.

---
### L16: Formal verification collaborations need explicit scope/value-exchange before commitment
- **Category:** METHODOLOGY
- **Issue:** The Richard Goodman collaboration on Lean formalization of ultrametric error confinement was approached without first establishing: (a) what exactly would be formalized (AGP specialization or stronger claim?), (b) what value each party would derive, and (c) whether the artifact would be a classical or quantum theorem. These ambiguities surfaced as "objections" mid-exchange, making it impossible to proceed. The collaboration was terminated ("not a fit," 2026-05-17).
- **Solution:** Before approaching any formal verification collaborator, produce a one-page spec: exact statement to be proved, assumptions inventory with physical correspondence, what the artifact means for QWAV, and what the collaborator receives (co-authorship, citation, payment, etc.).
- **Prevention:** Treat formal verification collaboration like any other external dependency — spec first, approach second.
- **Cross-Project:** YES — transfer to CROSS-PROJECT-LEARNINGS.md candidate.

### L17: Mathematical proof proves consistency, not physical reality — the "assumptions gap" is ineradicable
- **Category:** METHODOLOGY
- **Issue:** The "Can Math Prove Physics" project demonstrated that formal proofs (including Lean) prove logical consistency under stated assumptions, not physical behavior. The "assumptions gap" between model and reality is fundamental and unbridgeable by math alone. This is the central epistemological insight from the aborted collaboration and the published essay (DOI: 10.5281/zenodo.20266032).
- **Solution:** For every mathematical claim about ultrametric hardware, explicitly state: (a) what type of proof it is (consistency, impossibility, existence, or guarantee), (b) what assumptions it requires, (c) which assumptions are physically verified vs. hypothesized, and (d) what experiment would refute the physical claim. This is the "proof-physics contract" from the essay.
- **Prevention:** Every QWAV publication that makes a mathematical claim about physical behavior should include an explicit assumptions audit.
- **Cross-Project:** YES — transfer to CROSS-PROJECT-LEARNINGS.md candidate.

### L18: Three of Richard Goodman's four technical objections remain unaddressed in current releases
- **Category:** RESEARCH
- **Issue:** Richard Goodman's May 2026 technical review identified 4 objections to the ultrametric error confinement papers: (1) decoder asymmetry at p=2 → RESOLVED by Symmetric Extension (p=3). (2) AGP 2006 prior art not cited → OPEN. (3) Classical vs. quantum scope mismatch → OPEN. (4) Heydeman et al. (2018) and Boettcher (2020) not cited → OPEN. Objections 2-4 are substantive gaps that weaken the papers' scholarly positioning.
- **Solution:** Address objections 2-4 in the next Symmetric Extension revision. Cite AGP 2006, clarify classical/quantum scope, and engage with HMPS 2018 and Boettcher 2020. These are tracked as QWAV BACKLOG items P42-P44.
- **Prevention:** Before claiming novelty, always search for and cite prior art on the specific mathematical structure (Bruhat-Tits trees) used as substrate.
- **Cross-Project:** YES — transfer to CROSS-PROJECT-LEARNINGS.md candidate.


### L19: Legal/financial/jurisdictional tasks require user verification before execution — exogenous information exists outside project files

- **Category:** METHODOLOGY
- **Issue:** P30 (entity formation assessment) was executed autonomously as a WHAT'S NEXT? PROCEED task. The resulting `strategy/0.4.md` assumed (a) no corporate entities exist, (b) any new entity would be US-based (Pennsylvania), and (c) SBIR eligibility requires forming a new entity. All three assumptions were wrong: Empowering Change (IL 501c3) and Data For Good LLC (IL corporation) already exist, and future incorporation is planned in the Netherlands, not the US. The LLM didn't ask because the task was framed as "research and draft" — a technical pattern — when it was actually a legal/financial/jurisdictional decision requiring exogenous information.
- **Solution:** Before executing ANY backlog task, classify it as: (a) **Technical** (simulation, writing, analysis, code) — safe for autonomous execution, or (b) **Legal/financial/jurisdictional** (entity formation, grant eligibility, tax, contracts, incorporation) — MUST ask the user to verify assumptions before proceeding. Ask: "What entities already exist? What jurisdictions are relevant? What constraints do you already know about that aren't in the project files?"
- **Prevention:** Add a pre-execution gate to the WHAT'S NEXT? PROCEED protocol: if the next task touches legal, financial, or jurisdictional decisions, PAUSE and query the user. Do not assume the project files contain complete information about externally-registered entities, tax status, or jurisdiction plans.
- **Cross-Project:** YES — transfer to CROSS-PROJECT-LEARNINGS.md candidate.

### L20: Agent persona boundaries — QWAV Program Manager vs. Projects Executor are different roles requiring different prompts
- **Category:** METHODOLOGY
- **Issue:** The QWAV agent (this thread) repeatedly crossed from portfolio-level strategy/direction into individual project execution — suggesting specific implementation details, micro-managing what a Projects thread should do rather than defining the handoff and trusting the Projects agent to execute. Root cause: the QWAV system prompt positions the agent as a generalist ("equally capable of creative ideation, rigorous research, structured writing") with no role-boundary language. The same underlying model is used for both QWAV and Projects threads, but the prompt doesn't enforce the structural distinction — QWAV = program manager (strategy, documentation, handoff, portfolio coordination, project initiation), Projects = individual project executor (research, computation, implementation, deep work). **Critical nuance:** The QWAV agent MAY initiate new projects (create directory, scaffold 7 mandatory docs, write initial SPRINT.md + handoff) and MAY spin off project documentation — but the QWAV agent does NOT execute the project work itself. Project execution ALWAYS delegates to the Projects agent.
- **Solution:** (1) Add explicit role definition to QWAV system prompt: "You are the QWAV Strategy Program Manager. Your scope: portfolio-level strategy, project documentation, cross-project coordination, handoff to Projects agent, Buffer monitoring, release management. You do NOT execute individual project tasks — you define them and delegate." (2) Add symmetric role definition to Projects system prompt: "You are a Projects Executor. Your scope: research, computation, code implementation, data analysis, deep domain work. You receive handoff instructions from QWAV and return completed work to Obsidian/releases." (3) Add a boundary-enforcement rule: when the QWAV agent starts to specify low-level implementation details, it should STOP and reformulate as a handoff instruction.
- **Prevention:** See `strategy/0.10.md` — Prompt Remediation: Agent Role Boundaries — for the full diagnosis and draft prompt amendments. Every future session: QWAV agent reads its role definition first, confirms scope before acting. When a task crosses the boundary into Projects-executor territory, delegate, don't execute. **Initiation boundary:** Creating project scaffolding (directory + 7 docs) and writing handoff/SPRINT documents is QWAV scope. Writing code, running simulations, or producing computational results is Projects scope. When uncertain, ask: "Am I setting up work for someone else to do, or am I doing the work myself?" If the latter, delegate.
- **Cross-Project:** YES — transfer to CROSS-PROJECT-LEARNINGS.md. Any multi-agent setup with different roles (manager vs. executor) needs explicit prompt-level role definitions.

### L21: Portfolio boundary clarity requires explicit domain classification and spinoff tracking
- **Category:** METHODOLOGY
- **Issue:** The QWAV BACKLOG mixed portfolio-level tasks (strategy, documentation, grants, IP) with delegated project tasks (Q-PNA specification) without any domain label. This made it unclear which items were QWAV scope vs. delegated spinoffs vs. meta/ecosystem tasks (prompt engineering). The only active spinoff (Q-PNA) was tracked informally with no registry, return protocol, or status dashboard. Additionally, the `site/` subdirectory (14 files) had no documented purpose.
- **Solution:** (1) Added a `Domain` column to BACKLOG.md with three values: 🟠 QWAV (core portfolio), 🟣 SPINOFF (delegated to Projects agent), 🟡 META (Prompts workspace). All 40 items classified. (2) Fixed P6 status inconsistency (was "NOT STARTED" in BACKLOG but DONE in SPRINT). (3) Added "Spinoff Projects" section to PROJECT STATE.md with Q-PNA registry and spinoff lifecycle protocol (handoff → scaffold → execute → releases → monitor → close). (4) Added "Directory Structure" section to README.md documenting all subdirectories including `site/` (archive-only static content). (5) Verified L20 prompt remediation already completed — both QWAV-DEFAULT.md (§0.9) and DEFAULT.md (§0.9) have symmetric role boundary language.
- **Prevention:** Every backlog item should carry an explicit domain classification at creation time. New spinoff projects should be immediately registered in PROJECT STATE.md's Spinoff Projects table. The decision tree from the audit ("Does this belong in QWAV?") should be consulted before adding any new task.
- **Cross-Project:** YES — any multi-project portfolio being managed by a Strategy Program Manager agent needs explicit domain classification and spinoff tracking.


### L22: Handoff return protocol — verify release file, update docs, capture lessons, commit immediately
- **Category:** METHODOLOGY
- **Issue:** The Q-PNA spinoff (Projects agent) returned a comprehensive handoff with 5 critical lessons about Archive search breadth, computational-before-specification methodology, and the false dichotomy of Bruhat-Tits vs. cophenetic trees. These lessons needed to be captured immediately before context was lost, and the PROJECT STATE/SPRINT/CHANGELOG needed updating to reflect full completion.
- **Solution:** (1) Verified release file existence at `Obsidian/releases/2026/05/` via PowerShell `Test-Path`. (2) Updated PROJECT STATE.md — ACTION #5 → DONE (full completion), spinoff registry updated with DOI, GitHub, and archive location. (3) Updated SPRINT.md — P6 status with handoff completion details. (4) Added CHANGELOG v2.34 entry. (5) Captured 5 Projects-agent lessons as L22. (6) Committed immediately on `feature/action-plan-execution`.
- **Prevention:** When a spinoff project returns a handoff: (a) verify the release file exists on disk, (b) update all 3 documentation targets (PROJECT STATE, SPRINT, CHANGELOG) immediately, (c) extract cross-project lessons before context is lost, (d) update the spinoff registry table, (e) commit before the next task. Never defer handoff processing — the Projects agent's context window is gone the moment the handoff is delivered.
- **Cross-Project:** YES — any multi-agent setup with handoff/return protocols needs immediate documentation sync on handoff receipt.


### L24: Build gravity, don't wait for permission — endogenous momentum > exogenous validation
- **Category:** METHODOLOGY
- **Issue:** Strategy/2.0.md defined a program in "monitoring phase" — waiting for application outcomes, waiting for inbound contacts, waiting for exogenous events. This was correct defensive strategy but strategically inert. The program that built 5 publications, computational evidence at depth 7, 48× error reduction, and a glass-box AI architecture was not built by waiting — it was built by building. The monitoring posture produced stagnation and demoralization.
- **Solution:** Strategy/3.0.md reframed the program from passive to active: 10 assets across 3 tiers, 30-day concrete build plan, all D1-D13 compliant. The core insight: build something that creates its own gravitational pull. If applications come back positive, the built assets amplify the outcome. If they come back negative, the built assets ARE the outcome — a program too substantial to ignore. The flywheel: BUILD → PUBLISH → DISTRIBUTE → VISITOR EXPLORES → VISITOR RETURNS → INBOUND CONTACT (natural consequence, not hoped-for response).
- **Prevention:** When a program feels stagnant, audit whether the primary activities are internal (building, publishing, growing) or external (waiting, monitoring, hoping). If external activities exceed internal activities, the program has surrendered its agency. The fix is always: build something.
- **Cross-Project:** YES — any solo founder or independent research program facing the "waiting for permission" trap.

### L23: Papers aren't read. Interactive artifacts engage. — Multi-channel distribution is the only path out of obscurity.
- **Category:** METHODOLOGY
- **Issue:** Analytics across all 5 QWAV Zenodo publications confirm near-zero readership. The paper-first distribution model — publish, post to social, hope someone reads — has produced zero measurable engagement beyond the program's own activity. The theory of change audit (strategy/1.0.md §3) identified the reading link as the weakest in the chain — and this is no longer a hypothesis, it's a confirmed measurement. Publishing papers that nobody reads is demoralizing and strategically inert.
- **Solution:** Shift to an interactive-first, multi-channel distribution strategy. Every spinoff must produce an interactive public artifact — a GitHub Pages site, a working simulation, a visualization, a web tool — that a reader can engage with in 30 seconds rather than a paper that takes 30 minutes. The interactive artifact IS the engagement mechanism. The formal Zenodo DOI provides archival permanence, citability, and long-term discoverability for researchers who find the work years later via search — but it is NOT the primary engagement channel. Social media posts link to the interactive artifact, not to the paper. This is documented as D13 (DECISIONS.md) and integrated into the forward strategy (strategy/1.0.md §3.4, §8.2).
- **Prevention:** Before initiating any new spinoff, ask: "What is the interactive artifact? What can someone play with, click on, or watch in 30 seconds?" If the answer is "a paper," redesign. The paper is the archival backstop, not the primary output. Every project needs both: an interactive artifact for engagement, a DOI for posterity. Neither replaces the other.
- **Cross-Project:** YES — any open-access research program facing the "nobody reads papers" problem.

## Archived Learnings

*None yet — all learnings above are still active and applicable.*
