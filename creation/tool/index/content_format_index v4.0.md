# 20250402160200_content_format_index.md
[Store as: #creation/tool/index/content_format_index v4.0]
[Related: #creation/tool/index/comprehensive_taxonomy, #creation/tool/index/tana_tagging_reference]

---
title: "Content Format Index"
date: 2025-04-02
version: 4.0
type: reference
status: active
tags:
  - content_management
  - reference
  - project_organization
  - providential_identitarianism
  - maga_christianism
  - sermon_integration
  - lexicon
---

# Content Format Index v4.0

This document catalogues all content formats used in the MAGA Christianism and Providential Identitarianism Project, including prompt templates, file paths, and usage instructions.

## Lexicon Content

### Main Glossary Page
- **Description:** Central reference page that organizes and indexes all lexicon entries
- **Prompt Template:** `/tools/prompts/main_glossary_page_v1.0.md`
- **Output Location:** `/content/lexicon/main/christianism_lexicon.html`
- **Format:** HTML with consistent styling and organization structure
- **Usage:** Published as a Substack Page and added to site navigation
- **Primary Focus:** Providing organized access to all lexicon entries
- **Organization:** Both categorical and alphabetical with consistent styling

### Primary Concept Entries
- **Description:** Foundational theological concepts that ground the analysis
- **Prompt Template:** `/tools/prompts/lexicon_primary_concept_v1.0.md`
- **Output Location:** `/content/lexicon/primary_concepts/[concept_name].html`
- **Format:** HTML with consistent header, definition, etymology, usage, and significance sections
- **Usage:** Published as Substack Posts in "Lexicon" section (hidden from Home feed)
- **URL Format:** `lexicon-[term]` (e.g., "lexicon-christianism")
- **Word Count:** 600-1000 words
- **Primary Focus:** Establishing clear definitions for core analytical concepts

### Theological Mutation Entries
- **Description:** Entries defining the seven theological mutations and their expressions
- **Prompt Template:** `/tools/prompts/lexicon_theological_mutation_v1.0.md`
- **Output Location:** `/content/lexicon/theological_mutations/[mutation_name].html`
- **Format:** HTML with consistent structure outlining both MAGA and Providential expressions
- **Usage:** Published as Substack Posts in "Lexicon" section (hidden from Home feed)
- **URL Format:** `lexicon-[mutation]` (e.g., "lexicon-primitive-biblicism")
- **Word Count:** 800-1200 words
- **Primary Focus:** Comparing expressions of mutation across both theological formations

### Theological Alternative Entries
- **Description:** Entries defining constructive theological alternatives to mutations
- **Prompt Template:** `/tools/prompts/lexicon_theological_alternative_v1.0.md`
- **Output Location:** `/content/lexicon/theological_alternatives/[alternative_name].html`
- **Format:** HTML with consistent structure presenting orthodox alternatives
- **Usage:** Published as Substack Posts in "Lexicon" section (hidden from Home feed)
- **URL Format:** `lexicon-[alternative]` (e.g., "lexicon-participatory-freedom")
- **Word Count:** 800-1200 words
- **Primary Focus:** Constructive theological vision beyond mutations

### Theological Genealogy Entries
- **Description:** Entries tracing historical development of theological concepts
- **Prompt Template:** `/tools/prompts/lexicon_theological_genealogy_v1.0.md`
- **Output Location:** `/content/lexicon/theological_genealogy/[concept_name].html`
- **Format:** HTML with historical development, key figures, and contemporary relevance
- **Usage:** Published as Substack Posts in "Lexicon" section (hidden from Home feed)
- **URL Format:** `lexicon-[concept]` (e.g., "lexicon-covenant-theology")
- **Word Count:** 800-1200 words
- **Primary Focus:** Historical context for theological concepts

### Contemporary Movement Entries
- **Description:** Entries defining current religious-political phenomena
- **Prompt Template:** `/tools/prompts/lexicon_contemporary_movement_v1.0.md`
- **Output Location:** `/content/lexicon/contemporary_movements/[movement_name].html`
- **Format:** HTML with definition, characteristics, examples, and analysis
- **Usage:** Published as Substack Posts in "Lexicon" section (hidden from Home feed)
- **URL Format:** `lexicon-[movement]` (e.g., "lexicon-christian-nationalism")
- **Word Count:** 800-1200 words
- **Primary Focus:** Analysis of current religious-political formations

## Lexicon Integration Tools

### Inline Reference System
- **Description:** System for referencing lexicon terms within article content
- **Prompt Template:** `/tools/prompts/inline_reference_system_v1.0.md`
- **Output Location:** Integrated into all content streams
- **Format:** Italicized hyperlinks to lexicon entries on first mention
- **Usage:** Seamless connection between content and lexicon
- **Primary Focus:** Providing definitional clarity without disrupting reading experience

### End-of-Article Glossary
- **Description:** Concise definitions with links at the end of articles
- **Prompt Template:** `/tools/prompts/end_of_article_glossary_v1.0.md`
- **Output Location:** Appended to articles with technical terminology
- **Format:** Brief definitions with links to full lexicon entries
- **Usage:** Quick reference for technical terms used in article
- **Primary Focus:** Summarizing key terms for reader convenience

## Sermon Content

### Mark Sermons
- **Description:** Triple voice sermons based on Mark's Gospel that connect the counter-imperial message to modern theological mutations
- **Prompt Template:** `/tools/prompts/mark_sermon_creation_v2.0.md`
- **Output Location:** `/content/sermon/mark/[passage-reference]/[sermon-name].md`
- **Format:** Structured markdown with triple voice framework
- **Usage:** Primary sermon content for weekly delivery and integration with publication streams
- **Word Count:** 2000-2500 words
- **Triple Voice Structure:** Mark Says / MAGA Says / Providential Says / Participatory Freedom Says
- **Primary Mutation Focus:** Rotates through all seven mutations

### Sermon Integration Guides
- **Description:** Detailed guides for integrating sermon content with weekly publication streams
- **Prompt Template:** `/tools/prompts/sermon_integration_guide_v1.0.md`
- **Output Location:** `/content/integration/sermon_integrations/sermon[XX]_integration.md`
- **Format:** Structured markdown with content connections
- **Usage:** Internal guide for content creators to maintain thematic consistency
- **Word Count:** 1000-1500 words
- **Primary Focus:** Content integration and thematic connections

### Sermon Homilies
- **Description:** Concise homilies (5-7 minutes) based on Mark's Gospel
- **Prompt Template:** `/tools/prompts/mark_homily_creation_v1.0.md`
- **Output Location:** `/content/audio/homilies/mark/[passage-reference].md`
- **Format:** Markdown optimized for recording in Descript
- **Usage:** Secondary audio content for podcast episodes and church contexts
- **Word Count:** 750-1000 words
- **Primary Mutation Focus:** Varies by passage, addresses both mutations

## Written Content - MAGA Christianism

### MAGA Christianism Chapters
- **Description:** Full-length theological analysis chapters for the MAGA Christianism book
- **Prompt Template:** `/tools/prompts/maga_chapter_development_v2.0.md`
- **Output Location:** `/content/book/maga_christianism/chapters/[chapter-number]-[chapter-title].md`
- **Format:** Markdown with academic citations and footnotes
- **Usage:** Primary chapters for MAGA Christianism book publication
- **Word Count:** 4000-6000 words
- **Primary Mutation Focus:** Comprehensive analysis of all seven mutations in MAGA context
- **Sermon Connection:** Includes specific connections to relevant Mark passages
- **Lexicon Integration:** References lexicon entries for technical terms

## Written Content - Providential Identitarianism

### Providential Identitarianism Chapters
- **Description:** Full-length theological analysis chapters for the Providential Identitarianism book
- **Prompt Template:** `/tools/prompts/providential_chapter_development_v1.0.md`
- **Output Location:** `/content/book/providential_identitarianism/chapters/[chapter-number]-[chapter-title].md`
- **Format:** Markdown with academic citations and footnotes
- **Usage:** Primary chapters for Providential Identitarianism book publication
- **Word Count:** 4000-6000 words
- **Primary Mutation Focus:** Comprehensive analysis of all seven mutations in Providential context
- **Sermon Connection:** Includes specific connections to relevant Mark passages
- **Lexicon Integration:** References lexicon entries for technical terms

## Written Content - Shared Resources

### Common Life Politics Essays
- **Description:** Weekly theological essays connecting to both mutations and Mark's theology
- **Prompt Template:** `/tools/prompts/common_life_politics_essay_v2.0.md`
- **Output Location:** `/content/essay/common_life_politics/[essay-title].md`
- **Format:** Structured theological essay with practical application
- **Usage:** Wednesday publication on Substack
- **Word Count:** 2000-3000 words
- **Primary Focus:** Constructive theological alternatives
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Sermon Connection:** Integrates with weekly sermon theme
- **Lexicon Integration:** References lexicon entries for technical terms

### Personal Essays (Rooted & Reaching)
- **Description:** Personal narratives connecting spiritual formation to weekly themes
- **Prompt Template:** `/tools/prompts/rooted_reaching_essay_v2.0.md`
- **Output Location:** `/content/personal_essay/phase[X]_[category]/[essay-title].md`
- **Format:** Personal narrative with theological reflection
- **Usage:** Tuesday publication on Substack
- **Word Count:** 1500-2000 words
- **Primary Focus:** Personal application of theological concepts
- **Sermon Connection:** Subtle connection to weekly sermon theme
- **Lexicon Integration:** References lexicon entries when appropriate

### Historical Essays (Untold America)
- **Description:** Historical analyses examining American history through theological lens
- **Prompt Template:** `/tools/prompts/untold_america_essay_v2.0.md`
- **Output Location:** `/content/historical/phase[X]_[category]/[essay-title].md`
- **Format:** Historical narrative with theological analysis
- **Usage:** Thursday publication on Substack
- **Word Count:** 2000-3000 words
- **Primary Focus:** Historical dimensions of theological mutations
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Sermon Connection:** Historical context for weekly sermon theme
- **Lexicon Integration:** References lexicon entries for technical terms

### Satirical Pieces (Divine Republic)
- **Description:** Satirical content exposing contradictions in both theological mutations
- **Prompt Template:** `/tools/prompts/divine_republic_satire_v2.0.md`
- **Output Location:** `/content/satire/phase[X]_[category]/[piece-title].md`
- **Format:** Mock governmental proclamations with consistent visual elements
- **Usage:** Friday publication on Substack
- **Word Count:** 800-1200 words
- **Primary Focus:** Cultural commentary through satire
- **Mutations Addressed:** Alternates focus between both mutations
- **Sermon Connection:** Satirical application of weekly sermon theme
- **Lexicon Integration:** Satirical references to defined concepts

## Integration Content

### Weekly Theme Guides
- **Description:** Comprehensive guides for weekly thematic integration across content streams
- **Prompt Template:** `/tools/prompts/weekly_theme_guide_v1.0.md`
- **Output Location:** `/content/integration/weekly_themes/week[XX]_[theme-name].md`
- **Format:** Structured markdown with thematic connections
- **Usage:** Internal guide for content creators
- **Word Count:** 1000-1500 words
- **Primary Focus:** Thematic integration across content streams
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Sermon Connection:** Central integration with weekly sermon
- **Lexicon Integration:** Connects weekly theme to lexicon entries

### Mutation Comparison Essays
- **Description:** Comparative analyses of both mutations' expressions of theological distortions
- **Prompt Template:** `/tools/prompts/mutation_comparison_essay_v1.0.md`
- **Output Location:** `/content/integration/mutation_comparisons/comparison[XX]_[topic].md`
- **Format:** Structured comparison with theological analysis
- **Usage:** Reference material for content creators
- **Word Count:** 2000-3000 words
- **Primary Focus:** Comparative theological analysis
- **Mutations Addressed:** Side-by-side analysis of both mutations
- **Sermon Connection:** Connection to relevant Mark passages
- **Lexicon Integration:** References lexicon entries for technical terms

## Visual Content

### Teaching Slides
- **Description:** Presentation slides for classes and workshops
- **Prompt Template:** `/tools/prompts/teaching_slides_creation_v2.0.md`
- **Output Location:** `/content/presentations/[topic]-slides.md`
- **Format:** Markdown optimized for conversion to PowerPoint/Keynote
- **Usage:** Workshops, classes, and speaking engagements
- **Slide Count:** 20-30 slides per presentation
- **Primary Focus:** Educational visualization of theological concepts
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Sermon Connection:** Can be developed from sermon content
- **Lexicon Integration:** Incorporates definitions from lexicon

### Infographics
- **Description:** Single-image visual explanations of complex concepts
- **Prompt Template:** `/tools/prompts/infographic_design_v2.0.md`
- **Output Location:** `/content/visuals/infographics/[concept].md`
- **Format:** Design brief with text content and layout suggestions
- **Usage:** Social media sharing and website resources
- **Word Count:** 100-200 words of text content
- **Primary Focus:** Visual explanation of theological concepts
- **Mutations Addressed:** Can address either or both mutations
- **Sermon Connection:** Often derived from sermon illustrations
- **Lexicon Integration:** Visual representation of lexicon concepts

## Video Content

### Theological Primers
- **Description:** Short (90-second) videos explaining key theological concepts
- **Prompt Template:** `/tools/prompts/theological_primer_video_v2.0.md`
- **Output Location:** `/content/video/theological_primers/[concept].md`
- **Format:** Video script with visual directions
- **Usage:** Social media, YouTube, and website resources
- **Word Count:** 150-200 words
- **Primary Focus:** Clear explanation of single theological concept
- **Mutations Addressed:** Can address either or both mutations
- **Sermon Connection:** Often derived from sermon content
- **Lexicon Integration:** Video visualization of lexicon entries

### Mark Insights
- **Description:** Short videos explaining Mark's counter-imperial theology
- **Prompt Template:** `/tools/prompts/mark_insights_video_v1.0.md`
- **Output Location:** `/content/video/mark_insights/[passage-insight].md`
- **Format:** Video script with visual directions
- **Usage:** Social media, YouTube, and website resources
- **Word Count:** 150-200 words
- **Primary Focus:** Mark's counter-imperial theology
- **Mutations Addressed:** Contrasts with both mutations
- **Sermon Connection:** Directly derived from sermon content
- **Lexicon Integration:** References relevant lexicon concepts

### Triple Voice Videos
- **Description:** Short videos presenting the triple voice structure
- **Prompt Template:** `/tools/prompts/triple_voice_video_v1.0.md`
- **Output Location:** `/content/video/triple_voice/[passage-topic].md`
- **Format:** Video script with visual directions for three distinct voices
- **Usage:** Social media, YouTube, and website resources
- **Word Count:** 250-300 words
- **Primary Focus:** Contrast between three theological voices
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Sermon Connection:** Directly derived from sermon content
- **Lexicon Integration:** Uses definitions from lexicon

## Audio Content

### Podcast Episodes
- **Description:** Audio discussions of theological topics related to both mutations
- **Prompt Template:** `/tools/prompts/podcast_episode_v2.0.md`
- **Output Location:** `/content/audio/podcast/[episode-title].md`
- **Format:** Podcast script with segment structure
- **Usage:** Weekly audio podcast
- **Duration:** 30-45 minutes
- **Primary Focus:** Theological analysis and discussion
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Sermon Connection:** Often expands on sermon themes
- **Lexicon Integration:** References lexicon entries with audio explanations

### Atomic Essays
- **Description:** Ultra-short (90-second) inspirational messages that address both theological mutations
- **Prompt Template:** `/tools/prompts/atomic_essay_creation_v2.0.md`
- **Output Location:** `/content/social/atomic/[key-concept].md`
- **Format:** Markdown optimized for social media video recording
- **Usage:** Facebook/Instagram Reels, YouTube Shorts, TikTok
- **Word Count:** Under 150 words
- **Primary Focus:** Pastoral encouragement with subtle theological subversion
- **Mutations Addressed:** Can address either or both mutations
- **Sermon Connection:** Often derived from sermon applications
- **Lexicon Integration:** Concise references to lexicon concepts

## E-Book Compilations

### MAGA Christianism Book
- **Description:** Compiled book of MAGA Christianism chapters with enhanced formatting
- **Prompt Template:** `/tools/prompts/maga_book_compilation_v2.0.md`
- **Output Location:** `/content/ebook/maga_christianism/[part-name].md`
- **Format:** Structured markdown for e-book conversion
- **Usage:** E-book publication and print-on-demand
- **Structure:** 6 parts with 3-4 chapters each
- **Primary Focus:** Comprehensive analysis of MAGA Christianism
- **Sermon Connection:** Includes sermon applications and illustrations
- **Lexicon Integration:** Includes glossary of key terms from lexicon

### Providential Identitarianism Book
- **Description:** Compiled book of Providential Identitarianism chapters with enhanced formatting
- **Prompt Template:** `/tools/prompts/providential_book_compilation_v1.0.md`
- **Output Location:** `/content/ebook/providential_identitarianism/[part-name].md`
- **Format:** Structured markdown for e-book conversion
- **Usage:** E-book publication and print-on-demand
- **Structure:** 6 parts with 3-4 chapters each
- **Primary Focus:** Comprehensive analysis of Providential Identitarianism
- **Sermon Connection:** Includes sermon applications and illustrations
- **Lexicon Integration:** Includes glossary of key terms from lexicon

### Sermon Collection
- **Description:** Compiled collection of Mark sermons with enhanced formatting
- **Prompt Template:** `/tools/prompts/sermon_collection_compilation_v1.0.md`
- **Output Location:** `/content/ebook/mark_sermons/[part-name].md`
- **Format:** Structured markdown for e-book conversion
- **Usage:** E-book publication and print-on-demand
- **Structure:** 4 parts organized by Mark's narrative structure
- **Primary Focus:** Triple voice sermons with applications
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Lexicon Integration:** Includes glossary of key terms from sermons

### Common Life Politics Collection
- **Description:** Compiled collection of Common Life Politics essays
- **Prompt Template:** `/tools/prompts/common_life_compilation_v2.0.md`
- **Output Location:** `/content/ebook/common_life_politics/[part-name].md`
- **Format:** Structured markdown for e-book conversion
- **Usage:** E-book publication and print-on-demand
- **Structure:** 4 parts with 3 essays each
- **Primary Focus:** Constructive theological alternatives
- **Mutations Addressed:** Both MAGA Christianism and Providential Identitarianism
- **Sermon Connection:** Integrated with sermon themes
- **Lexicon Integration:** Includes glossary of key terms from essays

## Usage Instructions

### 1. Selecting the Right Format
- Choose format based on audience, platform, and theological concept
- Consider which theological mutation is being addressed
- Match format to distribution channel
- Identify relevant sermon connection
- Align with weekly theme integration
- Determine appropriate lexicon entries to reference

### 2. Using Prompt Templates
- Copy the template path to your Claude conversation
- Fill in all required fields marked with [BRACKETS]
- Review generated content for theological accuracy
- Ensure appropriate connections to both mutations when relevant
- Verify sermon integration is appropriate
- Check that lexicon entries are referenced correctly
- Save to appropriate location in project structure

### 3. Content Scheduling
- Sermon content: Sunday delivery with weekly recording
- Monday content: MAGA and Providential book chapters
- Tuesday content: Personal essays
- Wednesday content: Common Life Politics essays and Lexicon entries
- Thursday content: Historical essays
- Friday content: Satirical pieces
- Integration content: Develop 4-6 weeks in advance
- Video content: Bi-weekly release schedule
- Audio content: Weekly podcast episodes

### 4. Sermon Integration
- Use weekly theme as unifying concept
- Connect sermon content to all publication streams
- Ensure lexicon entries are created before referenced in sermon
- Develop sermon content 3-4 weeks in advance
- Create integration guide 2-3 weeks in advance
- Use triple voice structure consistently

### 5. Lexicon Integration
- Create lexicon entries before referencing terms in content
- Follow consistent HTML template for all lexicon entries
- Publish entries as posts in "Lexicon" section
- Exclude lexicon entries from Home feed
- Update main glossary page when adding new entries
- Use consistent inline reference system in all content
- Add end-of-article glossaries to content with technical terms

### 6. Dual Mutation Approach
- Maintain parallel analysis of both mutations
- Identify shared theological roots
- Highlight distinctive characteristics of each
- Show how both contrast with Mark's theology
- Present constructive alternatives to both
- Balance attention between both mutations

## Implementation Guidelines

### Visual Consistency
- Maintain consistent visual language across streams
- Use blue gradient design for lexicon entries
- Use photographic headers with dark overlays for analytical posts
- Use distinctive design for each mutation when presented separately
- Use integrated design when presenting comparative analysis
- Create clear visual distinction for Mark's counter-imperial voice
- Follow consistent HTML structure for lexicon entries

### Voice Consistency
- Maintain analytical tone for book chapters
- Use personal narrative voice for Tuesday essays
- Use educational tone for lexicon entries
- Use prophetic voice for historical essays
- Use satirical voice for Friday content
- Use distinctive voices for triple voice sermon structure
- Ensure consistent voice across lexicon entries

### Theological Framework Consistency
- Maintain seven mutations framework across all content
- Show shared Calvinist roots of both mutations
- Present participatory freedom theology as consistent alternative
- Use Mark's counter-imperial voice as theological standard
- Balance critique with constructive alternatives
- Maintain distinction between mutations and orthodox alternatives
- Ensure lexicon entries align with theological framework

### Lexicon Maintenance Guidelines
- Review lexicon entries quarterly for accuracy and completeness
- Update main glossary page whenever adding new entries
- Ensure cross-linking between related lexicon entries
- Check for broken links between content and lexicon
- Monitor usage patterns to identify needed new entries
- Maintain alphabetical organization in main glossary
- Update "Coming Soon" labels as entries are published

## Version History

v4.0 - 2025-04-02 - Added lexicon content formats, integration tools, and implementation guidelines
v3.0 - 2025-03-31 - Comprehensive update to incorporate dual mutation framework, sermon integration, and triple voice structure
v2.0 - 2025-03-15 - Updated with expanded content formats for seven mutations framework
v1.1 - 2025-03-01 - Added Atomic Essays format
v1.0 - 2025-02-15 - Initial format index creation