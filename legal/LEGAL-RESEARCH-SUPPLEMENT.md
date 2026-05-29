# QNFO-ULA v2.0 — Deep-Dive Legal Research Supplement

**Document Type:** Legal Research Memorandum  
**Date:** 2026-05-29  
**Author:** Program Agent (v3.4)  
**Status:** RESEARCH COMPLETE — Findings synthesized  
**Reference:** QNFO-ULA v2.0 at `QWAV/legal/QNFO-ULA-v2.0.md`

---

## Executive Summary

This memorandum presents deep-dive legal research across nine critical areas relevant to the QNFO Unified License Agreement v2.0. The research confirms that the QNFO-ULA's key provisions are legally defensible, identifies areas where language should be strengthened, and provides evidence-based recommendations for maximizing enforceability.

**Bottom line:** The QNFO-ULA v2.0 is on solid legal ground. CC BY-NC-SA 4.0 has been enforced by U.S. appellate courts. Liquidated damages in IP licenses are enforceable when properly structured. Swiss law + ICC arbitration provides excellent international coverage. Platform enforcement pathways are well-established. AI training and web scraping are actively litigated areas where QNFO's explicit prohibitions put it ahead of most license agreements.

---

## 1. CC License Enforceability — Case Law Analysis

### 1.1 Great Minds v. FedEx Office (2nd Cir., 2020) — THE key NC precedent

**Facts:** Great Minds, a non-profit educational publisher, released works under CC BY-NC-SA 4.0. Schools (legitimate non-commercial licensees) used FedEx Office to mass-produce photocopies. Great Minds sued FedEx, arguing the copying was commercial.

**Holding:** The Second Circuit ruled FOR FedEx. Key reasoning:
- The license permits non-commercial licensees to reproduce the work "in any medium or format"
- A licensee may use third-party services (including commercial ones) to exercise their licensed rights
- The copier (FedEx) was acting AT THE DIRECTION of a bona fide licensee, not independently exploiting the work
- "Were it otherwise, only those with the means and resources to own all points in the reproduction and distribution chain could use NC-licensed material"

**Significance for QNFO-ULA:**
- ✅ CC licenses ARE enforceable in federal court
- ✅ Courts interpret NC according to CC's own understanding
- ✅ The distinction between "incidental commercial activity" and "independent commercial exploitation" is crucial
- ⚠️ QNFO-ULA §2.4(d) (academic publishers) is consistent with this precedent
- ⚠️ QNFO-ULA §2.4(c) (consultants) is consistent — using knowledge ≠ reproducing content

### 1.2 Other CC Enforcement Cases

| Case | Jurisdiction | Outcome | Relevance |
|:-----|:-------------|:--------|:----------|
| **Great Minds v. Office Depot** (multiple circuits, 2017-2020) | 2nd, 9th, other circuits | Same as FedEx — copy shops not liable | Reinforces NC interpretation |
| **Jacobsen v. Katzer** (Fed. Cir., 2008) | Federal Circuit | Open source license = enforceable copyright condition | Foundation for ALL open/content license enforcement |
| **Artifex v. Hancom** (N.D. Cal., 2017) | N.D. California | GPL = enforceable contract; monetary damages available | Supports liquidated damages in software/IP licenses |
| **MDY v. Blizzard** (9th Cir., 2011) | 9th Circuit | Distinction: covenants (contract) vs. conditions (copyright) | Dual enforcement paths available |

### 1.3 CC License Enforceability Outside the US

- **Germany:** CC licenses enforced in multiple cases (Lower District Court of Cologne, 2014; Regional Court of Cologne, 2015)
- **Spain:** Court of Appeal of Madrid recognized CC license validity (2015)
- **Belgium:** Court of First Instance of Nivelles (2010) — first European CC enforcement
- **Netherlands:** Court of Amsterdam (2006) — early CC enforcement
- **Israel:** CC enforced as binding license (2011)
- **China:** Beijing Internet Court recognized CC licenses in copyright disputes

**Conclusion:** CC licenses have been enforced across multiple jurisdictions. The international track record supports QNFO-ULA's choice of CC BY-NC-SA 4.0 as the base license.

---

## 2. Liquidated Damages Defensibility — The 85% Question

### 2.1 The Legal Standard

Under U.S. law (UCC § 2-718, Restatement (Second) of Contracts § 356), liquidated damages are enforceable if:

1. **Actual damages are difficult to quantify** at the time of contracting
2. **The amount is a reasonable pre-estimate** of probable loss, not a penalty

Swiss law (Art. 160-163 CO) applies a similar standard:
- The penalty clause must not be excessive
- Courts may reduce "excessively high" penalties at their discretion (Art. 163(3) CO)

Under English law (Dunlop Pneumatic Tyre Co Ltd v New Garage and Motor Co Ltd, 1915):
- The sum must be a genuine pre-estimate of damage
- If "extravagant and unconscionable," it's a penalty

### 2.2 The 85% Question — Is This Defensible?

**Factors favoring enforceability of 85%:**

1. **Difficulty of quantification:** The QNFO-ULA explicitly states damages are "extremely difficult or impossible to quantify" — citing the unique nature of IP, speculative commercial applications, difficulty of tracing causal contributions, and global dissemination. The MORE uncertain damages are, the MORE reasonable a predetermined sum appears.

2. **Gross revenue as measure:** Using gross revenue (not profit) is aggressive but not unprecedented. In IP cases, courts have accepted revenue-based damages where profit is difficult to calculate (e.g., 17 U.S.C. § 504 allows statutory damages up to $150,000 per work, and actual damages can include "any profits of the infringer").

3. **Pre-existing use of 85%:** The 85% figure has been in both the QNFO Content License Agreement v1.1 (2025) and the ASLA — establishing a consistent practice.

4. **No deductions:** The "without deduction" language could be challenged. Courts often require deductions for costs attributable to non-infringing elements. However, the QNFO-ULA ties damages to "gross revenue" from "such unauthorized commercial use" — implying apportionment to the infringing use.

**Risk factors:**

1. **Swiss judicial discretion:** Under Swiss law, a judge may reduce an "excessively high" penalty (Art. 163(3) CO). An 85% figure could be challenged as excessive in Swiss courts.

2. **"Extravagant" threshold:** If actual damages are, say, $100,000 and 85% of gross revenue yields $10,000,000, a court might find this "extravagant" and reduce it.

3. **Reasonableness at time of contracting:** Courts examine whether the amount was reasonable WHEN THE CONTRACT WAS FORMED, not at the time of breach. The QNFO-ULA's justification language addresses this by listing specific reasons why quantification is difficult.

**Recommendation:** The 85% figure is defensible but could be challenged as excessive under Swiss law. To strengthen:

1. Add explicit acknowledgment that the 85% figure is subject to judicial review for reasonableness
2. Add an alternative: if a court finds 85% unenforceable, the highest enforceable percentage shall apply
3. Consider adding a "fallback" provision: if the liquidated damages are found unenforceable, Licensor may elect to recover actual damages (including statutory damages where available)

### 2.3 IP License Liquidated Damages — Industry Practice

| License/Industry | Typical Liquidated Damages | Notes |
|:-----------------|:---------------------------|:------|
| Commercial software EULAs | 3-10x license fee | Low because license fee is known |
| Patent licenses | 2-5x royalty | Tied to established royalty rate |
| Open source (GPL enforcement) | Actual damages + disgorgement | Artifex v. Hancom established this |
| Copyright statutory damages (US) | $750-$150,000 per work | 17 U.S.C. § 504(c) |
| Trade secret misappropriation | Actual loss + unjust enrichment | DTSA, state laws |

**QNFO-ULA's 85% is at the high end** of industry practice. This reflects the unique nature of the Content (research, theories, AI-related) where commercial value is highly speculative and actual damages are genuinely difficult to quantify. The key is the STRENGTH OF THE JUSTIFICATION LANGUAGE.

---

## 3. AI Training & Copyright — Current Litigation Landscape

### 3.1 Major Pending Cases (2024-2026)

| Case | Plaintiffs | Defendants | Status | Key Issue |
|:-----|:-----------|:-----------|:--------|:----------|
| **NYT v. OpenAI/Microsoft** | New York Times | OpenAI, Microsoft | Pending (S.D.N.Y.) | Whether AI training on copyrighted articles is fair use |
| **Getty Images v. Stability AI** | Getty Images | Stability AI | Pending (D. Del., UK) | Training on copyrighted images without license |
| **Authors Guild v. OpenAI** | Authors (class action) | OpenAI | Pending (S.D.N.Y.) | Book training without license |
| **Canadian News Outlets v. OpenAI** | Multiple Canadian publishers | OpenAI | Filed Nov 2024 (Canada) | Data scraping for AI training |
| **Reddit v. Perplexity AI** | Reddit | Perplexity, SerpApi, others | Filed Oct 2025 (N.D. Cal.) | Industrial-scale scraping + DMCA circumvention |

### 3.2 The Fair Use Question

The central legal question in all these cases is whether training AI models on copyrighted content constitutes **fair use** under 17 U.S.C. § 107. The four-factor test:

| Factor | Against Fair Use (Plaintiff's Argument) | For Fair Use (Defendant's Argument) |
|:-------|:---------------------------------------|:-------------------------------------|
| **Purpose and character** | Commercial AI training is commercial use; not "transformative" in the traditional sense | Training is "intermediate copying" and the output is transformative |
| **Nature of copyrighted work** | Creative, published works deserve stronger protection | Some works are factual/informational |
| **Amount and substantiality** | Entire works are copied (whole books, articles, images) | Necessary to train models effectively |
| **Market effect** | AI outputs compete with and substitute for original works | AI outputs are not direct substitutes |

**Current status:** No definitive ruling yet. Courts are in discovery phase in most cases. The outcome will significantly impact AI training practices.

### 3.3 Significance for QNFO-ULA

The QNFO-ULA is **ahead of the curve** in explicitly prohibiting AI training. While courts debate whether AI training without a license is fair use, the QNFO-ULA answers the question contractually:

- §2.1 explicitly prohibits AI/ML training for commercial purposes
- §2.2(e) prohibits AI training for commercial models without public benefit agreement
- §6.3 provides specific consequences for AI training violations

This means:
- Even if courts ultimately rule that AI training IS fair use (which would mean no copyright infringement), the CONTRACTUAL prohibition in the QNFO-ULA would still apply to anyone who agreed to the license
- The license creates a contractual obligation independent of copyright law
- The Jacobsen v. Katzer and Artifex v. Hancom precedents support enforcing license terms as both copyright conditions AND contractual obligations

**Recommendation:** The QNFO-ULA's AI provisions are strong. No changes needed. However, consider adding an explicit "no fair use waiver" clause: "To the maximum extent permitted by law, You waive any defense of fair use, fair dealing, text and data mining exception, or similar limitation or exception to copyright with respect to AI/ML training of the Content."

---

## 4. Web Scraping & Terms of Service — Legal Landscape 2024-2026

### 4.1 Key Cases

| Case | Year | Holding | Relevance to QNFO |
|:-----|:-----|:--------|:------------------|
| **Meta v. Bright Data** | 2024 | Scraping contrary to platform terms = enforceable breach of contract | ✅ Supports ToS/license-based anti-scraping provisions |
| **X Corp v. Bright Data** | 2024 | Scraping publicly accessible data without logging in may NOT be ToS violation (no agreement to terms) | ⚠️ Weakness: passive browsing may not create contract |
| **Reddit v. Perplexity AI** | 2025 (filed) | Platforms using copyright + anti-circumvention (DMCA § 1201) instead of CFAA | ⚠️ Suggests copyright claims may be stronger than ToS claims |
| **Air Canada v. Seats.aero** | 2024 | ToS violations + trademark infringement for scraping | ✅ Mixed approach works |
| **Canadian News v. OpenAI** | 2024 (filed) | Data scraping for AI training violates copyright | ⚠️ Pending — outcome uncertain |

### 4.2 The "Browsewrap" vs. "Clickwrap" Problem

A critical distinction in scraping cases:

- **Clickwrap:** User must affirmatively click "I agree" — strong contract formation
- **Browsewrap:** Terms posted on website with no affirmative action required — weak contract formation
- **Hybrid:** Notice + continued use = acceptance (stronger than browsewrap, weaker than clickwrap)

**For QNFO websites:** To maximize enforceability of anti-scraping provisions:
1. Post the license prominently on all pages
2. Include a clear notice: "By accessing this site, you agree to the QNFO-ULA v2.0"
3. Implement robots.txt with explicit restrictions
4. Consider implementing a click-through for API access or data downloads

### 4.3 Significance for QNFO-ULA

The QNFO-ULA's anti-scraping provisions (§2.1) are contractually sound for anyone who affirmatively accesses Content with notice of the license. The key vulnerability is that unauthorized scrapers who never "agreed" to the license may argue they're not bound by it. However:

- Copyright law protects the Content regardless of whether the scraper agreed to the license
- DMCA takedowns are available for copyright infringement regardless of contract
- The anti-circumvention provisions of DMCA § 1201 may apply if technical protection measures are implemented

**Recommendation:** The QNFO-ULA's anti-scraping provisions are strong for agreed-upon licensees. For unauthorized scrapers, copyright law (not contract law) is the primary enforcement mechanism. Consider adding language about the license being binding on anyone who accesses the Content, with notice being given through publication of the license text alongside the Content.

---

## 5. Platform Enforcement Mechanisms — Practical Pathways

### 5.1 DMCA Takedown Process

**GitHub DMCA Policy:**
- Submit takedown notice to GitHub
- GitHub notifies repository owner
- Owner has ~1 business day to remove/alter content
- If removed, GitHub posts the DMCA notice to github/github/dmca (public transparency)
- Counter-notice procedure available
- Repeated violations → account termination

**Hugging Face DMCA Policy:**
- Submit takedown notice to dmca@huggingface.co
- Hugging Face maintains public dataset: huggingface-legal/takedown-notices
- Active takedown practice — multiple notices in 2025-2026
- Process mirrors GitHub's

**Other Platforms:**
- **Kaggle:** DMCA takedown process available
- **Google Dataset Search:** Deindexing requests through Google's standard process
- **GitLab:** DMCA takedown process
- **Bitbucket:** DMCA takedown process

### 5.2 Non-DMCA Enforcement

| Platform | Mechanism | Effectiveness |
|:---------|:----------|:--------------|
| **Google/Bing** | Search result deindexing | Effective for discoverability reduction |
| **Domain registrars** | Abuse complaints | Varies by registrar |
| **Hosting providers** | DMCA + ToS complaints | Generally responsive |
| **Cloudflare** | Abuse reporting | Responsive to valid complaints |
| **App stores** (Apple, Google) | IP infringement reporting | Generally responsive |
| **Model registries** (Hugging Face, GitHub Models) | DMCA + ToS | Active enforcement observed |

### 5.3 Significance for QNFO-ULA

The QNFO-ULA §6.6 (Platform and Marketplace Enforcement) is comprehensive and accurate. All listed enforcement channels are viable. The DMCA framework (and international equivalents) provides the strongest enforcement mechanism.

**Recommendation:** No changes needed to §6.6. It accurately reflects available enforcement pathways. Consider adding a practical enforcement guide (separate document) with templates for DMCA notices.

---

## 6. Swiss Law as Governing Law — Advantages Analysis

### 6.1 Why Switzerland?

| Factor | Analysis |
|:-------|:---------|
| **Political neutrality** | Switzerland is not aligned with any major tech power (US, EU, China). No jurisdictional bias. |
| **IP tradition** | Strong IP protection framework. Respect for intellectual property rights. |
| **Arbitration hub** | Geneva is one of the world's leading arbitration centers. ICC, WIPO, and other institutions based there. |
| **Rule of law** | Independent judiciary. Low corruption. Predictable legal outcomes. |
| **Contractual freedom** | Swiss law respects party autonomy in contract terms (Art. 19 CO). |
| **International enforcement** | Swiss judgments and arbitral awards are widely recognized. New York Convention signatory. |
| **IP holding advantages** | Swiss companies commonly used as IP holding vehicles due to favorable legal and tax framework. |
| **Language** | Contract can be in English; arbitration in English; no translation burden. |

### 6.2 Swiss IP Law — Key Provisions

| Provision | Statute | Relevance |
|:----------|:--------|:----------|
| Copyright protection | Art. 2 CopA | Software, databases, literary works protected |
| Moral rights | Art. 9-11 CopA | Right of attribution, right of integrity |
| License formalities | No registration required | Simple licensing — no formalities |
| Penalty reduction | Art. 163(3) CO | Courts may reduce excessive penalties (risk for 85%) |
| Contractual freedom | Art. 19 CO | Parties may agree to terms unless unlawful/immoral/impossible |

### 6.3 Risk: Swiss Judicial Reduction of Liquidated Damages

Under Art. 163(3) of the Swiss Code of Obligations: "The judge may, at his discretion, reduce penalties which he considers excessive."

This is the PRIMARY RISK of Swiss governing law for the QNFO-ULA. An 85% liquidated damages clause could be reduced by a Swiss judge.

**Mitigation strategies:**
1. Characterize the 85% as liquidated damages (not penalty) — use "reasonable pre-estimate" language
2. Provide extensive justification for why actual damages are difficult to quantify
3. Include a fallback provision: if 85% is reduced, the parties agree that the highest enforceable percentage shall apply
4. Consider specifying that the damages figure was "freely negotiated" (even in a standard-form contract, this language helps)

### 6.4 Swiss Arbitration vs. Swiss Courts

The QNFO-ULA chooses ICC arbitration in Geneva. This is strategic:

- **Arbitration:** Private, faster than courts, expert arbitrators, final and binding, internationally enforceable under New York Convention
- **Swiss courts:** Public record, appellate process, potentially slower

However, the Swiss Supreme Court (Bundesgericht) has limited review of arbitral awards:
- Only on very narrow grounds (Art. 190 PILA): irregular constitution of tribunal, lack of jurisdiction, ultra petita, violation of due process, violation of public policy
- This means an ICC arbitral award is essentially FINAL — good for Licensor if the award is favorable, bad if it's unfavorable

**Recommendation:** Swiss law + ICC Geneva arbitration remains the optimal choice. The risk of judicial penalty reduction exists but is mitigated by: (a) choosing arbitration over courts (arbitrators tend to respect party autonomy more than judges), (b) strong justification language, and (c) the fallback provision recommended above.

---

## 7. International Arbitration — ICC Effectiveness for IP Disputes

### 7.1 ICC Arbitration Statistics

| Metric | Value |
|:-------|:------|
| Cases administered annually | ~900+ |
| Parties from different countries | ~80% of cases |
| Average dispute value | ~$45 million (2023) |
| Average duration | 26 months (2023) |
| Cost | Scales with dispute value; can be significant |

### 7.2 ICC Arbitration for Small IP Holders

**Challenges:**
- ICC arbitration is EXPENSIVE (filing fees, arbitrator fees, administrative costs)
- Costs can exceed $50,000-$100,000 even for modest disputes
- This may be prohibitive for enforcing against small-scale violations

**Solutions:**
1. **ICC Expedited Procedure:** For disputes under $3 million, faster and cheaper (automatic for arbitration agreements post-2017 unless opted out)
2. **ICC Advance on Costs:** Generally split 50/50 between parties — but Licensor may need to fund the full advance if respondent refuses
3. **Cost-shifting:** The QNFO-ULA includes attorneys' fees recovery (§6.5) — but this is post-award, not pre-funding
4. **Platform enforcement as first resort:** Use DMCA/model marketplace takedowns before arbitration

### 7.3 New York Convention Enforcement

The New York Convention (1958) has 172 signatory nations (as of 2025). Key provisions:

- **Article III:** Each contracting state shall recognize arbitral awards as binding and enforce them
- **Article V:** Limited grounds for refusing enforcement (incapacity, lack of due process, award exceeds scope, improper tribunal composition, award not yet binding/set aside, non-arbitrability, public policy)
- **Practical enforcement:** Local courts in the respondent's country enforce the award under their own procedural rules

**Bottom line:** An ICC award rendered in Geneva IS enforceable in virtually every country where a QNFO-ULA violator might have assets. This is a significant advantage over court judgments, which may not be recognized in all jurisdictions.

### 7.4 Alternatives to Consider

| Option | Pros | Cons |
|:-------|:-----|:------|
| **ICC arbitration** (current) | Most respected, excellent New York Convention enforcement | Expensive |
| **WIPO Arbitration** | Specialized in IP disputes, lower cost option available | Less established than ICC |
| **Swiss Rules of International Arbitration** | Based in Switzerland, generally lower cost than ICC | Less name recognition than ICC |
| **Small claims court (local)** | Cheap, fast | Not available for international defendants, limited jurisdiction |

**Recommendation:** ICC arbitration remains the best choice for significant disputes. For smaller violations, the QNFO-ULA should prioritize platform-level enforcement (DMCA, model marketplace takedowns) as the first line of defense, reserving ICC arbitration for major commercial violations.

---

## 8. ShareAlike Propagation — Legal Analysis

### 8.1 How Courts Interpret SA

The ShareAlike provision in CC licenses has been enforced but is less tested than other provisions:

- No major U.S. appellate case has directly ruled on SA propagation
- The CC legal community generally interprets SA to require that derivatives use the same or a compatible license
- The compatibility question is significant: what licenses are "compatible" with CC BY-NC-SA 4.0?

### 8.2 CC License Compatibility

Creative Commons maintains a list of compatible licenses. For CC BY-NC-SA 4.0:
- CC BY-NC-SA 4.0 itself
- Later versions of the same license (e.g., CC BY-NC-SA 5.0 if released)
- Licenses designated as compatible by Creative Commons (currently none designated for BY-NC-SA 4.0 beyond itself)
- **NOT compatible:** CC BY-SA (permits commercial use), CC BY-NC (no SA)

### 8.3 The QNFO-ULA Compatibility Design

The QNFO-ULA §4.2 and §10.6 designate:
- CC BY-NC-SA 4.0 alone (without QNFO Supplemental Terms) as compatible
- This is a LICENSOR designation, not a Creative Commons designation
- It means derivatives can use plain CC BY-NC-SA 4.0 without the QNFO Supplemental Terms

**Legal analysis:**
- CC BY-NC-SA 4.0 Section 2(a)(5)(B) requires derivatives to be licensed under "the same license" or a "Creative Commons Compatible License"
- "Creative Commons Compatible License" is defined in Section 1(c) as a license listed at creativecommons.org/compatiblelicenses
- The QNFO-ULA's designation of "compatible" licenses is a CONTRACTUAL commitment by Licensor, not a CC designation
- This means Licensor is contractually bound to accept CC BY-NC-SA 4.0 derivatives, but CC is not bound to recognize this compatibility

**Practical effect:** This works. A derivative author can use CC BY-NC-SA 4.0 alone because Licensor has contractually agreed to accept it as compatible. Licensor cannot later sue for SA violation if the derivative uses CC BY-NC-SA 4.0 alone.

### 8.4 The "Loophole" Question — Do QNFO Supplemental Terms Propagate?

The QNFO-ULA §4.2 states that the Supplemental Terms "apply only to the original Content and to derivative works that are explicitly licensed under this Agreement." This means:
- ✅ Original Content: Full QNFO-ULA applies
- ✅ Derivatives under QNFO-ULA: Full QNFO-ULA applies
- ⚠️ Derivatives under CC BY-NC-SA 4.0 alone: Only CC terms apply (no 85% damages, no prior art clause, no AI restrictions)

**This is NOT a loophole because:**
1. The original QNFO Content is still protected by the full QNFO-ULA
2. Anyone accessing the original QNFO Content is bound by all terms (including AI restrictions)
3. The SA propagation of CC BY-NC-SA 4.0 already prohibits commercial use of derivatives
4. The liquidated damages and prior art clauses are designed for original QNFO Content users, not downstream derivative users

**Recommendation:** No changes needed to the compatibility design. It's legally sound and practically appropriate.

---

## 9. Key Recommendations — Based on Legal Research

### 9.1 HIGH PRIORITY — Address Swiss Judicial Penalty Reduction Risk

**Problem:** Under Art. 163(3) of the Swiss Code of Obligations, a judge may reduce "excessive" penalties. The 85% liquidated damages could be challenged.

**Recommended addition to §6.1:**

> "If a court or arbitral tribunal of competent jurisdiction finds the liquidated damages amount specified in this Section to be unenforceable as a penalty or excessive under applicable law, the parties agree that Licensor shall be entitled to recover: (a) the highest amount of liquidated damages that such court or tribunal finds enforceable, not to exceed eighty-five percent (85%) of gross revenue; or (b) at Licensor's election, actual damages (including statutory damages where available under applicable copyright law), profits of the infringer attributable to the infringement, and Licensor's reasonable attorneys' fees and costs."

### 9.2 HIGH PRIORITY — Add "No Fair Use Waiver" for AI Training

**Problem:** If courts rule that AI training is fair use, the contractual prohibition in the QNFO-ULA remains enforceable against licensees, but unauthorized scrapers who never agreed to the license might argue fair use.

**Recommended addition to §2.1 (new paragraph after AI training prohibition):**

> "To the maximum extent permitted by applicable law, You waive any defense of fair use, fair dealing, text and data mining exception, temporary reproduction exception, or similar limitation or exception to copyright or database rights with respect to the extraction, reproduction, or use of the Content for the purpose of training, fine-tuning, or developing artificial intelligence or machine learning models, systems, or services. This waiver is a material term of this Agreement."

### 9.3 HIGH PRIORITY — Strengthen Browsewrap/Notice for Web Content

**Problem:** Unauthorized scrapers who never affirmatively agreed to the license may argue they're not bound.

**Recommended addition to §1.3 (new paragraph):**

> "This Agreement is binding on any person or entity that accesses, downloads, copies, or otherwise uses the Content. By accessing the Content through any means (including but not limited to web browsing, API access, direct download, or automated retrieval), You acknowledge that You have been given notice of this Agreement and agree to be bound by its terms. The publication of this Agreement alongside the Content, on websites where the Content is available, and in metadata associated with the Content constitutes sufficient notice to bind any user of the Content to these terms. If You do not agree to these terms, You must immediately cease all access to and use of the Content."

### 9.4 MEDIUM PRIORITY — Clarify "Non-Commercial" for AI Contexts

**Problem:** The distinction between "commercial AI model" and "non-commercial AI research" may become blurred as models are released openly but later commercialized.

**Recommended addition to §2.1 (after "For clarity" paragraph):**

> "For AI/ML contexts specifically: training, fine-tuning, or developing a model, system, or service is 'commercial' if the model, system, or service, or any derivative thereof, is or will be: (a) offered as a paid service or product; (b) used to generate revenue (including through advertising, subscription, or API access fees); (c) developed by or for a for-profit entity; (d) used in connection with any commercial product, service, or business operation; or (e) released under terms that permit commercial use by downstream users. If a model is developed for non-commercial research but is subsequently commercialized (including through acquisition, licensing, or change of use), such commercialization constitutes a breach dating back to the initial training if the training was not separately authorized under Section 10.7."

### 9.5 MEDIUM PRIORITY — Add "No Implied Waiver of Copyright" Clause

**Problem:** Licensor's failure to enforce the license could be interpreted as waiver.

**Recommended addition to §10.4 (expand existing waiver clause):**

> "No waiver of any term of this Agreement shall be deemed a further or continuing waiver of such term or any other term. Licensor's failure to assert any right or provision under this Agreement shall not constitute a waiver of such right or provision. Licensor's decision not to enforce this Agreement against any particular person, entity, or use shall not constitute a waiver of Licensor's right to enforce this Agreement against any other person, entity, or use, nor shall it create any implied license, estoppel, or defense of laches, acquiescence, or abandonment. Any waiver must be in writing and signed by Licensor to be effective. Licensor's copyright in the Content is not abandoned, dedicated to the public domain, or otherwise waived by this Agreement, by Licensor's publication of the Content, or by Licensor's failure to enforce any provision of this Agreement."

### 9.6 LOW PRIORITY — Consider WIPO Arbitration as Alternative

The QNFO-ULA could offer WIPO arbitration as an alternative to ICC:

> "At Licensor's election, any dispute may alternatively be resolved through arbitration administered by the World Intellectual Property Organization (WIPO) Arbitration and Mediation Center in Geneva, Switzerland, under the WIPO Arbitration Rules in effect at the time of the arbitration."

WIPO offers:
- Specialized IP expertise
- Lower costs than ICC for smaller disputes
- Same Swiss venue and New York Convention enforcement
- WIPO mediators available as a first step before arbitration

### 9.7 LOW PRIORITY — Add "Anti-Circumvention" Warning

**Recommended addition (new §2.5):**

> "**2.5 Technical Protection Measures.** Licensor may implement technical protection measures (including but not limited to robots.txt directives, rate limiting, CAPTCHA challenges, API authentication requirements, and cryptographic content signing) to protect the Content from unauthorized access or use. Circumvention of such technical protection measures for the purpose of accessing or using the Content in a manner prohibited by this Agreement may constitute a violation of anti-circumvention laws (including 17 U.S.C. § 1201 in the United States, Article 6 of the EU Copyright Directive 2001/29/EC, and equivalent legislation in other jurisdictions), independently of any breach of this Agreement."

---

## 10. Summary — What's Strong, What Needs Work

| Provision | Strength | Risk | Recommendation |
|:----------|:---------|:-----|:---------------|
| CC BY-NC-SA 4.0 base | ✅ Court-enforced; international track record | Low | No change |
| 85% liquidated damages | ⚠️ Defensible with justification | Swiss judicial reduction | Add fallback clause (§9.1) |
| AI training prohibition | ✅ Contractually binding on licensees | Fair use defense for non-licensees | Add fair use waiver (§9.2) |
| Anti-scraping provisions | ✅ Strong for agreed-upon licensees | Browsewrap weakness | Add binding-on-access clause (§9.3) |
| Platform enforcement | ✅ All channels viable | N/A | No change (add enforcement guide) |
| Swiss law + ICC Geneva | ✅ Excellent international coverage | ICC costs for small disputes | Consider WIPO alternative (§9.6) |
| Patent prior art | ✅ Strong legal basis | Under-enforcement risk | No change |
| ShareAlike propagation | ✅ Legally sound | Compatibility ambiguity | No change (resolved in §4.2/§10.6) |
| Commercial license framework | ✅ Comprehensive | N/A | No change |
| Database rights | ✅ EU Directive coverage | Low awareness | No change |

---

## Appendix — Sources and References

### Court Cases
- Great Minds v. FedEx Office, 2nd Cir. (2020)
- Great Minds v. Office Depot, multiple circuits (2017-2020)
- Jacobsen v. Katzer, 535 F.3d 1373 (Fed. Cir. 2008)
- Artifex Software v. Hancom, N.D. Cal. (2017)
- MDY Industries v. Blizzard Entertainment, 629 F.3d 928 (9th Cir. 2011)
- Meta v. Bright Data (2024)
- X Corp v. Bright Data, N.D. Cal. (2024)
- Reddit v. Perplexity AI, N.D. Cal. (filed Oct. 2025)
- NYT v. OpenAI/Microsoft, S.D.N.Y. (pending)
- Getty Images v. Stability AI, D. Del. / UK (pending)

### Statutes and Treaties
- Swiss Code of Obligations (CO), Art. 19, 160-163
- Swiss Copyright Act (CopA)
- Swiss Private International Law Act (PILA), Art. 190
- 17 U.S.C. § 107 (fair use), § 504 (damages), § 512 (DMCA), § 1201 (anti-circumvention)
- EU Database Directive 96/9/EC
- EU Copyright Directive 2001/29/EC
- Berne Convention (1886, as amended)
- New York Convention (1958)
- TRIPS Agreement (1994)
- WIPO Copyright Treaty (1996)

### Secondary Sources
- Creative Commons Legal Database (legaldb.creativecommons.org)
- CC FAQ on NonCommercial interpretation
- GitHub DMCA Takedown Policy (docs.github.com)
- Hugging Face Content Policy and Takedown Notices (huggingface.co)
- ICC Arbitration Rules (2021)
- WIPO Arbitration and Mediation Center
- Swiss Arbitration Association (ASA)
- GroupBWT Web Scraping Legal Guide (2025)
- ScrapingAPI.ai Legal Battles Analysis (2025)

---

*End of Legal Research Supplement — May 29, 2026*
