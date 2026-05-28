# PROJECT HANDOFF: The Living Paper (#82)

**Parent Program:** QWAV Phase 3
**Priority:** HIGH
**Status:** Ready — all infrastructure provisioned
**Estimated Effort:** 2 sessions

## Vision

Transform QWAV papers into **interactive publications**. Every equation is clickable — click it to see its derivation, numerical evaluation, and connected concepts across the corpus.

## Infrastructure Available

| Resource | Detail |
|:---------|:-------|
| Cloudflare Pages | Existing paper sites (13) — add JS interactivity layer |
| Workers AI | LLM for equation explanation, concept linking |
| Vectorize | Semantic search for "show me related concepts" |
| MathJax | Already loaded on paper sites |
| R2 | Paper assets (PDFs, figures) |

## MVP (Session 1)
- [ ] Add JavaScript layer to existing paper Pages sites
- [ ] Click any equation → show definition + connected equations from other papers
- [ ] Sidebar: "Related concepts" widget powered by Vectorize similarity
- [ ] Live code cells: click "Run" → Workers AI evaluates and shows output

## Enhancement (Session 2)
- [ ] Dynamic graph visualization of concept relationships
- [ ] "Cite this equation" button → generates BibTeX
- [ ] Export to Jupyter Notebook
- [ ] Toggle between paper view and interactive view

## Key References
- Existing paper repos: all under `G:\My Drive\projects\` and deployed at `*.qnfo.org`
- Workers AI: `@cf/meta/llama-3.1-8b-instruct-fp8` (same as Ask QWAV)
- Vectorize index: `qwav-research` (949 vectors)

## Success Criteria
- [ ] Equation click → explanation + related equations from corpus within 3s
- [ ] Works on at least 3 paper sites
- [ ] No degradation of existing paper rendering
