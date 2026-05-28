# PROJECT HANDOFF: QWAV Agent Swarm — Autonomous Research Agents (#90)

**Parent Program:** QWAV Phase 3
**Priority:** LOW
**Status:** Ready
**Estimated Effort:** 3 sessions (most complex)

## Vision

Autonomous AI agents that explore the QWAV research space: an Explorer agent generates hypotheses, a Synthesizer agent combines insights across papers, and a Reviewer agent critiques findings. The swarm operates continuously, producing research insights.

## Agent Roles
1. **Explorer** — Given a seed concept, search arXiv + web + corpus for related work, generate novel hypotheses
2. **Synthesizer** — Combine insights from multiple papers into coherent narratives
3. **Reviewer** — Critique hypotheses against QWAV methodology, flag logical gaps

## Architecture
```
Scheduler (Queues) → Explorer (Workers AI + Browser Rendering) 
  → Synthesizer (Workers AI + Vectorize) 
  → Reviewer (Workers AI) 
  → D1 (insight database) 
  → Dashboard (Pages)
```

## Infrastructure
| Resource | Detail |
|:---------|:-------|
| Queues | Schedule agent runs |
| Workers AI | LLM for all three agents |
| Browser Rendering | Web search + arXiv scraping |
| Vectorize | Cross-paper similarity |
| D1 | Insight storage |
| Pages | Agent activity dashboard |

## Success Criteria
- [ ] At least 1 novel hypothesis generated and reviewed
- [ ] Agents run autonomously on a schedule
- [ ] Dashboard shows agent activity and discoveries
- [ ] No hallucinations — all claims traceable to sources
