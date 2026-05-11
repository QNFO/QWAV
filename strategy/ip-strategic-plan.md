# IP Strategic Plan — QWAV Intellectual Property & Patent Portfolio

**Version:** 1.0
**Date:** 2026-05-11
**Purpose:** Complete strategic plan for inventorying, organizing, assessing, and filing intellectual property related to QWAV. Self-contained document — hand this to a fresh chat thread and say "execute the plan."

---

## 0. For the Next LLM Agent — Read This First

**Your task:** Execute the step-by-step plan in Section 4 to inventory, organize, and assess the patent portfolio at `G:\My Drive\Patents\`.

**Critical rules (DO NOT VIOLATE):**

1. **NEVER use `Move-Item` with `-Force -ErrorAction SilentlyContinue`.** This combination lost concept directories in the previous session. Use `Copy-Item` to a safe location first, verify the copy, then `Remove-Item` the original. Or just reorganize in-place by renaming directories.

2. **NEVER assume filing dates or jurisdictions from directory names.** Read the actual documents. The previous agent incorrectly assumed 2024 filing dates and Canadian filings — the founder confirms no 2024 filings and all were US.

3. **NEVER recommend filing a mathematical framework as a provisional patent.** Mathematical formulas, abstract ideas, and laws of nature are not patentable under 35 U.S.C. § 101. Only recommend filing for concepts with specific, novel technical implementations that solve concrete technical problems.

4. **DO NOT file provisionals unless there is a 12-month conversion plan.** US provisionals cost $325 each and expire after 12 months. Filing without a plan to convert to non-provisional or PCT is wasted money.

5. **All work is read-only assessment + reorganization + planning.** Do not file anything. Do not spend money. Produce a plan the founder reviews before any filing.

**What to produce:**
- Updated inventory with every draft package classified (Filing-Ready / Develop / Archive)
- Reorganized directory structure (consolidated, clean, logical)
- Prioritized filing shortlist (max 2-3 US provisionals, $325 each)
- IP integration recommendations connecting patents to QWAV strategy

---

## 1. Current State of `G:\My Drive\Patents\`

### 1.1 Directory Structure (as of 2026-05-11)

```
G:\My Drive\Patents\
├── _ARCHIVE/                              ← Research notes, templates, USPTO guides (~30 files)
├── _TBD Applications/                     ← 3 application concepts
│   ├── Adaptive Topoelectric Transducer/
│   ├── Topologic Computing Materials/     ← Versioned drafts (P0A.1.md → Q5.1.3.md)
│   └── Twisted Bi-2212 HTS/
├── EU PCT/                                ← European PCT materials
├── FILED APPLICATION MATERIALS ONLY/      ← ALL draft patent packages (~25 packages, ~1000+ files)
│   └── 2025/                              ← Organized by date
│       ├── 20250719-1/                    ← 17 files, July 2025 draft
│       ├── 20250719-2/                    ← 23 files, July 2025 draft
│       ├── 2025-11 HIGH-TEMPERATURE.../   ← 20 files, ADS only
│       ├── 2025-12-02 Systems and.../     ← 99 files, 3 sub-packages, ADS
│       ├── 63940352 QUANTUM COMPUTING.../ ← 190 files, 4 sub-concepts, ADS
│       ├── Various Computing...2025-10-05/← 114 files, Cover + ADS (most formal)
│       ├── Various Computing...2025-10-09/← 71 files, ADS
│       ├── Systems and Methods...10-25/   ← 93 files, versioned drafts
│       ├── PHOTONIC COMPUTING.../         ← 142 files, ADS
│       ├── ... (~15 more packages)/
│       └── [26 loose files at 2025/ root]
├── References/                            ← External papers
├── TIER_3_ARCHIVE/                        ← Empty subdirectories (created in previous session)
│   ├── Experimental/
│   ├── Obsolete_or_Redundant/
│   └── Requires_Collaboration/
```

### 1.2 What Was Lost (Data Loss Acknowledged)

During the 2026-05-11 reorganization attempt, the following concept directories were lost due to an erroneous batch `Move-Item` operation into non-existent destination directories:

| Lost Concept | Estimated Value | Recovery Path |
|:-------------|:----------------|:--------------|
| **Geometric Attention Networks** | ⭐⭐⭐⭐⭐ HIGHEST | Check Obsidian/releases, QWAV docs, ResearchGate |
| **Bruhat-Tits Quantum Processor** | ⭐⭐⭐⭐ | Check Obsidian/releases |
| **Spin and Magnetization** | ⭐⭐⭐⭐ | Check Obsidian/releases |
| QBT (Quantum Bayesian Theory) | ⭐⭐⭐ | Check Obsidian/releases |
| Dual-Parameter Cryptographic | ⭐⭐⭐ | Search for files elsewhere |
| QRC (Quantum Resonance Computing) concepts | ⭐⭐⭐ | Surviving draft packages exist in FILED/2025/ |
| Alpha Pi Project | ⭐⭐ | Search _ARCHIVE |
| AQF (All Qubit Framework) | ⭐⭐ | Search _ARCHIVE |
| Hypergraph Sequential Function | ⭐⭐ | Search |
| Prime Attention Mechanism | ⭐⭐ | Search |
| Verified Compilation (Lean) | ⭐⭐⭐ | Overlaps with Richard Goodman collaboration |
| ~10 other concept directories | ⭐ | Low priority |

**Recovery priority order:**
1. Geometric Attention Networks (most commercially viable — Q-PNA mechanism)
2. Bruhat-Tits Quantum Processor (UQC hardware — QWAV quantum pillar)
3. Spin and Magnetization (topological QC connection with experimental data)
4. QBT (quantum Bayesian formalism — merge into Geometric Attention as dependent claims)

**Search locations:** `G:\My Drive\Obsidian\releases\`, ResearchGate, Zenodo, SSRN, `_ARCHIVE` directory.

### 1.3 Filing History

Based on the documents found and the founder's confirmation:

| Filing | Type | Year | Status | Notes |
|:-------|:-----|:-----|:-------|:------|
| **ALL non-provisional filings** | Non-provisional | Various | ❌ Rejected or Abandoned | Founder confirms |
| **Past provisionals** | US Provisional | Pre-2025 | ⏰ Expired | $325 each, 12-month window expired |
| **Current active filings** | — | — | **None** | Nothing currently active at USPTO |

**Key finding:** The "FILED APPLICATION MATERIALS ONLY" directory contains draft packages — not confirmed USPTO filings. Most packages lack formal Specification, Claims, and Abstract documents. The "Cover Letters" found are Obsidian-generated PDF coversheets, not USPTO filing receipts. No office actions, examiner correspondence, or serial number confirmations were found.

**The most likely interpretation:** These are well-organized draft packages prepared for potential filing. Some may have been filed and the filing receipts are stored elsewhere. The founder should verify whether any of these packages were actually submitted to the USPTO Patent Center.

---

## 2. The 25 Draft Packages — Quick Inventory

### 2.1 Package Inventory (from FILED APPLICATION MATERIALS ONLY/2025/)

| # | Package Name | Files | Has Formal Docs? | Quick Assessment |
|:--|:-------------|:------|:-----------------|:-----------------|
| 1 | 63940352 QUANTUM COMPUTING SYSTEMS 2025-12-14 | 190 | ADS only | **Largest package.** 4 sub-concepts: Quantum Processing with Twistronic Gap Engineering (67 files), Cytoplasm-Inspired Superconducting Heterostructures (23 files), Macroscopic Terahertz Quantum Oscillator (18 files), Liquid Helium Operation (16 files) |
| 2 | SYSTEMS AND METHODS FOR PHOTONIC COMPUTING 2025-11-25 | 142 | ADS only | Photonic computing. Subdirs: CRYO, MONO, PASS. Large but may overlap with quantum packages |
| 3 | Various Computing Systems and Methods 2025-10-05 | 114 | Cover + ADS | **Most formal package.** Has cover letter and ADS. Subdirs: Optimization, PESM, RADIO URC |
| 4 | 2025-12-02 Quantum Information Processing & Photonics | 99 | ADS only | 3 sub-packages: Deterministic Graphoepitaxial Synthesis (31 files), Soliton Generation (27 files), Resonant Kerr-Cancellation (31 files) |
| 5 | Systems and Methods for Computing 2025-10-25 | 93 | None | Versioned drafts (0.0.1→0.3.x). Subdirs: BIOMIMETIC CHEMICAL, PHYSICAL FACTORIZATION, ROOM-TEMPERATURE |
| 6 | Various Computing Systems and Methods 2025-10-09 | 71 | ADS | Hybrid Du... subdir, Topologic... subdir |
| 7 | TOPOLOGICAL COMPUTING SYSTEMS AND METHODS | 59 | None | Subdirs: CRYPTOGRAPHY BASED, MACHINE LEARNING, TOPOLOGICAL QUANTUM |
| 8 | Systems and Methods for Topolgical Computing | 38 | None | "Topolgical" (typo). Subdirs: Computation, TOPOLOGICAL QUANTUM |
| 9 | Topological Quantum Computation (Number-Theoretic) | 24 | None | **p-adic / number theory connection to QWAV.** Versioned drafts (0.0.1→0.3.2) |
| 10 | 20250719-2 | 23 | None | July 2025 draft |
| 11 | 2025-11 HIGH-TEMPERATURE TOPOLOGICAL QUANTUM PROCESSING | 20 | ADS | **4K operation, chiral symmetry — QWAV-relevant** |
| 12 | 20250719-1 | 17 | None | July 2025 draft |
| 13 | Analog Quantum Observation (Non-Collapsing Probabilistic States) | 16 | 2 ADS | Non-collapsing measurement |
| 14 | QUANTUM RESONANCE COMPUTING SYSTEMS | 14 | None | QRC concept |
| 15 | QRC-PPA-20250818 | 14 | None | QRC PPA (Pre-Provisional Assessment?) |
| 16 | WAVE-BASED COMPUTATIONAL SYSTEMS | 13 | **1 Specification** | **Only package with actual specification doc** |
| 17 | Bio-Inspired | 11 | ADS | Biomimetic computing |
| 18 | Probabilistic Quantum Information Processing | 5 | **3 Abstracts** | Has abstracts, no spec |
| 19 | Phase-Encoded Information System | 5 | None | Small |
| 20 | Quantum Processing Unit (Bio-Inspired Lattice) | 5 | None | Small |
| 21 | GM-PPA-20250808 | 5 | None | PPA draft |
| 22 | Resonant Field Computing | 4 | None | Tiny |
| 23 | Liquid-Shielded Quantum Device | 4 | ADS | Tiny |
| 24 | Controlled Decoherence | 2 | None | Tiny |
| 25 | [26 loose files at 2025/ root] | 26 | N/A | Loose files — need sorting |

### 2.2 Formal Document Status

| Document Type | Packages with this | Count |
|:--------------|:-------------------|:------|
| **Specification** | Wave-Based only | 1 of 25 |
| **Claims** | None found | 0 of 25 |
| **Abstract** | Probabilistic QIP (3) | 1 of 25 |
| **Cover Letter** | Various Computing 2025-10-05 (Obsidian PDF) | 1 of 25 |
| **ADS Sheet** | 8 packages have ADS (all Obsidian-generated PDFs) | 8 of 25 |
| **USPTO Filing Receipt** | None found | 0 of 25 |
| **Office Action** | None found | 0 of 25 |

---

## 3. QWAV IP Integration

### 3.1 How Patents Strengthen QWAV

QWAV has two pillars — quantum (passive fault tolerance via UQC) and AI (glass-box explainability via Q-PNA). Patents on specific implementations of these pillars provide:

1. **Defensibility:** If QWAV's thesis is correct, patents prevent others from implementing ultrametric architectures without licensing
2. **Licensing revenue:** The IP-Only Licensing Strategy (Strategy B) depends on a defensible patent portfolio
3. **Credibility:** Filed patents signal seriousness to investors, collaborators, and fellowship reviewers
4. **Priority date:** Filing a provisional establishes a priority date — critical if the ultrametric paradigm gains traction

### 3.2 Which Draft Packages Align with QWAV

| Draft Package | QWAV Connection | Strength |
|:--------------|:----------------|:---------|
| Topological Quantum Computation (Number-Theoretic) | p-adic / number theory methods — directly QWAV-relevant | ⭐⭐⭐ |
| 2025-11 HIGH-TEMPERATURE TOPOLOGICAL QUANTUM PROCESSING | 4K operation — QWAV's thermodynamic wall solution | ⭐⭐⭐ |
| QUANTUM RESONANCE COMPUTING SYSTEMS | QRC is QWAV's alternative quantum paradigm | ⭐⭐⭐ |
| 63940352 QUANTUM COMPUTING SYSTEMS | Includes Twistronic Gap Engineering (quantum) + Liquid Helium (cooling) | ⭐⭐⭐ |
| TOPOLOGICAL COMPUTING SYSTEMS | Topological QC is adjacent to ultrametric QC | ⭐⭐ |
| Wave-Based Computational Systems | Only package with specification — most developed | ⭐⭐ |

### 3.3 Lost Concepts That Directly Strengthen QWAV

| Lost Concept | QWAV Pillar | Recovery Priority |
|:-------------|:------------|:------------------|
| Geometric Attention Networks | AI (Q-PNA mechanism) | **URGENT — highest commercial value** |
| Bruhat-Tits Quantum Processor | Quantum (UQC hardware) | **URGENT** |
| Spin and Magnetization | Quantum (topological QC connection) | High |
| QBT (Quantum Bayesian Theory) | Cross-cutting (math foundation) | Medium |

---

## 4. Step-by-Step Execution Plan

### STEP 1: Full Inventory Audit (1-2 hours)

**Goal:** Produce a complete, accurate inventory of every file in `G:\My Drive\Patents\`.

**Actions:**
```powershell
# 1a. Count all files
Get-ChildItem "G:\My Drive\Patents" -Recurse -File | Measure-Object | Select-Object Count

# 1b. Directory-by-directory file count
Get-ChildItem "G:\My Drive\Patents\FILED APPLICATION MATERIALS ONLY\2025" -Directory | ForEach-Object {
    $count = (Get-ChildItem $_.FullName -Recurse -File | Measure-Object).Count
    Write-Output "$count files — $($_.Name)"
}

# 1c. Find all formal patent documents
Get-ChildItem "G:\My Drive\Patents" -Recurse -File | Where-Object {
    $_.Name -match "Specification|Claims|Abstract|Cover.Letter|ADS|Filing.Receipt|Office.Action"
} | Select-Object FullName, @{N='KB';E={[math]::Round($_.Length/1KB,1)}} | Sort-Object FullName

# 1d. Save complete inventory to file
Get-ChildItem "G:\My Drive\Patents" -Recurse -File | Select-Object FullName, @{N='KB';E={[math]::Round($_.Length/1KB,1)}}, @{N='Date';E={$_.LastWriteTime.ToString('yyyy-MM-dd')}} | Sort-Object FullName | Export-Csv "G:\My Drive\Patents\_INVENTORY.csv" -NoTypeInformation
```

**Output:** `_INVENTORY.csv` — complete file listing with sizes and dates.

### STEP 2: Read and Assess Each Package (3-4 hours)

**Goal:** Read the main document from each of the 25 draft packages. Assess quality, novelty, patentability, and QWAV alignment.

**For each package:**
1. Find the main specification/concept document (usually the largest .md file)
2. Read the first 100 lines to understand the core idea
3. Answer:
   - **Novelty:** Is this a genuinely new idea? (1-5)
   - **Patentability:** Is there a specific technical implementation, not just math? (Yes/No)
   - **QWAV alignment:** Does this strengthen QWAV's quantum or AI pillar? (Direct/Adjacent/None)
   - **Completeness:** How developed is this package? (Draft/Early/Polished)
   - **Commercial potential:** Is there a clear market application? (Yes/Maybe/No)

**Read command template:**
```powershell
Get-Content "G:\My Drive\Patents\FILED APPLICATION MATERIALS ONLY\2025\[PACKAGE_NAME]\[MAIN_DOC].md" | Select-Object -First 150
```

**Priority read order** (largest/most developed first):
1. 63940352 QUANTUM COMPUTING SYSTEMS (190 files)
2. SYSTEMS AND METHODS FOR PHOTONIC COMPUTING (142 files)
3. Various Computing Systems 2025-10-05 (114 files — most formal)
4. 2025-12-02 Quantum Info Processing & Photonics (99 files)
5. Systems and Methods for Computing 2025-10-25 (93 files)
6. Then all others in descending file count order

### STEP 3: Quality Classification (1 hour)

**Goal:** Classify every package into one of three categories.

| Category | Criteria | Action |
|:---------|:---------|:-------|
| **FILING-READY** | Specific technical implementation + clear commercial application + well-developed + QWAV-aligned | Prepare for US provisional |
| **DEVELOP** | Promising idea but needs more work (specification, claims, validation) | Keep, develop further |
| **ARCHIVE** | Math framework (not patentable), too early, redundant, or tiny (2-5 files) | Move to archive, do not file |

**§101 Screening (MANDATORY for FILING-READY):**

Before recommending any concept for filing, verify it passes the patentable subject matter test:
- ❌ "A mathematical framework for..." → NOT patentable (abstract idea)
- ❌ "A method for computing using primes..." → Likely NOT patentable (mathematical algorithm)
- ✅ "A quantum processor comprising [specific hardware] configured to [specific operation] that [specific technical result]" → Patentable
- ✅ "A neural network architecture wherein attention weights are computed by [specific geometric operation on specific data structure]" → Patentable

### STEP 4: Reorganize Directory (1 hour)

**Goal:** Create a clean, logical directory structure. Consolidate related packages. Archive duds.

**Proposed structure:**
```
G:\My Drive\Patents\
├── 01_ACTIVE_CONCEPTS/              ← Concepts worth developing or filing
│   ├── Quantum_Computing_Systems/   ← Consolidated from 63940352 + others
│   ├── Quantum_Resonance/           ← Consolidated QRC + QRC-PPA
│   ├── Topological_Computing/       ← Consolidated all topological packages
│   ├── High_Temperature_QPU/        ← 4K topological processing
│   ├── Photonic_Computing/          ← Photonic computing
│   └── Wave_Based/                  ← Only package with specification
│
├── 02_DRAFT_PACKAGES/               ← Other draft packages (non-priority)
│   ├── [Each remaining package as subdirectory]
│
├── 03_FILING_MATERIALS/             ← ADS sheets, templates, USPTO guides
│
├── 04_REFERENCES/                   ← External papers (keep as-is)
│
├── 05_TBD_APPLICATIONS/             ← Application-specific concepts (keep as-is)
│
├── 06_EU_PCT/                       ← European PCT (keep as-is)
│
├── 07_ARCHIVE/                      ← Everything else (old versions, duds, duplicates)
│
├── PATENT_INVENTORY.md              ← Master inventory (this document, updated)
├── _INVENTORY.csv                   ← Full file listing (from Step 1)
└── README.md                        ← Original readme
```

**⚠️ REORGANIZATION SAFETY PROTOCOL:**
```
# DO NOT use Move-Item in bulk. Use this pattern:
# 1. Create destination directory
New-Item -ItemType Directory -Path "DEST_PATH" -Force

# 2. COPY files (not move)
Copy-Item -Path "SOURCE" -Destination "DEST_PATH" -Recurse

# 3. VERIFY the copy succeeded
$srcCount = (Get-ChildItem "SOURCE" -Recurse -File | Measure-Object).Count
$dstCount = (Get-ChildItem "DEST_PATH" -Recurse -File | Measure-Object).Count
if ($srcCount -eq $dstCount) { Write-Output "VERIFIED: $srcCount files copied" }

# 4. ONLY THEN remove original
Remove-Item -Path "SOURCE" -Recurse -Force
```

### STEP 5: Recovery Search (1-2 hours)

**Goal:** Find the lost concept directories (Geometric Attention Networks, Bruhat-Tits Processor, Spin and Magnetization, etc.).

**Search locations:**
```powershell
# Search Obsidian releases
Get-ChildItem "G:\My Drive\Obsidian\releases" -Recurse -Directory | Where-Object { $_.Name -match "Geometric|Bruhat|Spin|QBT|Attention" }

# Search entire G: drive (may take minutes)
Get-ChildItem "G:\My Drive" -Directory -Filter "*Geometric Attention*" -Recurse -Depth 3 -ErrorAction SilentlyContinue
```

**If found:** Copy to `01_ACTIVE_CONCEPTS/` directory.
**If not found:** Note in inventory. These documents may need to be recreated from QWAV's published materials (Technical Deep-Dive, QA modules, papers/).

### STEP 6: QWAV Alignment Assessment (1 hour)

**Goal:** For each FILING-READY or DEVELOP concept, document how it strengthens QWAV.

| Concept | QWAV Pillar | How It Connects | Priority |
|:--------|:------------|:----------------|:---------|
| [Concept from Step 3] | Quantum / AI / Both | Specific connection | 1/2/3 |

### STEP 7: Provisional Filing Recommendations (1 hour)

**Goal:** Produce a prioritized shortlist of 1-3 concepts to file as US provisionals.

**For each recommendation, document:**
1. **Concept name** and which draft package it comes from
2. **Specific technical implementation** (the patentable subject matter — not the math)
3. **Why it passes §101** (what specific hardware/process/method makes it patentable)
4. **Commercial application** (who would license this and why)
5. **QWAV connection** (how it strengthens QWAV's position)
6. **Filing readiness** (what needs to be done before filing — estimated hours)
7. **12-month conversion plan** (how will you convert this to non-provisional or PCT within 12 months?)
8. **Estimated filing cost:** $325 per provisional

**Maximum recommended spend: $650 (2 provisionals).**

### STEP 8: Maintain and Iterate

**Quarterly actions:**
1. Review DEVELOP concepts — promote to FILING-READY if they've matured
2. Check 12-month deadlines for any filed provisionals
3. Update inventory with any new concepts developed
4. Cross-reference with QWAV strategy updates

---

## 5. Decision Framework: File, Develop, or Archive?

Use this flowchart for every concept:

```
Is there a specific, novel TECHNICAL IMPLEMENTATION? (not just math)
    ├── NO → ARCHIVE (not patentable)
    └── YES → Is there a clear commercial application?
                ├── NO → DEVELOP (identify application first)
                └── YES → Is the package well-developed?
                            ├── NO → DEVELOP (write spec, claims, abstract)
                            └── YES → Does it pass §101 screening?
                                        ├── NO → ARCHIVE (or reframe)
                                        └── YES → FILING-READY
                                                    └── Do you have a 12-month conversion plan?
                                                        ├── NO → DEVELOP (create plan first)
                                                        └── YES → FILE PROVISIONAL ($325)
```

---

## 6. Cost Analysis

### 6.1 Current Costs

| Item | Cost | Status |
|:-----|:-----|:-------|
| Past non-provisional filings | Unknown (filing + attorney fees) | All rejected/abandoned |
| Past US provisionals | $325 each | All expired |
| **Current active filings** | **$0** | **Nothing active** |

### 6.2 Recommended Future Spend

| Phase | Action | Max Cost | Timeline |
|:------|:-------|:---------|:---------|
| Phase 1 | Inventory + Assessment (Steps 1-3) | $0 | 1-2 weeks |
| Phase 2 | Reorganization + Recovery (Steps 4-5) | $0 | 1 week |
| Phase 3 | File 1-2 US provisionals | $325–$650 | Month 1-2 |
| Phase 4 | Develop remaining concepts | $0 | Months 3-12 |
| Phase 5 | Convert provisionals (if validated) | Attorney fees ($1K–$10K each) | Month 12 |

**Total recommended spend in Year 1: $650 (2 provisionals). No non-provisional conversion without external funding.**

### 6.3 The $325 Question

Before filing any provisional, answer:
- **Will I have the resources to convert this within 12 months?** If no, don't file.
- **Does this concept have a clear commercial pathway?** If no, develop it first.
- **Is this concept better as a trade secret?** Some ideas are worth more if kept secret.
- **Am I filing to feel productive, or because this is genuinely worth protecting?** Be honest.

---

## 7. Connectivity to QWAV

### 7.1 Patents → QWAV Strategy Documents

| If you file a patent on... | Update this QWAV document |
|:---------------------------|:--------------------------|
| Any quantum computing concept | `strategy/ip-strategic-plan.md` — add to active filings table |
| Geometric Attention / AI architecture | `strategy/ip-only-licensing-strategy.md` — add to IP assets |
| Ultrametric / p-adic methods | `strategy/external-sources.md` — add as primary source |
| Any new filing | `SPRINT.md` — add to completed items; `CHANGELOG.md` — add entry |
| Any abandoned concept | Update inventory; remove from active tracking |

### 7.2 QWAV Documents → Patent Concepts

| QWAV Document | Patent Concept It Supports |
|:-------------|:--------------------------|
| Technical Deep-Dive (UQC) | Bruhat-Tits Quantum Processor, High-Temperature Topological, QRC |
| Technical Deep-Dive (Q-PNA) | Geometric Attention Networks |
| Mathematical Foundations | QBT (if reframed as implementation), Threshold Theorem |
| Experimental Validation Roadmap | Any concept validated by Tier 0 simulation data |
| IP-Only Licensing Strategy | ALL filed provisionals become licensing assets |

---

## 8. FAQ

**Q: Should I file a provisional on the ultrametric threshold theorem?**
A: No. Mathematical theorems are not patentable. However, a specific quantum circuit that implements ultrametric error correction IS patentable. File the implementation, not the theorem.

**Q: Should I refile any of the rejected/abandoned non-provisionals?**
A: Probably not. They were rejected for a reason. If the underlying concept is still good, draft a new provisional with improved claims rather than refiling old rejected material.

**Q: What about international (PCT) filings?**
A: NOT until you have external funding or a clear licensing pathway. PCT filings cost thousands in filing fees + translations + national phase entry. US provisionals ($325) are the only cost-effective option for now.

**Q: How do I know if a concept is "developed enough" to file?**
A: Can you answer: (1) What specific thing does it do? (2) How does it do it? (3) What problem does it solve? (4) Who would pay for it? If you can answer all four with specificity, it's developed enough. If any answer is "it's a framework for..." — it's not.

**Q: What if Geometric Attention Networks is lost forever?**
A: Recreate it from QWAV's published materials. The Q-PNA architecture is described in the Technical Deep-Dive and QA modules. The Tier 0 simulation demonstrates the core mechanism. A new draft incorporating the computational validation data would be stronger than the original.

---

## Appendix A: Key File Paths for Assessment

### Most Important Files to Read

| Priority | File | Why |
|:---------|:-----|:----|
| 1 | `63940352 QUANTUM COMPUTING SYSTEMS 2025-12-14/` — all 4 sub-concepts | Largest package, most developed |
| 2 | `Various Computing Systems and Methods 2025-10-05/` — cover letter + subdirs | Most formal package |
| 3 | `WAVE-BASED COMPUTATIONAL SYSTEMS/` — specification | Only package with actual specification |
| 4 | `2025-11 HIGH-TEMPERATURE TOPOLOGICAL QUANTUM PROCESSING/` | QWAV-relevant (4K operation) |
| 5 | `Topological Quantum Computation Using Number-Theoretic/` | QWAV-relevant (p-adic/number theory) |

### Template Documents Worth Keeping

| File | Location | Use |
|:-----|:---------|:----|
| USPTO Provisional Application Guide | `_ARCHIVE/` | Reference for drafting new provisionals |
| Minimalist Application Template | `_ARCHIVE/` | Template structure |
| ADS Sheet Generator | `_ARCHIVE/` | Generating ADS sheets |

---

*Plan v1.0 — 2026-05-11. Hand this document to a fresh LLM chat thread with the instruction "Execute the IP Strategic Plan at G:\My Drive\Patents." The plan is self-contained — no additional context needed.*
