# 20250415175000_lexicon_implementation_guide
[Store as: #creation/tool/reference/lexicon_implementation_guide v5.0]
[Related: #creation/tool/index/content_format_index v7.0, #creation/tool/template/lexicon_entry_template v1.0]

---
title: "Lexicon Implementation Guide"
date: 2025-04-15
type: reference
status: complete
tags:
  - lexicon
  - implementation
  - artifact
  - substack
  - html
  - cross_reference
---

# Lexicon Implementation Guide v5.0

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
- **Update Related Entries**: Add reciprocal cross-references to other lexicon entries
- **Verify Link Integrity**: Test all cross-references to ensure proper linking
- **Update Term Registry**: Document the new entry in your master lexicon tracking system

## Artifact-Based Inline References in Content

When referring to lexicon terms within your content artifacts:

### 1. First Mention Reference

In the artifact for a main content piece (Monday chapter, Wednesday essay, etc.), include HTML for lexicon references:

```html
<a href="/p/lexicon-[term]"><i>[Term]</i></a>
```

Example artifact command for creating content with lexicon references:

```
Please create a content artifact for a Monday Dominative Christianism chapter with proper lexicon references for the following terms:
- Primitive Biblicism
- Binary Apocalypticism 
- Participatory Freedom

The references should follow the standard italicized link format on first mention.
```

### 2. End-of-Article References

For content artifacts with multiple technical terms, include a glossary section at the end:

```html
<hr>
<h3>Key Terms</h3>
<p><strong>[Term 1]</strong>: Brief definition. <a href="/p/lexicon-[term-1]">Full entry →</a></p>
<p><strong>[Term 2]</strong>: Brief definition. <a href="/p/lexicon-[term-2]">Full entry →</a></p>
<hr>
```

Example artifact command for adding an end-of-article glossary:

```
Please add an end-of-article glossary section to my content artifact that includes brief definitions and links to the following lexicon terms:
- Primitive Biblicism
- Binary Apocalypticism
- Participatory Freedom

Follow the standard format with horizontal rules, bolded terms, and arrow links.
```

## HTML Template for Lexicon Artifacts

For creating lexicon entry artifacts, Claude should use this standardized HTML template:

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
        <p class="metadata">📘 [CATEGORY] • [DATE]</p>
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

## Handling "Coming Soon" Entries

For terms that need to be referenced but don't yet have published entries:

1. **Placeholder References**:
   - In content artifacts, still link to the unpublished lexicon entry
   - Format: `<a href="/p/lexicon-[term]"><i>[Term]</i></a> <small>(coming soon)</small>`

2. **Main Glossary Placeholders**:
   - Include unpublished terms in the main glossary
   - Format: `[Term] (coming soon)`
   - Update these references when entries are published

3. **Creation Priority List**:
   - Maintain a prioritized list of "coming soon" entries
   - Create these entries before their references appear in published content

## Updating Existing Entries for Terminology Changes

When terminology changes (e.g., from "MAGA Christianism" to "Dominative Christianism"):

1. **Create New Entry**: 
   - Create a new artifact for the updated term
   - Ensure it contains all the same core content as the original

2. **Redirect Strategy**:
   - Create a minimal artifact for the old URL that redirects to the new one:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=/p/lexicon-[new-term]">
    <title>Redirecting to [NEW TERM]</title>
</head>
<body>
    <p>This term has been updated to <a href="/p/lexicon-[new-term]">[NEW TERM]</a>. You will be redirected automatically.</p>
</body>
</html>
```

3. **Update References**:
   - Use search functionality in your text editor to locate all references to the old term
   - Create updated artifacts for all content referencing the old term
   - Update the main glossary page to reflect the terminology change

4. **Publication Status**:
   - Publish the new entry as normal
   - Publish the redirect entry with "unlisted" status to maintain the URL without featuring in feeds

## Lexicon Categories and Organization

The artifact-based approach maintains consistency across these five lexicon categories:

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

## Main Glossary Page Artifact

The main glossary page should be created as an artifact using both categorical and alphabetical organization:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Christianism Lexicon</title>
    <style>
        /* Add styling similar to individual entries */
    </style>
</head>
<body>
    <div class="header-banner">
        <h1 class="title">Christianism Lexicon</h1>
        <p class="metadata">A comprehensive theological reference</p>
    </div>
    
    <div class="divider"></div>
    
    <h2>About This Lexicon</h2>
    <p>This lexicon provides clear definitions of theological concepts, mutations, and alternatives used throughout the Dominative Christianism and Providential Identitarianism project.</p>
    
    <div class="divider"></div>
    
    <h2>By Category</h2>
    
    <h3>Primary Concepts</h3>
    <ul>
        <li><a href="/p/lexicon-christianism">Christianism</a></li>
        <li><a href="/p/lexicon-dominative-christianism">Dominative Christianism</a></li>
        <li><!-- Additional terms --></li>
    </ul>
    
    <h3>Theological Mutations</h3>
    <ul>
        <li><a href="/p/lexicon-primitive-biblicism">Primitive Biblicism</a></li>
        <li><!-- Additional terms --></li>
    </ul>
    
    <!-- Additional categories -->
    
    <div class="divider"></div>
    
    <h2>Alphabetical Index</h2>
    
    <h3>A-C</h3>
    <ul>
        <li><a href="/p/lexicon-binary-apocalypticism">Binary Apocalypticism</a></li>
        <li><a href="/p/lexicon-christianism">Christianism</a></li>
        <li><!-- Additional terms --></li>
    </ul>
    
    <!-- Additional alphabetical sections -->
    
    <div class="divider"></div>
    
    <p class="footer">This lexicon was last updated on [DATE]</p>
</body>
</html>
```

## Artifact-Based Maintenance Schedule

- **Weekly Review**: Use artifacts to review any entries needing updates
- **Monthly Audit**: Run a comprehensive audit of all lexicon artifacts
- **Quarterly Expansion**: Plan systematic expansion of the lexicon system

## Version History

v5.0 - 2025-04-15 - Updated to reflect comprehensive artifact-based workflow for all lexicon creation and implementation
v4.0 - 2025-04-05 - Added detailed implementation protocol for Substack
v3.0 - 2025-04-03 - Updated to reflect terminology change from "MAGA Christianism" to "Dominative Christianism"
v2.0 - 2025-04-01 - Added HTML template and cross-reference framework
v1.0 - 2025-03-15 - Initial lexicon implementation guide