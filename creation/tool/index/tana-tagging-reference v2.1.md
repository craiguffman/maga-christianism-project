/Users/craiguffman/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub/maga-christianism-project/tools/indexes/20250331143300_tana_tagging_reference.md

# 20250331143300_tana_tagging_reference
[Store as: #creation/tool/index/tana_tagging_reference v2.1]
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
---

# Tana Tagging Reference

This reference ensures consistent tagging format when creating content or tools for the MAGA Christianism project. It aligns with the comprehensive taxonomy and provides standardized formats for all project elements.

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

### Monday: MAGA Christianism Book Chapters
```markdown
[Store as: #creation/content/essay/maga_christianism/[chapter_name] v[version]]
[Collection: #creation/content_collection/maga_christianism_book]
[Related: #knowledge/source_integration/[source_name], #knowledge/thematic_integration/[theme_name]]
```

### Tuesday: Rooted & Reaching Personal Essays
```markdown
[Store as: #creation/content/personal_essay/phase[1|2|3]_[category]/[essay_name] v[version]]
[Collection: #creation/content_collection/rooted_reaching]
[Related: #knowledge/autobiographical/[anecdote_name]]
```

### Wednesday: Common Life Politics Essays
```markdown
[Store as: #creation/content/essay/common_life_politics/[essay_name] v[version]]
[Collection: #creation/content_collection/common_life_politics]
[Related: #knowledge/source_integration/[source_name], #knowledge/thematic_integration/[theme_name]]
```

### Wednesday: Lexicon Entries
```markdown
[Store as: #creation/content/lexicon/[category]/[concept_name] v[version]]
[Collection: #creation/content_collection/lexicon]
[Related: #knowledge/source_integration/[source_name], #knowledge/thematic_integration/[theme_name]]
```

### Thursday: Untold America Historical Confessionals
```markdown
[Store as: #creation/content/historical/phase[1|2|3]_[category]/[essay_name] v[version]]
[Collection: #creation/content_collection/untold_america]
[Related: #knowledge/source_integration/[source_name], #knowledge/autobiographical/[anecdote_name]]
```

### Friday: Divine Republic Satirical Pieces
```markdown
[Store as: #creation/content/satire/phase[1|2|3]_[category]/[piece_name] v[version]]
[Collection: #creation/content_collection/divine_republic]
[Related: #knowledge/thematic_integration/[theme_name]]
```

### Video Content
```markdown
[Store as: #creation/content/video/[category]/[video_name] v[version]]
[Collection: #creation/content_collection/theological_videos]
[Related: #creation/content/essay/[related_essay], #creation/content/lexicon/[related_concept]]
```

### Ebook Compilations
```markdown
[Store as: #creation/content/ebook/[book_name]/[part_name] v[version]]
[Collection: #creation/content_collection/ebooks]
[Related: #creation/content/essay/[related_essay], #creation/content/personal_essay/[related_essay]]
```

## Tool Tagging

### Templates
```markdown
[Store as: #creation/tool/template/[template_name] v[version]]
[Related: #creation/content/[related_content_type]]
```

### Indexes
```markdown
[Store as: #creation/tool/index/[index_name] v[version]]
[Related: #creation/tool/[related_tool], #knowledge/reference/[related_reference]]
```

### Scripts
```markdown
[Store as: #creation/tool/script/[script_name] v[version]]
[Related: #creation/tool/[related_tool]]
```

### Prompts
```markdown
[Store as: #creation/tool/prompt/[prompt_name] v[version]]
[Related: #creation/tool/[related_tool], #knowledge/reference/[related_reference]]
```

### Workflows
```markdown
[Store as: #creation/tool/workflow/[workflow_name] v[version]]
[Related: #creation/tool/[related_tool], #creation/content/[related_content_type]]
```

## Knowledge Object Tagging

Knowledge objects represent conceptual, structural, and analytical units fundamental to research organization. These differ from notes and creation elements.

### Knowledge Topic Objects
```markdown
[Store as: #knowledge/topic/[topic_name] v[version]]
[Related: #knowledge/concept/[related_concept], #knowledge/framework/[related_framework]]
```

### Knowledge Concept Objects
```markdown
[Store as: #knowledge/concept/[concept_name] v[version]]
[Related: #knowledge/topic/[related_topic], #knowledge/mental_model/[related_model]]
```

### Knowledge Framework Objects
```markdown
[Store as: #knowledge/framework/[framework_name] v[version]]
[Related: #knowledge/topic/[related_topic], #knowledge/concept/[related_concept]]
```

### Knowledge Mental Model Objects
```markdown
[Store as: #knowledge/mental_model/[model_name] v[version]]
[Related: #knowledge/framework/[related_framework], #knowledge/concept/[related_concept]]
```

### Knowledge Syntopical Document Objects
```markdown
[Store as: #knowledge/syntopical_document/[document_name] v[version]]
[Related: #knowledge/topic/[related_topic], #knowledge/concept/[related_concept]]
```

## Note Object Tagging

Note objects represent research processing at varying levels of synthesis and abstraction.

### Atomic Notes
```markdown
[Store as: #note/atomic_note/[note_name] v[version]]
[Related: #knowledge/source_integration/[related_source]]
```

### Synthesis Notes
```markdown
[Store as: #note/synthesis_note/[note_name] v[version]]
[Related: #note/atomic_note/[related_note], #knowledge/topic/[related_topic]]
```

## Source Integration Tagging

### Source Integration
```markdown
[Store as: #knowledge/source_integration/[source_name] v[version]]
[Related: #knowledge/thematic_integration/[related_theme]]
```

### Thematic Integration
```markdown
[Store as: #knowledge/thematic_integration/[theme_name] v[version]]
[Related: #knowledge/source_integration/[related_source]]
```

### Reference Documents
```markdown
[Store as: #knowledge/reference/[reference_name] v[version]]
[Related: #creation/tool/[related_tool]]
```

### Autobiographical Content
```markdown
[Store as: #knowledge/autobiographical/[anecdote_name] v[version]]
[Related: #creation/content/personal_essay/[related_essay]]
```

## Mutation Framework Tagging

When content relates to specific theological mutations, include the relevant mutation tags:

```markdown
tags:
  - primitive_biblicism
  - practical_atheism
  - binary_apocalypticism
  - disordered_nationalism
  - prosperity_materialism
  - authoritarian_spirituality
  - tribal_epistemology
```

## Alternative Theological Framework Tagging

When content relates to constructive theological alternatives, include the relevant tags:

```markdown
tags:
  - participatory_freedom
  - being_with
  - trinitarian_theology
  - prophetic_patriotism
  - covenant_community
  - biblical_justice
  - freedom_non_domination
```

## Implementation in Claude Interactions

1. When requesting Claude to generate content, specify the exact tagging format required
2. Include relevant paths from the comprehensive taxonomy
3. Request that Claude include proper version numbering and header format
4. Specify any collections or related resources that should be referenced

## Version History

v2.1 - 2025-03-31 - Added comprehensive knowledge object tagging schema
v2.0 - 2025-03-31 - Updated with complete integration to comprehensive taxonomy and expanded tagging structure
v1.0 - Initial reference guide for Tana tagging