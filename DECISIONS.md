
### D12: No external dependencies — single-thread completable only
- **Date:** 2026-05-20
- **Decision:** Every task undertaken or delegated by the QWAV program must be completable by a single Projects agent in a single DeepSeek/DeepChat LLM thread. Tasks requiring external collaborators, external APIs, external labs, or multi-thread coordination are out of scope. Formal verification collaborations (Lean, Coq) are excluded — they require external human collaborators and cannot be completed in-house.
- **Rationale:** External dependencies introduce latency, coordination overhead, and dependency risk that are incompatible with the solo-founder, written-first, inbound-only strategy. The program's advantage is speed and autonomy — external dependencies erode both. If a task cannot be completed in a single LLM thread, it shouldn't be part of QWAV strategy.
- **Alternatives considered:** Continue formal verification collaboration (rejected: requires external collaborator, introduces competitive dynamics documented in L10, L16). Build internal formal verification capability (rejected: cannot be completed in a single LLM thread).
- **Reversible?** Yes — but only if the founder directly secures a collaborator or the LLM tooling evolves to support self-contained formal verification in a single thread.
