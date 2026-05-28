# HANDOFF: Enable Workers AI for "Ask QWAV" RAG Synthesis

> **Type:** Program → Project  
> **Date:** 2026-05-28  
> **Priority:** 🔴 P0 — Single highest-leverage Cloudflare move per blue-sky blueprint §1  
> **Sessions:** 2  
> **Phase:** 3 (Enhancement)  
> **Cross-Reference:** Cloudflare Audit §7, Action #3; Blue-Sky Blueprint §1 ("Ask QWAV — The Research Oracle")

---

## SCOPE

The `ask-qwav` Worker currently performs Vectorize search (returns relevant document chunks) but does NOT synthesize those chunks into a coherent answer using Workers AI. This handoff adds the RAG (Retrieval-Augmented Generation) layer: query → vector search → LLM synthesis → cited response.

**What the Projects Agent should produce:**

1. A modified `ask-qwav` Worker that:
   - Accepts natural language queries via HTTP GET/POST
   - Queries the existing Vectorize index (`qwav-research`, 768-dim, 949 vectors, 13 repos, 163 MD files)
   - Passes retrieved chunks to Workers AI (Llama 3.1 or similar) with a system prompt: "You are 'Ask QWAV', a research oracle. Answer questions based ONLY on the provided QWAV research excerpts. Cite the source paper and section for every claim. If the answer cannot be found in the provided excerpts, say so."
   - Returns a synthesized answer with inline citations (paper name + section)
   - Handles errors gracefully (no results → "I couldn't find relevant QWAV research on that topic")

2. A simple test page (HTML served from the Worker or standalone on Pages) with:
   - Text input + submit button
   - Response display with formatted citations
   - Loading state

3. Documentation comment in the Worker code explaining the RAG pipeline

## SUCCESS CRITERIA

- [ ] Worker responds to "What does QWAV say about ultrametric geometry and fault tolerance?" with a synthesized answer citing specific papers
- [ ] Worker responds to "What is the strong triangle inequality?" with accurate definition from QWAV corpus
- [ ] Worker responds to "Tell me about pasta recipes" with "I couldn't find relevant QWAV research on that topic" (or similar — does NOT hallucinate)
- [ ] Citations include paper names (e.g., "ultrametric-quantum §3.2" or "hierarchical-universe §5")
- [ ] Response time < 10 seconds
- [ ] Worker deployed and verified via `curl` test

## CONSTRAINTS

- **Free tier only.** Workers AI free quota (Neurons) is sufficient for testing. Do NOT configure paid billing.
- **Existing Worker:** Modify the deployed `ask-qwav` Worker at `ask-qwav.q08.workers.dev`. Do NOT create a new Worker.
- **Existing Vectorize index:** Use `qwav-research` (already populated with 949 vectors). Do NOT re-index.
- **No new dependencies.** Use Workers AI binding (already available in wrangler.toml). No external API keys needed.
- **Git hygiene:** Commit changes to the appropriate repo (the ask-qwav Worker source). If source is not in a git repo, create one under `rwnq8/ask-qwav`.

## RESEARCH TRAIL

| File / Resource | Purpose |
|:----------------|:--------|
| `G:\My Drive\QWAV\briefings\platform\cloudflare-comprehensive-audit-2026-05-28.md` §1.3 AI — Workers AI details, cost, use cases |
| `G:\My Drive\QWAV\archive\cloudflare-blue-sky-blueprint-2026-05-27.md` §1 — "Ask QWAV" design specification with example Q&A |
| `G:\My Drive\QWAV\PROGRAM-STATE.md` — Current Vectorize index stats (949 vectors, 768 dims, 13 repos) |
| `G:\My Drive\QWAV\archive\cloudflare-master-strategy-2026-05-27.md` — P3.2 specification |
| Cloudflare Dashboard → Workers & Pages → ask-qwav — View current Worker code and bindings |
| `npx wrangler vectorize index list` — Confirm index name and binding |
| Cloudflare Docs: [Workers AI](https://developers.cloudflare.com/workers-ai/), [Vectorize](https://developers.cloudflare.com/vectorize/) |

## RETURN PROTOCOL

1. Deploy updated Worker → verify via `curl` test
2. Provide test results (3-5 example Q&A pairs with full response text)
3. Update PROGRAM-STATE.md Worker row: `⚠️ → ✅`
4. Report back to Program Agent with: Worker URL, test results, any issues encountered
5. If Worker needs domain: suggest `ask.qwav.tech` or `ask.qnfo.org` (Pages custom domain binding)

---

*Projects Agent: This is the single highest-leverage Cloudflare integration. It transforms QWAV from "published papers you have to read" to "research you can ask questions of." See the blue-sky blueprint for the full vision.*
