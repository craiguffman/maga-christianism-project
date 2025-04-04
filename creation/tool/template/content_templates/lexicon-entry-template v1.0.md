# 20250404162500_lexicon_entry_template
[Store as: #creation/tool/template/lexicon_entry_template v1.0]
[Related: #creation/tool/index/content_format_index, #creation/tool/workflow/substack_publication_workflow]

---
title: "Lexicon Entry Template"
date: 2025-04-04
type: template
status: complete
tags:
  - lexicon
  - template
  - artifact
  - html
  - substack
---

# Lexicon Entry Template v1.0

This template provides the standardized HTML structure for creating lexicon entry artifacts. The template includes all styling elements, structural components, and cross-reference patterns required for consistent lexicon implementation.

## Template Structure

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lexicon: [TERM]</title>
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
    <p>[DEFINITION - A clear, concise 2-3 sentence definition that establishes the core meaning of the term, its theological significance, and its relevance to the project.]</p>
    
    <h2>Key Characteristics</h2>
    <ul>
        <li>[CHARACTERISTIC 1 - A specific attribute or quality that defines this concept, with brief explanation.]</li>
        <li>[CHARACTERISTIC 2 - A second defining attribute with explanation.]</li>
        <li>[CHARACTERISTIC 3 - A third defining attribute with explanation.]</li>
        <li>[CHARACTERISTIC 4 - Optional fourth attribute if needed.]</li>
        <li>[CHARACTERISTIC 5 - Optional fifth attribute if needed.]</li>
    </ul>
    
    <h2>Historical Context</h2>
    <p>[HISTORICAL CONTEXT - A paragraph explaining the historical development of this concept, including key figures, movements, or events that shaped its evolution. Focus on theological genealogy when relevant.]</p>
    
    <h2>Expressions in Dominative Christianism</h2>
    <p>[DOMINATIVE EXPRESSIONS - How this concept manifests in Dominative Christianism, with specific examples or characteristics. Should highlight distinctive expressions within this theological mutation.]</p>
    
    <h2>Expressions in Providential Identitarianism</h2>
    <p>[PROVIDENTIAL EXPRESSIONS - How this concept manifests in Providential Identitarianism, with parallel examples or characteristics. Should highlight both similarities and differences with Dominative expressions.]</p>
    
    <h2>Orthodox Alternative</h2>
    <p>[ORTHODOX ALTERNATIVE - For mutation entries, describe the orthodox theological alternative to this mutation. For other entries, describe the theological grounding of the concept in orthodox Christianity.]</p>
    
    <div class="divider"></div>
    
    <div class="related-terms">
        <h3>Related Terms</h3>
        <ul>
            <li><a href="/p/lexicon-[related-term-1]">[RELATED TERM 1]</a></li>
            <li><a href="/p/lexicon-[related-term-2]">[RELATED TERM 2]</a></li>
            <li><a href="/p/lexicon-[related-term-3]">[RELATED TERM 3]</a></li>
            <li><a href="/p/lexicon-[related-term-4]">[RELATED TERM 4 - Optional]</a></li>
            <li><a href="/p/lexicon-[related-term-5]">[RELATED TERM 5 - Optional]</a></li>
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

## Implementation Instructions

### Using This Template with Claude

To request a lexicon entry artifact from Claude, use the following prompt format:

```
Please create a lexicon entry artifact for the term "[TERM]" with the following specifications:

Category: [PRIMARY CONCEPTS / THEOLOGICAL MUTATIONS / THEOLOGICAL ALTERNATIVES / THEOLOGICAL GENEALOGY / CONTEMPORARY MOVEMENTS]

Definition: [BRIEF DEFINITION]

Key Characteristics:
- [CHARACTERISTIC 1]
- [CHARACTERISTIC 2]
- [CHARACTERISTIC 3]
- [ADDITIONAL CHARACTERISTICS IF NEEDED]

Historical Context: [BRIEF HISTORICAL BACKGROUND]

Dominative Expression: [HOW IT MANIFESTS IN DOMINATIVE CHRISTIANISM]

Providential Expression: [HOW IT MANIFESTS IN PROVIDENTIAL IDENTITARIANISM]

Orthodox Alternative: [ORTHODOX THEOLOGICAL UNDERSTANDING]

Related Terms:
- [RELATED TERM 1]
- [RELATED TERM 2]
- [RELATED TERM 3]
- [ADDITIONAL RELATED TERMS IF NEEDED]

The artifact should use the standard lexicon HTML template with blue gradient styling and proper cross-references to related terms.
```

### Customization by Lexicon Category

#### Primary Concepts
- Focus on foundational definition and theological significance
- Include etymological information when relevant
- Connect to broader theological tradition
- Emphasize how concept operates in both theological mutations
- Include URL pattern: `lexicon-[concept]`

#### Theological Mutations
- Clearly identify which of the seven mutations is being defined
- Contrast with orthodox theological understanding
- Provide examples from both Dominative and Providential expressions
- Connect to historical developments or precedents
- Include URL pattern: `lexicon-[mutation]`

#### Theological Alternatives
- Establish connection to orthodox theological tradition
- Present as constructive alternative to theological mutations
- Ground in trinitarian and christological foundations
- Connect to participatory freedom theological framework
- Include URL pattern: `lexicon-[alternative]`

#### Theological Genealogy
- Focus on historical development and key figures
- Trace evolution of concept over time
- Identify turning points or transformations
- Connect to contemporary expressions
- Include URL pattern: `lexicon-[genealogy-concept]`

#### Contemporary Movements
- Define current religious-political phenomena
- Analyze theological roots and expressions
- Connect to broader cultural patterns
- Identify distinctive characteristics
- Include URL pattern: `lexicon-[movement]`

### Optional Sections

The template can be customized with additional or alternative sections as needed:

- **Etymology**: Origin and development of the term
- **Biblical Foundations**: Scriptural grounding for the concept
- **Theological Significance**: Importance within theological framework
- **Contemporary Applications**: Modern expressions or implications
- **Critiques and Controversies**: Scholarly debates or criticisms
- **Additional Resources**: Books, articles, or other resources for further study

### Publication Process

1. Copy the completed HTML artifact content
2. Create new post in the Lexicon section on Substack
3. Switch to HTML mode in the editor
4. Paste the complete HTML code
5. Preview to ensure proper rendering
6. Configure custom URL following pattern: `lexicon-[term]`
7. Set to hide from Home feed but remain accessible via URL
8. Publish immediately or schedule as needed

### Cross-Reference Management

- Ensure all related terms have existing lexicon entries
- If entries don't exist yet, create "Coming Soon" placeholder entries
- Update the main glossary page to include the new entry
- Add reciprocal references in related entries
- Update any content that should reference this lexicon entry

## Content Guidelines

### Definition Quality
- Clear, concise, and accurate definition of the term
- Establish theological significance and relevance
- Avoid unnecessary jargon or complex language
- Define complex terms within the definition

### Characteristics Selection
- Choose distinctive characteristics that define the term
- Provide brief explanations for each characteristic
- Order characteristics from most to least important
- Ensure characteristics don't overlap significantly

### Historical Context
- Focus on development rather than comprehensive history
- Highlight key figures, movements, or events
- Connect historical development to contemporary expressions
- Provide sufficient context for understanding

### Expression Analysis
- Compare and contrast expressions in both theological mutations
- Use specific examples whenever possible
- Identify structural patterns rather than just individual instances
- Maintain analytical distance and theological precision

### Related Terms Selection
- Include directly related terms that enhance understanding
- Provide variety of relation types (broader, narrower, related)
- Ensure all related terms have existing or planned entries
- Limit to 3-5 most relevant terms

## Version History

v1.0 - 2025-04-04 - Initial lexicon entry template with comprehensive structure and styling
