# 20250404160100_content_format_index.md
[Store as: #creation/tool/index/content_format_index v6.0]
[Related: #creation/tool/index/comprehensive_taxonomy, #creation/tool/index/tana_tagging_reference]

---
title: "Content Format Index"
date: 2025-04-04
version: 6.0
type: reference
status: active
tags:
  - content_management
  - reference
  - project_organization
  - dominative_christianism
  - providential_identitarianism
  - sermon_integration
  - lexicon
  - artifacts
  - substack
---

# Content Format Index v6.0

This document catalogues all content formats used in the Dominative Christianism and Providential Identitarianism Project, including artifact templates, formatting standards, and implementation guidelines.

## Substack Formatting Standards

This section provides comprehensive guidelines for artifact-based content delivery on Substack, including formatting conventions, URL patterns, and cross-referencing structures for each content type.

### Artifact-Based Approach Benefits
- **Consistent Formatting**: Standardized approach ensures visual consistency across all content types
- **Efficient Workflow**: Templates streamline content creation and reduce formatting time
- **Cross-Platform Compatibility**: Artifacts work consistently across Substack, VSCode, and other tools
- **Version Control**: Facilitates tracking changes and maintaining content history
- **Error Reduction**: Standardized approach minimizes formatting errors during publication
- **Cross-Reference Integrity**: Consistent URL patterns ensure reliable cross-referencing
- **Batch Processing**: Enables efficient creation of multiple content pieces with consistent formatting

### General Formatting Principles

#### Markdown Structure
- **Headers**: Use standard markdown headers (`#`, `##`, `###`) with consistent hierarchy
- **Bold/Italic**: Use `**bold**` and `*italic*` for emphasis consistently
- **Lists**: Use standard markdown list formatting for bulleted and numbered lists
- **Blockquotes**: Use `>` for quotations with proper attribution
- **Line Spacing**: Include blank lines between paragraphs and sections
- **Section Dividers**: Use `---` for horizontal rules between major sections
- **Link Formatting**: Use standard markdown `[text](URL)` format for all links
- **Image Embedding**: Use `![alt text](image-url)` format for inline images

#### Substack-Specific Considerations
- **Header Images**: Include standardized header image reference at top of each artifact
- **Pull Quotes**: Format using Substack's specific HTML structure for proper rendering
- **Footnotes**: Use Substack-compatible footnote syntax at end of document
- **Comments Section**: Include standardized prompt for comments when appropriate
- **Subscription Call**: Include standardized subscription call to action at end of piece
- **Navigation Links**: Include standardized navigation to related content at bottom of each piece
- **Mobile Responsiveness**: Ensure all formatting works on mobile devices (shorter paragraphs, appropriate image sizing)
- **Preview Text**: Include carefully crafted preview text for email distribution

### URL Structure and Cross-Referencing

#### URL Patterns by Content Type
- **Monday Dominative**: `dominative-[topic]` (e.g., `dominative-primitive-biblicism`)
- **Monday Providential**: `providential-[topic]` (e.g., `providential-covenant-theology`)
- **Tuesday Personal**: `rooted-[topic]` (e.g., `rooted-metrics-matter`)
- **Wednesday Theological**: `commonlife-[topic]` (e.g., `commonlife-bullshit`)
- **Thursday Historical**: `untold-[topic]` (e.g., `untold-textbook-lied`)
- **Friday Satirical**: `republic-[topic]` (e.g., `republic-library-renovation`)
- **Lexicon Entries**: `lexicon-[term]` (e.g., `lexicon-dominative-christianism`)
- **Sermon Content**: `sermon-[passage]` (e.g., `sermon-mark-1-1-15`)
- **Weekly Themes**: `theme-[week]-[topic]` (e.g., `theme-01-introduction`)

#### Cross-Reference Implementation
- **Inline Lexicon References**: Format as `[*term*](/p/lexicon-term)` (italicized with link)
- **End-of-Article Glossary**: Use standardized HTML format for term definitions with links
- **Related Content Section**: Include standardized section at end of each artifact with related content links
- **Sermon Connections**: Include standardized reference to related sermon content
- **Weekly Theme Reference**: Include subtle reference to weekly theme in each content piece
- **Series Navigation**: Include "Previous" and "Next" links for content in sequential series

### Content Type-Specific Artifact Templates

#### Monday: Dominative Christianism Chapters

```markdown
---
title: "Dominative Christianism: [Title]"
subtitle: "[Subtitle]"
image: "[Header Image URL]"
---

![Header Image: [Title]](header-image-url)

## Introduction

[Opening paragraph introducing the theological concept or mutation being explored.]

[Connection to weekly theme and relevant sermon passage.]

## [Section 1 Heading]

[Content exploring aspect 1 of the concept.]

> **PULL QUOTE**: A particularly insightful or provocative statement from this section.

[Additional paragraphs developing this section.]

## [Section 2 Heading]

[Content exploring aspect 2 of the concept.]

[Integration of relevant lexicon terms with inline references.]

## [Section 3 Heading]

[Content exploring aspect 3 of the concept.]

[Connection to Providential Identitarianism's parallel expression.]

## [Section 4 Heading]

[Content exploring aspect 4 of the concept.]

[Integration of relevant source material with proper citation.]

## Conclusion

[Summary of key insights.]

[Connection back to weekly theme and sermon content.]

[Call to reflection or action.]

---

### Key Terms

**[Term 1]**: Brief definition. [Full entry →](/p/lexicon-term-1)

**[Term 2]**: Brief definition. [Full entry →](/p/lexicon-term-2)

**[Term 3]**: Brief definition. [Full entry →](/p/lexicon-term-3)

---

### Related Content

- [Related Monday Chapter →](/p/dominative-related-topic)
- [Sermon Connection →](/p/sermon-mark-passage)
- [Weekly Theme →](/p/theme-week-topic)

---

#### Notes

[1] Footnote reference 1.
[2] Footnote reference 2.
```

#### Lexicon Entry Artifact Structure

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lexicon: [Term]</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .header-banner {
            background: linear-gradient(135deg, #1a365d 0%, #2564eb 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
        }
        
        .title {
            margin: 0;
            font-size: 28px;
        }
        
        .metadata {
            margin-top: 10px;
            font-size: 14px;
            opacity: 0.9;
        }
        
        .divider {
            border-bottom: 1px solid #e5e7eb;
            margin: 25px 0;
        }
        
        h2 {
            font-size: 22px;
            margin-top: 30px;
            margin-bottom: 15px;
            color: #1a365d;
        }
        
        p {
            margin-bottom: 20px;
        }
        
        ul {
            margin-bottom: 20px;
        }
        
        li {
            margin-bottom: 10px;
        }
        
        .related-terms {
            background-color: #f9fafb;
            padding: 15px;
            border-radius: 8px;
            margin: 25px 0;
        }
        
        .related-terms h3 {
            margin-top: 0;
            color: #1a365d;
        }
        
        .footer {
            font-size: 14px;
            font-style: italic;
            color: #6b7280;
            margin: 30px 0;
        }
        
        .navigation {
            display: flex;
            justify-content: space-between;
            margin: 30px 0;
        }
        
        .navigation a {
            text-decoration: none;
            color: #2564eb;
        }
    </style>
</head>
<body>
    <div class="header-banner">
        <h1 class="title">Lexicon: [TERM]</h1>
        <p class="metadata">📘 [CATEGORY] | [DATE]</p>
    </div>
    
    <div class="divider"></div>
    
    <h2>Definition</h2>
    <p>[DEFINITION]</p>
    
    <h2>Key Characteristics</h2>
    <ul>
        <li>[CHARACTERISTIC 1]</li>
        <li>[CHARACTERISTIC 2]</li>
        <li>[CHARACTERISTIC 3]</li>
    </ul>
    
    <h2>Historical Context</h2>
    <p>[HISTORICAL CONTEXT]</p>
    
    <h2>[ADDITIONAL SECTION]</h2>
    <p>[ADDITIONAL CONTENT]</p>
    
    <div class="divider"></div>
    
    <div class="related-terms">
        <h3>Related Terms</h3>
        <ul>
            <li><a href="/p/lexicon-[related-term-1]">[RELATED TERM 1]</a></li>
            <li><a href="/p/lexicon-[related-term-2]">[RELATED TERM 2]</a></li>
            <li><a href="/p/lexicon-[related-term-3]">[RELATED TERM 3]</a></li>
        </ul>
    </div>
    
    <p class="footer">This lexicon entry was last updated on [DATE]</p>
    
    <div class="navigation">
        <a href="/p/christianism-lexicon">⬅️ Return to Main Glossary</a>
        <a href="/">➡️ Return to Home</a>
    </div>
</body>
</html>
```

### Artifact Implementation Process

#### Creation Phase
1. **Select Template**: Choose appropriate template for content type
2. **Generate Artifact**: Create artifact in Claude with complete formatting
3. **Review Formatting**: Ensure all markdown/HTML elements render correctly
4. **Cross-Reference Check**: Verify all links use correct URL patterns
5. **Metadata Completion**: Ensure all metadata fields are properly populated

#### Publication Phase
1. **Copy Artifact**: Copy complete artifact content to clipboard
2. **Substack Editor**: Open Substack and create new post with appropriate settings
3. **Paste Content**: Paste complete artifact content into editor
4. **Format Check**: Review rendering in Substack preview mode
5. **Adjust as Needed**: Make minor adjustments if Substack renders differently than expected
6. **Set URL Pattern**: Configure custom URL following established pattern
7. **Configure Settings**: Set appropriate publication settings (section, schedule, visibility)
8. **Publish**: Publish content or schedule for appropriate publication slot

#### Maintenance Phase
1. **Update Cross-References**: When publishing new content, update related content links
2. **URL Verification**: Periodically verify all cross-references are functioning
3. **Content Updates**: When updating content, maintain consistent formatting
4. **Template Evolution**: Update templates as formatting needs evolve
5. **Metadata Management**: Keep metadata consistent across all content

### Implementation Examples

#### Example 1: Inline Lexicon Reference

**Artifact Code:**
```markdown
This analysis examines how [*Primitive Biblicism*](/p/lexicon-primitive-biblicism) manifests in both Dominative Christianism and Providential Identitarianism.
```

**Rendered Output:**
This analysis examines how *Primitive Biblicism* manifests in both Dominative Christianism and Providential Identitarianism.

#### Example 2: End-of-Article Glossary

**Artifact Code:**
```markdown
---

### Key Terms

**Primitive Biblicism**: Claims direct, unmediated access to biblical meaning. [Full entry →](/p/lexicon-primitive-biblicism)

**Practical Atheism**: Removes Jesus as exemplar, replacing with pragmatic politics. [Full entry →](/p/lexicon-practical-atheism)

**Participatory Freedom**: Freedom as capacity to love God and neighbor without domination. [Full entry →](/p/lexicon-participatory-freedom)

---
```

**Rendered Output:**
### Key Terms

**Primitive Biblicism**: Claims direct, unmediated access to biblical meaning. [Full entry →]

**Practical Atheism**: Removes Jesus as exemplar, replacing with pragmatic politics. [Full entry →]

**Participatory Freedom**: Freedom as capacity to love God and neighbor without domination. [Full entry →]

#### Example 3: Related Content Section

**Artifact Code:**
```markdown
---

### Related Content

- [Dominative Christianism: Biblical Interpretation →](/p/dominative-biblical-interpretation)
- [Sermon: Mark 2:23-28 (Sabbath Controversies) →](/p/sermon-mark-2-23-28)
- [Weekly Theme: Scripture Authority →](/p/theme-02-scripture-authority)
- [Lexicon: Biblical Hermeneutics →](/p/lexicon-biblical-hermeneutics)

---
```

**Rendered Output:**
### Related Content

- [Dominative Christianism: Biblical Interpretation →]
- [Sermon: Mark 2:23-28 (Sabbath Controversies) →]
- [Weekly Theme: Scripture Authority →]
- [Lexicon: Biblical Hermeneutics →]

## Lexicon Content

[Content continues from previous version...]
