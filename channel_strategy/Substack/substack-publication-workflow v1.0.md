# 20250404161500_substack_publication_workflow
[Store as: #creation/tool/workflow/substack_publication_workflow v1.0]
[Related: #creation/tool/index/content_format_index, #creation/tool/index/comprehensive_taxonomy]

---
title: "Substack Publication Workflow"
date: 2025-04-04
type: workflow
status: complete
tags:
  - substack
  - publication
  - artifacts
  - workflow
  - troubleshooting
---

# Substack Publication Workflow v1.0

This comprehensive workflow document provides a step-by-step process for creating, formatting, and publishing content on Substack using the artifact-based approach. Following this standardized workflow ensures consistent quality and formatting across all content streams in the Dominative Christianism and Providential Identitarianism project.

## Overview of Artifact-Based Publication

The artifact-based publication workflow centralizes content creation, formatting, and cross-referencing in a single process that produces publication-ready content optimized for Substack. This approach ensures:

- **Consistent Formatting**: All content follows standardized templates
- **Efficient Cross-References**: All content includes properly formatted links
- **Streamlined Publication**: Content moves from draft to publication with minimal friction
- **Error Reduction**: Formatting issues are addressed before publication
- **Visual Consistency**: All content shares a cohesive visual identity
- **Version Control**: All content maintains clear version history

## Pre-Publication Planning

### 1. Content Calendar Alignment
- **Check Weekly Theme**: Verify content aligns with current weekly theme
- **Confirm Publication Slot**: Verify content fits designated day of week
- **Review Related Content**: Identify connections to recently published pieces
- **Assess Lexicon Requirements**: Identify any lexicon entries needed for this content

### 2. Lexicon Preparation
- **Create Needed Entries**: Develop lexicon artifacts for any referenced terms
- **Publish Lexicon Entries**: Ensure all referenced lexicon entries are published
- **Update Glossary**: Make sure main glossary includes all referenced terms
- **Test Lexicon Links**: Verify all lexicon links are functional

### 3. Visual Assets Preparation
- **Header Image**: Create or select appropriate header image
- **In-Text Images**: Prepare any supplementary images needed
- **Image Optimization**: Resize and optimize all images for web
- **Image Storage**: Upload images to appropriate hosting location

## Artifact Creation Process

### 1. Content Type Selection
- **Monday**: Dominative Christianism or Providential Identitarianism chapter
- **Tuesday**: Rooted & Reaching personal essay
- **Wednesday**: Common Life Politics theological essay
- **Thursday**: Untold America historical essay
- **Friday**: Divine Republic satirical piece
- **Lexicon**: Specialized lexicon entry

### 2. Template Selection
- Select appropriate artifact template based on content type
- Review template for any needed customization
- Ensure template includes all required sections
- Verify template includes proper metadata structure

### 3. Artifact Generation
- **Request from Claude**: Use standardized artifact request prompt:

```
Please create a [CONTENT TYPE] artifact with the following specifications:
- Title: [TITLE]
- Subtitle: [SUBTITLE]
- Weekly Theme Connection: [THEME]
- Key Sections: [LIST MAIN SECTIONS]
- Lexicon Terms: [LIST TERMS TO REFERENCE]
- Related Content: [LIST RELATED CONTENT]
- Special Requirements: [ANY SPECIAL NEEDS]

The artifact should follow our standard [CONTENT TYPE] template with proper formatting and cross-references.
```

- **Review Draft Artifact**: Carefully examine generated artifact for:
  - Proper markdown/HTML formatting
  - Correct section structure
  - Appropriate content flow
  - Proper cross-references
  - Consistent styling

- **Request Revisions**: If needed, request specific revisions to the artifact:

```
Please update the artifact with these changes:
- Revise section [SECTION] to: [NEW CONTENT]
- Add a new section on: [TOPIC]
- Modify the cross-references to include: [NEW REFERENCES]
- Fix the formatting issue in: [SECTION]
```

- **Finalize Artifact**: Once satisfied, save the final artifact

## Substack Publication Process

### 1. Substack Setup
- **Login**: Access your Substack dashboard
- **Create New Post**: Click "New post" button
- **Select Section**: Choose appropriate section for content type
- **Set Editor Mode**: Switch to markdown mode if needed

### 2. Content Transfer
- **Copy Artifact**: Copy the complete content from the finalized artifact
- **Paste into Substack**: Paste complete content into Substack editor
- **Format Check**: Review how formatting transferred to Substack
- **Address Issues**: Fix any formatting that didn't transfer correctly

### 3. Header Image Setup
- **Add Header Image**: Upload or link to prepared header image
- **Set Alt Text**: Add descriptive alt text for accessibility
- **Adjust Cropping**: Ensure image displays properly on different devices
- **Check Rendering**: Verify image appears correctly in preview

### 4. Publication Settings
- **Set URL Pattern**: Configure custom URL following established pattern:
  - Monday Dominative: `dominative-[topic]`
  - Monday Providential: `providential-[topic]`
  - Tuesday Personal: `rooted-[topic]`
  - Wednesday Theological: `commonlife-[topic]`
  - Thursday Historical: `untold-[topic]`
  - Friday Satirical: `republic-[topic]`
  - Lexicon Entries: `lexicon-[term]`

- **Configure Visibility Settings**:
  - Standard Content: Visible in feed and emails
  - Lexicon Entries: Hidden from feed but accessible via URL
  - Special Content: Configure based on specific needs

- **Set Email Options**:
  - Email Subject: Customize if different from title
  - Email Preview Text: Create compelling preview text
  - Email Settings: Configure based on content type

- **Schedule or Publish**:
  - Schedule: Set future publication date/time
  - Immediate: Publish now

### 5. Post-Publication Verification
- **View Published Content**: Check the live published version
- **Test All Links**: Verify all links function correctly
- **Mobile Check**: Verify rendering on mobile devices
- **Email Test**: Check how content appears in email (if sent)

## Cross-Reference Management

### 1. Weekly Theme Integration
- **Update Weekly Theme Guide**: Add new content to weekly theme guide
- **Add Reciprocal Links**: Update related content to link to new piece
- **Check Navigation Flow**: Ensure logical path through related content

### 2. Lexicon Integration
- **Update Related Lexicon Entries**: Add references to new content
- **Verify Inline References**: Check that all lexical terms link correctly
- **Update Main Glossary**: Add new content connections to glossary

### 3. Series Navigation
- **Update Previous Post**: Add "Next" link to previous post in series
- **Prepare for Next Post**: Include placeholder for upcoming content
- **Series Index**: Update series index if applicable

## Troubleshooting Guide

### 1. Formatting Issues

#### Markdown Not Rendering Correctly
- **Problem**: Markdown syntax not converting to proper formatting
- **Solution**: 
  - Switch to HTML mode and check for syntax errors
  - Ensure proper spacing around markdown elements
  - Verify Substack supports the specific markdown syntax used
  - Consider using HTML alternatives for problematic elements

#### HTML Not Rendering Correctly
- **Problem**: HTML elements not displaying as expected
- **Solution**:
  - Check for unclosed tags or nested elements
  - Verify Substack supports the HTML elements used
  - Use simpler HTML structures for complex elements
  - Test alternative HTML approaches for problematic elements

#### Image Display Problems
- **Problem**: Images not displaying correctly
- **Solution**:
  - Verify image URLs are accessible
  - Check image dimensions and file size
  - Try re-uploading images directly to Substack
  - Use alternative image formats if necessary

### 2. Cross-Reference Problems

#### Broken Links
- **Problem**: Links not directing to correct content
- **Solution**:
  - Verify URL structure follows established patterns
  - Check for typos in URLs
  - Ensure referenced content is published and accessible
  - Test links in preview mode before publishing

#### Missing References
- **Problem**: Content should reference other materials but doesn't
- **Solution**:
  - Update artifact to include missing references
  - Follow standard reference patterns for consistency
  - Update related content to include reciprocal references
  - Use the weekly theme guide to identify needed connections

#### Circular References
- **Problem**: Content creates circular reference patterns
- **Solution**:
  - Map out reference structure to identify circles
  - Restructure references to create logical progression
  - Use hierarchical reference structure when appropriate
  - Maintain directional flow in reference network

### 3. Publication Issues

#### Scheduling Problems
- **Problem**: Content not publishing at scheduled time
- **Solution**:
  - Check timezone settings in Substack
  - Verify scheduling was confirmed (not just drafted)
  - Look for error messages in Substack dashboard
  - Manually publish if scheduled publication fails

#### Email Delivery Issues
- **Problem**: Email version not delivering properly
- **Solution**:
  - Check email settings in Substack dashboard
  - Verify content isn't flagged by spam filters
  - Test simpler email formats if complex ones fail
  - Use Substack's email test feature before sending

#### Section Assignment Problems
- **Problem**: Content appearing in wrong section
- **Solution**:
  - Verify section selection during publication
  - Check section settings in Substack dashboard
  - Update content if already published to wrong section
  - Review section organization for potential improvements

## Artifact Templates for Different Content Types

### Monday: Dominative/Providential Chapter Artifact

```markdown
---
title: "[Title]"
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

[Connection to parallel theological mutation in the other framework.]

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

### Tuesday: Personal Essay Artifact

```markdown
---
title: "[Title]"
subtitle: "[Subtitle]"
image: "[Header Image URL]"
---

![Header Image: [Title]](header-image-url)

[Opening personal anecdote or scene setting.]

[Introduction of personal theme and connection to broader project.]

## [Section 1 Heading]

[Personal narrative exploring first dimension of theme.]

[Connection to personal experience or memory.]

## [Section 2 Heading]

[Development of personal insight or struggle.]

[Integration of metaphor or analogy.]

## [Section 3 Heading]

[Transition to broader application or lesson.]

[Connection to theological concept without explicit academic language.]

## [Section 4 Heading]

[Integration of practical application.]

[Subtle connection to weekly theme.]

## Conclusion

[Return to opening anecdote with new perspective.]

[Invitation to reader's own reflection.]

[Final image or metaphor that resonates with theme.]

---

### From My Garden

*This is part of my "Rooted & Reaching" series exploring spiritual formation through the metaphors of gardening, cooking, and endurance training.*

[Brief description of where this fits in personal journey.]

---

### Related Content

- [Previous Essay in Series →](/p/rooted-previous-topic)
- [Related Theological Content →](/p/commonlife-related-topic)
- [Weekly Theme →](/p/theme-week-topic)
```

### Lexicon Entry Artifact

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

## Integration with Other Tools

### VSCode Integration
- Use VSCode to review artifact markdown before publication
- Maintain templates in VSCode for offline reference
- Use VSCode's diff functionality to track changes between artifact versions

### Tana Integration
- Track all published content with appropriate Tana tags
- Link content pieces to each other in Tana's knowledge graph
- Use Tana to monitor content schedule and publication status

### Scrivener Integration
- Import published Substack content into Scrivener for book compilation
- Use Scrivener to organize content into thematic collections
- Maintain parallel structure between Substack and Scrivener organization

### Descript Integration
- Use artifacts as scripts for audio recordings in Descript
- Maintain consistent audio intro/outro based on content type
- Use Descript's Studio Sound for consistent audio quality

## Maintaining Publication Consistency

### Weekly Publishing Rhythm
- **Monday**: Dominative or Providential chapter
- **Tuesday**: Personal essay
- **Wednesday**: Theological essay
- **Thursday**: Historical essay
- **Friday**: Satirical piece
- **As Needed**: Lexicon entries (prior to being referenced)

### Content Batching
- Create artifacts in batches by type
- Develop all content for a weekly theme simultaneously
- Ensure cross-references are consistent within batch
- Schedule publication in advance when possible

### Quality Control Checkpoints
- **Pre-Artifact**: Content aligns with project goals and weekly theme
- **Artifact Creation**: Content follows standard template and formatting
- **Pre-Publication**: Content renders correctly in Substack preview
- **Post-Publication**: Content displays correctly and links function
- **Weekly Review**: All content for the week forms coherent whole

## Version History

v1.0 - 2025-04-04 - Initial comprehensive Substack publication workflow document