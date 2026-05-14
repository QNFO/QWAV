# QWAV PROJECT LEARNINGS

> **Purpose:** Project-specific lessons discovered during execution. Machine-readable format for kaizen (continuous improvement). Read this before starting new work to avoid repeating mistakes.

**Last updated:** 2026-05-12 | **Status:** Paper published — L8 added

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
- **Solution:** Active outreach (written applications to specific programs) + computational evidence (Tier 0 simulation) + targeted collaboration (Richard Goodman for Lean formalization) replaced passive publishing. The 301st paper won't do what the first 300 didn't — a different approach is needed.
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
- **Solution:** Tier 0 simulation + Lean 4 formal verification (via Richard Goodman collaboration) provide the evidence layer. Open-access ensures the evidence is accessible; the evidence itself must exist first.
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

## Archived Learnings

*None yet — all learnings above are still active and applicable.*
