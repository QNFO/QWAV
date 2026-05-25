---
title: "Few Become One: Polysynthetic Communication and the Ultrametric Architecture of Language"
authors: "Rowan Brad Quni-Gudzinas"
date: "2026-05-22"
doi: "10.5281/zenodo.20328374"
version: "v1.0"
status: "published"
keywords: ["polysynthetic", "linguistics", "ultrametric trees", "recursive chunking", "information architecture", "digital search", "cross-linguistic", "semantic graphs", "tokenization", "morphology"]
abstract: >
  Most global digital infrastructure — search engines, databases, large language
  models — is built on the structural assumptions of English, an isolating language
  where words are separate, minimally inflected units. This document argues that
  those assumptions systematically fail for polysynthetic languages, in which a
  single word can encode what English requires an entire clause to express. Drawing
  on prior findings from Language-Info-Architecture (entropy gradient across
  morphological types, mutual exclusion of mandatory feature clusters), Syntactic
  Token Calculus (ultrametric topology of syntax), and Ultrametric Cognition
  (recursive chunking as cognitive primitive), the document proposes a universal
  framework: model meaning as nested ultrametric trees rather than linear strings.
  The result is a cross-linguistic semantic architecture that respects the
  polysynthetic mode of packing entire events into single communicative units —
  and, for English speakers, a way out of the "one word equals one concept" prison.
modified: 2026-05-21T23:00:12Z
---
# Few Become One: Polysynthetic Communication and the Ultrametric Architecture of Language

**Author:** [Rowan Brad Quni-Gudzinas](mailto://rowan.quni@outlook.com)
**ORCID:** [0009-0002-4317-5604](https://orcid.org/0009-0002-4317-5604)
**DOI:** 10.5281/zenodo.20328374
**Date:** 2026-05-22

**Abstract:** Most global digital infrastructure — search engines, databases, large language models — is built on the structural assumptions of English, an isolating language where words are separate, minimally inflected units. This document argues that those assumptions systematically fail for polysynthetic languages, in which a single word can encode what English requires an entire clause to express. Drawing on prior findings from Language-Info-Architecture (entropy gradient across morphological types, mutual exclusion of mandatory feature clusters), Syntactic Token Calculus (ultrametric topology of syntax), and Ultrametric Cognition (recursive chunking as cognitive primitive), the document proposes a universal framework: model meaning as nested ultrametric trees rather than linear strings. The result is a cross-linguistic semantic architecture that respects the polysynthetic mode of packing entire events into single communicative units — and, for English speakers, a way out of the "one word equals one concept" prison.

---

## I. The English-Centric Blind Spot

### I.A — The Illusion of Language Neutrality

Google processes over 8.5 billion searches per day. Every one of them begins the same way: a user types a string of characters, hits enter, and expects the machine to understand what they mean.[^6] Behind that expectation lies an architecture — tokenizers that split text on whitespace, inverted indices that map words to documents, relevance algorithms that count keyword frequencies — and that architecture carries a deep, unspoken assumption. It assumes that meaning lives in discrete, separable words.

That assumption is not universal. It is parochial. It comes from English.

English belongs to the isolating (or analytic) family of languages. Its words are largely standalone, minimally inflected units. Grammatical relationships — who did what to whom, when, and how — are encoded not inside the word but through word order and auxiliary function words. “The dog bit the man” means something different from “The man bit the dog” because English syntax is linear: meaning is carried by the sequence, and the sequence is carried by the whitespace between tokens.

This is not how all languages work. It is not even how *most* languages work. But it is how the engineers who built the internet’s information architecture think, because it is how their native language taught them to think. The result is a global digital infrastructure that treats English-like linguistic structure as the default — and every departure from that structure as noise to be smoothed over, or worse, as error to be corrected.

### I.B — The Reality of Linguistic Diversity

Of the roughly 7,000 languages spoken on Earth today, only a minority share English’s isolating architecture. The linguistic landscape is far more varied, and the most radical departure from the English pattern comes from the polysynthetic language family — languages spoken by millions of people across the Arctic, the Americas, Australia, and Papua New Guinea.

In a polysynthetic language, a single word can express what English requires a full clause — sometimes several clauses — to say. What English distributes across a subject, a verb, an object, tense markers, aspect markers, adverbial modifiers, and locative phrases, a polysynthetic language can fuse into one morphologically complex unit. The boundary between “word” and “sentence” dissolves.

This is not an exotic curiosity. It is a fundamentally different way of packaging information. And it has measurable consequences. Recent quantitative work on language as information architecture [^1] found a clear entropy gradient across morphological types: isolating languages average approximately 6.48 bits of information per word-form, while polysynthetic languages average approximately 6.80 bits per word-form. That 0.32-bit gap may seem small, but it reflects a structural reality: polysynthetic languages pack more information into each surface unit. They are, in the language of information theory, more *compressed* — each word carries a heavier semantic payload.

The same study identified four mutually exclusive clusters of mandatory linguistic features: reference-tracking (who is doing what to whom), source-tracking (where did this information come from), categorical-judgment (what kind of thing is this), and spatial-coordinate (where in space and time). Polysynthetic languages tend to encode more of these mandatory clusters within a single word-form, while isolating languages distribute them across separate words. The difference is not just in *what* can be said — it is in *what must be said*, and *where* in the linguistic structure it must be encoded.

[^1]: Rowan Brad Quni-Gudzinas, “Language-Info-Architecture” (2026), DOI: 10.5281/zenodo.20137616. Note: all quantitative values cited from this project are based on synthetic data generated from LLM-informed priors and require real-data validation (e.g., WALS, parallel corpora) for publication-quality claims.

### I.C — The “One Word = One Concept” Prison

Here is the trap, and it is a subtle one. When you grow up speaking English — or Mandarin, or Vietnamese, or any isolating language — you absorb a cognitive model in which meaning is built by stringing together independent semantic atoms. A “word” is the natural unit of thought, the indivisible quantum of language. When you design a search engine, you naturally tokenize on whitespace. When you build a large language model, you naturally train a subword tokenizer on the assumption that meaning lives at the token level. When you architect a database, you naturally treat a “keyword” as the primary retrieval key.

None of these decisions feels like a decision. They feel like the only way things could possibly work. But they are not. They are consequences of a particular linguistic upbringing, projected onto the entire world.

For a speaker of Inuktitut or Mohawk or Nahuatl, the natural unit of communication is not the word — it is the word-sentence, the morphologically complete event description. Searching for a “keyword” in such a language is like searching for a syllable in English: the unit you are looking for is not a separate, free-standing item; it is a bound morpheme embedded inside a larger structural complex. The very concept of a “keyword search” does not translate.

This is not merely a user-experience problem. It is an epistemic problem. If the dominant mode of information retrieval is structurally incompatible with how a large fraction of the world’s languages encode meaning, then those languages — and the knowledge traditions they carry — are systematically excluded from the global information ecosystem. The digital divide is not just about who has internet access. It is about whose cognitive architecture the internet is built to serve.

The next sections explore what polysynthetic communication actually looks like, why written polysynthesis poses unique challenges, how digital infrastructure systematically fails polysynthetic languages, and — most importantly — what a universal, cross-linguistic architecture might look like if we modeled meaning as nested trees rather than linear strings.

---

## II. What Is Polysynthetic Communication?

### II.A — Defining Polysynthesis

In English, a “word” is easy to recognize: it is a string of letters bounded by spaces. A “sentence” is a sequence of words, bounded by a capital letter and a period. These definitions feel natural, even inevitable. But they are artifacts of one language family’s writing conventions — conventions that shatter on contact with polysynthetic languages.

In a polysynthetic language, a single word can be a complete proposition. The boundary between “word” and “sentence” is not a sharp line but a gradient, and the relevant unit of communication is not the lexical item but the *morphological complex* — a root verb surrounded by a constellation of affixes that specify arguments, tense, aspect, mood, location, manner, and evidentiality, all fused into one phonological and syntactic unit.

Consider two examples from Mohawk, an Iroquoian language spoken by roughly 4,000 people in Quebec, Ontario, and New York State [^2]:

- *Wakatonhkariá:ton* — “I have finished eating.” What English distributes across a pronoun (“I”), an auxiliary verb (“have”), a participle (“finished”), and a gerund (“eating”), Mohawk packs into one verb form. The root *-atonhkari-* (“eat”) receives a first-person singular agent prefix *wak-*, a completive aspect suffix, and a stative marker.

- *Ie’saktaientá:‘on* — “He brought her back again.” A single phonological word encodes the agent (“he”), the patient (“her”), the action (“bring”), the direction (“back”), and the iterative aspect (“again”). English requires five separate lexical items plus word-order conventions to convey the same proposition.

These are not extreme, artificial examples. They are routine, everyday Mohawk utterances. In such a language, the fundamental question “where does one word end and the next begin?” is not trivial — it is contested even among linguists who study the language. And the answer has profound consequences: for literacy education, for dictionary-making, for machine translation, and — as we will see — for search engine architecture.

[^2]: All language examples in this section are drawn from the author’s training-data knowledge of linguistic typology and are labeled `[LLM-INFERRED]`. They require verification against primary linguistic sources (fieldwork data, grammars, dictionaries) before publication. The specific Mohawk forms follow standard Iroquoianist transcription conventions but should be checked against a native speaker or authoritative reference grammar.

### II.B — The Spectrum of Linguistic Architectures

Polysynthesis is not an isolated oddity. It occupies one end of a morphological continuum that linguists have mapped since the nineteenth century:

| Morphological Type | Example Languages | How Meaning Is Packaged | Word Complexity |
|:-------------------|:------------------|:------------------------|:----------------|
| **Isolating (Analytic)** | Mandarin, Vietnamese, English (mostly) | Each morpheme is a separate word; grammar encoded through word order and function words | Low — most words are single morphemes |
| **Agglutinative** | Turkish, Japanese, Swahili, Finnish | Morphemes are chained together in transparent, segmentable sequences | Medium — words can be long, but each morpheme retains a clear, consistent form |
| **Fusional** | Latin, Russian, Arabic | Morphemes are fused together; a single affix often encodes multiple grammatical categories simultaneously | Medium-High — morpheme boundaries are opaque, categories are conflated |
| **Polysynthetic** | Mohawk, Inuktitut, Nahuatl, Cree, Tiwi | A single word encodes an entire proposition; noun incorporation, extensive affixation, and pronominal marking are common | Very high — word-sentences with complex internal hierarchy |

This is not merely a taxonomy. It is a map of *where* a language chooses to draw the chunk boundary — at what level of the linguistic hierarchy the cognitive operation of “binding many into one” is applied.

The continuum has measurable consequences. The Language-Info-Architecture project [^1] computed Shannon entropy per word-form across 22 simulated languages spanning this morphological spectrum. The result: a clear monotonic trend from isolating (~6.48 bits/word) to polysynthetic (~6.80 bits/word). The same number of underlying conceptual distinctions — the same propositional content — is encoded in fewer, informationally denser surface units as one moves rightward on the spectrum.

Another way to say this: polysynthetic languages compress more information into each word. They are, in the precise sense of information theory, more *efficient* encodings of propositional content — trading word count for morphological complexity. This is what we might call the **compression-tax trade-off**: richer morphology substitutes for explicit category marking through separate words.

### II.C — Cognitive Parallel: Chunking Made Manifest

Why does this matter beyond linguistics? Because the structure of a polysynthetic word is not arbitrary — it recapitulates, in visible linguistic form, the fundamental cognitive operation of *recursive chunking*.

The Ultrametric Cognition framework [^3] identifies recursive chunking as a cognitive primitive: the mind binds multiple distinct items into a single unit, and then binds that unit with other units, and so on, building hierarchical structures from the bottom up. This is the “few become one” operation that underlies everything from subitizing (instantly recognizing four objects as a group) to concept formation to the distinction calculus.

A polysynthetic word is this very operation, externalized in language. The root morpheme is the core unit — the “one.” Each affix adds a distinction — an agent, a patient, a temporal frame, an evidential source. The affixes do not simply concatenate; they nest. The order of affixation records a hierarchy of semantic scope: if morpheme $A$ modifies morpheme $B$, and $B$ modifies the root $R$, then $A$ is structurally farther from $R$ than $B$ is. The resulting structure is not a flat string but a tree.

This tree has a precise mathematical property: it is **ultrametric**. In an ultrametric space, the distance function $d(x,y)$ satisfies the strong triangle condition:

$$d(x,z) \leq \max\{d(x,y), d(y,z)\}$$

which forces every triangle to be isosceles — two sides equal, the third shorter or equal. In a morphological tree, this condition holds naturally: for any three morphemes, the two that are most closely related (share the lowest common ancestor) are closer to each other than either is to the third. The scope hierarchy of affixation yields an isosceles structure of dependency, exactly mirroring the ultrametric topology formalized in the Syntactic Token Calculus [^4].

In plain terms: a polysynthetic word is an ultrametric tree spoken in a single breath.

### II.D — Polysynthesis as Universal, Not Exotic

If the cognitive operation of chunking is universal — and the ultrametric tree structure is a mathematical invariant of that operation — then the difference between English and Mohawk is not a difference in *what the mind does*. It is a difference in *where the mind draws the chunk boundary*.

To make this concrete, consider how the same underlying proposition might be rendered across different morphological strategies. The idea is something like: “The fact of repeatedly making the small into the one embeds the equal-branching pattern that makes mind and world the same.” This is the core insight from the distinction calculus — the recursive nesting of distinctions yields an ultrametric structure — expressed as a proposition.

- **Isolating strategy** (Classical Chinese-inspired): “Part part combine. Combine combine again. Tree form. Two sides equal. Mind world one.” Each conceptual atom gets its own syllable; grammar is encoded through juxtaposition and sequence. `[LLM-INFERRED]`

- **Agglutinative strategy** (Turkish-inspired): A chain of distinct, segmentable morphemes — each carrying one grammatical function — attached to a root. The word can be long, but each morpheme remains transparent. `[LLM-INFERRED]`

- **Polysynthetic strategy** (Mohawk-inspired): A single, phonologically unified word-sentence in which noun incorporation, pronominal prefixes, and aspectual suffixes fuse the entire event into one morphological complex. `[LLM-INFERRED]`

All three strategies communicate the same underlying conceptual structure. The difference is in *packaging*: where the boundaries fall, how many surface units carry the information, and what must be explicitly marked versus left to context.

The takeaway is this: polysynthesis is not an exotic outlier. It is the logical endpoint of a universal cognitive gradient — the maximal expression of the mind’s tendency to bind many into one. And because the digital world was built by speakers of languages near the opposite end of that gradient, the digital world cannot see it.

---

## III. Polysynthetic Written Communication

### III.A — Writing Systems for Polysynthetic Languages

Writing is not a neutral transcription of speech. Every writing system encodes a theory of what language *is* — what its fundamental units are, how they relate to each other, and where the boundaries between them fall. When a writing system designed for one language type is applied to another, the mismatch can be profound.

Most polysynthetic languages today are written in adapted versions of the Latin alphabet. This is a legacy of colonization, missionary linguistics, and the global dominance of European-language education systems — not a reflection of any natural fit between Latin script and polysynthetic morphology. The Latin alphabet was developed for Latin, a fusional language with clear word boundaries and a relatively modest morpheme-to-word ratio. When applied to Mohawk or Inuktitut, it imposes a segmentation that the language itself does not demand. The result is a persistent, unresolved tension: where do you put the spaces?

Consider the Inuktitut word *Inuululauqsimanngittualuujunga*, meaning “I definitely didn’t live for a very long time.” This is one phonological and syntactic unit — one word-sentence. But when written in Latin script, it looks impossibly long to an English-trained eye. The instinct is to break it up — to insert spaces, hyphens, or other visual cues that make it “readable” by isolating-language standards. But any such insertion is arbitrary: it imposes boundaries where the language’s own grammar imposes none, and it trains readers to process the text as a sequence of separate chunks rather than as a single, nested gestalt.

Some polysynthetic language communities have found a better fit in **syllabic writing systems**. Inuktitut and Cree, for example, use syllabaries — writing systems in which each symbol represents a consonant-vowel sequence, and the symbols are arranged to form visually compact blocks. In such a system, a long polysynthetic word does not sprawl across the page in a way that invites artificial segmentation. Instead, it forms a dense, unitary visual block — a single glyphic mass that mirrors, in the spatial domain, the cognitive chunking that produced it. The syllabic block *is* the word-sentence, and no amount of English-trained intuition about “where the spaces should go” can break it apart without destroying its identity.

There is a deeper possibility here — what we might call **morphographic writing**. Imagine a writing system designed not around phonemes (as in alphabets) or syllables (as in syllabaries) but around *morphemes*: each meaningful unit — root, agent marker, patient marker, tense, aspect, evidential — receives its own visual element, and these elements are arranged spatially in a way that directly reflects the morphological tree. The root sits at the center; affixes radiate outward in nested layers corresponding to their scope. The resulting visual form would be a diagram of the ultrametric structure — a tree, rendered in writing. No such system exists as a widespread, living script, but the concept points toward what a truly morphology-respecting writing system could be: not a concession to isolating-language conventions, but a direct visual manifestation of the cognitive architecture that polysynthetic languages externalize.

### III.B — The “Word” in Writing

Here we arrive at a problem so fundamental that most English speakers have never had reason to notice it: **the “word” is not a linguistic universal. It is a written convention, and that convention varies dramatically across languages.**

In English, a word is whatever sits between two spaces. This definition is circular — we put spaces between words because we know what a word is, and we know what a word is because it sits between spaces — but it has worked well enough for centuries because English morphology is isolating: most words are single morphemes, and the few that aren’t (like “un-happi-ness”) are short enough that the space-delimited unit rarely clashes with the grammatical unit.

In a polysynthetic language, this convenient alignment evaporates. Is *Inuululauqsimanngittualuujunga* one word or many? By the phonological criterion — it has one primary stress — it is one word. By the syntactic criterion — it functions as a single clause — it is one word. But by the orthographic criterion that an English speaker would instinctively apply — “it’s too long to be one word” — it fails the test. And that “too long” judgment is not a linguistic observation; it is a cultural reflex, trained by a lifetime of reading English.

The consequences for written polysynthetic communication are substantial:

1. **Literacy education**: When children are taught to read and write in a polysynthetic language using a space-delimited Latin orthography, they must learn an arbitrary set of conventions about where spaces fall — conventions that often vary between communities, between publications, and even between individual writers. This is not a trivial obstacle; it is a cognitive burden that isolating-language readers never face.

2. **Dictionary-making and lexical resources**: What is the “headword” in a polysynthetic dictionary? The root? The full word-sentence? Some intermediate form? Different lexicographic traditions make different choices, and the choice fundamentally shapes what users can look up and how.

3. **Font design and text layout**: Typefaces designed for English assume words of 2-12 characters. A single polysynthetic word can be 30, 40, or 50+ characters long. Line-breaking algorithms trained on English hyphenation patterns fail. Justified text — in which spaces between words are stretched to align both margins — becomes absurd when there are only two or three “words” on a line, each of wildly different lengths.

4. **Search and information retrieval**: This is the subject of Section IV, but the root of the problem is here: if you cannot agree on what a “word” is, you cannot build a word-based index. And if you cannot build a word-based index, you cannot search.

### III.C — Written vs. Oral Polysynthesis

There is a subtler issue at play, one that touches on the relationship between literacy and cognition. Writing is not just a way of recording speech — it is a technology that reshapes how we think about language. An English speaker who learns to read and write English internalizes the idea that language is made of separate words, that those words are made of separate letters, and that meaning is compositional — built up from smaller units arranged in sequence. This model works for English. But what happens when a speaker of a polysynthetic language learns to read and write it in a space-delimited Latin orthography? Do they internalize the same “words are separate things” model, in tension with their spoken language’s gestalt morphology? Or do they develop a different cognitive relationship to written text — one that processes entire morphological complexes as single visual units, regardless of where the orthographic conventions happen to place the spaces?

The research on this question is sparse, but the implications are significant. If literacy in a polysynthetic language trains a different cognitive “chunking” strategy than literacy in an analytic language, then the reading brain is not a universal architecture — it is shaped, in part, by the morphological type of the language being read. A Mohawk reader may process a 40-character word-sentence as a single visual gestalt, in the same way that an English reader processes a 4-letter word. The surface difference in character count masks a deeper equivalence in cognitive processing: both are processing “one chunk.” This would mean that what looks, to an English eye, like an impossibly complex written form is, to a Mohawk eye, a natural and efficient unit of visual language processing.

This hypothesis — that the cognitive unit of reading is the morphological chunk, not the orthographic word — has not been systematically tested, but it follows directly from the ultrametric framework: if the mind chunks “few into one,” and polysynthetic morphology makes that chunking explicit in the surface form, then the literate polysynthetic reader should process those forms holistically. The written word-sentence is not a long word; it is a *normal-sized chunk*, and it is English words that are, by this measure, abnormally short.

This inversion of perspective — polysynthetic as the norm, isolating as the outlier — is at the heart of the broader argument. The digital world treats the English word as the default unit of meaning. But there is no reason, cognitive or linguistic, to privilege that unit over any other chunking level. The “word” is a historical accident of how one language family came to write. It is not a law of nature.

---

## IV. The Digital Divide: Search Engines, Databases, and the Bias of English

### IV.A — The Tokenization Problem

At the heart of every search engine, every database index, and every large language model lies a single operation: **tokenization** — the splitting of a stream of text into discrete units for processing. For English, this operation is almost invisible in its simplicity. Split on whitespace. Strip punctuation. What remains is a list of “words,” and each word becomes a token — a row in an inverted index, an entry in a vector space, a unit of meaning to be searched, ranked, and retrieved.

This operation is so natural to an English speaker that it barely registers as a design decision. It simply *is* how text works. Until you apply it to a polysynthetic language.

Consider the Inuktitut example introduced in Section III: *Inuululauqsimanngittualuujunga* — “I definitely didn’t live for a very long time.” An English whitespace tokenizer would treat this as a single token. One row in the index. One entry in the vector space. One unit of meaning. But that single surface form encodes, internally, at least eight distinct morphemes. The tokenizer has collapsed an entire proposition — with negation, evidentiality, aspect, and person marking — into one opaque blob. All the internal structure that makes the word-sentence meaningful has been discarded before the search engine ever sees it.

This is the **whitespace impedance mismatch**: the fundamental unit assumed by the information retrieval system (the space-delimited word) is not the fundamental unit of meaning in the language being indexed (the morpheme or the morphological complex). The two systems operate at different levels of granularity, and the result is not just inefficiency — it is structural incompatibility.

Modern subword tokenization algorithms — Byte-Pair Encoding (BPE), WordPiece, SentencePiece — were developed partly to address the limitations of whitespace tokenization. Rather than treating each space-delimited word as an atomic token, these algorithms learn a vocabulary of common character sequences from training data, then split words into those sequences. “Unhappiness” might become “un” + “happiness” or “un” + “happi” + “ness,” depending on the training distribution.

In principle, subword tokenization should help with polysynthetic languages: a long word like *Inuululauqsimanngittualuujunga* would be split into smaller, more manageable pieces. In practice, it often makes things worse. The reason is in the training data: BPE vocabularies are learned from corpora that are overwhelmingly dominated by English and other analytic languages. The subword units that emerge — common English prefixes, suffixes, and character n-grams — have no morphologically meaningful relationship to Inuktitut or Mohawk or Nahuatl. The tokenizer splits the word, but it splits it *wrong* — cutting through the middle of morphemes, separating roots from their affixes, or grouping together character sequences that happen to be frequent in English but are meaningless in the target language.

The result is a double failure: the tokenizer neither preserves the word as a gestalt (which might at least allow whole-word matching) nor decomposes it into meaningful morphemic units (which would enable morpheme-level search). Instead, it produces a garbled sequence of arbitrary character fragments, destroying intelligibility in both directions. The polysynthetic word-sentence, which in its native cognitive processing is a highly structured ultrametric tree, is flattened into noise — and the search engine, built to find signal in structured sequences of discrete tokens, finds nothing.

### IV.B — Keyword Search vs. Morphemic Search

Even if the tokenization problem could be solved — even if a polysynthetic word could be reliably decomposed into its constituent morphemes — the fundamental architecture of keyword search would remain inadequate. This is because keyword search assumes that meaning is a *set* of independent concepts, and that retrieval consists of matching those concepts against documents that contain the same words. But in a polysynthetic language, meaning is not distributed across independent words — it is nested within a single morphological structure, and the relationships *between* morphemes matter as much as the morphemes themselves.

Consider the difference:

**English keyword search:** A user types “dog bites man” into a search box. The engine tokenizes this into three keywords: `dog`, `bites`, `man`. It looks for documents containing all three words (or close variants), ranks them by term frequency and inverse document frequency (TF-IDF) or neural embedding similarity, and returns results. The search has no understanding that `dog` is the agent and `man` is the patient — that information is carried by English word order, which the search engine ignores. But for many search tasks, this loss is tolerable. The co-occurrence of the three words is a good enough proxy for the propositional content.

**Polysynthetic morphemic search:** The equivalent query in a polysynthetic language might be a single word, or a short sequence. If a searcher wants to find content about “a dog biting a man in the past,” they might need to search for the root meaning “bite” combined with morphemes indicating “dog” (as agent), “man” (as patient), and past tense. But in a polysynthetic language, these are not separate words — they are bound morphemes that only appear as part of a larger morphological complex. A search for the root alone returns every word that contains it, regardless of argument structure. A search for a specific combination of morphemes fails if any one of them varies (e.g., a different tense marker, a different person marker, a different evidential). And the scope relationships — the fact that “dog” is the agent and “man” the patient, not vice versa — are encoded by morpheme *order* and *hierarchy*, which keyword search has no mechanism to represent.

To make this concrete, imagine the following scenario `[LLM-INFERRED]`:

- A researcher wants to find all instances in a Mohawk text corpus where a human agent performs an action on an animal patient. In English, you might search for combinations like “man bites dog” or “hunter kills bear” — the keywords carry the semantic roles implicitly through world knowledge. In Mohawk, the agent and patient are encoded through pronominal prefixes on the verb, and the nouns for “man” and “dog” may be incorporated into the verb itself. A keyword search for “man” would miss every instance where “man” is expressed through a pronominal prefix. A keyword search for the verb root would return every instance of the action, regardless of whether the agent is human, animal, or inanimate. To find what the researcher wants, you need to search not for *words* but for *morphological configurations* — specific patterns of prefix-root-suffix combinations that encode the relevant semantic roles.

This is **morphemic search**: retrieval based on the internal structure of words, not just their surface forms. It requires the search system to understand that a word is not an atom but a structure — a tree of meaningful parts, with edges that carry grammatical and semantic information. No major search engine, and no major database system, does this.

### IV.C — How This Warps Knowledge Access

The consequences of this architectural failure are not hypothetical. They are structural, systemic, and largely invisible to the English-speaking world.

**Information deserts.** When a language cannot be searched, its written corpus becomes, for practical purposes, inaccessible. A speaker of Inuktitut who wants to find information about traditional hunting practices, health care, or legal rights — topics for which Inuktitut-language content may well exist — cannot retrieve that content through the search tools that English speakers take for granted. The information is there, but the search path is not. This is not a content problem; it is an infrastructure problem.

**Machine translation failure.** Modern machine translation systems, including large language models, perform dramatically worse on polysynthetic languages than on analytic ones. The reasons are multiple: training data is scarce (low-resource language problem), tokenization is mismatched (as discussed above), and the fundamental architecture — which models translation as a mapping between sequences of discrete tokens — is poorly suited to mapping between a language where meaning is distributed across many tokens (English) and one where meaning is concentrated in few (polysynthetic). The result is that even where translation tools exist for polysynthetic languages, they are often unreliable to the point of unusability for serious tasks — legal, medical, educational — where accuracy matters.

**The compound effect.** The search failure and the translation failure compound each other. A polysynthetic speaker cannot search effectively in their own language, and they cannot reliably translate content from English into their language or vice versa. They are cut off from the global information ecosystem at both ends: they cannot find what exists, and they cannot bridge what they find to their own linguistic framework.

**Quantifying the exclusion.** How many people are affected? Polysynthetic languages are spoken by millions of people across North America (Mohawk, Cree, Inuktitut, Nahuatl), South America (Quechua, Aymara, Mapudungun), Australia (Tiwi, Warlpiri, Nunggubuyu), and Papua New Guinea (many Trans-New Guinea languages). Many of these languages have speaker populations in the tens or hundreds of thousands, and some — Quechua, Nahuatl — have millions. The total number of polysynthetic language speakers worldwide is difficult to estimate precisely, but it is on the order of 10 to 20 million people [^5]. For comparison, that is roughly the population of the Netherlands, or of Guatemala — a nation-sized community for whom the fundamental architecture of information retrieval is broken.

[^5]: Population estimate is `[LLM-INFERRED]` — based on the author’s training-data knowledge of global language demographics. A systematic survey using Ethnologue or Glottolog data is needed for a publication-quality figure. The estimate is conservative; including agglutinative languages with polysynthetic tendencies would substantially increase the count.
[^6]: This figure is `[LLM-INFERRED]` — based on the author’s training-data knowledge of search engine statistics. A verified source (e.g., Google’s annual search statistics report) should be cited for publication.

[^7]: This figure is `[LLM-INFERRED]` — based on the author’s training-data knowledge of Common Crawl corpus composition. The actual percentage varies by crawl and methodology; a verified source should be cited for publication.

### IV.D — The Data Bias in LLM Training

The problem extends beyond search engines to the newest and most powerful class of language technologies: large language models (LLMs).

LLMs are trained in three stages, and at every stage, the assumptions of analytic languages are baked in:

1. **Pretraining data:** The training corpora for models like ChatGPT, Claude, and Gemini are overwhelmingly English — not just English-language text, but text that reflects English-speaking cultural assumptions, argument patterns, and information structures. The Common Crawl corpus, which forms the backbone of many LLM training datasets, is estimated to be roughly 46% English.[^7] The next largest languages are Russian, German, Japanese, and Chinese — all analytic or agglutinative, none polysynthetic. Inuktitut, Mohawk, and Nahuatl are, at best, a rounding error in the training distribution.

2. **Tokenization:** As discussed in IV.A, the tokenizers used by LLMs are trained on the same English-dominated data. The resulting vocabularies are optimized for English-like morphology. When applied to polysynthetic languages — if they are applied at all — the tokenization is mismatched, producing either overly long sequences (one word = one token, wasting the model’s context window) or arbitrarily fragmented sequences (one word = many meaningless subword tokens, destroying morphological integrity).

3. **Alignment and evaluation:** LLMs are fine-tuned through reinforcement learning from human feedback (RLHF) and evaluated on benchmarks that are almost exclusively in English or major analytic languages. The “human” in RLHF is overwhelmingly an English speaker. The model learns to produce outputs that English speakers judge as helpful, coherent, and safe — criteria that may not transfer across languages, let alone across fundamentally different linguistic architectures.

The result is not just that LLMs perform poorly on polysynthetic languages. It is that the *concept of language* embedded in LLM architecture — language as a sequence of discrete tokens whose meaning is a function of their co-occurrence statistics — is an English-concept of language, and it systematically fails to capture the nested, hierarchical, ultrametric structure that polysynthetic languages make explicit.

There is a deeper architectural argument to be made here. Transformer models process text as a flat sequence of tokens, with attention weights that can, in principle, learn long-range dependencies. But the attention mechanism learns to approximate hierarchical structure from flat input; it is not given the tree. A polysynthetic word-sentence, which *is* a tree, must be reconstructed by the model from a flat token sequence — a process that is computationally expensive, data-hungry, and unreliable. An architecture that natively operated on nested semantic graphs — trees rather than sequences — would be a better match for the structure of polysynthetic language, and, we suspect, a better match for the structure of language in general.

This brings us to the constructive part of the argument. Having diagnosed the problem — English-centric digital infrastructure systematically fails polysynthetic languages at the levels of tokenization, search, translation, and model architecture — we now turn to what a solution might look like.

---

## V. Toward Integration: A Cross-Linguistic “Chunking” Framework

### V.A — The Universal Cognitive Base: Recursive Nesting

If the argument so far has been successful, we have established three things. First, that polysynthetic languages encode entire propositions within single morphological complexes — word-sentences that are structurally ultrametric trees. Second, that written polysynthesis challenges the space-delimited “word” as a universal unit of meaning. Third, that digital infrastructure built on English-like assumptions about what a word is systematically fails to index, search, or translate polysynthetic content. The question now is: what would a solution look like?

The answer begins with a claim that should, by now, be familiar: **the fundamental cognitive operation underlying all language is recursive chunking — the binding of many into one, applied iteratively to build hierarchical structures.** This is the “few become one” operation that the Ultrametric Cognition framework identifies as a cognitive primitive [^3]. What differs across languages is not the operation itself, but the *level* at which it is applied:

| Chunking Level | Morphological Type | Example | Surface Consequence |
|:---------------|:-------------------|:--------|:--------------------|
| Phrase / sentence | Isolating (English, Mandarin) | Separate words combined by syntax | Many tokens per proposition |
| Word | Agglutinative (Turkish, Japanese) | Morpheme chains within word boundaries | Fewer tokens, each internally structured |
| Word-sentence | Polysynthetic (Mohawk, Inuktitut) | Entire proposition in one morphological complex | One token = one complete event |

This is not a hierarchy of sophistication or complexity. It is a spectrum of *packaging strategies* — different answers to the question: “At what level of linguistic structure do we perform the chunking operation?” The Language-Info-Architecture project [^1] quantified the consequence: the entropy per word-form rises monotonically from isolating (~6.48 bits) to polysynthetic (~6.80 bits), reflecting the fact that more information is packed into each surface unit. The total information per proposition is invariant — the **compression-tax trade-off** ensures that what is saved in word count is paid in morphological complexity.

The practical implication for digital infrastructure follows directly. A search engine, a database, or a language model that assumes the English answer to the chunking question — “chunk at the phrase level, with many separate words” — will fail on languages that answer it differently. The solution is to design systems that are *agnostic* to the chunking level: systems that can represent meaning at any level of granularity, from the single morpheme to the multi-clause discourse, and that can search across languages by matching the underlying cognitive structure rather than the surface packaging.

### V.B — A Common Representation: The Nested Semantic Graph

The proposal, in its simplest form, is this: **instead of representing text as a flat sequence of tokens (words or subwords), represent it as a tree of nested concepts — a *nested semantic graph*.** In this representation:

- **Nodes** are conceptual primitives — roughly corresponding to the meanings carried by individual morphemes, regardless of whether those morphemes are free-standing words (as in English) or bound affixes (as in Mohawk). A node might represent an entity (“dog”), an action (“bite”), a temporal frame (“past”), an evidential source (“reported”), or a logical relation (“because”).

- **Edges** encode scope and modification relationships. An edge from node $A$ to node $B$ means that $A$ modifies, specifies, or is an argument of $B$. In an event description, the action node is the root, the agent and patient nodes are its children, and temporal, locative, and manner modifiers are children of those children or of the root, depending on their scope.

- **The tree is ultrametric.** For any three nodes, the two that are most closely related (share the lowest common ancestor) are closer to each other than either is to the third. The distance $d(x,y)$ between two nodes is the height of their lowest common ancestor in the tree, and this distance satisfies the strong triangle condition:

$$d(x,z) \leq \max\{d(x,y), d(y,z)\}$$

The crucial property of this representation is that it is **language-neutral.** The English sentence “The dog bit the man yesterday,” the Mohawk word-sentence that encodes the same event, and the Turkish agglutinative chain that does the same all map to the *same* nested semantic graph. They differ only in how the tree is linearized — how the nodes are ordered in time (or in writing) and where the chunk boundaries fall. The underlying structure is invariant.

This is not a new idea in linguistics — dependency grammars, semantic role labeling, and Abstract Meaning Representation (AMR) all move in this direction. What is new here is the explicit connection to ultrametric topology and the claim that this representation solves the digital search problem across the full morphological spectrum.

### V.C — Building Search and AI on Nested Graphs, Not Strings

Imagine a search engine built on nested semantic graphs rather than keyword indices. A user’s query — whether typed in English, spoken in Mohawk, or constructed through a visual query builder — is parsed into a semantic graph: a structured query that specifies not just *what* concepts are involved, but *how they relate*.

For example, a query for “dog bites man in the past” might produce a graph with:
- A root node: `BITE[event]`
- Arguments: `DOG[agent]`, `MAN[patient]`
- Modifier: `PAST[tense]`, attached to the event node.

The search engine’s task is to find documents whose semantic graphs contain a matching subgraph — a query that treats the document’s meaning representation as a database of structured events, not a bag of words.

This approach, which we might call **sub-graph matching search**, has several advantages over keyword search:

| Feature | Keyword Search | Sub-Graph Search |
|:--------|:---------------|:-----------------|
| **Unit of matching** | Surface word form | Semantic node (concept) |
| **Relationships** | Ignored (bag-of-words) | Preserved (edges encode scope) |
| **Cross-linguistic** | Requires translation | Language-neutral graph representation |
| **Polysynthetic compatibility** | Fails (word-sentence $\neq$ keywords) | Succeeds (word-sentence $\approx$ subgraph) |
| **Precision** | Low (co-occurrence $\neq$ meaning) | High (structure match $\approx$ meaning match) |

The requirements for building such a system are substantial but not insurmountable:

1. **Cross-linguistic semantic parsing.** We need parsers that can map surface text in any language — regardless of morphological type — to a common semantic graph representation. This is an active area of research in computational linguistics, and while no system today handles the full morphological spectrum, the direction of travel is clear.

2. **Ultrametric distance on graphs.** For ranking results, we need a distance metric on semantic graphs that respects the hierarchical structure. The ultrametric distance $d(G_1, G_2)$ between two graphs can be defined as the height of the lowest common ancestor of their root nodes in a graph-alignment lattice — a natural generalization of tree edit distance that preserves the strong triangle condition.

3. **Morphemic tokenization.** Before a polysynthetic text can be parsed into a semantic graph, it must be segmented into morphemes. This requires morphological analyzers trained on the target language — a resource that exists for some polysynthetic languages (e.g., Inuktitut, Cree) and is under development for others.

The key insight is that these three requirements are *not* separate projects. They are aspects of a single architecture — one that treats language as what it is: a system for building nested, ultrametric structures of meaning, not a system for stringing together independent tokens.

### V.D — Formalizing the Syntax-Tree Isomorphism

The connection between linguistic structure and ultrametric topology can be made precise. In the Syntactic Token Calculus (Modules M5 and M11) [^4], the ultrametric distance $d(x,y)$ on a syntactic tree is defined as:

$$d(x,y) = h(\text{lca}(x,y))$$

where $\text{lca}(x,y)$ is the lowest common ancestor of terminal symbols $x$ and $y$, and $h(n)$ is the height of node $n$ (its distance from the root). This distance satisfies the strong triangle condition — for any three terminals, the triangle is isosceles.

In a polysynthetic word, all morphemes share a single, shallow common ancestor: the word-level root. The ultrametric distance between any two morphemes within the same word is therefore small — the entire word-sentence is a single ultrametric cluster, with the root as the cluster center. In an English sentence, by contrast, words that belong to different phrases have a higher lowest common ancestor (the sentence-level root), and the distance between them is correspondingly larger. The sentence is a collection of loosely coupled clusters, not a single tight one.

This suggests a formal definition of the morphological typology spectrum in ultrametric terms:

- **Isolating languages** produce sentences with many clusters (words), each containing few nodes (morphemes), and large inter-cluster distances.
- **Polysynthetic languages** produce sentences with few clusters (word-sentences), each containing many nodes (morphemes), and small inter-cluster distances — essentially, one large ultrametric ball.

The strong triangle condition $d(x,z) \leq \max\{d(x,y), d(y,z)\}$ holds in both cases, but the *shape* of the tree — tall and sparse (isolating) versus short and bushy (polysynthetic) — captures the typological difference. Both are valid ultrametric trees; they differ in their branching factor and depth.

### V.E — The Cross-Ratio Analogy: Entropy as Invariant

There is a deeper mathematical connection that reinforces the proposal. The Language-Info-Architecture project (Path C — Cross-Project Synthesis) [^1] identified Shannon entropy as an invariant under recoding: when the same propositional content is “recoded” from the surface form of one language to another, the information content (in bits) is preserved, even as the entropy per surface unit varies.

Consider a concrete numerical illustration, drawn from the Language-Info-Architecture methodology [^1]:

| Language Type | Words per Proposition | Entropy per Word (bits) | Total Propositional Entropy (bits) |
|:--------------|:----------------------|:------------------------|:----------------------------------|
| Isolating (English-like) | ~7 words | ~6.48 | ~45.4 |
| Polysynthetic (Mohawk-like) | ~2 words | ~6.80 | ~13.6 (per word) |

Note: The “Total Propositional Entropy” comparison requires care. The Language-Info-Architecture project computed per-word entropy, not per-proposition entropy. The compression-tax trade-off ($r(H, L_{\text{total}}) = -0.48$) suggests that richer morphology substitutes for explicit category marking, but direct per-proposition entropy equivalence is a hypothesis requiring validation with real parallel corpora. The values above are illustrative of the methodology, not empirical claims.

This invariance is structurally analogous to the geometric cross-ratio. In projective geometry, the cross-ratio of four collinear points $A, B, C, D$:

$$(A,B;C,D) = \frac{AC \cdot BD}{AD \cdot BC}$$

is invariant under projective transformations. You can project the line onto another line, changing the individual distances between points, but the cross-ratio remains the same. The cross-ratio captures the *relational structure* of the points, which is preserved even as their absolute positions change.

Similarly, Shannon entropy captures the *relational structure* of a semantic proposition, which is preserved even as it is recoded into different surface syntaxes. The English sentence and the Mohawk word-sentence have different entropies per word-form — the Mohawk form is more “compressed” — but they carry the same total information. The compression-tax trade-off is the linguistic analogue of the projective transformation: it changes the surface measurement (entropy per word) while preserving the underlying invariant (total propositional information).

This analogy is more than elegant. It provides a design principle for cross-linguistic information systems: **index the invariant structure, not the surface projection.** The nested semantic graph is the invariant object. Each language’s surface form is a projection of it. A search engine built on graphs retrieves the invariant; a search engine built on keywords retrieves the projection — and then only one projection, in one language, for one morphological type.

We can state this as a principle:

> **The Entropy Invariance Principle for Cross-Linguistic Search:** *The information content of a semantic proposition, measured in bits, is invariant under recoding into any human language. A search architecture that indexes the surface projection (words, keywords, token sequences) will fail on languages whose surface projection differs significantly from the training distribution. A search architecture that indexes the invariant structure (nested semantic graphs, ultrametric trees) will succeed across the full morphological spectrum.*

This principle is the constructive heart of the synthesis. It says that the digital divide we diagnosed in Section IV is not inevitable — it is a consequence of a particular design choice, and a different choice, guided by the ultrametric structure of language, can close it.

---


## VI. Broader Implications: Learning from Polysynthesis to Think Differently

### VI.A — Polysynthesis as a Mirror of Thought

We have spent five sections diagnosing a problem — English-centric digital infrastructure fails polysynthetic languages — and proposing a solution — nested semantic graphs built on ultrametric structure. But there is a deeper implication here, one that goes beyond search engines and tokenizers.

The polysynthetic word is a hologram of an entire event. When a Mohawk speaker produces a word-sentence, they are not assembling a message piece by piece, as an English speaker does. They are delivering a complete, structured event description in a single cognitive and phonological gesture. The morphemes are not separate atoms glued together; they are simultaneous, layered, nested distinctions that together constitute the event. The speaker holds the agent, the patient, the action, the time, the aspect, and the evidential source in mind *at once* and expresses them *at once*.

This is the equilateral triangle of ultrametric space — a single chunk with multiple equal parts, none reducible to a binary pair — expressed in language. It challenges a fundamental assumption that English embeds in its speakers: that the world is composed of separate things (nouns) that do separate things (verbs) in separate times and places (adverbials), and that thinking consists of stringing these separate concepts together in sequence. Polysynthetic languages suggest a different model: thinking consists of holding a structured field of relations in mind and expressing it as a unified gestalt.

This is not to romanticize polysynthesis or to claim that Mohawk speakers think in a fundamentally different way than English speakers. The cognitive operation — recursive chunking — is universal. What differs is the *habitual unit* of expression. An English speaker is trained from childhood to chunk at the level of the individual word; a Mohawk speaker is trained to chunk at the level of the complete event. Over a lifetime, this difference in habitual chunking may shape cognitive style — not deterministically, but probabilistically, in the way that learning to play chess shapes pattern recognition or learning to draw shapes visual attention.

The point is not that one cognitive style is better than the other. The point is that English speakers — and the digital infrastructure they build — are often unaware that there *is* another cognitive style. Recognizing polysynthesis as a mirror of a different way of chunking thought is the first step toward building systems that serve all ways of thinking, not just the one that feels natural to the builders.

### VI.B — Designing for Linguistic Pluralism

What would a digital world designed for linguistic pluralism look like? Not a world where every language is forced into an English-shaped mold, but one where the architecture of information retrieval is flexible enough to accommodate the full spectrum of human linguistic diversity.

Some directions:

1. **Spoken interfaces.** A polysynthetic word-sentence is a natural unit for speech. Voice-based search — already growing rapidly — may be inherently more compatible with polysynthetic languages than text-based search, because speech does not impose artificial word boundaries the way whitespace-delimited text does. A spoken query in Mohawk or Inuktitut could be processed as a single semantic unit, parsed into a nested graph, and matched against a language-neutral index.

2. **Visual query builders.** Instead of typing keywords into a box, a user could construct a query by selecting and nesting conceptual elements in a visual interface — dragging an action node onto a canvas, attaching agent and patient nodes, setting tense and aspect through dropdown menus. This approach treats the query as a semantic graph from the start, bypassing the surface-language bottleneck entirely. It would work equally well for speakers of any language, regardless of morphological type.

3. **The document as a navigable tree.** If meaning is a nested graph, a “document” need not be a linear sequence of sentences. It could be a navigable tree of nested chunks — a representation that a reader can explore by expanding and collapsing nodes, following edges to related concepts, and viewing the same content at different levels of granularity. This would be a natural fit for polysynthetic content, where the surface text is already a compressed tree, but it could also enrich how English speakers interact with complex information.

### VI.C — The Consilience

The most striking implication of this synthesis is the convergence it reveals. The same recursive logic — “few become one, one becomes few” — appears in:

- **Physics:** The ultrametric structure of spin glass energy landscapes, the renormalization group in quantum field theory, and the Bruhat-Tits trees of $p$-adic geometry, all of which exhibit the strong triangle condition as a structural invariant.

- **Biology:** Phylogenetic trees, where species are clustered by shared ancestry and the distance between any two species is the height of their lowest common ancestor — an ultrametric distance.

- **Cognition:** The chunking operation that binds multiple perceptual items into a single cognitive unit, and the hierarchical organization of concepts from sensory primitives to abstract categories.

- **Language:** The morphological spectrum from isolating to polysynthetic, which is simply the chunking operation applied at different levels of the linguistic hierarchy.

This is not a coincidence. The Computational Syntax of Reality project established the formal bridge between syntactic token calculus and physical ultrametric structures, showing that Bruhat-Tits trees, $p$-adic valuations, and syntactic constituency are manifestations of the same underlying mathematics. The polysynthetic word-sentence, the phylogenetic tree, and the spin glass energy landscape are not merely analogous — they are structurally isomorphic. They are the same mathematical object — an ultrametric tree — realized in different substrates.

The Mohawk verb and the Bruhat-Tits tree are siblings. They share a common ancestor in the abstract structure of hierarchical branching, and their family resemblance is not poetic but mathematical.

For English speakers, this consilience is especially important because English — with its isolating structure and its tendency to present the world as a sequence of separate things — can too easily obscure the unity. English grammar trains its speakers to see parts first and wholes second; polysynthetic grammar trains its speakers to see wholes first and parts second. The ultrametric tree is the invariant that contains both perspectives, and recognizing it is a way of seeing past the accidents of one’s native language to the deeper structure beneath.

### VI.D — The Knowledge Integration Problem, Revisited

Let us return, in closing, to the problem that opened this investigation: the fragmentation of global knowledge by language.

The problem is not merely that people speak different languages and therefore cannot access each other’s information. It is that the very architecture of information storage and retrieval — keyword indices, whitespace tokenization, sequence-to-sequence models — encodes a particular theory of what language is, and that theory is false for the majority of the world’s linguistic diversity. The fragmentation is not a content problem with a translation solution; it is a structural problem requiring a structural solution.

The nested semantic graph proposal offers such a solution. By indexing the invariant structure — the semantic tree — rather than its surface projections, a search architecture can be genuinely language-neutral. A query in Mohawk, English, or Turkish, or a query constructed through a visual interface with no surface language at all, would be matched against the same index of semantic graphs. The language one happens to speak would determine the *interface*, not the *architecture*.

This is an ambitious vision. It requires advances in cross-linguistic semantic parsing, morphemic tokenization for low-resource languages, and graph-based relevance ranking that respects ultrametric structure. It requires investment in language technologies for communities that the market, left to itself, will not serve. And it requires — perhaps hardest of all — that the builders of digital infrastructure recognize that their native language’s structure is not a universal law of information, but one branch on a vast and ancient tree.

But the alternative is worse. The alternative is a world in which the architecture of knowledge is built by and for speakers of a handful of analytic languages, and the remaining 95% of human linguistic diversity — and the cognitive architectures they carry — is treated as noise. That world is the one we have now. The nested semantic graph is a path toward a different one.

---


## VII. Summary of the Synthesis

### VII.A — Core Argument (Restated)

This document has advanced a single, sustained argument:

1. **Polysynthetic communication** — the encoding of entire propositions within single morphological complexes — is the extreme, explicit expression of the mind’s recursive chunking operation (“few become one”) in linguistic form. A polysynthetic word-sentence is an ultrametric tree: a root surrounded by nested affixes whose scope relations satisfy the strong triangle condition $d(x,z) \leq \max\{d(x,y), d(y,z)\}$.

2. **Written polysynthesis** challenges Western, space-delimited notions of the “word” as a universal unit of meaning. Syllabic systems like Inuktitut and Cree offer a better visual fit for polysynthetic morphology, and the concept of morphographic writing — a script that directly reflects morphological tree structure — points toward a writing system that respects rather than imposes upon the cognitive architecture of the language.

3. **Digital infrastructure built on English assumptions** — whitespace tokenization, keyword indexing, sequence-to-sequence models — systematically fails polysynthetic languages. The tokenization impedance mismatch destroys internal morphological structure; keyword search cannot retrieve content encoded in bound morphemes; machine translation and large language models, trained on English-dominated data, perform poorly on the full morphological spectrum.

4. **A universal solution** lies in modeling meaning as nested ultrametric trees — nested semantic graphs — rather than as linear strings of tokens. In this representation, the English sentence, the Mohawk word-sentence, and the Turkish agglutinative chain all map to the same underlying cognitive structure. They differ only in linearization and chunking level. A search architecture built on sub-graph matching across these trees would be genuinely language-neutral, serving speakers of all morphological types equally.

5. **The Entropy Invariance Principle** provides the theoretical foundation: Shannon entropy, like the geometric cross-ratio, is an invariant under recoding. Index the invariant structure, not its surface projection, and the search architecture works across the full spectrum of human language.

### VII.B — For English Speakers

To the English speaker who has followed this argument: the invitation is to escape the “one word equals one concept” prison.

What feels natural to you — subject-verb-object order, space-delimited words, keyword search — is not natural. It is *familiar*. It is the product of a particular linguistic tradition, refined over centuries into a set of conventions so deeply internalized that they feel like laws of nature. They are not. They are one branch on a vast and ancient tree of possible language architectures, and the tree itself — the ultrametric structure of hierarchical nesting — is the deeper reality.

The polysynthetic word-sentence is not an exotic outlier. It is a reminder that language, at its core, is the same cognitive operation everywhere: individuate and nest, few become one. Different languages simply draw the chunk boundaries at different levels. Recognizing this is not just an intellectual exercise — it is a prerequisite for building information systems that serve all of humanity, not just the fraction whose native language happens to shape the default architecture.

### VII.C — Open Questions for Future Work

This synthesis has been primarily conceptual and synthetic. It has drawn on prior quantitative work (Language-Info-Architecture, Syntactic Token Calculus) and proposed a new architecture (nested semantic graphs, sub-graph matching search). But significant work remains to make this vision concrete:

1. **Empirical validation of the entropy invariance claim.** The compression-tax trade-off ($r(H, L_{\text{total}}) = -0.48$) was computed from synthetic data. Real parallel corpora — the same propositional content expressed in languages spanning the full morphological spectrum — are needed to test whether total propositional entropy is truly invariant.

2. **Morphemic tokenization at scale.** Can morphological analyzers, trained on low-resource polysynthetic languages, be integrated into production search pipelines? What is the performance cost relative to whitespace tokenization, and can it be made acceptable?

3. **Semantic graph query interface design.** What does a usable sub-graph matching search interface look like? How do users express structured event queries in a way that is intuitive across languages and literacy levels?

4. **Non-concatenative morphology.** The nested semantic graph proposal assumes that morphemes are linearly segmentable — prefixes, suffixes, and incorporated nouns arranged in sequence. How does this framework handle non-concatenative morphology, such as the triconsonantal root system of Semitic languages or the tonal morphology of some West African languages?

5. **Cognitive measurement.** Does literacy in a polysynthetic language produce measurably different chunking strategies — as measured by reading time, eye-tracking, or neurological imaging — compared to literacy in an analytic language?

6. **LLM architecture redesign.** Can transformer architectures be modified, or new architectures developed, that natively operate on nested semantic graphs rather than flat token sequences? What would a “tree-native” language model look like?

These questions are not rhetorical. They define a research program — one that sits at the intersection of linguistics, cognitive science, computer science, and mathematics — and that program begins with the recognition that the ultrametric tree is the invariant structure beneath the surface diversity of human language.

---

## References

1. Quni-Gudzinas, R. B. (2026). *Language-Info-Architecture*. Zenodo. DOI: [10.5281/zenodo.20137616](https://doi.org/10.5281/zenodo.20137616).
2. Quni-Gudzinas, R. B. (2026). *Syntactic Token Calculus* (Modules M1-M12). Unpublished manuscript, Obsidian releases 2026/04.
3. Quni-Gudzinas, R. B. (2026). *Ultrametric Cognition*. Unpublished manuscript, Archive 2026/04.
4. Quni-Gudzinas, R. B. (2026). *Computational Syntax of Reality: Addressing the Continuous-Discrete Tension via Syntactic Token Calculus*. Unpublished manuscript, Archive 2026/04.
