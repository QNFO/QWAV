# QWAV PROJECT DECISIONS

> **Purpose:** Record of architecture and design decisions with rationale. Prevents revisiting settled questions. Updated whenever a key decision is made.

**Last updated:** 2026-05-12

---

## Active Decisions

### D1: No physical lab experiments — computational validation only
- **Date:** 2026-05 (established during strategy recalibration)
- **Decision:** All "experimental" validation will be computational (Python simulations, Tier 0+), not physical (lab equipment, dilution refrigerators, qubit arrays).
- **Rationale:** No lab access. No experimental collaborator. Computational physics is a legitimate field — simulations produce falsifiable, reproducible, shareable results. Tier 0 already demonstrated LER=0 at depth 3+.
- **Alternatives considered:** Seek lab collaboration (rejected: no contacts, cold outreach unproven). Abandon experimental validation entirely (rejected: evidence gap must be closed).
- **Reversible?** Yes — if a lab collaborator emerges organically, physical experiments can supplement (not replace) computational validation.

### D2: No peer review — open-access publication only
- **Date:** Established before 2026-05 (years of rejection informed this)
- **Decision:** All publications go through open-access channels (Zenodo, ResearchGate, SSRN, arXiv). Peer-reviewed journals are not targeted.
- **Rationale:** Academic gatekeepers have repeatedly rejected this work. Peer review is considered broken. Credibility should come from substance and falsifiable predictions, not journal acceptance. Readers evaluate directly.
- **Alternatives considered:** Continue submitting to journals (rejected: proven failure mode). Hybrid approach with preprints + journals (rejected: adds delay without benefit).
- **Reversible?** Yes — but only if a specific journal with a known editor actively solicits submission. No unsolicited journal submissions.

### D3: Written-only communication — no live pitches
- **Date:** 2026-05 (codified during strategy recalibration)
- **Decision:** All external communication is written. No live pitching, no networking events, no conference presentations, no video calls for fundraising. (Exception: scheduled collaboration calls like P11 collaborator are substantive working sessions, not pitches.)
- **Rationale:** Aligned with founder's introvert energy patterns. Written communication selects for audiences that evaluate substance over presentation. The library-based assembly strategy makes written applications efficient and sustainable.
- **Alternatives considered:** Traditional startup networking (rejected: draining, misaligned with founder strengths). Hybrid approach (rejected: written-only is a strategic filter, not a limitation).
- **Reversible?** Yes — but only if a specific opportunity requires a live component AND the expected value justifies the energy cost.

### D4: Solo founder — no team-building as a goal
- **Date:** 2026-05
- **Decision:** QWAV operates as a solo venture. Team-building is not an active goal. Collaborators may emerge organically (e.g., P11 collaborator for Lean formalization) but recruitment is not pursued.
- **Rationale:** The work is highly specialized and doesn't fit within any single discipline. Finding aligned collaborators through traditional channels is inefficient. Organic collaboration (people finding the work and reaching out) is preferred.
- **Alternatives considered:** Active recruiting (rejected: misaligned with introvert path, dilutes focus). Co-founder search (rejected: adds complexity without clear benefit at this stage).
- **Reversible?** Yes — if funding is secured and specific expertise gaps must be filled, team-building can be revisited.

### D5: Substance-first evaluation — target only merit-based audiences
- **Date:** 2026-05
- **Decision:** All applications, outreach, and collaboration targets are selected based on whether they evaluate ideas on substance (not credentials, institutional affiliation, or publication venue). Programs requiring PhDs, university affiliation, or peer-reviewed publications are excluded.
- **Rationale:** Founder has no PhD, no institutional affiliation, and no peer-reviewed publications. Targeting credential-based evaluators guarantees rejection. Merit-based evaluators (Emergent Ventures, Foresight Institute, EWOR, Convergent Research) are the only viable path.
- **Alternatives considered:** Get a PhD first (rejected: multi-year delay, work doesn't fit any single discipline). Build institutional affiliation (rejected: requires conformity to existing paradigms).
- **Reversible?** Partially — if QWAV develops sufficient independent credibility (e.g., Lean-verified proofs, published computational results), credential requirements may become irrelevant.

### D6: Open-source everything — no paywalls, no NDAs
- **Date:** 2026-05 (codified on website)
- **Decision:** All QWAV materials — code, documents, simulations, strategy papers, meeting briefings — are publicly available. No paywalls. No NDAs for initial conversations.
- **Rationale:** Transparency builds trust. Open-source enables verification. The core thesis is mathematically novel enough that obscurity is not a competitive advantage — adoption is.
- **Alternatives considered:** Proprietary/closed development (rejected: contradicts substance-first philosophy, limits verification). Selective sharing with NDAs (rejected: adds friction, misaligned with open-access strategy).
- **Reversible?** No — this is a foundational identity decision. Reversing would undermine the project's credibility.

### D7: No patent filings without a funded conversion plan
- **Date:** 2026-05-11
- **Decision:** Do not file any new provisional patents unless a specific, funded 12-month conversion plan exists. The existing High-Temp Chiral provisional outline is held pending application outcomes.
- **Rationale:** Historical data: ~18 previous provisionals filed (~$6,000), zero converted. Quantitative EV analysis: expected net value negative in all scenarios (-$453 to +$59 for one filing). The ultrametric encoding mechanism (QWAV's core novel contribution) has ZERO patent protection — but filing without a conversion plan is pure cost.
- **Alternatives considered:** File proactively to secure priority dates (rejected: negative EV, no conversion plan). File nothing ever (rejected: may file if funded conversion plan emerges).
- **Reversible?** Yes — if VSD/FRO/EWOR funding is secured and a 12-month conversion plan exists, filing becomes viable.

### D8: P11 formal verification collaboration — Shape #1 formalization transport
- **Date:** 2026-05 (intro call scheduled)
- **Decision:** Pursue Shape #1 collaboration with P11 collaborator Labs: formal verification of ultrametric QEC threshold theorem in Lean 4. Co-authored paper + machine-verified repository.
- **Rationale:** A Lean proof that type-checks is unassailable — no reviewer, no gatekeeper. This bypasses both the peer-review barrier and the lab-experiment barrier. Produces a verifiable artifact that can be cited, shared, and built upon.
- **Alternatives considered:** Shape #2 (three-way program with Veselov + HeytingLean — deferred as more complex). Shape #3 (position paper on substrate computation — deferred as less concrete).
- **Reversible?** Yes — scope and timeline are adjustable. The intro call determines mutual interest and feasibility.
