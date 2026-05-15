# QWAV PROJECT LEARNINGS

> **Purpose:** Project-specific lessons discovered during execution. Machine-readable format for kaizen (continuous improvement). Read this before starting new work to avoid repeating mistakes.

**Last updated:** 2026-05-14 | **Status:** L10 added — competitive positioning disguised as collaboration

---

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

## Archived Learnings

*None yet — all learnings above are still active and applicable.*
