# 20250331160200_tana_tagging_reference
[Store as: #creation/tool/index/tana_tagging_reference v3.0]
[Related: #creation/tool/index/comprehensive_taxonomy, #creation/tool/index/project_reference_index]

---
title: "Tana Tagging Reference"
date: 2025-03-31
type: reference
status: complete
tags:
  - tana
  - workflow
  - tagging
  - organization
  - providential_identitarianism
  - maga_christianism
  - sermon_integration
---

# Tana Tagging Reference v3.0

This reference ensures consistent tagging format when creating content or tools for the expanded MAGA Christianism and Providential Identitarianism project. It aligns with the comprehensive taxonomy and provides standardized formats for all project elements.

## Standard Header Format

Every document should include the following header structure:

```markdown
# YYYYMMDDHHMM_descriptive_filename
[Store as: #tag/path/to/location v1.0]
[Collection: #tag/collection/name] (if applicable)
[Related: #tag/related/resource1, #tag/related/resource2] (if applicable)

---
title: "Document Title"
date: YYYY-MM-DD
type: essay|analysis|reference|template|etc.
status: draft|review|complete
tags:
  - relevant_tag1
  - relevant_tag2
---
```

## Version Numbering Convention

| Version | Meaning |
|---------|---------|
| v1.0, v2.0, v3.0 | Major versions (substantial revisions) |
| v1.1, v1.2, v2.1 | Minor versions (small updates) |
| v0.1, v0.2 | Pre-release versions (internal drafts) |

* Initial public drafts always start at v1.0
* Include version history section at end of document

## Content Tagging

### Content Stream Assignment Tags
All content should include tags identifying the relevant content stream:
```markdown
tags:
  - monday_content  # MAGA Christianism or Providential Identitarianism book chapters
  - tuesday_content # Rooted & Reaching personal essays
  - wednesday_content # Common Life Politics essays or Lexicon entries
  - thursday_content # Untold America historical essays
  - friday_content # Divine Republic satirical pieces
  - sunday_content # Mark sermon series
  - integration_content # Integration materials
```

### Monday: MAGA Christianism Book Chapters
```markdown
[Store as: #creation/content/essay/maga_christianism/[chapter_name] v[version]]
[Collection: #creation/content_collection/maga_christianism_book]
[Related: #knowledge/source_integration/[source_name], #knowledge/thematic_integration/[theme_name], #creation/content/sermon/[related_sermon]]
```

### Monday: Providential Identitarianism Chapters
```markdown
[Store as: #creation/content/essay/providential_identitarianism/[chapter_name] v[version]]
[Collection: #creation/content_collection/providential_identitarianism_book]
[Related: #knowledge/source_integration/[source_name], #knowledge/thematic_integration/[theme_name], #creation/content/sermon/[related_sermon]]
```

### Tuesday: Rooted & Reaching Personal Essays
```markdown
[Store as: #creation/content/personal_essay/phase[1|2|3]_[category]/[essay_name] v[version]]
[Collection: #creation/content_collection/rooted_reaching]
[Related: #knowledge/autobiographical/[anecdote_name], #creation/content/sermon/[related_sermon]]
```

### Wednesday: Common Life Politics Essays
```markdown
[Store as: #creation/content/essay/common_life_politics/[essay_name] v[version]]
[Collection: #creation/content_collection/common_life_politics]
[Related: #knowledge/source_integration/[source_name], #knowledge/thematic_integration/[theme_name], #creation/content/sermon/[related_sermon]]
```

### Wednesday: Lexicon Entries
```markdown
[Store as: #creation/content/lexicon/[category]/[concept_name] v[version]]
[Collection: #creation/content_collection/lexicon]
[Related: #knowledge/source_integration/[source_name], #knowledge/thematic_integration/[theme_name], #creation/content/sermon/[related_sermon]]
```

### Thursday: Untold America Historical Confessionals
```markdown
[Store as: #creation/content/historical/phase[1|2|3|4]_[category]/[essay_name] v[version]]
[Collection: #creation/content_collection/untold_america]
[Related: #knowledge/source_integration/[source_name], #knowledge/autobiographical/[anecdote_name], #creation/content/sermon/[related_sermon]]
```

### Friday: Divine Republic Satirical Pieces
```markdown
[Store as: #creation/content/satire/phase[1|2|3|4]_[category]/[piece_name] v[version]]
[Collection: #creation/content_collection/divine_republic]
[Related: #knowledge/thematic_integration/[theme_name], #creation/content/sermon/[related_sermon]]
```

### Sunday: Mark Sermons
```markdown
[Store as: #creation/content/sermon/[passage_reference]/[sermon_name] v[version]]
[Collection: #creation/content_collection/mark_sermons]
[Related: #knowledge/thematic_integration/[theme_name], #creation/content/integration/sermon_integrations/[integration_name]]
```

### Integration: Weekly Theme Integration
```markdown
[Store as: #creation/content/integration/weekly_themes/week[XX]_[theme_name] v[version]]
[Collection: #creation/content_collection/weekly_integrations]
[Related: #creation/content/sermon/[related_sermon], #creation/content/essay/[related_essay]]
```

### Integration: Sermon Integration Guides
```markdown
[Store as: #creation/content/integration/sermon_integrations/sermon[XX]_integration v[version]]
[Collection: #creation/content_collection/sermon_integrations]
[Related: #creation/content/sermon/[related_sermon], #creation/content/integration/weekly_themes/[related_theme]]
```