# class-b-template-v1-0
[Store as: #creation/tool/template/class_b_template v1.0]
[Related: #creation/tool/index/content_classification_framework]

---
title: "Class B Content Template: Dropbox-Bound References"
date: 2025-04-04
type: template
status: complete
tags:
  - class_b
  - dropbox
  - github
  - template
  - reference
---

# Class B Content Template: Dropbox-Bound References

This template provides the standard structure and formatting guidelines for all Class B content (Dropbox-bound references) in the Dominative Christianism and Providential Identitarianism project. Class B content comprises research materials, analyses, and drafts that are stored in the project's Dropbox structure and managed with GitHub version control.

## Filename Convention
```
descriptive-name-v1-0.md
```
- Lowercase with hyphens
- Version number with hyphens
- Example: `source-analysis-hauerwas-v1-0.md`

## Directory Structure
```
/research/[content_type]/[category]/[subcategory]/
```
Examples:
- `/research/sources/analyses/primary/hauerwas-with-grain.md`
- `/research/themes/mutations/primitive-biblicism.md`
- `/research/drafts/chapters/theological-framework.md`

## Standard Frontmatter Structure
```markdown
---
title: "Document Title"
author: "Your Name"
date: YYYY-MM-DD
version: 1.0
type: source_analysis|thematic_synthesis|draft_chapter|research_note
status: draft|in_progress|complete|archived
sources:
  - "Source 1"
  - "Source 2"
related_content:
  - "/path/to/related/content1.md"
  - "/path/to/related/content2.md"
tags:
  - relevant_tag1
  - relevant_tag2
  - relevant_tag3
---
```

## Body Structure
The body of Class B content should follow this general structure:

### Required Sections

#### 1. Executive Summary
A brief summary (150-250 words) of the document's key points and significance.

```markdown
## Executive Summary

This document [provides/analyzes/synthesizes] [brief description of content]. The key insights include [1-3 bullet points of main takeaways]. This material is particularly significant for [specific aspect of the project] and connects to [related themes or concepts].
```

#### 2. Core Content
The main content section, structured according to the specific content type.

For **Source Analysis**:
```markdown
## Source Information
- **Title**: [Full title]
- **Author**: [Author name]
- **Publication**: [Publication details]
- **Date**: [Publication date]
- **Pages/Locations**: [Page range or location numbers analyzed]

## Key Arguments
1. [First key argument]
2. [Second key argument]
3. [Third key argument]

## Relevance to Theological Mutations
### Primitive Biblicism
[Analysis of how the source relates to this mutation]

### Practical Atheism
[Analysis of how the source relates to this mutation]

[Additional mutations as relevant]

## Quotes for Potential Use
> "Direct quote with page number" (p. XX)

> "Direct quote with page number" (p. XX)

## Methodological Notes
[Notes on the author's methodology, biases, or limitations]
```

For **Thematic Synthesis**:
```markdown
## Theme Overview
[Description of the theme and its significance]

## Sources Integrated
- [Source 1 with brief description]
- [Source 2 with brief description]
- [Source 3 with brief description]

## Key Insights
1. [First key insight with supporting evidence]
2. [Second key insight with supporting evidence]
3. [Third key insight with supporting evidence]

## Connections to Project Framework
[How this theme connects to the project's theoretical framework]

## Research Gaps
[Identification of areas needing further research]

## Application to Content Streams
[How this theme can be applied across content streams]
```

For **Draft Chapters**:
```markdown
## Chapter Overview
[Brief description of the chapter's purpose and place in the book]

## Outline
1. Introduction
   a. [Key point]
   b. [Key point]
2. Section One: [Title]
   a. [Key point]
   b. [Key point]
3. [Continue with remaining sections]
4. Conclusion
   a. [Key point]
   b. [Key point]

## Key Arguments
[The central arguments of the chapter]

## Sources to Incorporate
[List of sources with specific aspects to include]

## Visual Elements
[Notes on potential diagrams, charts, or images]

## Editorial Notes
[Notes on writing approach, tone, or specific challenges]
```

#### 3. Cross-References
Explicit connections to other project materials.

```markdown
## Cross-References
- **Tana Objects**: [#knowledge/topic/relevant_topic, #knowledge/concept/relevant_concept]
- **Research Materials**: [/research/themes/related-theme.md, /research/sources/relevant-source.md]
- **Content Drafts**: [/content/monday/relevant-chapter.md]
```

#### 4. Next Steps
Clear action items for further development.

```markdown
## Next Steps
- [ ] Action item 1
- [ ] Action item 2
- [ ] Action item 3
```

#### 5. Version History
A record of version changes.

```markdown
## Version History
v1.0 - YYYY-MM-DD - Initial draft
v1.1 - YYYY-MM-DD - Minor updates [description]
v2.0 - YYYY-MM-DD - Major revision [description]
```

## GitHub Integration

### Commit Convention
Format commit messages as:
```
[content-type]: Brief description of changes

Longer description of what changed and why.

Ref: #issue-number (if applicable)
```

Example:
```
[source-analysis]: Complete Hauerwas analysis

Added analysis of connections to practical atheism and binary apocalypticism.
Updated quotes section with key passages for potential use.

Ref: #42
```

### Branch Strategy
- `main`: Stable, reviewed content
- `draft/[content-name]`: Work in progress
- `review/[content-name]`: Ready for review

## Dropbox Organization
Maintain consistent organization in Dropbox:
- Use the established directory structure
- Keep filenames consistent with GitHub
- Include version numbers in filenames
- Use the appropriate file extensions

## Creation Process

### 1. Initial Draft with Claude
- Use artifact-based approach in Claude
- Specify Class B format in your request
- Include all required sections
- Request proper frontmatter and structure

### 2. VSCode Refinement
- Open in VSCode for editing
- Apply consistent markdown formatting
- Check frontmatter formatting
- Ensure proper heading structure
- Verify cross-references

### 3. GitHub Integration
- Save to appropriate directory
- Stage and commit changes
- Push to appropriate branch
- Create pull request if needed

### 4. Reference in Tana
- Add reference to relevant Tana objects
- Include path to Dropbox file
- Add version information

## Conversion Guidelines

### To Class C (Platform Optimization)
When converting Class B content to Class C:
1. Extract core content from Dropbox file
2. Apply platform-specific formatting
3. Add visual elements and styling
4. Optimize for platform requirements
5. Include cross-references to source material

### From Class A (Tana Integration)
When converting Class A content to Class B:
1. Export from Tana with proper formatting
2. Expand with additional context and details
3. Structure according to Class B template
4. Add appropriate frontmatter
5. Place in correct Dropbox directory

## Version History

v1.0 - 2025-04-04 - Initial template for Class B content
