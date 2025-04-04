# Lexicon Implementation Guide v3.0

## Overview

This guide provides a standardized approach for implementing lexicon entries on your Substack using artifacts, ensuring consistent structure, navigation, and visual styling across all entries. The system is designed to be easy to maintain while providing a professional and cohesive user experience for your Dominative Christianism and Providential Identitarianism project.

## Artifact-Based Lexicon Implementation

The artifact-based approach streamlines lexicon creation, ensuring consistency across all entries while enabling efficient cross-referencing throughout your Substack content.

### Benefits of Artifact-Based Lexicon Creation

- **Formatting Consistency**: Ensures all lexicon entries follow identical HTML structure and styling
- **Efficient Creation**: Templates eliminate repetitive formatting work
- **Error Reduction**: Standardized approach minimizes HTML errors and inconsistencies
- **Version Control**: Facilitates tracking of lexicon entry updates over time
- **Cross-Reference Integrity**: Maintains consistent URL pattern for reliable linking
- **Batch Processing**: Enables creation of multiple related entries with consistent formatting
- **Seamless Integration**: Ensures lexicon entries work harmoniously with other content types

## URL Structure

All lexicon entries follow a consistent URL pattern:

```
/p/lexicon-[term]
```

Examples:
- `/p/lexicon-christianism`
- `/p/lexicon-dominative-christianism`
- `/p/lexicon-providential-identitarianism`

For terms with multiple words, use hyphens to separate words in the URL.

## Main Glossary Page

The main glossary page acts as the central hub for all lexicon entries and is published as a Substack Page (not a Post) with the URL:

```
/p/christianism-lexicon
```

This page should be added to your Substack navigation menu for easy access.

## Artifact-Based Publication Protocol

1. **Create as Artifacts**: 
   - Use Claude to create lexicon entries as artifacts using the standard HTML template
   - Request HTML format within the artifact to ensure proper rendering
   - Verify all styling elements are included in the artifact

2. **Publication Settings**:
   - Publish all individual lexicon entries as Substack Posts, not Pages
   - Assign all entries to a dedicated "Lexicon" section
   - Configure the Lexicon section to be hidden from the Home feed
   - Set custom URL following the lexicon URL pattern

3. **Maintaining Consistency**:
   - Use the artifact template for each new entry
   - Update the artifact template if design changes are needed across all entries
   - Periodically audit published entries for formatting consistency

## Artifact-Based Implementation Workflow

### 1. Preparation Phase

- **Identify Terms**: Determine lexicon terms needed for upcoming content
- **Prioritize Creation**: Create entries before they are referenced in main content
- **Research Content**: Gather necessary information for comprehensive definitions
- **Cross-Reference Planning**: Identify related terms that should be cross-referenced

### 2. Artifact Creation Phase

- **Request Artifact**: Ask Claude to create a lexicon entry artifact using this prompt:

```
Please create a lexicon entry artifact for the term "[TERM]" with the following specifications:
- Term Category: [CATEGORY]
- Definition: [BRIEF DEFINITION]
- Key Characteristics: [LIST 3-5 KEY POINTS]
- Historical Context: [BRIEF HISTORICAL BACKGROUND]
- Related Terms: [LIST 3-5 RELATED TERMS]
- Additional Section (if needed): [SECTION NAME] - [CONTENT]

The artifact should use the standard lexicon HTML template with blue gradient styling and proper cross-references to related terms.
```

- **Review Artifact**: Carefully review the generated artifact for:
  - Correct HTML structure
  - Proper styling elements
  - Accurate content
  - Functioning cross-references
  - Consistent formatting

- **Refine Artifact**: Request adjustments to the artifact if needed:

```
Please update the lexicon artifact with these changes:
- Revise the definition to: [NEW DEFINITION]
- Add an additional characteristic: [NEW CHARACTERISTIC]
- Update the historical context section: [NEW CONTENT]
- Add/modify the related terms: [UPDATED RELATED TERMS]
```

### 3. Publication Phase

- **Copy Artifact Content**: Copy the complete HTML from the artifact
- **Create Substack Post**: Create a new post in the Lexicon section
- **Paste HTML Content**: Switch to HTML mode in Substack editor and paste the complete code
- **Preview Rendering**: Check that all elements render correctly in preview mode
- **Set Custom URL**: Configure the custom URL following the lexicon pattern
- **Configure Settings**: 
  - Section: Lexicon
  - Visibility: Hide from Home feed
  - SEO Description: First sentence of definition
  - Schedule: Immediate or scheduled as needed

- **Publish Entry**: Publish the lexicon entry

### 4. Cross-Reference Integration Phase

- **Update Main Glossary**: Add the new entry to both categorical and alphabetical sections
- **Update Related Entries**: Add reciprocal cross-references in related entries
- **Verify URL Function**: Test all links to ensure proper redirection
- **Check Inline References**: If term will be referenced in upcoming content, verify reference format

### 5. Maintenance Phase

- **Periodic Audits**: Quarterly review of all lexicon entries
- **Content Updates**: When updating content, generate new artifact version
- **URL Monitoring**: Periodically verify all cross-references function properly
- **Template Evolution**: Update the artifact template as design needs evolve

## Updating Lexicon for "Dominative Christianism"

For existing content referencing "MAGA Christianism," follow these artifact-based update process:

1. **Create New Entry Artifact**: 
   - Generate a new "Dominative Christianism" lexicon entry artifact using the standardized template
   - Ensure it includes the same core theological mutations and characteristics
   - Update the URL references to `/p/lexicon-dominative-christianism`

2. **Redirect Strategy Artifact**:
   - Create a minimal redirect artifact for the old URL (`/p/lexicon-maga-christianism`) 
   - Include a notice: "This term has been updated to Dominative Christianism" with a link to the new entry
   - Set publication status to "unlisted" to maintain the URL without featuring in feeds or search

3. **Update References Systematically**:
   - Create an artifact-based search-and-replace document to track all instances of `/p/lexicon-maga-christianism` 
   - Replace with `/p/lexicon-dominative-christianism` in all content
   - Update any inline text references from "MAGA Christianism" to "Dominative Christianism"

4. **Main Glossary Update Artifact**:
   - Create an updated main glossary artifact
   - Update all references in the main glossary page
   - Include a note about the terminology change
   - Maintain alphabetical and categorical organization

## Content Categories

Organize lexicon artifacts into these five categories:

1. **Primary Concepts**
   - Christianism
   - Dominative Christianism
   - Providential Identitarianism
   - Kingdom/Empire
   - Biblical Hermeneutics
   - Theological Anthropology
   - Religious Economics

2. **Theological Mutations**
   - Primitive Biblicism
   - Practical Atheism
   - Binary Apocalypticism
   - Disordered Nationalism
   - Prosperity Materialism
   - Authoritarian Spirituality
   - Tribal Epistemology

3. **Theological Alternatives**
   - Participatory Freedom
   - Being With
   - Prophetic Patriotism
   - Biblical Justice
   - Hospitality
   - Prophetic-Pastoral
   - Christian Citizenship

4. **Theological Genealogy**
   - Calvinist Roots
   - Puritan Development
   - Covenant Theology
   - Dominion Theology
   - Manifest Destiny
   - Prosperity Gospel
   - Civil Religion

5. **Contemporary Movements**
   - Christian Nationalism
   - Identity Synthesis
   - Post-Truth Politics
   - Authoritarian Religion
   - Evangelical Accommodation

## Artifact-Based Maintenance Schedule

- **Weekly Artifact Review**: Generate a review artifact to check for broken links or references
- **Monthly Artifact Update**: Create update artifacts for existing entries that need refreshing
- **Quarterly Artifact Audit**: Develop comprehensive audit artifact covering the entire lexicon system

## Artifact-Based Formatting Guidelines

- **Definitions**: Concise, clear, 2-3 sentences in each artifact
- **Characteristics**: Bulleted lists for easy scanning in artifacts
- **Historical Context**: Brief paragraph with key developments in each artifact
- **Distinctions**: Clear contrasts with related concepts in each artifact
- **Related Terms**: 3-5 most relevant connected concepts with links in each artifact

## Lexicon Artifact HTML Template

Use this standardized HTML template for all lexicon artifacts:

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

## Lexicon Artifact Integration with Content Artifacts

Every content artifact should integrate with lexicon artifacts through:

1. **Inline Term References**: Format as `[*term*](/p/lexicon-term)` in content artifacts
2. **End-of-Artifact Glossaries**: Include a glossary section at the end of each content artifact:

```markdown
---

### Key Terms

**[Term 1]**: Brief definition. [Full entry →](/p/lexicon-term-1)

**[Term 2]**: Brief definition. [Full entry →](/p/lexicon-term-2)

**[Term 3]**: Brief definition. [Full entry →](/p/lexicon-term-3)

---
```

3. **Related Content Links**: Include lexicon connections in the related content section:

```markdown
---

### Related Content

- [Related Article →](/p/article-name)
- [Lexicon: Related Term →](/p/lexicon-related-term)
- [Weekly Theme →](/p/theme-week-topic)

---
```

## Artifact-Based Integration with Other Tools

### VSCode Integration
- Store lexicon artifact templates in VSCode for quick reference
- Use VSCode for artifact review before Substack publication
- Maintain version history of artifact templates in VSCode

### Tana Integration
- Track all lexicon artifacts in Tana with appropriate tags
- Link lexicon artifacts to related content artifacts in Tana
- Use Tana to monitor cross-references between artifacts

### Scrivener Integration
- Import lexicon artifacts into Scrivener for book compilation
- Link content sections to relevant lexicon artifacts
- Use Scrivener to organize lexicon artifacts for print publication

## Troubleshooting Artifact Issues

### Common Artifact Problems and Solutions

1. **HTML Rendering Issues**:
   - Problem: HTML in artifact doesn't render correctly in Substack
   - Solution: Review HTML in VSCode, validate before pasting into Substack
   
2. **Broken Cross-References**:
   - Problem: Links between artifacts not functioning
   - Solution: Use artifact audit tool to systematically check all links
   
3. **Inconsistent Styling**:
   - Problem: Style elements vary between artifacts
   - Solution: Update artifact template and regenerate affected artifacts
   
4. **URL Pattern Conflicts**:
   - Problem: Duplicate or inconsistent URL patterns
   - Solution: Maintain URL registry artifact to track all URLs
   
5. **Artifact Update Propagation**:
   - Problem: Updates to lexicon artifacts not reflected in content
   - Solution: Create update tracking artifact to manage changes

By following this artifact-based approach to lexicon implementation, you'll create a cohesive, professional lexicon system that enhances your readers' understanding while maintaining an efficient workflow for managing entries across all your publishing platforms.

## Version History

v3.0 - 2025-04-04 - Updated with comprehensive artifact-based workflow and integration instructions
v2.0 - 2025-04-03 - Updated to reflect renaming from "MAGA Christianism" to "Dominative Christianism"
v1.0 - 2025-04-02 - Initial lexicon implementation guide