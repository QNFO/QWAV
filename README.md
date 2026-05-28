# QWAV -- Ultrametric Quantum Computing & AI

**Passive fault tolerance. Glass-box AI. One mathematical correction.**

> QWAV is the flagship research initiative of [QNFO](https://github.com/QNFO/.github),
> a scientific research incubator advancing knowledge for the **collective benefit
> of all**. All work
> is governed by the [QNFO Content License Agreement](LICENSE) and
> [Code of Conduct](CODE_OF_CONDUCT.md).

---

## What QWAV Is

QWAV replaces Archimedean (continuous) geometry with ultrametric (tree-based) geometry for quantum computing and artificial intelligence. The Bruhat-Tits tree -- a structure from $p$-adic number theory -- provides passive error suppression through the strong triangle inequality, operating at 4 K with no active error correction.

## Key Results

- **Zero logical errors at depth 7** -- ternary Bruhat-Tits tree encoding, validated at physical error rates up to 40%
- **Hierarchical error confinement** -- errors propagate only within their tree branch, never cross branches
- **Glass-box AI** -- neural architectures on tree topologies where decisions are auditable by construction
- **40-atom neutral atom specification** -- within demonstrated experimental capabilities

## Interactive Demos

| # | Artifact | Live Demo (Cloudflare) | GitHub Mirror | Description |
|:--|:---------|:-----------------------|:--------------|:------------|
| A1 | Error Confinement | — | [Demo](https://qnfo.github.io/ultrametric-error-confinement/) | Bruhat-Tits tree error simulation |
| A2 | Q-PNA Playground | — | [Demo](https://qnfo.github.io/Q-PNA/) | Quantum-Native p-Adic Neural Architecture explorer |
| A3 | Convergence Explorer | — | [Demo](https://qnfo.github.io/ultrametric-convergence/) | Ultrametric vs Euclidean clustering |
| A4 | Tree Distance | — | [Demo](https://qnfo.github.io/tree-distance/) | Interactive cophenetic distance comparison |
| A5 | Hardware Visualizer | — | [Demo](https://qnfo.github.io/hardware-pathway/) | 3D neutral atom tree visualization |
| A6 | Tree Universality | — | [Demo](https://qnfo.github.io/ultrametric-tree-universality/) | Cross-domain tree universality explorer |
| A7 | Tree & Shadow Viz | — | [Demo](https://qnfo.github.io/tree-and-shadow-viz/) | Phase diagram visualization |
| A8 | Game of Life | — | [Demo](https://qnfo.github.io/ultrametric-game-of-life/) | Conway's Game of Life on tree topologies |
| K1 | Technical Hub | [deep.qwav.tech](https://deep.qwav.tech) | [Hub](https://qnfo.github.io/QWAV/) | Program overview with live demos |
| K2 | QLOP Primer | [primer.qwav.tech](https://primer.qwav.tech) | — | Laws of Form introduction |
| K3 | Research Archive | [archive.qnfo.org](https://archive.qnfo.org) | — | QNFO research archive (15 sites) |
| — | **Ask QWAV** | [ask-qwav.q08.workers.dev](https://ask-qwav.q08.workers.dev) | — | AI research oracle (949 vectors indexed) |

> Cloudflare Pages hosts 16 sites on custom domains (qnfo.org, qwav.tech). GitHub Pages mirrors preserved as redundancy.

## Project Repositories

All QWAV projects are self-contained GitHub repos under [QNFO](https://github.com/QNFO):

| Repo | Description | Live Demo |
|:-----|:------------|:----------|
| [QWAV](https://github.com/QNFO/QWAV) | Program hub — papers, site, wiki, discussions | [Site](https://qnfo.github.io/QWAV/) |
| [ultrametric-error-confinement](https://github.com/QNFO/ultrametric-error-confinement) | Tier 0: Bruhat-Tits tree error simulation | [Demo](https://qnfo.github.io/ultrametric-error-confinement/) |
| [Q-PNA](https://github.com/QNFO/Q-PNA) | Quantum-Native p-Adic Neural Architecture | [Demo](https://qnfo.github.io/Q-PNA/) |
| [ultrametric-convergence](https://github.com/QNFO/ultrametric-convergence) | Ultrametric vs Euclidean particle simulation | [Demo](https://qnfo.github.io/ultrametric-convergence/) |
| [tree-distance](https://github.com/QNFO/tree-distance) | Cophenetic/ultrametric/Euclidean distance comparison | [Demo](https://qnfo.github.io/tree-distance/) |
| [hardware-pathway](https://github.com/QNFO/hardware-pathway) | 3D rotatable neutral atom tree visualization | [Demo](https://qnfo.github.io/hardware-pathway/) |
| [ultrametric-tree-universality](https://github.com/QNFO/ultrametric-tree-universality) | Cross-domain tree universality explorer | [Demo](https://qnfo.github.io/ultrametric-tree-universality/) |
| [tree-and-shadow-viz](https://github.com/QNFO/tree-and-shadow-viz) | Tree and Shadow phase diagram visualization | [Demo](https://qnfo.github.io/tree-and-shadow-viz/) |
| [ultrametric-game-of-life](https://github.com/QNFO/ultrametric-game-of-life) | Conway's Game of Life on tree topologies | [Demo](https://qnfo.github.io/ultrametric-game-of-life/) |
| [Physics-of-Rationalization](https://github.com/QNFO/Physics-of-Rationalization) | Superdeterminism and the Illusion of Choice | — |
| [Beyond-Belief](https://github.com/QNFO/Beyond-Belief) | Functional Anatomy of Human Ultimate Concern | — |
| [zenodo-automation](https://github.com/QNFO/zenodo-automation) | One-command Zenodo DOI registration pipeline | — |
| [nested-semantic-graph](https://github.com/QNFO/nested-semantic-graph) | Language-neutral IR on Nested Semantic Trees | — |
| [license](https://github.com/QNFO/license) | QNFO Content License Agreement | — |
| [.github](https://github.com/QNFO/.github) | Organization profile and defaults | — |

## Infrastructure (Cloudflare-Native)

> QWAV's entire infrastructure runs on Cloudflare's free tier — $0/month. Zero servers to manage. All edge-native.

| Layer | Technology | What It Powers |
|:------|:-----------|:---------------|
| **Hosting** | Cloudflare Pages (16 sites) | All QWAV research sites, interactive demos, living papers |
| **Compute** | Workers + Sandboxes | API endpoints, AI inference, PDF builds, reproducibility verification |
| **Storage** | R2 (zero egress) | Publication PDFs, research data, model weights |
| **Database** | D1 (SQLite) + Vectorize (vectors) | Citation graph, experiment tracking, semantic search across all papers |
| **AI** | Workers AI + AI Gateway | "Ask QWAV" RAG oracle, paper chat, research synthesis |
| **DNS** | 10 zones | qnfo.org, qwav.tech, bulk redirects from 6 legacy domains |
| **Email** | Email Routing + Email Service | papers@qnfo.org, collab@qnfo.org, programmatic email processing |
| **Agents** | Agents SDK + Workflows + Agent Memory | Autonomous research pipeline, Agent Swarm (planned) |
| **Security** | Turnstile + WAF + Secrets Store | Protection, rate limiting, API key management |

**Full audit:** [`briefings/platform/cloudflare-comprehensive-audit-2026-05-28.md`](briefings/platform/cloudflare-comprehensive-audit-2026-05-28.md)

## Program Management — LLM-Discoverable Architecture

QWAV uses a unified `llms.txt` hierarchy for LLM agent discovery. Start at [`llms.txt`](llms.txt).

| Layer | Index | Contents |
|:------|:------|:---------|
| **Root** | [`llms.txt`](llms.txt) | Everything — program, strategy, briefings, projects, sessions |
| **Strategy** | [`strategy/llms.txt`](strategy/llms.txt) | v1.0-v3.0, action plan, IP, fundraising, brand |
| **Briefings** | [`briefings/llms.txt`](briefings/llms.txt) | Platform docs, research, templates, handoff tracker |
| **Projects** | [`projects/llms.txt`](projects/llms.txt) | 16 handoffs (7 active Phase 3, 9 legacy Phase 4/5) |
| **Sessions** | [`sessions/llms.txt`](sessions/llms.txt) | Session records, audits, outreach records |

| Key Document | Purpose |
|:-------------|:--------|
| [PROGRAM-STATE.md](PROGRAM-STATE.md) | Canonical program state — phase status, infrastructure, next actions |
| [briefings/HANDOFF-TRACKER.md](briefings/HANDOFF-TRACKER.md) | All 16 project handoffs with status, dependencies, repos |
| [strategy/3.0.md](strategy/3.0.md) | Current strategy — Build Gravity, Don't Wait for Permission |
| [briefings/FILE-MANAGEMENT-STRATEGY.md](briefings/FILE-MANAGEMENT-STRATEGY.md) | Why each file belongs — comprehensive audit |
| [sessions/2026/05/](sessions/2026/05/) | Current session records |
| [GitHub (source control only)](https://github.com/QNFO/QWAV) | Issues, PRs, git remote |

**Migrated content:** Papers (539 files → [rwnq8/qwav-papers](https://github.com/rwnq8/qwav-papers), served at [deep.qwav.tech/papers/](https://deep.qwav.tech/papers/)). Interactive demos (5 repos → [rwnq8/convergence-explorer](https://github.com/rwnq8/convergence-explorer), etc.). Test suite migrated with demos.

## Publications

**Core publications:** 8 papers with registered Zenodo DOIs (see table below).

**Legacy archive:** 45 publications in the [QNFO/.github archive](https://github.com/QNFO/.github/blob/master/releases/papers/index.md) (historical, pre-QWAV).  
**Full Zenodo community:** [85 records](https://zenodo.org/communities/qwav/) across all QWAV publications.  
**GitHub-native archive:** [564 markdown papers](https://github.com/QNFO/.github) in QNFO/.github (browsable, with auto-PDF generation).

Key QWAV publications:

- [Ultrametric Quantum Computing Foundations](https://doi.org/10.5281/zenodo.15107688)
- [Validation of Ultrametric Error Confinement](https://doi.org/10.5281/zenodo.15113616)
- [Symmetric Extension of Ultrametric Error Confinement](https://doi.org/10.5281/zenodo.15129661)
- [The Tree Is Real](https://doi.org/10.5281/zenodo.15241485)
- [Tree at the Bottom of Everything](https://doi.org/10.5281/zenodo.15276773)

## License

**QNFO Content License Agreement v1.1** -- see [LICENSE](LICENSE) for full terms.

Non-commercial use only. Attribution required. Patent prior-art citation mandatory.
All QNFO org and rwnq8 personal repositories carry this license.
Effective retroactively across all repos (2026-05-24).

*Key terms:* Non-exclusive, non-transferable, revocable. Commercial use requires
separate agreement. 85% liquidated damages for unauthorized commercial use.
Swiss governing law, ICC Geneva arbitration.

---

*QNFO -- the open-source home of QWAV. Everything public. Everything tracked.*
