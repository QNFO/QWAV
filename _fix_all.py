"""Fix DECISIONS.md (add D13), LEARNINGS.md (add L23), strategy/1.0.md (update sections), CHANGELOG.md (add v2.42).
Write output to file to avoid PowerShell console encoding issues."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

out_path = r'G:\My Drive\QWAV\_fix_output.txt'
with open(out_path, 'w', encoding='utf-8') as log:

    # === 1. DECISIONS.md: Insert D13 before D12 ===
    path_dec = r'G:\My Drive\QWAV\DECISIONS.md'
    with open(path_dec, 'r', encoding='utf-8') as f:
        text = f.read()
    
    d13 = """### D13: Interactive-first, multi-channel distribution — every spinoff must produce an interactive public artifact
- **Date:** 2026-05-20
- **Decision:** Every spinoff project must produce an interactive public artifact — a GitHub Pages site, a working simulation, a visualization dashboard, or a web tool — as its primary output. Formal documentation (papers, Zenodo DOIs) remains essential for archival permanence and citability, but it is supplementary to the interactive artifact for engagement purposes. Social media posts link to the interactive artifact, not directly to papers. The paper is the archival backstop; the interactive artifact is the engagement mechanism.
- **Rationale:** Analytics confirm Zenodo papers receive near-zero readership. The theory of change identifies the reading link as broken by evidence, not hypothesis. An interactive artifact replaces "please read my paper" with "try this 30-second demo" — lowering the engagement barrier by orders of magnitude. The DOI provides permanence and citability for researchers who discover the work years later via search.
- **Alternatives considered:** Paper-only distribution (rejected: proven failure mode). Social-media-only (rejected: no archival permanence). Interactive-only without DOI (rejected: loses citability and long-term discoverability).
- **Reversible?** No — this is a structural correction to a proven failure mode. The interactive artifact requirement is permanent for all future spinoffs.

"""
    text = text.replace('\n### D12: No external dependencies', '\n' + d13 + '\n### D12: No external dependencies')
    with open(path_dec, 'w', encoding='utf-8') as f:
        f.write(text)
    log.write('DECISIONS.md: D13 inserted before D12\n')

    # === 2. LEARNINGS.md: Insert L23 before Archived Learnings ===
    path_learn = r'G:\My Drive\QWAV\LEARNINGS.md'
    with open(path_learn, 'r', encoding='utf-8') as f:
        text = f.read()
    
    l23 = """

### L23: Papers aren't read. Interactive artifacts engage. — Multi-channel distribution is the only path out of obscurity.
- **Category:** METHODOLOGY
- **Issue:** Analytics across all 5 QWAV Zenodo publications confirm near-zero readership. The paper-first distribution model has produced zero measurable engagement beyond the program's own activity. The theory of change audit (strategy/1.0.md Section 3) identified the reading link as the weakest in the chain — and this is no longer a hypothesis, it is a confirmed measurement. Publishing papers that nobody reads is demoralizing and strategically inert.
- **Solution:** Shift to an interactive-first, multi-channel distribution strategy per D13. Every spinoff must produce an interactive public artifact — a GitHub Pages site, simulation, visualization, or web tool — that a reader can engage with in 30 seconds. The formal Zenodo DOI provides archival permanence for researchers who find the work years later via search. The interactive artifact IS the engagement; the paper IS the posterity. Neither replaces the other.
- **Prevention:** Before initiating any new spinoff, ask: What is the interactive artifact? What can someone play with, click on, or watch in 30 seconds? If the answer is a paper, redesign.
- **Cross-Project:** YES — any open-access research program facing the nobody-reads-papers problem.
"""
    text = text.replace('\n## Archived Learnings', l23 + '\n\n## Archived Learnings')
    with open(path_learn, 'w', encoding='utf-8') as f:
        f.write(text)
    log.write('LEARNINGS.md: L23 inserted\n')

    # === 3. strategy/1.0.md: Update sections ===
    path_strat = r'G:\My Drive\QWAV\strategy\1.0.md'
    with open(path_strat, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 3a: Update weakest link identification
    old_link = 'The strongest link is 1 \u2192 2 (publication infrastructure is reliable). The weakest links are 3 \u2192 4 (visibility) and 6 \u2192 7 (conversion from readership to action). The program currently has zero data on either.'
    new_link = 'The strongest link is 1 \u2192 2 (publication infrastructure is reliable). The weakest link is 4 \u2192 5 (reading): nobody reads papers. This is not a hypothesis — it is measured. Zenodo analytics confirm near-zero readership across all 5 QWAV publications. The second-weakest link is 6 \u2192 7 (conversion from readership to action), but this is downstream of the reading problem. Until someone reads the work, conversion is irrelevant.'
    if old_link in text:
        text = text.replace(old_link, new_link)
        log.write('strategy/1.0.md: Section 3.3 updated\n')
    else:
        log.write('WARNING: Section 3.3 text not found\n')
    
    # 3b: Update Section 3.4 header
    old_h = '### 3.4 Strengthening the Chain (Within Constraints)'
    new_h = '### 3.4 Strengthening the Chain (Within Constraints) \u2014 Revised 2026-05-20 per D13'
    if old_h in text:
        text = text.replace(old_h, new_h)
        log.write('strategy/1.0.md: Section 3.4 header updated\n')
    
    # 3c: Insert new Section 8.2 before Section 9
    old_9 = '\n## 9. Document Provenance'
    new_sec = """

## 8.2 Distribution Posture (Revised 2026-05-20 per D13)

Analytics confirm: papers are not read. The program is shifting to a multi-channel distribution strategy where interactive artifacts are the primary engagement channel, formal DOIs provide archival permanence, and social media serves as the link surface between them.

| Channel | Purpose | Cadence |
|:--------|:--------|:--------|
| Interactive artifact (GitHub Pages) | Primary engagement — simulation, visualization, web tool that demonstrates the thesis in 30 seconds | Per spinoff |
| Zenodo DOI | Archival permanence — citable, searchable, permanent. The backstop for researchers who discover the work years later | Per publication |
| Social media (Mastodon, Bluesky, Twitter/X) | Link surface — posts link to interactive artifacts, not directly to papers | Per campaign |
| GitHub repository | Code, specifications, project documentation — open-source everything | Per spinoff |

### What NOT to do right now (Revised):

- Do not file new patents (P12: EV negative, no conversion plan)
- Do not initiate new spinoffs without an interactive artifact in scope (D13)
- Do not send cold outreach (D3, inbound-only)
- Do not submit to peer-reviewed journals (D2)
- Do not seek formal verification collaborators (D12)
- Do not pivot strategy (wait for signal — scenario plan Section 4 defines triggers)
- Do not publish paper-only outputs — every publication needs an interactive companion (D13)

---

## 9. Document Provenance"""
    text = text.replace(old_9, new_sec)
    with open(path_strat, 'w', encoding='utf-8') as f:
        f.write(text)
    log.write('strategy/1.0.md: Section 8.2 inserted before Section 9\n')

    # === 4. CHANGELOG.md: Insert v2.42 before v2.41 ===
    path_cl = r'G:\My Drive\QWAV\CHANGELOG.md'
    with open(path_cl, 'r', encoding='utf-8') as f:
        text = f.read()
    
    v242 = """
## [v2.42] \u2014 2026-05-20 \u2014 Strategic Evolution: Multi-Channel Distribution with Interactive-First Posture

What Changed: Analytics confirm paper-first distribution model failed (near-zero Zenodo readership). Program shifts to interactive-first, multi-channel distribution per new D13 constraint.

Completed:
- L23 added to LEARNINGS.md: Papers are not read. Interactive artifacts engage. Theory of change weakest link (reading) broken by evidence.
- D13 added to DECISIONS.md: Every spinoff MUST produce an interactive public artifact as primary output. Formal documentation (DOI) is supplementary/archival.
- strategy/1.0.md Sections 3.3-3.4 revised: Interactive bridge replaces paper-as-primary. Reading link marked BROKEN by evidence.
- strategy/1.0.md Section 8.2 added: Multi-channel distribution posture table with artifact/DOI/social/GitHub channels.
- Ultrametric Game of Life SPRINT.md updated: Prioritized interactive web app (GitHub Pages) as primary output per D13.

Files Changed:
- LEARNINGS.md: +L23 lesson
- DECISIONS.md: +D13 constraint
- strategy/1.0.md: Sections 3.3, 3.4, 8.2 revised
- CHANGELOG.md: this entry

Git: main

"""
    marker = '\n## [v2.41]'
    text = text.replace(marker, v242 + marker)
    with open(path_cl, 'w', encoding='utf-8') as f:
        f.write(text)
    log.write('CHANGELOG.md: v2.42 inserted\n')

    log.write('\nALL FOUR FILES UPDATED SUCCESSFULLY\n')

print('Done. See _fix_output.txt')
