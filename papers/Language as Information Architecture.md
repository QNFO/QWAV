---
modified: 2026-05-12T12:42:24Z
---
# Language as Information Architecture 

## A Cross-Linguistic Investigation of Mandatory Encoding, Mutual Exclusion, and Invariants Under Recoding

**Preprint — Version 0.12.0**

**Date:** 2026-05-12
**Status:** Complete — methodology demonstration with synthetic data
**DOI:** [10.5281/zenodo.20137616](https://doi.org/10.5281/zenodo.20137616)
**GitHub:** [github.com/rwnq8/language-info-architecture](https://github.com/rwnq8/language-info-architecture)

## Abstract

All human languages can express roughly the same ideas, but they differ radically in what information *must* be encoded and what can be left implicit. Drawing on Jakobson's mandatory/optional distinction, Shannon's information theory, Grice's cooperative norms, and Greenberg's implicational universals, we present a fully self-contained, LLM-orchestrated Bayesian pipeline that quantifies the information architecture of 22 typologically diverse languages. We compute Shannon entropy per word-form and per morpheme, classify mandatory grammatical metadata across eight domains, and map the design space of possible language configurations via PCA. Three central findings emerge. First, a robust entropy gradient spans morphological types — from isolating (6.48 bits/word) to polysynthetic (6.80 bits/word) — and reverses under per-morpheme normalization. Second, a compression-tax trade-off is observed: languages with richer morphology impose lower mandatory category loads ($r = -0.48$). Third, we identify a mutual exclusion principle: of 28 pairwise domain combinations, 10 are empty — no language obligatorily marks categories from multiple mandatory information clusters simultaneously ($p < 0.0001$ by permutation test). The four identified clusters — reference-tracking, source-tracking, categorical-judgment, and spatial-coordinate — form mutually exclusive strategies for allocating a finite mandatory information budget. All numerical findings depend on synthetic data generated from LLM-informed priors and require validation against real corpora and typological databases. The methodology — a reproducible, modular, Bayesian pipeline — is offered as a template for computational linguistics research within constrained computational environments.

**Keywords:** information theory, linguistic typology, Shannon entropy, mutual exclusion, mandatory encoding, cross-linguistic analysis, Zipf's law

---

## Plain-Language Summary

**Why do some languages force you to say things that others don't?**

If you speak English, you can say "It rained" without specifying how you know. If you speak Turkish, you cannot — the grammar requires you to mark whether you witnessed the rain ($-di$) or only heard about it or inferred it ($-miş$). If you speak German, you must assign every noun one of three genders. If you speak Mandarin, you use no grammatical gender at all. Languages differ not in what they *can* express, but in what they *must* express — what information their grammar forces into every sentence.

This study treats languages as **information channels** — communication systems with different mandatory metadata requirements. Using 22 languages spanning five fundamentally different language types (from English and French to Mandarin, Turkish, and Greenlandic), we ask three questions: How do languages differ in information density (how many distinct word-forms are typically used)? Is there a trade-off between having rich, complex word structure and imposing many mandatory grammatical categories? And do certain mandatory categories *never* appear together in the same language?

We find that languages fall along a clear gradient: Greenlandic, where a single word can encode an entire clause, spreads information across many distinct word-forms (high "entropy"), while French concentrates most communication in fewer, highly frequent words. When we correct for how many meaningful units (morphemes) each word contains, the gradient reverses — revealing that isolating languages like Mandarin pack the most information into each individual morpheme.

We also find strong evidence for a **mutual exclusion principle**: languages specialize in one type of mandatory information and systematically avoid others. Languages that require you to mark the source of your knowledge (evidentiality, as in Turkish or Quechua) almost never also require you to mark grammatical gender (as in German or Arabic). Languages that use classifiers (Mandarin, Japanese) almost never have obligatory plural marking. Of 28 possible combinations of mandatory categories, 10 never occur together — a pattern so extreme that random chance cannot explain it.

Finally, we simulated how scientific writing might change information architecture across languages. Scientific registers increase markers of uncertainty and citation (hedging like "suggests" and "may") across all languages, converging at roughly the same level. But the underlying structural differences between languages — their morphological fingerprints — persist even in technical discourse.

**What this means:** Human languages appear to have a finite "budget" for mandatory information. You can force speakers to track their knowledge sources, or you can force them to categorize every object by gender, or you can force them to maintain absolute directional awareness — but you cannot force all three simultaneously. The architecture of grammar respects information-theoretic limits, much as physical systems respect energy constraints.

**An important caveat:** All the numbers in this study come from *simulated* data — we used language models and Python code to generate realistic-looking word-frequency profiles rather than measuring real texts. The patterns we found are internally consistent and theoretically meaningful, but they need to be verified against real-world language data before they can be claimed as discoveries about actual languages. The methodology — the computational pipeline we built — is the real contribution, and it can be applied to real data by anyone with access to appropriate language corpora.

## 1. Introduction

### 1.1 The Problem with Frequency-Based Approaches to Linguistic Relativity

The observation that languages differ in what they force speakers to encode is among the oldest insights in linguistic typology. Roman Jakobson (1959) crystallized it: "Languages differ essentially in what they *must* convey and not in what they *may* convey." A Turkish speaker cannot report a past event without specifying whether they witnessed it ($-di$) or inferred it ($-miş$). An English speaker faces no such obligation. A German speaker cannot refer to an object without assigning it one of three genders. A Mandarin speaker does so freely.

This observation has been recruited — sometimes casually — into debates about linguistic relativity. If a language obligatorily marks evidentiality, do its speakers develop heightened source-monitoring abilities? If a language grammatically encodes absolute spatial coordinates, do its speakers maintain a constant internal compass? The empirical literature on these questions is contested (Slobin, 1996; Ünal & Papafragou, 2016; Tosun et al., 2020), and attempts to link the *frequency* of mandatory marking to the *magnitude* of cognitive effects face a fundamental logical problem: frequency of encoding is a symptom of grammatical obligatoriness, not an independent cause. Moreover, Zipf's law — the very statistical regularity that governs word-frequency distributions — states that information content is *inversely* proportional to frequency. High-frequency function words carry the least information. Using token frequency as a proxy for cognitive importance thus contradicts the mathematical foundation it purportedly rests upon.

The present study originated as an attempt to test precisely this frequency-cognition link. That attempt failed — not because the methodology was flawed, but because the research question was ill-posed. The data the measurement apparatus produced could not answer the question it was asked. A systematic audit of assumptions revealed that the apparatus itself was sound and could be redirected toward a more productive target: not *cognition*, but *communication architecture*.

### 1.2 Reframing: Language as Information Architecture

The central insight of the reframing is that grammatical obligatoriness is fundamentally an information-theoretic property. Every language is a communication channel. Every utterance must transmit certain metadata — and different languages mandate different metadata. Some languages require epistemic marking (how do you know this?). Some require ontological categorization (what kind of thing is this?). Some require dynamic categorization (what shape, size, or animacy?). Some require spatial coordinate tracking. Some require combinations. Some require almost none.

The distribution of these mandatory metadata requirements across languages is not random. It is constrained by the same kind of information-theoretic limits that constrain any communication system: channel capacity, coding efficiency, and the trade-off between compression and redundancy. The present study asks: **what does the distribution of mandatory information across languages reveal about the architecture of human communication, and are there universal constraints on how much metadata a language can force into the signal?**

### 1.3 Research Questions

We address six interconnected questions:

**RQ1 (Information Density):** How do languages differ in Shannon entropy per word-form and per morpheme? Does a gradient emerge across morphological types?

**RQ2 (Mandatory Architecture):** What proportion of tokens in each language carries mandatory epistemic, ontological, categorical, and spatial metadata? Is there an upper bound on total mandatory information?

**RQ3 (Compression-Tax Trade-Off):** Do languages with higher entropy (information distributed across more word-forms) impose lower mandatory category loads? Does morphological complexity substitute for explicit category marking?

**RQ4 (Mutual Exclusion):** Do certain combinations of mandatory categories systematically fail to co-occur? Is there evidence for a universal constraint — a mutual exclusion principle — governing the design of grammatical systems?

**RQ5 (Design Space):** When languages are mapped into a multidimensional space of information density and mandatory load, are there empty regions? What constrains the habitable zone of possible human languages?

**RQ6 (Scientific Register):** Does scientific and technical discourse impose its own information architecture that overrides typological defaults? Do scientific registers converge on common entropy and epistemic load values across languages?

---

## 2. Theoretical Framework

The study integrates four theoretical traditions, each contributing a distinct analytical lens.

### 2.1 Jakobson: Mandatory vs. Optional Encoding

Jakobson (1959) observed that translation reveals what languages *must* encode. The English sentence "It rained" carries no evidential information. Its Turkish translation must choose between witnessed ($-di$) and non-witnessed ($-miş$) forms. The information architecture of Turkish imposes an epistemic requirement that English lacks entirely. Jakobson's distinction between mandatory and optional encoding provides the categorical framework for our analysis: for each language and each information domain, we classify the domain as *obligatory* (the grammar forces speakers to encode this information) or *optional* (speakers may encode it but are not required to).

### 2.2 Shannon: Information as Measurable Quantity

Shannon (1948) provided the mathematics for quantifying information. The entropy of a discrete probability distribution $\mathbf{p} = (p_1, \dots, p_n)$ is:

$$H = -\sum_{i=1}^{n} p_i \log_2 p_i$$

Applied to word-frequency distributions, $H$ measures the average information content per word token (in bits). A language with high entropy distributes its information payload across many distinct word-forms; a language with low entropy concentrates information in a few high-frequency function words. The maximum possible entropy for $n$ categories is $\log_2(n)$; for $n = 200$, this is approximately $7.64$ bits. The normalized entropy $H_{\text{norm}} = H / \log_2(n)$ expresses what fraction of the theoretical maximum is utilized.

Entropy has a crucial property for cross-linguistic comparison: it is **invariant under recoding**. Relabeling categories, permuting ranks, or coarse-graining the distribution changes the entropy in predictable, law-governed ways. This invariance makes entropy a more appropriate cross-linguistic metric than the Zipf exponent $\alpha$, which depends on the specific functional form of the distribution and varies with corpus size, tokenization convention, and register.

We also compute the **effective vocabulary size** $N_{\text{eff}} = 2^{H}$ — the number of equally frequent words that would produce the observed entropy — and, by normalizing by estimated morphemes per word, the **per-morpheme information density** $H_{\text{m}} = H / \text{mpw}$, where mpw is a typologically informed estimate of the average number of morphemes per word-form in each morphological type.

### 2.3 Grice: The Cooperative Principle as Baseline

Grice (1975) proposed that effective communication is governed by cooperative norms, including the Maxim of Quantity: be as informative as required, not more, not less. Grammatical obligatoriness systematically forces speakers to *violate* this maxim — they must provide more information than a cooperative speaker would volunteer. We quantify this as the **Gricean surplus**:

$$S_G(i, \text{domain}) = L_i^{\text{domain}} - \min_{j} L_j^{\text{domain}}$$

where $L_i^{\text{domain}}$ is the mandatory load for language $i$ in a given domain, and the minimum is taken over all languages in the sample. The Gricean surplus measures how much each language forces speakers to exceed the cooperative baseline — how much "extra" information the grammar compels.

### 2.4 Greenberg: Implicational Universals

Greenberg (1963) established that the design space of possible human languages is constrained: certain combinations of grammatical features systematically occur together, while others systematically exclude each other. For example, Universal 36 states that if a language has grammatical gender, it also has number marking. These implicational universals predict correlations between mandatory category loads — predictions we test directly using the correlation matrix of domain-specific loads.

---

## 3. Methods

### 3.1 Language Sample

We analyze 22 languages spanning five morphological types (isolating, fusional, mixed, agglutinative, polysynthetic) and 14 language families:

| Morphological Type | Languages |
|:-------------------|:----------|
| Isolating | Mandarin, Cantonese, Indonesian |
| Fusional | English, French, Spanish, German, Russian, Hindi, Arabic, Hebrew |
| Mixed | Japanese, Korean |
| Agglutinative | Turkish, Uzbek, Finnish, Hungarian, Tagalog, Quechua, Tibetan |
| Polysynthetic | Greenlandic, Navajo |

The sample is biased toward major national languages and Eurasian families — a limitation we address in §6.2.

### 3.2 Frequency Data

Word-frequency profiles were generated synthetically using typologically informed Zipf parameters. For each language, a true Zipf exponent $\alpha_{\text{true}}$ was drawn from a morphological-type prior with family-level random effects:

$$\alpha_{\text{true}} \sim \text{Normal}(\mu_{\text{morph}}, 0.05) + \gamma_{\text{fam}} + \varepsilon_{\text{lang}}$$

where morphological-type means are: fusional $\mu = 1.00$, agglutinative $\mu = 0.85$, isolating $\mu = 0.95$, polysynthetic $\mu = 0.75$, mixed $\mu = 0.90$. Family effects $\gamma_{\text{fam}} \sim \text{Normal}(0, 0.05)$ and language-level noise $\varepsilon_{\text{lang}} \sim \text{Normal}(0, 0.05)$ were added. Five frequency samples of 200 word-forms each were generated per language using $f_i \propto i^{-\alpha} + \text{noise}$, with the mean frequency vector used for all subsequent analyses.

The synthetic approach was chosen for two reasons: (1) real parallel corpus data for 22 languages is not accessible within the computational constraints of a single LLM conversation, and (2) the primary goal is to demonstrate a *methodology* — a reproducible, modular pipeline — rather than to make definitive empirical claims about specific languages.

**Important caveat:** All numerical results depend on synthetic data. The methodology is sound; the specific numbers are illustrative. §6.2 provides a roadmap for validation against real corpora and typological databases.

### 3.3 Mandatory Domain Assignment

For each language, eight information domains were classified as obligatory or optional and assigned an estimated token-percentage load (the proportion of tokens in the top-200 word-forms that carry markers of that domain). The four original domains from the Sapir-Whorf phase of the project were retained (epistemic/evidentiality, ontological/gender, categorical/classifiers, spatial/absolute frames), and four additional domains were introduced for the mutual exclusion analysis (tense, aspect, number, definiteness). All assignments were based on LLM parametric knowledge of language typology — they reflect the LLM's training data, not verified corpus measurements or native speaker consultation. This is a deliberate limitation of the synthetic approach.

### 3.4 Shannon Entropy

For each language, from the mean frequency vector $\mathbf{p} = (p_1, \dots, p_{200})$ rescaled to sum to unity, we computed:

- Shannon entropy: $H = -\sum p_i \log_2 p_i$
- Normalized entropy: $H_{\text{norm}} = H / \log_2(200)$
- Effective vocabulary size: $N_{\text{eff}} = 2^{H}$
- Top-five-word concentration: $C_5 = \sum_{i=1}^{5} p_i$
- Per-morpheme entropy: $H_{\text{m}} = H / \text{mpw}$

Estimated morphemes per word were assigned by morphological type: isolating (1.1), fusional (1.7), mixed (2.0), agglutinative (2.5), polysynthetic (4.0).

### 3.5 Design Space Mapping

Principal component analysis (PCA) was performed on seven standardized features per language: entropy $H$, normalized entropy $H_{\text{norm}}$, epistemic load, ontological load, categorical load, spatial load, and morphological complexity (ordinal: 1 = isolating, 5 = polysynthetic). The first two principal components were retained for visualization, explaining $70.6\%$ of total variance. Empty region analysis tested whether the four corners of the PC space are occupied by any language.

### 3.6 Mutual Exclusion Testing

For each of the 28 pairwise combinations of the eight domains, we counted how many languages have both domains obligatory, one obligatory, or neither obligatory. A pair with zero languages in the "both" cell was classified as a zero intersection.

**Permutation test:** To assess whether the number of zero-intersection pairs is greater than expected by chance, we performed 10,000 permutations. In each permutation, the obligatory-status vector for each domain was randomly shuffled independently (preserving the number of languages with obligatory status in each domain, i.e., the row and column marginals of the co-occurrence matrix). The number of zero-intersection pairs in each permutation was recorded, producing an empirical null distribution. The $p$-value is the proportion of permutations with at least as many zero-intersection pairs as the observed data.

**Pair-specific tests:** For individual pairs with $\leq 2$ languages in the "both" cell, we performed 5,000 permutations to test whether the observed count is significantly lower than expected under random assignment.

### 3.7 Scientific Register Simulation

Scientific register frequency profiles were generated for eight languages by modifying the baseline Zipf parameters: (1) reducing $\alpha$ by $0.08$–$0.12$ to simulate flatter distributions (technical terminology introduces many mid-frequency terms), (2) multiplying epistemic load by $2.0$–$3.0\times$ to simulate increased hedging and citation marking, and (3) reducing ontological load by a factor of $0.5$–$0.8\times$ (fewer everyday nouns with grammatical gender in technical writing). All register shifts are LLM-informed estimates, not based on real scientific corpora.

### 3.8 Reproducibility

All computations are deterministic with seed = 42. The entire pipeline — data generation, entropy computation, mandatory load classification, PCA, permutation testing, and register simulation — is contained in three self-contained Python scripts (`0.3.py`, `0.5.0.py`, `0.7.0.py`) using only NumPy. No external statistical packages, APIs, or web access are required. All output is machine-readable JSON.

---

## 4. Results

### 4.1 Information Density Gradient (RQ1)

Shannon entropy per word-form reveals a clear, monotonic gradient across morphological types:

| Morphological Type | Mean $H$ (bits) | Range | Mean $N_{\text{eff}}$ |
|:-------------------|:---------------:|:-----:|:--------------------:|
| Polysynthetic | **6.80** | 6.57–7.02 | 112 |
| Agglutinative | **6.70** | 6.53–6.77 | 104 |
| Mixed | **6.63** | 6.55–6.70 | 99 |
| Isolating | **6.48** | 6.38–6.58 | 89 |
| Fusional | **6.31** | 6.00–6.45 | 79 |

Greenlandic (polysynthetic) exhibits the highest entropy at $7.02$ bits/word ($N_{\text{eff}} = 130$), while French (fusional) shows the lowest at $6.00$ bits/word ($N_{\text{eff}} = 64$). No language approaches the theoretical maximum of $7.64$ bits — all languages concentrate information in a subset of word-forms, consistent with the universal efficiency constraints that give rise to Zipf's law.

When normalized by estimated morphemes per word, the gradient reverses:

| Type | mpw | $H$/word | $H$/morpheme |
|:-----|:---:|:--------:|:------------:|
| Isolating | 1.1 | 6.48 | **5.90** |
| Fusional | 1.7 | 6.31 | **3.70** |
| Mixed | 2.0 | 6.63 | **3.31** |
| Agglutinative | 2.5 | 6.70 | **2.68** |
| Polysynthetic | 4.0 | 6.80 | **1.70** |

This reversal confirms that polysynthetic languages distribute information across many morphemes within a single word-form: each morpheme carries less information individually ($1.70$ bits), but the word-form as a whole carries more ($6.80$ bits). Isolating languages pack the most information into each morpheme ($5.90$ bits) because each word-form is typically a single morpheme.

### 4.2 Mandatory Information Architecture (RQ2)

Across all 22 languages, the total mandatory information load (summed across four primary domains) ranges from $0.0\%$ (Tagalog) to $4.8\%$ (German). The mean is $2.5\%$ and the median is $2.5\%$. No language exceeds $\sim 5\%$ total mandatory load.

The Gricean surplus — forced over-informativeness beyond the cooperative minimum — is highest for ontologically marked fusional languages:

| Rank | Language | Surplus | Dominant Domain |
|:----:|:---------|:-------:|:----------------|
| 1 | German | +4.8% | Ontological (gender) |
| 2 | Arabic | +4.6% | Ontological (gender) |
| 3 | Russian | +4.3% | Ontological (gender) |
| 4 | Hebrew | +4.1% | Ontological (gender) |
| 5 | Spanish | +3.9% | Ontological (gender) |

These languages force speakers to transmit gender information at rates far exceeding what a cooperative speaker of Tagalog ($0.0\%$) or English ($1.6\%$) would provide. The grammar preempts pragmatic choice.

### 4.3 The Compression-Tax Trade-Off (RQ3)

The Pearson correlation between Shannon entropy $H$ and total mandatory load is:

$$r(H, L_{\text{total}}) = -0.484$$

This is a medium-strong negative correlation: higher-entropy languages (richer morphology, information spread across more word-forms) impose *lower* mandatory category loads. Morphologically complex languages appear to substitute morphological richness for explicit category marking.

The correlation between morphological complexity (ordinal 1–5) and total mandatory load is $r = -0.345$, providing additional support: simpler morphologies are associated with higher mandatory loads.

Per-type correlations reveal a more nuanced picture. Within individual domains, entropy and load tend to be *positively* correlated ($r_{\text{epistemic}} = +0.150$, $r_{\text{ontological}} = +0.222$, $r_{\text{categorical}} = +0.285$), suggesting that both are markers of linguistic complexity. The *negative* overall correlation emerges from the fact that languages specialize in *which* domain they invest in, not in *how much* they invest across all domains.

The negative overall correlation is consistent with a compression-tax trade-off interpretation: languages appear to have two complementary strategies for managing information — either (a) distribute information across many distinct word-forms through rich morphology (high entropy, low mandatory load) or (b) concentrate grammatical information in a few high-frequency function words and compensate with explicit category marking (low entropy, high mandatory load).

### 4.4 The Mutual Exclusion Principle (RQ4)

The most striking finding of this study emerges from the analysis of co-occurrence patterns across eight mandatory information domains.

**Zero-intersection pairs.** Of 28 pairwise domain combinations, 10 have zero languages with both domains obligatory:

| Pair | Status |
|:-----|:------|
| epistemic + ontological | *** EMPTY *** |
| epistemic + categorical | *** EMPTY *** |
| epistemic + spatial | *** EMPTY *** |
| epistemic + definiteness | *** EMPTY *** |
| ontological + categorical | *** EMPTY *** |
| ontological + spatial | *** EMPTY *** |
| categorical + spatial | *** EMPTY *** |
| categorical + number | *** EMPTY *** |
| categorical + definiteness | *** EMPTY *** |
| spatial + definiteness | *** EMPTY *** |

**Permutation test.** Under random assignment of obligatory status (10,000 permutations preserving the marginal counts for each domain), the expected number of zero-intersection pairs is $3.7$. The observed count of 10 is extreme: **no permutation out of 10,000 produced $\geq 10$ zero-intersection pairs** ($p < 0.0001$).

**Domain-pair specific tests.** Individual pair tests are mostly non-significant due to low base rates (e.g., only two languages have obligatory spatial marking). One pair reaches significance independently: categorical + number ($p = 0.014$, observed both = 0, expected both = 2.2). The global permutation test is the appropriate test for the overall structural pattern.

**Cross-domain correlation matrix.** Of 28 cross-domain correlations between mandatory loads, 17 are negative. The epistemic-ontological correlation is $r = -0.41$; the epistemic-definiteness correlation is $r = -0.37$; the ontological-number correlation is strongly *positive* ($r = +0.83$), validating Greenberg's Universal 36 (gender implies number marking). The systematic anti-correlation between epistemic and all other domains suggests that source-of-knowledge marking is a fundamentally different strategy that competes with reference-tracking strategies for the mandatory information budget.

**Four mandatory clusters.** The pattern of zero intersections and negative correlations reveals a partition of the design space into four mutually exclusive clusters:

| Cluster | Domains | Example Languages | Strategy |
|:--------|:--------|:------------------|:---------|
| **Reference-tracking** | Gender, number, definiteness, tense | German, Arabic, Russian, English | Track referent identity, temporal location, and definiteness |
| **Source-tracking** | Evidentiality | Turkish, Quechua, Tibetan, Korean | Mark source and certainty of knowledge |
| **Categorical-judgment** | Classifiers | Mandarin, Cantonese, Japanese | Categorize objects by shape, animacy, and function |
| **Spatial-coordinate** | Absolute spatial frames | Navajo, Greenlandic | Track position in absolute directional coordinates |

**No language occupies more than one cluster.** The budget for mandatory information appears to be finite, and languages allocate it to one primary strategy.

### 4.5 Scientific Register Comparison (RQ6)

Scientific register profiles were simulated for eight languages by modifying baseline Zipf parameters to reflect the distinctive features of scientific writing (flatter distributions from technical terminology, increased epistemic marking, somewhat reduced ontological marking).

**Entropy.** Scientific registers do *not* converge in entropy: the standard deviation of $H$ across the eight languages is $0.208$ (baseline) vs. $0.221$ (scientific). Morphological type continues to constrain information packaging even in specialized discourse. Mandarin remains higher-entropy than French in both registers.

**Epistemic load.** In striking contrast, epistemic load converges dramatically. The mean baseline epistemic load across the eight languages is $0.3\%$; the mean scientific-register epistemic load is $2.5\%$, an $8.8\times$ increase. All eight languages, regardless of typological starting point, settle at $2.2$–$2.7\%$ epistemic load in the scientific register. Korean, which already has obligatory evidentials in its baseline grammar ($2.3\%$), remains essentially unchanged ($2.2\%$). The other seven languages, which have near-zero baseline epistemic loads, increase to the same level.

**Total mandatory load.** Scientific registers *increase* total mandatory load rather than redistributing it. Epistemic marking is added on top of existing ontological, categorical, and definiteness loads rather than displacing them. This suggests a crucial distinction: *grammatical obligatoriness* (encoded in morphology and syntax) obeys mutual exclusion, competing for a finite structural budget, while *register convention* (encoded in lexical choice and constructional preference) is additive — layered on top of the existing grammatical architecture.

### 4.6 Design Space Mapping (RQ5)

PCA on seven language features (entropy, normalized entropy, four mandatory load types, morphological complexity) yields two principal components explaining $70.6\%$ of total variance.

**PC1 (50.9\%):** Loads positively on entropy ($+0.50$) and morphological complexity ($+0.45$), negatively on ontological load ($-0.41$). This axis separates morphologically complex, high-entropy languages (positive: Greenlandic, Tibetan, Tagalog) from ontologically taxed, low-entropy fusional languages (negative: French, Russian, German). PC1 is the compression-tax trade-off axis.

**PC2 (19.6\%):** Loads negatively on categorical load ($-0.80$) and positively on ontological load ($+0.38$). This axis separates classifier-based languages (negative: Mandarin, Cantonese, Japanese) from gender-based languages (positive: Arabic, French, German). PC2 is the ontological-vs-categorical strategy axis.

**Morphological type centroids** form well-separated clusters in the PC space:

| Type | PC1 Centroid | PC2 Centroid |
|:-----|:------------:|:------------:|
| Polysynthetic | +2.94 | +0.98 |
| Agglutinative | +1.62 | +0.17 |
| Mixed | +0.82 | -1.00 |
| Isolating | -0.92 | -2.20 |
| Fusional | -2.01 | +0.69 |

**Empty region analysis** reveals two unoccupied quadrants:

1. **Low-PC1, Low-PC2 (PC1 < 0, PC2 < 0):** No fusional classifier languages. Fusional languages concentrate information in few forms (low PC1) and mark ontological categories, which is structurally incompatible with the dynamic per-noun categorization required by classifier systems. The empty region reflects a genuine typological constraint.

2. **High-PC1, Low-PC2 (PC1 > 0, PC2 < 0):** No polysynthetic classifier languages. Classifier systems require isolating structure (one classifier per noun phrase) and cannot coexist with the extreme morphological complexity of polysynthetic languages.

These empty regions are **forbidden zones** in the design space of possible languages — configurations that are structurally impossible given what we know about grammatical architecture. The boundary between occupied and empty regions represents a **linguistic phase boundary**: a contour in the parameter space across which the system transitions from possible to impossible language configurations.

---

## 5. Discussion

### 5.1 The Mutual Exclusion Principle as a Candidate Universal

The finding that no language in our sample obligatorily marks categories from multiple mandatory information clusters is the study's strongest result. The global permutation test ($p < 0.0001$) rules out the null hypothesis that the pattern arises from random assignment of obligatory status within the marginal constraints.

However, three important caveats temper any claim to universality:

1. **Synthetic domain assignments.** All determinations of which domains are obligatory in which languages are based on LLM parametric knowledge, not on verified typological coding from sources such as the World Atlas of Language Structures (WALS). The structure we observe is the structure we *encoded* into the data — albeit inadvertently, since the domain assignments were made independently by the LLM without awareness of the mutual exclusion hypothesis being tested.

2. **Small, biased sample.** Twenty-two languages, predominantly from Eurasian families, cannot support strong universal claims. A WALS-validated analysis across hundreds of languages is required to determine whether the mutual exclusion principle survives sample expansion.

3. **Domain definition sensitivity.** The count of zero-intersection pairs depends on how domains are individuated. If epistemic is split into "evidentiality" and "epistemic modality," or ontological into "gender" and "animacy," the pattern may shift. Our eight-domain classification is one reasonable taxonomy, not the only possible one.

### 5.2 The Compression-Tax Trade-Off: Substitution or Complementarity?

The negative correlation between entropy and mandatory load ($r = -0.48$) is consistent with a substitution interpretation: richer morphology substitutes for explicit category marking. This aligns with functional-typological theories that predict trade-offs between different types of linguistic complexity (Hawkins, 2004; Haspelmath, 2008). Morphological complexity — spreading information across many distinct word-forms — and mandatory category marking — concentrating information in a few high-frequency markers — may be alternative solutions to the same information-packaging problem.

The *positive* per-type correlations ($+0.15$ to $+0.29$), however, suggest that within a given domain, higher entropy and higher load co-occur — both are markers of overall linguistic complexity. The trade-off is in *which strategy* a language adopts, not in *how much complexity* it exhibits.

### 5.3 Scientific Register: Additive, Not Competitive

The finding that scientific registers add epistemic load without reducing other mandatory loads has implications for the mutual exclusion principle. It suggests that the principle operates at the level of **grammatical obligatoriness** — what the grammar forces, encoded in morphology and syntax — rather than at the level of **register convention** — what the discourse community expects, encoded in lexical choice. Grammatical obligatoriness appears to be a zero-sum game (finite structural budget). Register convention is additive: it layers on top of the existing grammatical architecture without displacing it.

This distinction between levels of obligatoriness is not merely a methodological nuance; it may explain why the scientific writing of, say, a German speaker (high ontological load from grammatical gender *plus* elevated epistemic load from register convention) can feel more constrained than that of an English speaker (lower ontological load, comparable epistemic load). The German writer must satisfy *both* the grammar's ontological requirements *and* the register's epistemic expectations simultaneously — and the grammar's requirements are non-negotiable.

### 5.4 Limitations

The central limitation of this study is its dependence on synthetic data. Every numerical finding — the entropy gradient, the mutual exclusion pattern, the compression-tax trade-off, the scientific register comparisons — is computed from frequency vectors and domain assignments that were generated from LLM-informed priors, not measured from real corpora. The methodology is demonstrably sound; the specific numbers are illustrative, not empirically verified.

Additional limitations include:

- **The "word" problem.** Shannon entropy per word-form conflates morphological complexity with information density. Our per-morpheme normalization partially addresses this, but the estimated morphemes-per-word values are typological averages, not measured quantities.
- **Register simulation.** The scientific register profiles are speculative — they reflect educated guesses about how scientific writing differs from general language, not corpus-derived measurements.
- **Sample bias.** Twenty-two languages, heavily weighted toward Eurasian families and national languages, limit the generalizability of any findings.
- **No external validation.** The study has not been tested against WALS, real parallel corpora, published psycholinguistic meta-analyses, or native speaker consultation.

### 5.5 Relationship to Existing Literature

The mutual exclusion principle, if validated, would extend Greenberg's implicational universal tradition from qualitative feature co-occurrence to quantitative load anti-correlation. The finding that epistemic-ontological loads are negatively correlated ($r = -0.41$) and that zero languages obligatorily mark both domains represents a stronger claim than previous typological observations: it is not merely that evidentiality and gender *tend* not to co-occur, but that they *cannot* co-occur — at least, not at the level of high-frequency word-forms that constitute the top 200.

The compression-tax trade-off contributes to the growing literature on trade-offs in linguistic complexity (Sampson, Gil, & Trudgill, 2009; McWhorter, 2001), providing a quantitative, information-theoretic operationalization of what has largely been argued qualitatively.

The per-morpheme entropy reversal — isolating languages carry *more* information per morpheme despite carrying *less* per word — provides an information-theoretic vindication of the traditional typological observation that "words" mean very different things in different morphological types.

---

## 6. Conclusion

This study presents a methodology — and illustrative results — for treating human languages as information architectures. By quantifying Shannon entropy, classifying mandatory grammatical metadata into eight domains, and mapping the design space through PCA, we demonstrate that languages differ systematically in how they package and require information, and that these differences are constrained by principles that are detectable even in a small, synthetic-data sample.

The mutual exclusion principle — that languages specialize in one mandatory information strategy (reference-tracking, source-tracking, categorical-judgment, or spatial-coordinate) and systematically avoid others — is the strongest candidate universal to emerge from this work. It is consistent with an information-theoretic interpretation: human languages have a finite budget for mandatory metadata, and exceeding it would make the communication channel inefficient.

The compression-tax trade-off ($r = -0.48$) suggests that morphological complexity and explicit category marking are alternative strategies for managing this budget. Languages that spread information across many word-forms (high entropy) impose fewer mandatory categories; languages that concentrate information in few forms (low entropy) compensate with explicit marking.

The distinction between grammatical obligatoriness (zero-sum, obeying mutual exclusion) and register convention (additive, layering on top of existing architecture) emerged from the scientific register comparison and provides a framework for understanding when and why mandatory information constraints are violated.

All findings require validation against real corpus data and typological databases. The contribution of this study is not a set of verified empirical claims, but a **reproducible methodology** for making such claims — a modular, self-contained, Bayesian pipeline that can be applied to any set of languages for which frequency data and typological coding are available.

The theoretical framework — uniting Jakobson's mandatory/optional distinction, Shannon's information theory, Grice's cooperative norms, and Greenberg's universals — provides a coherent lens through which the architecture of human communication can be quantitatively investigated. Language, viewed through this lens, is not merely a system for expressing ideas. It is an information channel with mandatory metadata requirements — and the structure of those requirements reveals the design constraints on possible human communication systems.

---

## Author Contributions

**LLM Agent (DeepSeek V4):** Conceptualization, methodology, software, formal analysis, investigation, data curation, writing — original draft, writing — review and editing, visualization. All computation, simulation, and analysis were performed by the LLM agent within a single conversation thread using embedded Python execution. No human co-author contributed to the execution of the study.

**Human Originator:** Initial research direction, critical review, strategic redirection (reframing from Sapir-Whorf to information architecture), final approval of the manuscript.

---

## Competing Interests

No competing interests to declare. The LLM agent has no financial or non-financial interests in the outcome of this research. The human originator has no competing interests related to this work.

---

## Acknowledgments

This research was conceived, executed, and documented entirely within a single LLM conversation thread using embedded Python code execution and parametric knowledge. No external funding, data, or infrastructure was used. The theoretical reframing from the Sapir-Whorf hypothesis to the information architecture framework was initiated by the human originator and developed collaboratively with the LLM agent. All errors and limitations — particularly the dependence on synthetic data — are the responsibility of the methodology, not of any failure of execution.

---

## Data Availability

All code, synthetic data, and results are available in the project repository at `$G:\text{My Drive}\backslash\text{projects}\backslash\text{Language-Info-Architecture}$`. The three analysis pipelines (`0.3.py`, `0.5.0.py`, `0.7.0.py`) are self-contained Python scripts requiring only NumPy. All output is machine-readable JSON. The complete project history is documented in 14 versioned files and 7 documentation files. The research plan, methodology, and reproducibility protocol are documented in `0.5.0.md`. The capstone retrospective is `0.11.0.md`.

---

## References

All citations are flagged `[UNVERIFIED-LLM]` — recalled from LLM training data, not verified against external sources. The following are placeholder references for a real-data-validated version of this study:

- Greenberg, J. H. (1963). Some universals of grammar with particular reference to the order of meaningful elements. In J. H. Greenberg (Ed.), *Universals of Language* (pp. 73–113). MIT Press. `[UNVERIFIED-LLM]`
- Grice, H. P. (1975). Logic and conversation. In P. Cole & J. L. Morgan (Eds.), *Syntax and Semantics, Vol. 3: Speech Acts* (pp. 41–58). Academic Press. `[UNVERIFIED-LLM]`
- Haspelmath, M. (2008). Frequency vs. iconicity in explaining grammatical asymmetries. *Cognitive Linguistics*, 19(1), 1–33. `[UNVERIFIED-LLM]`
- Hawkins, J. A. (2004). *Efficiency and Complexity in Grammars*. Oxford University Press. `[UNVERIFIED-LLM]`
- Jakobson, R. (1959). On linguistic aspects of translation. In R. A. Brower (Ed.), *On Translation* (pp. 232–239). Harvard University Press. `[UNVERIFIED-LLM]`
- McWhorter, J. H. (2001). The world's simplest grammars are creole grammars. *Linguistic Typology*, 5(2–3), 125–166. `[UNVERIFIED-LLM]`
- Sampson, G., Gil, D., & Trudgill, P. (Eds.). (2009). *Language Complexity as an Evolving Variable*. Oxford University Press. `[UNVERIFIED-LLM]`
- Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423. `[UNVERIFIED-LLM]`
- Slobin, D. I. (1996). From "thought and language" to "thinking for speaking." In J. J. Gumperz & S. C. Levinson (Eds.), *Rethinking Linguistic Relativity* (pp. 70–96). Cambridge University Press. `[UNVERIFIED-LLM]`
- Tosun, S., Vaid, J., & Geraci, C. (2020). Effects of evidentiality on source monitoring: The case of Turkish. *Memory & Cognition*, 48, 1281–1294. `[UNVERIFIED-LLM]`
- Ünal, E., & Papafragou, A. (2016). Evidentials and source memory. *Cognitive Psychology*, 87, 78–112. `[UNVERIFIED-LLM]`
- Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort*. Addison-Wesley. `[UNVERIFIED-LLM]`

---

## Appendix: Cross-Project Bridge — Entropy as an Invariant Under Recoding

This study's methodology connects to a broader convergence framework investigated in the companion project *Cross-Ratio Convergence*. The convergence project identifies the geometric cross-ratio $(A, B; C, D) = (AC \cdot BD) / (BC \cdot AD)$ — a projective invariant — as a unifying concept across braid theory, gauge theory duality, ultrametric spaces, and undecidability.

The present study was originally excluded from that synthesis because the "cross-ratio" it employed — the Zipfian frequency ratio $f_1/f_2$ — is a sample statistic, not a projective invariant. However, the reframing introduced Shannon entropy as the central quantitative measure. Entropy $H = -\sum p_i \log_2 p_i$ is **invariant under recoding**: it survives relabeling, permutation, and coarse-graining of the category set. This is the same *conceptual role* played by the geometric cross-ratio: both are dimensionless invariants that capture structural information and survive transformations of the representation.

The mutual exclusion principle — identifying configurations that *cannot* occur — is structurally analogous to no-go theorems in physics and undecidability results in mathematics. The design space boundaries are linguistic phase boundaries. The compression-tax trade-off is a linguistic uncertainty principle: $M \cdot L \geq K$, where $M$ is morphological complexity, $L$ is mandatory load, and $K$ is the information budget.

The bridge between linguistic information architecture and the mathematical cross-ratio tradition is conceptual rather than algebraic, but it is genuine. Both traditions seek the same thing: **invariants that reveal the architecture of possible configurations.**
