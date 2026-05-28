# HANDOFF: D1 Citation Graph Database — QWAV Structured Data Foundation

> **Type:** Program → Project  
> **Date:** 2026-05-28  
> **Priority:** 🔴 P0 — Foundational data layer. All Phase 3+ features depend on structured paper metadata.  
> **Sessions:** 1  
> **Phase:** 3 (Enhancement) — P3.4  
> **Cross-Reference:** Cloudflare Audit §1.2 (S2: D1), §7 Action #2; Master Strategy P3.4

---

## SCOPE

QWAV currently has no structured database of its papers, citations, or experiments. All metadata is scattered across Markdown files, Zenodo DOIs, and Git repos. This handoff creates a Cloudflare D1 database (serverless SQLite) with the core schema and seeds it with data from the existing 9 Zenodo-published papers and 29 repos.

**What the Projects Agent should produce:**

1. A D1 database named `qwav-research` (or similar) with these tables:

   **`papers`** — Core paper metadata
   | Column | Type | Description |
   |:-------|:-----|:------------|
   | id | TEXT PK | Short slug (e.g., "ultrametric-quantum") |
   | title | TEXT | Full paper title |
   | doi | TEXT | Zenodo DOI URL |
   | zenodo_id | TEXT | Zenodo record ID |
   | repo | TEXT | GitHub repo name |
   | published_date | TEXT | ISO date |
   | phase | TEXT | QWAV phase (Foundation/Validation/Expansion) |
   | category | TEXT | physics, ai, math, philosophy, tools |
   | abstract | TEXT | Abstract text |
   | page_count | INTEGER | Number of pages |

   **`citations`** — Paper-to-paper references
   | Column | Type | Description |
   |:-------|:-----|:------------|
   | source_id | TEXT FK | Paper that cites |
   | target_id | TEXT FK | Paper being cited |
   | context | TEXT | Brief description of why cited |
   | section | TEXT | Section where citation appears |

   **`concepts`** — Key concepts/theorems
   | Column | Type | Description |
   |:-------|:-----|:------------|
   | id | TEXT PK | Short slug |
   | name | TEXT | Human-readable name |
   | description | TEXT | Brief definition |
   | category | TEXT | theorem, method, structure, phenomenon |

   **`paper_concepts`** — Junction table (papers ↔ concepts)
   | Column | Type | Description |
   |:-------|:-----|:------------|
   | paper_id | TEXT FK | Paper slug |
   | concept_id | TEXT FK | Concept slug |
   | relevance | TEXT | primary, secondary, mentioned |

2. **Seed data:** Populate all tables with data from existing QWAV papers:
   - 9 Zenodo-published papers → `papers` table
   - Cross-citations between papers → `citations` table
   - Core concepts (ultrametricity, fault tolerance, Bruhat-Tits tree, passive error suppression, strong triangle inequality, etc.) → `concepts` table
   - Paper-concept relationships → `paper_concepts` table

3. A query interface (one of):
   - **Option A:** A simple Worker that exposes the database via REST API (`GET /papers`, `GET /papers/:id`, `GET /papers/:id/citations`)
   - **Option B:** Direct D1 query via `wrangler d1 execute` with documented query patterns

4. A README.md documenting:
   - Schema diagram
   - How to query the database
   - How to add new papers
   - Seed data sources

## SUCCESS CRITERIA

- [ ] D1 database created and accessible via `wrangler d1 list`
- [ ] All 4 tables created with correct schema
- [ ] `papers` table contains at least 9 rows (one per published paper)
- [ ] `citations` table contains cross-references between papers
- [ ] `concepts` table contains at least 10 core QWAV concepts
- [ ] `paper_concepts` table links papers to concepts
- [ ] A sample query works: "Which papers cite 'ultrametric-quantum'?" → returns expected rows
- [ ] Schema documented in README.md

## CONSTRAINTS

- **D1 free tier:** 5 GB storage, 5M reads/month. Well within limits for this use case.
- **SQLite dialect:** D1 uses SQLite. Use standard SQL. No PostgreSQL-specific features.
- **Existing data only:** Seed from already-published papers. Do NOT invent or fabricate data.
- **Portability:** Schema should be exportable (SQLite dump = portable). Avoid Cloudflare-specific features that prevent migration.
- **Git hygiene:** Store schema SQL and seed SQL in a repo (`rwnq8/qwav-db` or similar).

## RESEARCH TRAIL

| File / Resource | Purpose |
|:----------------|:--------|
| `G:\My Drive\QWAV\briefings\platform\cloudflare-comprehensive-audit-2026-05-28.md` §1.2 S2 | D1 capability, pricing, use cases |
| `G:\My Drive\QWAV\PROGRAM-STATE.md` D1 section | Planned databases and purposes |
| `G:\My Drive\QWAV\README.md` Publications section | List of published papers with DOIs |
| `G:\My Drive\QWAV\papers/index.md` | Paper index |
| `G:\My Drive\QWAV\briefings/prior-work-catalog.md` | 30 external publications, concepts |
| Cloudflare Docs: [D1](https://developers.cloudflare.com/d1/) | API reference, wrangler commands |
| `npx wrangler d1 list` | Check if any D1 databases already exist |

### Key wrangler Commands

```bash
# Create database
npx wrangler d1 create qwav-research

# Execute schema
npx wrangler d1 execute qwav-research --file=./schema.sql --remote

# Query
npx wrangler d1 execute qwav-research --command="SELECT * FROM papers" --remote

# List databases
npx wrangler d1 list
```

## RETURN PROTOCOL

1. D1 database created → `wrangler d1 list` evidence
2. Schema applied → `wrangler d1 execute --command=".tables"` evidence
3. Seed data populated → row counts for all 4 tables
4. Sample queries demonstrated (3-5 meaningful queries with results)
5. Schema SQL and seed SQL committed to git repo
6. Report back to Program Agent with: database name, table counts, query examples
7. Update PROGRAM-STATE.md D1 row: `citation-graph: ⬜ → ✅`

---

*Projects Agent: This is the foundation for every data-driven feature in QWAV's future — Concept Graph, Cross-Paper Consistency Engine, Evidence Deck, Intellectual Genealogy, and the Living Paper cross-reference engine. Get the schema right now and everything else builds on it.*
