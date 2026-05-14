# arXiv Submission Guide — QWAV Tier 0 Paper

**Paper:** "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits"
**Current location:** Zenodo (DOI: 10.5281/zenodo.20134944)
**Target:** arXiv.org — the standard preprint server for physics, mathematics, and computer science

---

## Why arXiv Matters

Zenodo is a legitimate repository, but arXiv is where physicists and mathematicians actually look. The difference:

| Zenodo | arXiv |
|:-------|:------|
| General-purpose repository | Field-specific preprint server |
| DOI assigned | arXiv ID assigned (e.g., arXiv:2605.12345) |
| No moderation for content | Light moderation for topic relevance |
| Not indexed by INSPIRE-HEP | Indexed by INSPIRE-HEP, Google Scholar, Semantic Scholar |
| Researchers don't browse it | Researchers browse it daily by category |

arXiv is the standard — your paper isn't in "the literature" until it's on arXiv.

---

## Category Selection

| Category | Code | Description | Fit |
|:---------|:-----|:------------|:----|
| **Quantum Physics** | `quant-ph` | Quantum information, quantum computing, QEC | Primary — this is where QC people browse |
| **Mathematical Physics** | `math-ph` | Mathematical methods in physics | Cross-list — for the math side |
| **Disordered Systems & Neural Networks** | `cond-mat.dis-nn` | Spin glasses, disordered systems | Cross-list — Parisi's community |
| **Mathematical Physics (math)** | `math.MP` | Mathematical physics from math side | Alternative to math-ph |

**Recommendation:** Primary `quant-ph`, cross-list `math-ph`. This catches both the QC audience and the mathematical physics audience.

---

## Endorsement Requirement

**First-time arXiv submitters need endorsement.** This is the main hurdle.

### How Endorsement Works
- You create an arXiv account
- You attempt to submit to a category
- If you haven't submitted to that category before, arXiv asks for an endorser
- An endorser is someone who has submitted to that category and is "known" to arXiv
- The endorser vouches that your paper belongs in that category
- Alternatively: if you have a paper that is clearly within scope, arXiv moderators may approve it without endorsement

### Possible Endorsers for QWAV

| Person | Category | Likelihood |
|:-------|:---------|:-----------|
| **W.A. Zúñiga-Galindo** | math-ph, math.MP | If he responds positively to P17, ask if he'd endorse. |
| **Branko Dragovich** | math-ph, hep-th | If P19 leads to engagement. |
| **David Wales** | cond-mat.soft, physics.chem-ph | If P21 leads to engagement. |
| **arXiv moderator** (auto-review) | quant-ph | The paper includes genuine computational physics — it may pass moderation without an endorser. |

**Fallback strategy:** If no endorser is available, submit anyway. The paper contains real computational physics (Bruhat-Tits tree circuits, error injection, metrics) and is clearly within `quant-ph` scope. arXiv moderators approve well-formed papers from new authors regularly.

---

## Submission Requirements

### Format
arXiv accepts:
- **LaTeX** (preferred — `.tex` + figures as `.pdf`/`.eps`)
- **PDF** (less preferred but acceptable)

If the current paper is in Markdown/Word: convert to LaTeX. This is a few hours of work but produces a professional result. Use the `revtex4-2` document class (standard for physics preprints) or `article`.

### Required Metadata
- Title
- Author(s): Rowan Brad Quni-Gudzinas
- Abstract
- Category (primary + cross-list)
- Comments (e.g., "6 pages, 4 figures, computational validation")

### License
- Default: arXiv non-exclusive license to distribute
- Optional: Creative Commons license (CC BY, CC BY-SA, CC BY-NC-SA)
- **Recommendation:** CC BY (most permissive, maximizes visibility)

---

## Step-by-Step Process

1. **Create arXiv account:** [arxiv.org/register](https://arxiv.org/register)
2. **Prepare LaTeX version** of the paper (if not already in LaTeX)
3. **Submit** via [arxiv.org/submit](https://arxiv.org/submit)
4. **If endorsement required:** Either contact an endorser or proceed without one (moderator review)
5. **Paper appears:** Usually within 24-48 hours (with endorsement) or 3-7 days (without endorsement, via moderation)
6. **Update Zenodo:** Add the arXiv ID to the Zenodo record (they support linked identifiers)

---

## After Submission

- The paper gets an arXiv ID (e.g., `arXiv:2605.12345`)
- It appears in the daily mailing for `quant-ph` subscribers
- It's indexed by Google Scholar, INSPIRE-HEP, Semantic Scholar
- You can update it with revisions (v2, v3, etc.) — arXiv is version-controlled

---

## Blockers & Dependencies

| Blocker | Status |
|:--------|:-------|
| LaTeX conversion needed? | Check current paper format |
| Endorser? | None identified yet — consider asking Zúñiga-Galindo if P17 response is positive |
| Content changes needed? | The Zenodo paper is publication-ready; no changes needed for arXiv |

---

## Priority

**HIGH.** arXiv submission is one of the three highest-leverage actions (with P17 email and P24 "Why Ultrametricity" explainer). It requires no one's permission, costs nothing, and puts the paper in front of the exact audience that matters.
