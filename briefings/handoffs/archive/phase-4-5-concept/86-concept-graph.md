# PROJECT HANDOFF: Concept Graph — Living Knowledge Navigator (#86)

**Parent Program:** QWAV Phase 3
**Priority:** MEDIUM
**Status:** Ready
**Estimated Effort:** 1-2 sessions

## Vision

A graph visualization of QWAV's knowledge space. Concepts are nodes; edges are relationships (derives, applies, generalizes, contradicts). Click a concept to see all papers that discuss it, navigate along edges to related ideas.

## Approach

1. **Extract concepts** from paper text using Workers AI (NER + relationship extraction)
2. **Build graph** — nodes = concepts, edges = semantic relationships
3. **Store in D1** for querying
4. **Visualize** with D3.js or Cytoscape.js on Pages

## Infrastructure
| Resource | Detail |
|:---------|:-------|
| Workers AI | LLM for concept extraction |
| D1 | Graph storage |
| Pages | Interactive visualization |
| Vectorize | Semantic similarity for edge weights |

## Success Criteria
- [ ] Graph with 50+ concepts and 100+ relationships
- [ ] Click concept → show papers, related concepts, definitions
- [ ] Deployed at concepts.qwav.tech or similar
