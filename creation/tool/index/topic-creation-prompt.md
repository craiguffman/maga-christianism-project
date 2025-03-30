/Users/craiguffman/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub/maga-christianism-project/tools/prompts/20250331143600_topic_creation_prompt.md

# 20250331143600_topic_creation_prompt
[Store as: #creation/tool/prompt/topic_creation v1.0]
[Related: #creation/tool/index/knowledge_object_index]

---
title: "Topic Creation Prompt"
date: 2025-03-31
type: prompt
status: complete
tags:
  - claude
  - prompt
  - knowledge
  - topic
---

# Topic Creation Prompt

## Purpose
This prompt template is designed to generate structured #topic knowledge objects that integrate seamlessly with our knowledge management system and support the MAGA Christianism project's analytical framework.

## Storage Location
All topic objects should be stored in the following directory:
- `/Users/craiguffman/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub/maga-christianism-project/research/topics/zettlekasten/YYYYMMDDHHMM_[topic_name].md`

## Prompt Template

```
I need Claude to analyze the following content and create a comprehensive #topic knowledge object:

Source: [CONTENT OR SOURCE]

Create a markdown file for my Tana Zettelkasten with the following filename format:
YYYYMMDDHHMM_[topic_name_with_underscores].md

The content should follow this structure:

# YYYYMMDDHHMM_[topic_name_with_underscores]

## Metadata
- **Type**: #knowledge #topic
- **Source**: [Reference information]
- **Connected to**: [[Related topics]], [[Related concepts]], [[Related frameworks]]
- **Project**: MAGA Christianism Book
- **Status**: #active #synthesis

## Definition
[Core definition of the topic - 2-3 sentences that capture its essence]

## Key Components
- [Component 1]: [Brief explanation]
- [Component 2]: [Brief explanation]
- [Component 3]: [Brief explanation]
- [Component 4]: [Brief explanation]

## Significance
[Why this topic matters to the project - 3-5 sentences on its implications]

## Scholarly Context
[How this topic is situated in academic discourse - which scholars/disciplines have shaped it]

## Applications to MAGA Christianism Analysis
- [Application 1]: [Brief explanation]
- [Application 2]: [Brief explanation]
- [Application 3]: [Brief explanation]

## Related Concepts
- [[Concept 1]]: [Brief explanation of relationship]
- [[Concept 2]]: [Brief explanation of relationship]
- [[Concept 3]]: [Brief explanation of relationship]

## Research Questions
- [Question 1 that this topic raises or helps address]
- [Question 2 that this topic raises or helps address]
- [Question 3 that this topic raises or helps address]

## References
- [Citation 1]
- [Citation 2]
- [Citation 3]

#[topic_area_1] #[topic_area_2] #[topic_area_3] #[topic_area_4]
```

## Implementation Notes
- Use descriptive topic names with underscores between words
- Include appropriate related concepts, frameworks, and topics
- Ensure applications focus specifically on MAGA Christianism analysis
- Use double brackets [[like this]] for all related knowledge objects
- Include specific page numbers for citations when available
- Always include the timestamp in YYYYMMDDHHMM format at the beginning of the filename

## Usage Workflow
1. Identify source material containing key topic information
2. Use this prompt to generate a structured topic knowledge object
3. Review for accuracy and completeness
4. Store in the appropriate directory
5. Update the knowledge object index to include the new topic

## Version History

v1.0 - 2025-03-31 - Initial topic creation prompt