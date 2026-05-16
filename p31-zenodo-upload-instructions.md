# P31: Zenodo Upload — Companion Paper

**Status:** READY FOR UPLOAD — PDF generated. Only needs human to click "Publish" on Zenodo.
**File to upload:** `p31-companion-paper.pdf` (94.4 KB, generated 2026-05-17 via pandoc+xelatex)
**Source:** `G:\My Drive\projects\ultrametric_v2\companion-paper.md` (36,145 chars, 12 sections, ~5,900 words)

---

## Step 1: Upload to Zenodo

Go to: https://zenodo.org/deposit/new?type=publication

### Pre-Filled Metadata (Copy-Paste)

| Field | Value |
|:------|:------|
| **Upload type** | Publication → Preprint |
| **Title** | Symmetric Extension of Ultrametric Error Confinement — Ternary Tree Architecture with Bidirectional Validation |
| **Authors** | Quni-Gudzinas, Rowan Brad |
| **ORCID** | 0009-0002-4317-5604 |
| **Description** | Companion paper to "Computational Validation of Ultrametric Error Confinement in Bruhat–Tits Tree Quantum Circuits" (Zenodo, DOI: 10.5281/zenodo.20134944). Identifies and resolves a structural asymmetry in the original p=2 architecture: internal tie-breaking favors logical 0, collapsing the energy barrier for logical 1 to a constant B=2 at all depths. Presents a p=3 (ternary) symmetric architecture with bidirectional validation through d=8, exhaustive barrier verification, p-selection rationale, physical implementation pathway, classical baseline comparison, correlated noise advantage demonstration, and q-ary alphabet generalization achieving 48× LER reduction at zero additional qubit cost. All results computationally validated (Python 3.10+, standard library only, seed=42). |
| **Version** | 1.0.0 |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Keywords** | ultrametric error confinement, Bruhat-Tits tree, p-adic quantum computation, ternary tree, majority voting, hierarchical error correction, passive fault tolerance, neutral atom quantum computing |
| **Communities** | (Search and add: "quantum computing", "mathematical physics", "error correction" — if available) |
| **Related/alternate identifiers** | References: 10.5281/zenodo.20134944 (the original paper [1]). Relation: "Is supplement to" |
| **Publication date** | 2026-05-17 |
| **Language** | English |

### Additional Notes for Description (optional, paste after main description):

```
Key computational findings (all code-executed, reproducible):
- At depth 7 (2,187 leaves), zero logical errors at 40% physical error rate
  for BOTH logical states (36,000 trials)
- Ternary (p=3) branching eliminates tie-breaking asymmetry present in the
  original p=2 architecture
- Extended to p=5 and p=7 (all odd primes symmetric)
- Under correlated noise, the hierarchical structure outperforms classical
  repetition codes at matched qubit counts
- A q-ary generalization achieves 48× error rate reduction using existing
  atomic hyperfine levels (no additional qubits required)
- Concatenation with standard QEC codes provides zero additional benefit
  (the tree IS already a hierarchical repetition code)
- Hardware prototype design specification included: 40 atoms, d=3,
  implementable on existing neutral atom platforms with no modifications
```

---

## Step 2: Record the DOI

After publishing, Zenodo assigns a DOI in format: `10.5281/zenodo.XXXXXXXXX`

Record it here:
- **New companion DOI:** `________________________`

---

## Step 3: Update the Original Paper's Zenodo Record

Go to the original paper's Zenodo record: https://zenodo.org/record/20134944
Click "Edit" and add the following to the description or "Notes" field:

```
**Companion Publication:** Quni-Gudzinas, "Symmetric Extension of Ultrametric
Error Confinement — Ternary Tree Architecture with Bidirectional Validation,"
Zenodo, 2026. DOI: [INSERT NEW DOI]. This companion identifies a structural
asymmetry in the p=2 architecture (bit 1 receives constant barrier B=2 rather
than exponential protection) and provides the first fully symmetric,
bidirectionally validated architecture using p=3 ternary trees. Eight novel
computational findings beyond the original paper, all code-executed and
reproducible.
```

---

## Step 4: Update the Companion Paper's YAML Frontmatter

In `G:\My Drive\projects\ultrametric_v2\companion-paper.md`, update the frontmatter:

```yaml
doi: [INSERT NEW DOI]          # ADD THIS LINE
```

---

## Step 5: Record in QWAV

After DOI obtained:
1. Update `BACKLOG.md`: mark P31 as `[x]` DONE with DOI
2. Update `SPRINT.md`: mark P31 as `[x]` DONE
3. Update `CHANGELOG.md`: add entry with DOI
4. Proceed to P33 (refresh credential doc) and P32 (lab outreach) — both need this DOI

---

*Instructions generated 2026-05-17 by LLM agent during P31 execution.
The PDF file `p31-companion-paper.pdf` is ready for immediate upload.*
