# 20250415174000_content_format_index.md
[Store as: #creation/tool/index/content_format_index v7.0]
[Related: #creation/tool/index/comprehensive_taxonomy v6.0, #creation/tool/index/tana_tagging_reference]

---
title: "Content Format Index"
date: 2025-04-15
version: 7.0
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
  - weekend_wisdom
---

# Content Format Index v7.0

This document catalogues all content formats used in the Dominative Christianism and Providential Identitarianism Project, including artifact templates, formatting standards, and implementation guidelines.

## Content Type Overview

### Content Type-Specific Formatting

| Day | Content Type | Icon | URL Pattern | Word Count | Key Feature |
|-----|-------------|------|-------------|------------|-------------|
| Monday (Dominative) | Book Chapter | 📊 | `dominative-[topic]` | 4000-6000 | Academic analysis with lexicon integration |
| Monday (Providential) | Book Chapter | 📈 | `providential-[topic]` | 4000-6000 | Academic analysis with lexicon integration |
| Tuesday | Personal Essay | 🌱 | `rooted-[topic]` | 1500-2000 | Personal narrative with metaphors |
| Wednesday | Theological Essay | 🧭 | `commonlife-[topic]` | 2000-3000 | Theological concept with practical application |
| Thursday | Historical Essay | 🔍 | `untold-[topic]` | 2000-3000 | Historical analysis with personal confession |
| Friday | Satirical Piece | 🏛️ | `republic-[topic]` | 800-1200 | Governmental proclamation format |
| Saturday | Practices For... | 🛠️ | `practices-[topic]` | 2000-2500 | Specific steps with reflection questions |
| Saturday | Simply Said | 🎯 | `simply-[topic]` | 1000-1500 | Youth-oriented with relatable examples |
| Sunday | Sermons/Homilies | 🕊️ | `sermon-[passage]` | 2500-3500 | Triple voice structure with counter-imperial focus |
| Lexicon | Term Definition | 📘 | `lexicon-[term]` | 600-1200 | HTML structure with consistent formatting |
| Weekly Themes | Integration Guide | 🧩 | `theme-[week]-[topic]` | 1500-2000 | Cross-content integration framework |

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
- **Saturday Practices**: `practices-[topic]` (e.g., `practices-truthfulness`)
- **Saturday Simply Said**: `simply-[topic]` (e.g., `simply-truth`)
- **Sunday Sermon**: `sermon-[passage]` (e.g., `sermon-mark-1-1-15`)
- **Lexicon Entries**: `lexicon-[term]` (e.g., `lexicon-dominative-christianism`)
- **Weekly Themes**: `theme-[week]-[topic]` (e.g., `theme-01-introduction`)

#### Cross-Reference Implementation
- **Inline Lexicon References**: Format as `[*term*](/p/lexicon-term)` (italicized with link)
- **End-of-Article Glossary**: Use standardized HTML format for term definitions with links
- **Related Content Section**: Include standardized section at end of each artifact with related content links
- **Sermon Connections**: Include standardized reference to related sermon content
- **Weekly Theme Reference**: Include subtle reference to weekly theme in each content piece
- **Series Navigation**: Include "Previous" and "Next" links for content in sequential series

### Content Type-Specific Artifact Templates

#### Saturday: Weekend Wisdom (Practices For...)

```markdown
---
title: "Practices for [Virtue/Concept]"
subtitle: "[Subtitle]"
image: "[HEADER_IMAGE_URL]"
---

![Header Image: Practices for [Virtue/Concept]](header-image-url)

# 🛠️ Practices for [Virtue/Concept]

[Opening paragraph connecting to the weekly theme and previous content. This should establish how this virtue/concept has been explored throughout the week and why practical application matters.]

[Second paragraph establishing theological foundation for these practices. This should ground the practical disciplines in theological understanding.]

## 1. [Practice Name]

**The Practice**: [One-sentence description of the practice.]

**Steps**:
- [Step 1 with specific instruction]
- [Step 2 with specific instruction]
- [Step 3 with specific instruction]
- [Step 4 with specific instruction]
- [Step 5 with specific instruction]

**Reflection Questions**:
- [Question 1 for deeper engagement with the practice]
- [Question 2 for deeper engagement with the practice]
- [Question 3 for deeper engagement with the practice]

**Biblical Connection**: "[Relevant scripture verse]" ([Reference])

## 2. [Practice Name]

**The Practice**: [One-sentence description of the practice.]

**Steps**:
- [Step 1 with specific instruction]
- [Step 2 with specific instruction]
- [Step 3 with specific instruction]
- [Step 4 with specific instruction]
- [Step 5 with specific instruction]

**Reflection Questions**:
- [Question 1 for deeper engagement with the practice]
- [Question 2 for deeper engagement with the practice]
- [Question 3 for deeper engagement with the practice]

**Biblical Connection**: "[Relevant scripture verse]" ([Reference])

## 3. [Practice Name]

**The Practice**: [One-sentence description of the practice.]

**Steps**:
- [Step 1 with specific instruction]
- [Step 2 with specific instruction]
- [Step 3 with specific instruction]
- [Step 4 with specific instruction]
- [Step 5 with specific instruction]

**Reflection Questions**:
- [Question 1 for deeper engagement with the practice]
- [Question 2 for deeper engagement with the practice]
- [Question 3 for deeper engagement with the practice]

**Biblical Connection**: "[Relevant scripture verse]" ([Reference])

## 4. [Practice Name]

**The Practice**: [One-sentence description of the practice.]

**Steps**:
- [Step 1 with specific instruction]
- [Step 2 with specific instruction]
- [Step 3 with specific instruction]
- [Step 4 with specific instruction]
- [Step 5 with specific instruction]

**Reflection Questions**:
- [Question 1 for deeper engagement with the practice]
- [Question 2 for deeper engagement with the practice]
- [Question 3 for deeper engagement with the practice]

**Biblical Connection**: "[Relevant scripture verse]" ([Reference])

## 5. [Practice Name]

**The Practice**: [One-sentence description of the practice.]

**Steps**:
- [Step 1 with specific instruction]
- [Step 2 with specific instruction]
- [Step 3 with specific instruction]
- [Step 4 with specific instruction]
- [Step 5 with specific instruction]

**Reflection Questions**:
- [Question 1 for deeper engagement with the practice]
- [Question 2 for deeper engagement with the practice]
- [Question 3 for deeper engagement with the practice]

**Biblical Connection**: "[Relevant scripture verse]" ([Reference])

## Deeper Practice: [Advanced Practice Name]

For those seeking deeper formation in [virtue/concept], consider these contemplative practices:

**[Advanced Practice 1]**:
[Description of more advanced practice with guidance for implementation.]

**[Advanced Practice 2]**:
[Description of more advanced practice with guidance for implementation.]

**[Advanced Practice 3]**:
[Description of more advanced practice with guidance for implementation.]

## Prayer for [Virtue/Concept]

_[Opening address],_

_[First stanza of prayer]_
_[Second stanza of prayer]_
_[Third stanza of prayer]_
_[Fourth stanza of prayer]_

_Amen._

## This Week's Challenge

Choose one practice from this list to implement daily this week. [Specific instructions for documentation or reflection on the practice]. [Guidance for how to integrate insights from practice.]

Remember, [virtue/concept] isn't about [common misconception]. It's about [theological truth]. [Final encouragement for implementation].

---

### Related Content

- [Monday: [Title] →](/p/dominative-related-topic)
- [Tuesday: [Title] →](/p/rooted-related-topic)
- [Wednesday: [Title] →](/p/commonlife-related-topic)
- [Thursday: [Title] →](/p/untold-related-topic)
- [Friday: [Title] →](/p/republic-related-topic)
- [Simply Said: [Title] →](/p/simply-related-topic)
- [Sermon: [Title] →](/p/sermon-related-topic)

---
```

#### Saturday: Weekend Wisdom (Simply Said)

```markdown
---
title: "Simply Said: What is [Virtue/Concept] and How Do We Practice It?"
subtitle: "[Subtitle]"
image: "[HEADER_IMAGE_URL]"
---

![Header Image: Simply Said: [Virtue/Concept]](header-image-url)

# 🎯 Simply Said: What is [Virtue/Concept] and How Do We Practice It?

## What is [Virtue/Concept]?

[Opening paragraph using everyday language and relatable examples to introduce the concept. Make this immediately relevant to teenage experience through a question or scenario they would recognize.]

[Second paragraph providing simple definition of the concept, avoiding technical theological language but maintaining theological accuracy. Use analogies and concrete examples.]

[Third paragraph connecting the concept to Jesus's example and teaching. Show how Jesus embodied this virtue/concept in accessible ways.]

## The Two Fake Versions of [Virtue/Concept]

Today, there are two popular but fake versions of [virtue/concept]:

1. **"[Distortion 1 Name]"**: [Description of how this common distortion gets the concept wrong. Use examples relevant to youth experience. Connect to broader cultural patterns when possible.]

2. **"[Distortion 2 Name]"**: [Description of how this alternative distortion also misses the mark. Again, use relevant examples and connect to cultural patterns.]

Both versions miss that real [virtue/concept] [brief explanation of what both distortions miss].

## Practices for [Virtue/Concept]

### 1. **[Practice 1 Name]**
[1-2 sentences describing an accessible practice for youth to implement this virtue/concept. Be specific and actionable. Connect to their lived experience.]

### 2. **[Practice 2 Name]**
[1-2 sentences describing a second accessible practice. Ensure this is distinct from the first and targets a different aspect of the virtue/concept.]

### 3. **[Practice 3 Name]**
[1-2 sentences describing a third accessible practice. Consider making this one applicable to digital/online contexts.]

### 4. **[Practice 4 Name]**
[1-2 sentences describing a fourth accessible practice. Consider making this one relationship-focused.]

### 5. **[Practice 5 Name]**
[1-2 sentences describing a fifth accessible practice. Consider making this one community or group-oriented.]

### 6. **[Practice 6 Name]**
[1-2 sentences describing a sixth accessible practice. Consider making this one a reflective or contemplative practice adapted for youth.]

## Why This Matters

[First paragraph connecting this virtue/concept to Jesus's kingdom vision. Show how Jesus offered an alternative to both distortions and why this matters for discipleship.]

[Second paragraph explaining the personal benefits of practicing this virtue/concept. Focus on authentic human flourishing rather than mere moralism.]

[Final paragraph offering encouragement and inspiration. Acknowledge difficulties while emphasizing possibility of growth and transformation.]

## Questions for Reflection

1. [Question focusing on personal experience with this virtue/concept]
2. [Question examining cultural messages about this virtue/concept]
3. [Question exploring obstacles to practicing this virtue/concept]
4. [Question inviting practical application]

---

### Related Content

- [Monday: [Title] →](/p/dominative-related-topic)
- [Tuesday: [Title] →](/p/rooted-related-topic)
- [Wednesday: [Title] →](/p/commonlife-related-topic)
- [Thursday: [Title] →](/p/untold-related-topic)
- [Friday: [Title] →](/p/republic-related-topic)
- [Practices: [Title] →](/p/practices-related-topic)
- [Sermon: [Title] →](/p/sermon-related-topic)

---
```

#### Sunday: Sermon/Homily

```markdown
---
title: "[Passage]: [Title]"
subtitle: "[Subtitle]"
image: "[HEADER_IMAGE_URL]"
---

![Header Image: [Passage]](header-image-url)

# 🕊️ [Passage]: [Title]

[Opening paragraph introducing the passage and its significance. This should establish the context of the passage within Mark's gospel and within the counter-imperial narrative.]

[Second paragraph connecting this passage to the weekly theme and the theological mutations being addressed. This should provide a bridge between the biblical text and contemporary application.]

## Mark Says

[First paragraph explicating what Mark is saying in this passage. Focus on the counter-imperial dimensions and how Jesus challenges the dominant systems of his day.]

[Second paragraph digging deeper into the historical and cultural context. Provide insights that help readers understand the radical nature of Jesus's message in his time.]

[Third paragraph connecting this passage to broader themes in Mark's gospel. Show how this passage fits into Mark's overall narrative and theological vision.]

> "Relevant verse or verses from the passage that capture the core message."

[Fourth paragraph drawing out the theological implications of this passage. What does this tell us about God, humanity, and the kingdom of God?]

## Dominative Christianism Says

[First paragraph explaining how this passage is typically interpreted within Dominative Christianism. Focus on how the theological mutations distort the counter-imperial message.]

[Second paragraph identifying specific theological mutations evident in this interpretation. Connect to the seven mutations framework.]

[Third paragraph providing concrete examples of how this distorted interpretation manifests in contemporary religious and political life. Be specific but not partisan.]

[Fourth paragraph analyzing the consequences of this distorted interpretation for Christian witness and formation. What is lost when the text is read this way?]

## Providential Identitarianism Says

[First paragraph explaining how this passage is typically interpreted within Providential Identitarianism. Focus on how the theological mutations distort the counter-imperial message.]

[Second paragraph identifying specific theological mutations evident in this interpretation. Connect to the seven mutations framework.]

[Third paragraph providing concrete examples of how this distorted interpretation manifests in contemporary religious and political life. Be specific but not partisan.]

[Fourth paragraph analyzing the consequences of this distorted interpretation for Christian witness and formation. What is lost when the text is read this way?]

## Participatory Freedom Says

[First paragraph presenting the participatory freedom theological alternative. Show how this reading recovers the counter-imperial message of the text.]

[Second paragraph exploring the implications of this reading for contemporary Christian formation. How does this reshape our understanding of discipleship?]

[Third paragraph connecting this reading to constructive theological alternatives to the mutations. Show how this offers a way beyond both Dominative Christianism and Providential Identitarianism.]

[Fourth paragraph offering concrete practices that emerge from this reading. How might this passage shape our common life?]

## Conclusion

[First paragraph summarizing the key insights from this analysis. Highlight the core message of the passage as understood through a counter-imperial lens.]

[Second paragraph connecting these insights to the weekly theme and the broader project. Show how this passage contributes to our understanding of participatory freedom.]

[Final paragraph offering a blessing or commission that sends readers forth to embody the message of this passage in their daily lives.]

---

### Key Terms

**[Term 1]**: Brief definition. [Full entry →](/p/lexicon-term-1)

**[Term 2]**: Brief definition. [Full entry →](/p/lexicon-term-2)

**[Term 3]**: Brief definition. [Full entry →](/p/lexicon-term-3)

---

### Related Content

- [Monday: [Title] →](/p/dominative-related-topic)
- [Monday: [Title] →](/p/providential-related-topic)
- [Tuesday: [Title] →](/p/rooted-related-topic)
- [Wednesday: [Title] →](/p/commonlife-related-topic)
- [Thursday: [Title] →](/p/untold-related-topic)
- [Friday: [Title] →](/p/republic-related-topic)
- [Practices: [Title] →](/p/practices-related-topic)
- [Simply Said: [Title] →](/p/simply-related-topic)
- [Weekly Theme: [Title] →](/p/theme-week-topic)

---
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

#### Example 1: Inline Icon Reference for Saturday Content

**Artifact Code for Practices:**
```markdown
This week's exploration of truthfulness culminates in our 🛠️ [Practices for Truthfulness](/p/practices-truthfulness) guide, which provides concrete spiritual disciplines for cultivating truth in a post-truth age.
```

**Rendered Output:**
This week's exploration of truthfulness culminates in our 🛠️ Practices for Truthfulness guide, which provides concrete spiritual disciplines for cultivating truth in a post-truth age.

**Artifact Code for Simply Said:**
```markdown
For our younger readers, we've created 🎯 [Simply Said: What is Truth and How Do We Practice It?](/p/simply-truth), which translates these concepts into accessible language and practices for teens.
```

**Rendered Output:**
For our younger readers, we've created 🎯 Simply Said: What is Truth and How Do We Practice It?, which translates these concepts into accessible language and practices for teens.

#### Example 2: End-of-Article Related Content with Icons

**Artifact Code:**
```markdown
---

### Related Content

- 📊 [The Crisis of Primitive Biblicism →](/p/dominative-primitive-biblicism)
- 🌱 [Amending Soil: Healing Old Wounds →](/p/rooted-amending-soil)
- 🧭 [Bullshit: Truth as Foundation →](/p/commonlife-bullshit)
- 🔍 [The Textbook That Lied →](/p/untold-textbook-lied)
- 🏛️ [Library Renovation Committee Announcement →](/p/republic-library-renovation)
- 🛠️ [Practices for Truthfulness →](/p/practices-truthfulness)
- 🎯 [Simply Said: What is Truth? →](/p/simply-truth)
- 🕊️ [Mark 1:1-15: The Beginning of the Gospel →](/p/sermon-mark-1-1-15)

---
```

**Rendered Output:**
### Related Content

- 📊 The Crisis of Primitive Biblicism →
- 🌱 Amending Soil: Healing Old Wounds →
- 🧭 Bullshit: Truth as Foundation →
- 🔍 The Textbook That Lied →
- 🏛️ Library Renovation Committee Announcement →
- 🛠️ Practices for Truthfulness →
- 🎯 Simply Said: What is Truth? →
- 🕊️ Mark 1:1-15: The Beginning of the Gospel →

## Weekend Wisdom Content

### Weekend Wisdom: Practices Format

The Weekend Wisdom: Practices artifacts follow the distinct format designed for adult audience spiritual formation:

- **Icon**: 🛠️ (Tools) representing practical spiritual disciplines
- **Purpose**: Providing concrete spiritual practices for adult audience
- **Voice**: Instructional, practical, maintaining theological depth
- **Structure**: Clear practice-step-reflection format
- **Length**: 2000-2500 words
- **Key Feature**: Specific, actionable steps for implementing theological concepts
- **URL Pattern**: `practices-[virtue/concept]`
- **Publication Time**: Saturday morning
- **Email Format**: Standalone email with consistent visual identity

### Weekend Wisdom: Simply Said Format

The Weekend Wisdom: Simply Said artifacts follow a distinct format designed for youth audience (13-18):

- **Icon**: 🎯 (Target) representing simplified, direct communication
- **Purpose**: Translating complex theological concepts for youth
- **Voice**: Conversational, relatable, example-rich, free of technical jargon
- **Structure**: Question-answer format with practical applications
- **Length**: 1000-1500 words
- **Key Feature**: Examples relevant to youth experience and digital contexts
- **URL Pattern**: `simply-[topic]`
- **Publication Time**: Saturday afternoon
- **Email Format**: Standalone email with youth-oriented visual identity

### Sunday: Sermon/Homily Format

The sermon artifacts follow the triple voice structure designed to present Jesus's counter-imperial message:

- **Icon**: 🕊️ (Dove) representing the Spirit's guidance in scripture interpretation
- **Purpose**: Presenting Mark's counter-imperial message and contrasting theological mutations
- **Voice**: Exegetical, analytical, constructive
- **Structure**: Triple voice format (Mark/Dominative/Providential) with resolution
- **Length**: 2500-3500 words
- **Key Feature**: Counter-imperial exegesis with application to both mutations
- **URL Pattern**: `sermon-[passage]`
- **Publication Time**: Sunday morning
- **Email Format**: Standalone email with scripture-centered visual identity

## Project Integration Recommendations

1. **Weekly Theme Coordination**: All content for a given week should connect to the designated weekly theme
2. **Triple Voice Integration**: All content should engage with Mark's counter-imperial message and both theological mutations
3. **Lexicon Development**: Create lexicon entries in advance of their use in main content streams
4. **Cross-Stream Reference**: Each content piece should reference related content from other streams
5. **Visual Identity Consistency**: Maintain consistent visual identity across all content types
6. **URL Pattern Adherence**: Follow established URL patterns for all content types
7. **Icon Usage Consistency**: Use appropriate icons for each content type in all references

## Version History

v7.0 - 2025-04-15 - Added Weekend Wisdom content formats (Practices and Simply Said) and updated iconography system
v6.0 - 2025-04-03 - Updated with comprehensive artifact-based publication workflow specifications
v5.0 - 2025-04-02 - Added lexicon system structure and implementation details
v4.0 - 2025-03-31 - Expanded with dual mutation framework integration
v3.0 - 2025-03-15 - Enhanced with sermon integration framework
v2.0 - 2025-03-01 - Updated with expanded content types and formatting
v1.0 - 2025-02-01 - Initial format index creation