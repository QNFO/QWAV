# QNFO Unified Licensing Policy — Program Directive

**Document Type:** Program-Level Policy (Binding)  
**Effective Date:** 2026-05-29  
**Policy Number:** QNFO-POL-001  
**Status:** ACTIVE — Supersedes all prior licensing policies across QNFO and QWAV

---

## 1. Policy Statement

**All QNFO and QWAV ecosystem content is governed by a single, unified license:** the [QNFO Unified License Agreement v2.0](legal/QNFO-ULA-v2.0.md) ("QNFO-ULA v2.0").

QNFO is the parent organization. QWAV is the primary platform. This license applies to both — and to all content under either namespace — uniformly and without exception. There is no longer any variation by project, namespace, content type, or historical origin.

**One license. One policy. One canonical source of truth. For all QNFO/QWAV content, now and forever, unless and until changed/updated.**

---

## 2. Scope — Universal Application

This policy applies to **ALL** content across the following namespaces and directories:

| Namespace | Local Path | Cloudflare / Web |
|:----------|:-----------|:-----------------|
| QNFO (parent) | All QNFO-origin content in `G:\My Drive\projects\`, `G:\My Drive\Archive\`, `G:\My Drive\Downloads\` (QNFO-created) | `qnfo.org` |
| QWAV (platform) | `G:\My Drive\QWAV\` | `qwav.tech` |
| q08 (historical) | `G:\My Drive\Archive\q08.org\` | Archived |
| Obsidian | `G:\My Drive\Obsidian\` | N/A |
| Prompts | `G:\My Drive\prompts\` | N/A |
| All Archives | `G:\My Drive\Archive\` | N/A |
| All Downloads | `G:\My Drive\Downloads\` (QNFO-created files) | N/A |
| All Future Works | Any path, any medium | Any domain

**Content types covered:** Code, documentation, data, theories, publications, websites, prompts, configurations, images, diagrams, datasets, and all derivative works.

**Excluded:** Third-party dependencies (node_modules, vendor libraries) retain their upstream licenses.

---

## 3. The License

### 3.1 Canonical Text

The single canonical text is stored at:

- **Local:** `G:\My Drive\QWAV\legal\QNFO-ULA-v2.0.md`
- **Web:** `https://qnfo.org/legal/license` (primary) and `https://qwav.tech/legal/license` (mirror)
- **R2:** `qnfo/releases/licenses/QNFO-ULA-v2.0.md`

### 3.2 What QNFO-ULA v2.0 Is

| Element | Source |
|:--------|:-------|
| **Base license** | CC BY-NC-SA 4.0 (Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International) |
| **ShareAlike** | ✅ Derivatives MUST use same or compatible license |
| **Patent prior art citation** | QNFO v1.1 §4.2 — mandatory disclosure in patent applications |
| **Liquidated damages** | 85% of gross revenue from unauthorized commercial use |
| **AI/ML training restrictions** | Explicit prohibition on training commercial AI models without public benefit agreement |
| **RAIL-inspired behavioral restrictions** | Prohibitions on surveillance, disinformation, autonomous weapons, exploitative behavioral engineering |
| **Separate commercial license pathway** | Available at Licensor's discretion for public-good-aligned commercial uses |
| **Database rights** | Explicit coverage of EU sui generis database rights (Directive 96/9/EC) |
| **SPDX identifier** | `LicenseRef-QNFO-ULA-2.0` for machine-readable compliance |
| **Governing law** | Switzerland |
| **Dispute resolution** | ICC arbitration, Geneva, English language |
| **International enforcement** | New York Convention (170+ signatory nations) + Berne, TRIPS, WCT, Paris Convention references |
| **Ethical preamble** | Human dignity, ethical innovation, anti-exploitation principle |
| **Scope** | ALL QNFO/QWAV content, all types, all media, now and forever |

### 3.3 What QWAV-ULA v2.0 Is NOT

- **NOT ShareAlike** — derivative works are NOT required to use the same license (the SA clause from CC BY-NC-SA 4.0 and ASLA has been **removed**). Attribution and NonCommercial still apply.
- **NOT a public domain dedication** — all rights are reserved except those explicitly granted.
- **NOT MIT / Apache / GPL** — this is a custom non-commercial license with additional protections.

---

## 4. Migration — What Must Change

### 4.1 Immediate Actions (Program Agent)

- [x] Create `QNFO-ULA-v2.0.md` in `QWAV/legal/` (canonical text)
- [x] Create this policy document (`LICENSING-POLICY.md`)
- [x] Create research memorandum (`LICENSING-RESEARCH-MEMO.md`)
- [ ] Replace `G:\My Drive\LICENSE.md` with short pointer to QNFO-ULA v2.0
- [ ] Replace `G:\My Drive\QWAV\LICENSE` with short pointer to QNFO-ULA v2.0
- [ ] Replace `G:\My Drive\prompts\LICENSE` with short pointer to QNFO-ULA v2.0
- [ ] Deploy canonical text to `https://qnfo.org/legal/license` (Cloudflare Pages)
- [ ] Deploy mirror to `https://qwav.tech/legal/license` (Cloudflare Pages)
- [ ] Upload to R2: `qnfo/releases/licenses/QNFO-ULA-v2.0.md`
- [ ] Update Discovery Index to reflect new license
- [ ] Remove superseded `QWAV-UNIFIED-LICENSE-v2.0.md` (draft)

### 4.2 Per-Project Actions (Projects Agent — Delegated)

For each active project, the Projects Agent shall:

1. Replace any existing `LICENSE` file with a short pointer file:

```markdown
# License

This project is licensed under the **QWAV Unified License Agreement v2.0**.

Full text: https://qwav.tech/legal/license  
Local copy: `G:\My Drive\QWAV\legal\QWAV-UNIFIED-LICENSE-v2.0.md`

© 2026 Rowan Brad Quni-Gudzinas. All rights reserved except as granted.
```

2. Update `README.md` license section to reference QWAV-ULA v2.0
3. Update any `package.json` `"license"` field to `"QWAV-ULA-2.0"`
4. Remove any prior `LICENSE.md`, `LICENSE.txt`, or legacy license files
5. For publications: update the license block in frontmatter/YAML

### 4.3 Archived Projects

Archived projects shall NOT be modified retroactively. An archive-wide notice shall be placed at `G:\My Drive\Archive\LICENSE-MIGRATION-NOTICE.md` stating that all archived content is now governed by QWAV-ULA v2.0.

---

## 5. New Project Initiation — Updated Protocol

The QWAV Project Initiation Protocol (§0.9.1) is amended:

**New Step L0 (before directory creation):** The license pointer file shall be created as part of scaffolding. Every new project is automatically under QWAV-ULA v2.0. No project-level license decisions are permitted.

---

## 6. Enforcement

### 6.1 License Header Requirement

All new code files SHALL include a short license header:

```
# SPDX-License-Identifier: QWAV-ULA-2.0
# © YYYY Rowan Brad Quni-Gudzinas
# See https://qwav.tech/legal/license for full terms.
```

### 6.2 Publication Requirement

All publications (papers, reports, websites) SHALL include a license block in their frontmatter or footer referencing QWAV-ULA v2.0.

### 6.3 Compliance Check

The Kaizen engine shall periodically audit all active projects for license consistency. Any project still referencing a superseded license shall be flagged with `[KAIZEN-LICENSE-MIGRATION]`.

---

## 7. Rationale — Why Unification

| Problem | Solution |
|:--------|:---------|
| 5+ different licenses across ecosystem | One license for everything |
| Uncertainty about which license applies to which project | Clear, single canonical text |
| CC BY-NC-SA's ShareAlike was unnecessarily restrictive for academic use | Removed SA — now CC BY-NC only |
| QNFO v1.1 lacked the ethical preamble | Added ASLA preamble |
| ASLA lacked patent prior art enforcement | Added QNFO prior art clause |
| No clear international enforcement mechanism | Swiss law + ICC arbitration + New York Convention |
| License text scattered across filesystem | Single canonical source at `QWAV/legal/` |

---

## 8. Version History

| Version | Date | Author | Changes |
|:--------|:-----|:-------|:--------|
| 1.0 | 2026-05-29 | Program Agent (v3.4) | Initial unified policy — QWAV-ULA v2.0 created, supersedes all prior licenses |

---

*End of Policy Directive QWAV-POL-001*
