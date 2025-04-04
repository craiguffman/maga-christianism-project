# class-c-template-v1-0
[Store as: #creation/tool/template/class_c_template v1.0]
[Related: #creation/tool/index/content_classification_framework]

---
title: "Class C Content Template: Platform-Optimized Content"
date: 2025-04-04
type: template
status: complete
tags:
  - class_c
  - substack
  - epub
  - youtube
  - template
  - publication
---

# Class C Content Template: Platform-Optimized Content

This template provides the standard structure and formatting guidelines for all Class C content (platform-optimized content) in the Dominative Christianism and Providential Identitarianism project. Class C content comprises public-facing content specifically formatted for publication on external platforms including Substack, EPUB, and YouTube.

## Platform-Specific Templates

This master template includes specific formatting requirements for three primary publication platforms:
1. Substack posts (HTML-enhanced markdown)
2. EPUB chapters (Scrivener format)
3. YouTube scripts (Descript format)

## Common Elements Across Platforms

Regardless of platform, all Class C content should include:

- **Consistent Branding**: Visual and tonal elements that reinforce project identity
- **Cross-Platform References**: Links to related content on other platforms
- **Series Integration**: Clear identification of where content fits in publication streams
- **Lexicon References**: Links to relevant lexicon entries
- **Version Tracking**: Invisible metadata for internal reference
- **Backup Storage**: Complete copy in Dropbox with consistent naming

## Substack-Specific Template

### Filename Convention
```
YYYY-MM-DD-[day]-[shortened-title].md
```
Example: `2025-04-04-friday-library-renovation.md`

### Storage Location
```
/content/[day]/[filename].md
```
Example: `/content/friday/2025-04-04-friday-library-renovation.md`

### URL Pattern
```
[day]-[shortened-title]
```
Example: `friday-library-renovation`

### Content Structure

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Title]</title>
    <!-- Internal reference - not displayed on Substack -->
    <!-- Version: 1.0 -->
    <!-- Source: /research/drafts/[source-document].md -->
</head>
<body>

<!-- Header Section -->
<div class="header-image">
    <!-- This will be replaced by actual header image on Substack -->
    <!-- Use standardized header for content stream -->
</div>

<h1>[Title]</h1>
<p class="subtitle">[Subtitle]</p>

<!-- Introduction Section -->
<p class="intro">[Engaging introduction paragraph that hooks the reader]</p>

<!-- Main Content Section -->
<!-- For Monday Content (Dominative Christianism) -->
<h2>[Section Heading]</h2>
<p>[Content paragraph with <a href="/p/lexicon-term"><i>lexicon term</i></a> references]</p>

<blockquote>
    [Pull quote highlighting a key insight]
</blockquote>

<h2>[Section Heading]</h2>
<p>[Content paragraph]</p>

<h3>[Subsection Heading]</h3>
<p>[Content paragraph]</p>

<!-- For Tuesday Content (Personal Essays) -->
<p class="memory"><em>[Personal memory or anecdote in italics]</em></p>

<p>[Reflection paragraph connecting personal experience to broader theme]</p>

<img src="[image-url]" alt="[Description of personal image]" />
<p class="caption">[Image caption]</p>

<!-- For Wednesday Content (Theological Series) -->
<h2>[Theological Question]</h2>
<p>[Exploration of theological concept with <a href="/p/lexicon-term"><i>lexicon term</i></a> references]</p>

<h3>Biblical Connections</h3>
<p>[Analysis of relevant biblical passages]</p>

<!-- For Thursday Content (Historical Essays) -->
<div class="timeline">
    <div class="timeline-item">
        <h4>[Date]</h4>
        <p>[Historical event description]</p>
    </div>
    <!-- Additional timeline items -->
</div>

<h2>[Historical Analysis Heading]</h2>
<p>[Analysis connecting historical events to contemporary implications]</p>

<!-- For Friday Content (Satirical Pieces) -->
<div class="official-header">
    <h2>DIVINE REPUBLIC OF AMERICA</h2>
    <h3>[Official-Looking Subtitle]</h3>
    <p class="official-document">[Formal-sounding organizational descriptor]</p>
</div>

<p class="proclamation">[Satirical proclamation in formal language]</p>

<div class="committee-signatures">
    <p>Approved by the Committee for [Satirical Committee Name]</p>
    <!-- Additional committee details -->
</div>

<!-- For Saturday Content (Weekend Wisdom) -->
<div class="wisdom-box">
    <h3>Key Takeaway</h3>
    <p>[Simple, accessible summary of the week's core insight]</p>
</div>

<h2>Why This Matters</h2>
<p>[Accessible explanation connecting to everyday experience]</p>

<div class="practice-box">
    <h3>Try This</h3>
    <ol>
        <li>[Simple practice or application step]</li>
        <li>[Simple practice or application step]</li>
        <li>[Simple practice or application step]</li>
    </ol>
</div>

<!-- Conclusion Section -->
<h2>Conclusion</h2>
<p>[Concluding thoughts that circle back to introduction]</p>

<!-- Call to Action Section -->
<p class="cta">[Invitation to engage further, tailored to content type]</p>

<!-- Terms Glossary (if needed) -->
<hr>
<h3>Key Terms</h3>
<p><strong>[Term]</strong>: [Brief definition]. <a href="/p/lexicon-[term]">Full entry →</a></p>
<p><strong>[Term]</strong>: [Brief definition]. <a href="/p/lexicon-[term]">Full entry →</a></p>
<hr>

<!-- Cross-References Section -->
<div class="related-content">
    <h3>Related Content</h3>
    <ul>
        <li><a href="[url]">[Related content title]</a></li>
        <li><a href="[url]">[Related content title]</a></li>
    </ul>
</div>

</body>
</html>
```

### HTML Styling Elements
For Substack posts, use these HTML enhancements:

```html
<!-- Pull Quotes -->
<blockquote class="pullquote">
    [Compelling quote from the text]
</blockquote>

<!-- Section Dividers -->
<hr class="section-divider">

<!-- Highlighted Boxes -->
<div class="highlight-box">
    <h4>[Box Title]</h4>
    <p>[Important concept or takeaway]</p>
</div>

<!-- Image with Caption -->
<figure>
    <img src="[image-url]" alt="[Image description]">
    <figcaption>[Caption text]</figcaption>
</figure>

<!-- Two-Column Layout (for certain sections) -->
<div class="two-column">
    <div class="column">
        <h4>[Left Column Heading]</h4>
        <p>[Left column content]</p>
    </div>
    <div class="column">
        <h4>[Right Column Heading]</h4>
        <p>[Right column content]</p>
    </div>
</div>
```

### Lexicon Integration

Always format lexicon references consistently:
```html
<a href="/p/lexicon-[term]"><i>[Term]</i></a>
```

Example:
```html
Understanding <a href="/p/lexicon-dominative-christianism"><i>Dominative Christianism</i></a> requires examining how it manifests <a href="/p/lexicon-primitive-biblicism"><i>Primitive Biblicism</i></a> in its approach to scripture.
```

## EPUB-Specific Template (Scrivener Format)

### Folder Structure in Scrivener
```
/Manuscript
  /Front Matter
    /Title Page
    /Copyright
    /Dedication
    /Table of Contents
  /[Section 1]
    /Chapter 1
    /Chapter 2
  /[Section 2]
    /Chapter 3
    /Chapter 4
  /Back Matter
    /Appendix
    /Glossary
    /References
```

### Chapter Structure

```markdown
# [Chapter Title]

## [Chapter Subtitle]

[Opening paragraph that establishes the chapter's focus]

### [Section Heading]

[Content paragraphs with *formatted terms* that will be included in the glossary]

> [Block quote for emphasis]

#### [Subsection Heading]

[Content paragraphs]

**[Key Concept]**: [Brief explanation of concept]

### [Section Heading]

[Content paragraphs]

---

**Note**: [Special note or callout]

### [Section Heading]

[Content paragraphs]

### Summary

[Brief summary of the chapter's key points]

### For Further Reading

- [Reference 1]
- [Reference 2]
- [Reference 3]

```

### Scrivener Formatting Tips
- Use Scrivener's formatting presets consistently
- Apply style sheets for consistent typography
- Use compile settings to generate proper EPUB structure
- Include internal hyperlinks to glossary terms
- Set up proper front and back matter
- Configure metadata correctly in Scrivener

## YouTube Script Template (Descript Format)

### File Naming
```
YYYY-MM-DD-video-[shortened-title].descript
```

### Script Structure

```
[TITLE CARD]
"[Video Title]"
Duration: 3.0s

[INTRO]
"[Engaging hook line that captures attention]"
Duration: 5.0s

[HOST ON SCREEN]
"[Introduction to topic that frames the issue]"
Duration: 15.0s

[VISUAL: Brief description of visual]
"[Content explaining the visual with exact timing]"
Duration: 8.0s

[TEXT OVERLAY: Key concept definition]
"[Narration that elaborates on the concept]"
Duration: 10.0s

[VISUAL: Chart or diagram]
"[Explanation of what the visual represents]"
Duration: 12.0s

[HOST ON SCREEN]
"[Development of main idea with emphasis on key points]"
Duration: 20.0s

[VISUAL: Supporting evidence or example]
"[Narration connecting visual to main argument]"
Duration: 15.0s

[TEXT OVERLAY: Counterpoint]
"[Addressing potential objections or alternative viewpoints]"
Duration: 12.0s

[HOST ON SCREEN]
"[Resolution bringing together main arguments]"
Duration: 18.0s

[CONCLUSION]
"[Clear takeaway and call to action]"
Duration: 10.0s

[END CARD]
"Follow for more theological analysis
Subscribe to our newsletter at [website]"
Duration: 5.0s
```

### Descript Formatting Notes
- Include precise timing for each segment
- Mark visual transition points clearly
- Note text overlays and graphics
- Include camera direction notes
- Mark emphasis points for vocal delivery
- Include post-production notes for editors

## Backup and Storage

### Dropbox Backup Structure
```
/content/[platform]/[content_type]/[YYYY-MM-DD]-[title].[extension]
```

Examples:
- `/content/substack/friday/2025-04-04-library-renovation.html`
- `/content/epub/dominative-christianism/chapter-2-theological-framework.md`
- `/content/youtube/theological-primers/2025-04-04-primitive-biblicism.descript`

### Version Tracking
For platform content that may undergo revisions:
- Include invisible metadata with version number
- Store each major version in Dropbox
- Use consistent version numbering (v1.0, v1.1, v2.0)
- Maintain changelog for substantive changes

## Creation Process

### 1. Initial Draft with Claude
- Use artifact-based approach in Claude
- Specify Class C format for the specific platform
- Include all platform-specific elements
- Request proper formatting and structure

### 2. Platform Tool Refinement
- For Substack: Refine in VSCode with HTML preview
- For EPUB: Import to Scrivener and apply styling
- For YouTube: Import to Descript and adjust timing

### 3. Visual Enhancement
- Add appropriate header images
- Include diagrams and illustrations
- Apply consistent visual styling
- Optimize images for platform requirements

### 4. Platform-Specific Optimization
- For Substack: SEO optimization, preview text
- For EPUB: Navigation, table of contents, metadata
- For YouTube: Thumbnail creation, description, tags

### 5. Publication
- Publish on appropriate platform
- Schedule according to content calendar
- Coordinate cross-platform promotion
- Update tracking systems with publication status

### 6. Backup
- Save complete version to Dropbox
- Include publication URL in metadata
- Record analytics baseline
- Update relevant Class A tracking tools

## Conversion Guidelines

### From Class B (Research Material)
When converting Class B content to Class C:
1. Extract core insights from research material
2. Restructure for platform-specific format
3. Add engaging elements appropriate to platform
4. Simplify language while maintaining depth
5. Add visual components and styling
6. Include proper cross-references and lexicon links

## Version History

v1.0 - 2025-04-04 - Initial template for Class C content
