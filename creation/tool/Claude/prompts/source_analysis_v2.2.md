# Source Analysis Prompt Template
**File Path:** `/Users/craiguffman/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub/maga-christianism-project/tools/prompts/source_analysis_v2.2.md`

---
title: "Source Analysis Prompt Template"
date: 2025-03-30
version: 2.2
type: template
status: complete
related_chapters:
  - "All chapters requiring source analysis"
tags:
  - research
  - source_analysis
  - claude_prompt
---

# Source Analysis Prompt

## Purpose
This prompt template is designed to generate structured, modular source analyses that integrate seamlessly with our research synthesis system and support our five publication streams.

## Publication Context
Our analyses support five distinct publication streams:
- **Monday**: MAGA Christianism Book Chapters (theological analysis)
- **Tuesday**: "Rooted & Reaching" Personal Essays (spiritual formation)
- **Wednesday**: 12-Part Faith Series / Lexicon Entries (theological foundations)
- **Thursday**: "Untold America" Historical Confessionals (historical analysis)
- **Friday**: "Divine Republic" Satirical Pieces (cultural commentary)

## Storage Location
All source analyses should be stored in the following directory structure:
- `/Users/craiguffman/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub/maga-christianism-project/research/sources/analyses/[source-type]/[source-name].md`

Where [source-type] is one of:
- books
- articles
- speeches
- reports
- legal
- interviews
- media

## Prompt Template

```
I need you to analyze the following source for my MAGA Christianism and Untold America projects:

Source(s): [SOURCE_TITLE]

Please create a comprehensive markdown artifact with the file path at the very top of the document:

/Users/craiguffman/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub/maga-christianism-project/research/sources/analyses/[source-type]/[source-name].md

Then continue with these components:

## 1. Source Metadata
- **Title**: Full title
- **Author(s)**: All authors
- **Publication**: Journal/publisher
- **Year**: Publication year
- **Type**: Book, article, speech, etc.
- **Primary Discipline**: Theology, history, politics, etc.

## 2. Core Analysis
- **Central Thesis**: 1-2 sentence summary of main argument
- **Key Arguments**: 3-5 main points with brief explanation
- **Methodology**: Approach used by the author
- **Contextual Placement**: How this fits in scholarly conversation

## 3. Theological Mutation Connections
For each of our identified mutations, analyze relevant insights:

### Primitive Biblicism
- Relevant insights:
- Supporting quotes: (with page numbers)
- Potential applications:

### Practical Atheism
- Relevant insights:
- Supporting quotes: (with page numbers)
- Potential applications:

### Binary Apocalypticism
- Relevant insights:
- Supporting quotes: (with page numbers)
- Potential applications:

### Disordered Nationalism
- Relevant insights:
- Supporting quotes: (with page numbers)
- Potential applications:

### Prosperity Materialism
- Relevant insights:
- Supporting quotes: (with page numbers)
- Potential applications:

### Authoritarian Spirituality
- Relevant insights:
- Supporting quotes: (with page numbers)
- Potential applications:

### Tribal Epistemology
- Relevant insights:
- Supporting quotes: (with page numbers)
- Potential applications:

## 4. Publication Stream Applications
- **MAGA Christianism (Monday)**: Applications for theological analysis chapters
- **Rooted & Reaching (Tuesday)**: Connections to personal spiritual formation
- **Theological Series (Wednesday)**: Relevance for theological foundations
- **Untold America (Thursday)**: Value for historical confessionals
- **Divine Republic (Friday)**: Potential applications for satirical commentary

## 5. Interdisciplinary Dimensions
- **Economic Framework**: How does this source address economic assumptions or implications?
- **Political Theology**: Connections to political formation and practices
- **Historical Context**: Relevant historical background or connections

## 6. Constructive Theological Resources
- **Participatory Freedom**: Elements that support our theological framework
- **Being With**: Connections to incarnational "being with" theology
- **Alternative Models**: Constructive alternatives to MAGA Christianism mutations

## 7. Integration Points
- **Chapter Connections**: Specific chapters for MAGA Christianism and Untold America
- **Source Relationships**: How this connects to other analyzed sources
- **Thematic Contributions**: Key themes this source enhances

## 8. Research Gaps
- **Limitations**: What this source doesn't address
- **Follow-up Questions**: Areas needing further investigation
- **Potential Counterarguments**: Positions that might challenge this source
```

## Implementation Notes
- Always specify page numbers for quotes to enable verification
- Maintain our analytical voice while accurately representing the source
- Focus on theological implications rather than mere summary
- Structure output for easy integration with existing analyses
- Identify connections to both manuscripts and all five publication streams
- Include the full file path at the top of each analysis using the standard directory structure

## Version History

v2.2 - 2025-03-30 - Modified template to ensure file path appears at the top of each document
v2.1 - 2025-03-30 - Added storage location instructions
v2.0 - 2025-03-30 - Updated to include all seven mutations and five publication streams
v1.0 - Earlier version with basic analysis structure
