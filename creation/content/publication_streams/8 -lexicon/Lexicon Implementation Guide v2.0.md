# Lexicon Implementation Guide v2.0

## Overview

This guide provides a standardized approach for implementing lexicon entries on your Substack, ensuring consistent structure, navigation, and visual styling across all entries. The system is designed to be easy to maintain while providing a professional and cohesive user experience for your Dominative Christianism and Providential Identitarianism project.

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

## Publication Protocol

1. **Create as Posts**: All individual lexicon entries should be created as Substack Posts, not Pages
2. **Section Assignment**: Assign all entries to a dedicated "Lexicon" section
3. **Hide from Home**: Configure the Lexicon section to be hidden from the Home feed
4. **Maintaining Consistency**: Copy and paste the HTML template for each new entry, replacing placeholder content

## Implementation Steps

1. **Prepare Entry Content**:
   - Replace all placeholder text in brackets (e.g., `[TERM]`, `[DEFINITION]`, etc.)
   - Adjust sections as needed (add or remove based on entry requirements)
   - Ensure all related terms have corresponding lexicon entries or are marked as "Coming Soon"

2. **Format URLs Properly**:
   - For related terms, use lowercase hyphenated format: `/p/lexicon-primitive-biblicism`
   - Ensure the main glossary URL is always `/p/christianism-lexicon`

3. **HTML Editing in Substack**:
   - When creating a new entry, switch to HTML mode in the Substack editor
   - Paste the complete HTML template with your content
   - Preview before publishing to ensure proper formatting

4. **After Publishing**:
   - Update the main glossary page to include the new entry
   - Check that all cross-references work correctly
   - Update any "Coming Soon" references to the new entry

## Inline References in Articles

When referring to lexicon terms within your content:

1. **First Mention**: Use italicized links on first mention of a term
   ```html
   <a href="/p/lexicon-primitive-biblicism"><i>Primitive Biblicism</i></a>
   ```

2. **End-of-Article Glossary**: For articles with multiple technical terms, include a brief glossary at the end
   ```html
   <hr>
   <h3>Key Terms</h3>
   <p><strong>Primitive Biblicism</strong>: Brief definition. <a href="/p/lexicon-primitive-biblicism">Full entry →</a></p>
   <hr>
   ```

## Updating Lexicon for "Dominative Christianism"

For existing content referencing "MAGA Christianism," follow these steps:

1. **Create New Entry**: 
   - Create the new "Dominative Christianism" lexicon entry using the standardized template
   - Ensure it includes the same core theological mutations and characteristics
   - Update the URL to `/p/lexicon-dominative-christianism`

2. **Redirect Strategy**:
   - Create a minimal entry at the old URL (`/p/lexicon-maga-christianism`) 
   - Include a notice: "This term has been updated to Dominative Christianism" with a link to the new entry
   - Set publication status to "unlisted" to maintain the URL without featuring in feeds or search

3. **Update References**:
   - Search for all instances of `/p/lexicon-maga-christianism` across content
   - Replace with `/p/lexicon-dominative-christianism`
   - Update any inline text references from "MAGA Christianism" to "Dominative Christianism"

4. **Main Glossary Update**:
   - Update all references in the main glossary page
   - Include a note about the terminology change
   - Maintain alphabetical and categorical organization

## Content Categories

Organize lexicon entries into these five categories:

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

## Maintenance Schedule

- **Weekly Review**: Check for broken links or references
- **Monthly Update**: Review existing entries for potential updates
- **Quarterly Audit**: Comprehensive review of the entire lexicon system

## Formatting Guidelines

- **Definitions**: Concise, clear, 2-3 sentences
- **Characteristics**: Bulleted lists for easy scanning
- **Historical Context**: Brief paragraph with key developments
- **Distinctions**: Clear contrasts with related concepts
- **Related Terms**: 3-5 most relevant connected concepts with links

## HTML Template

Use this standardized HTML template for all lexicon entries:

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

By following this standardized approach, you'll create a cohesive, professional lexicon system that enhances your readers' understanding while maintaining an efficient workflow for managing entries.