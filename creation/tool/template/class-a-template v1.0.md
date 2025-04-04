# 20250404170100_class_a_template
[Store as: #creation/tool/template/class_a_template v1.0]
[Related: #creation/tool/index/content_classification_framework, #creation/tool/index/tana_tagging_reference]

---
title: "Class A Content Template: Tana-Bound Tools"
date: 2025-04-04
type: template
status: complete
tags:
  - class_a
  - tana
  - template
  - knowledge_management
---

# Class A Content Template: Tana-Bound Tools

This template provides the standard structure and formatting guidelines for all Class A content (Tana-bound tools) in the Dominative Christianism and Providential Identitarianism project. Class A content comprises knowledge objects and organizational tools that primarily live within the Tana knowledge management system.

## Filename Convention
```
YYYYMMDDHHMM_descriptive_name.md
```
Example: `20250404170100_class_a_template.md`

## Storage Tag Convention
```
#[primary_category]/[subcategory]/[name] v[version]
```
Example: `#creation/tool/template/class_a_template v1.0`

## Standard Header Structure
```markdown
# YYYYMMDDHHMM_descriptive_name
[Store as: #primary_category/subcategory/name v1.0]
[Related: #related/resource1, #related/resource2]
[Collection: #collection/name] (if applicable)

---
title: "Document Title"
date: YYYY-MM-DD
type: knowledge_object_type
status: draft|in_progress|complete|archived
tags:
  - relevant_tag1
  - relevant_tag2
  - relevant_tag3
---
```

## Body Structure
The body of Class A content should follow this general structure:

### Required Sections

#### 1. Overview/Introduction
A brief introduction explaining the purpose and function of the knowledge object or tool.

```markdown
# Document Title

Brief introduction explaining the purpose of this object within the knowledge management system.
```

#### 2. Core Content
The main content section, structured according to the specific knowledge object type.

For **Topic Objects**:
```markdown
## Definition
Concise definition of the topic.

## Key Components
- Component 1: Brief explanation
- Component 2: Brief explanation
- Component 3: Brief explanation

## Significance
Why this topic matters to our project.

## Applications
How this topic applies to our primary research focus.
```

For **Index Objects**:
```markdown
## Index Structure
Overview of the index organization.

## Primary Categories
```markdown
#category/subcategory
  └── item1 [description] v1.0
  └── item2 [description] v1.0
  └── item3 [description] v1.0
```

## Implementation Guidelines
Instructions for using and maintaining the index.
```

For **Reference Objects**:
```markdown
## Reference Structure
Overview of how the reference is organized.

## Key Reference Points
| Term | Definition | Usage |
|------|------------|-------|
| Term 1 | Definition 1 | Usage context 1 |
| Term 2 | Definition 2 | Usage context 2 |

## Application Guidelines
How to apply this reference in practice.
```

#### 3. Integration Section
Explains how this object connects to other elements of the knowledge system.

```markdown
## Integration with Knowledge System
- Connects to [[Related Object 1]] through [relationship description]
- Informs [[Related Object 2]] by providing [description]
- Depends on [[Related Object 3]] for [description]
```

#### 4. Version History
A record of version changes.

```markdown
## Version History
v1.0 - YYYY-MM-DD - Initial creation
v1.1 - YYYY-MM-DD - Minor updates [description]
v2.0 - YYYY-MM-DD - Major revision [description]
```

## Tana Implementation Notes

### Super Tags
Class A content uses the following Tana super tag structure:
- `#creation` - For tools and workflows
- `#knowledge` - For knowledge objects
- `#note` - For note objects

### Node Structure
In Tana, implement as follows:
1. Create a node with the primary name
2. Add the appropriate super tag
3. Add child nodes for each section
4. Add metadata as field values
5. Create version nodes as children
6. Establish bidirectional references to related nodes

### Export Format
When exporting from Tana to Dropbox, maintain the following structure:
```
/tools/tana_exports/YYYYMMDDHHMM_descriptive_name.md
```

## Creation Process

### 1. Initial Draft with Claude
- Use artifact-based approach in Claude
- Specify Class A format in your request
- Include all required sections
- Request proper tagging and formatting

### 2. Tana Import
- Copy markdown from Claude
- Create appropriate node in Tana
- Apply super tag
- Structure child nodes
- Add metadata

### 3. Integration
- Create bidirectional references
- Link to related knowledge objects
- Update any indices that should reference this content

### 4. Export Backup
- Export formatted markdown to Dropbox
- Maintain consistent naming convention
- Store in appropriate directory

## Version History

v1.0 - 2025-04-04 - Initial template for Class A content
