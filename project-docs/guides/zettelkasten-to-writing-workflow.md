# Zettelkasten to Book Project Workflow Protocol

This protocol establishes a systematic approach for moving from research (Zettelkasten) to writing (Book Project Management) in Tana, ensuring a smooth transition between knowledge collection and content creation.

## Phase 1: Research Collection & Organization

### 1.1 Topic Research Collection
- Use standard Zettelkasten tags (`#source`, `#quote`, `#claim`, `#evidence`, `#question`) to collect and organize research
- Tag relevant notes with topic-specific tags that align with your book's themes (e.g., `#primitive-biblicism`, `#practical-atheism`)
- Create structured search queries in Tana to gather related notes by theme

### 1.2 Research Review & Synthesis
- Create a temporary "Research Collection" node in Tana
- Gather all relevant Zettelkasten notes on a specific chapter topic using Tana's search
- Review collected notes, identifying key arguments, supporting evidence, and illustrative examples
- Create synthesis notes that connect multiple ideas using the standard Zettelkasten approach

## Phase 2: Chapter Planning & Outlining

### 2.1 Chapter Structure Creation
- Create a new `#BookChapter` node in Tana with required metadata:
  - `title`
  - `number`
  - `status: Outline`
  - `part` (I, II, III, or IV)
  - `targetWordCount`
- In the chapter node, create a bulleted list of potential sections based on your research synthesis

### 2.2 Chapter Section Definition
- For each section in your outline, create a `#ChapterSection` node
- Fill in the basic metadata:
  - `title`
  - `status: Outline`
  - `targetWordCount`
  - `keyPoints` (bulleted list of main arguments)
- Connect to research by adding:
  - `relatedNotes`: Link to relevant Zettelkasten synthesis notes
  - `relatedSources`: Link to primary sources from your Zettelkasten

### 2.3 Content Element Identification
- For each major argument, example, or case study, create a `#ContentElement` node
- Specify:
  - `elementType` (Argument, Example, Illustration, CaseStudy, Definition)
  - `description` of the content element
  - `category` (Primitive Biblicism, Practical Atheism, etc.)
- Connect to your Zettelkasten by adding:
  - `relatedQuotes`: Link to supporting quotes
  - `relatedClaims`: Link to theoretical claims
  - `relatedEvidence`: Link to evidence nodes

## Phase 3: Drafting Process

### 3.1 Section Drafting Setup
- Update the `#ChapterSection` status to "Draft"
- Create a new Scrivener document for the section (if using Scrivener)
  - Create a folder in Scrivener that matches your Tana structure
  - Import your outline as document notes in Scrivener
- Open the Tana `#ChapterSection` node with all linked `#ContentElement` nodes visible

### 3.2 Writing From Research
- For each `#ContentElement`, review all linked Zettelkasten notes
- Follow this sequence for content development:
  1. State your main argument (from `relatedClaims`)
  2. Present supporting evidence (from `relatedEvidence`)
  3. Illustrate with examples or quotes (from `relatedQuotes`)
  4. Connect to broader themes (from `category` field)
- As you incorporate content from your Zettelkasten, mark it as "used" or add a tag to track utilization

### 3.3 Section Completion
- Update word count in the `#ChapterSection` `wordCount` property
- Update status to "Review" when draft is complete
- Create any `#EditingNote` nodes for self-review items that need attention

## Phase 4: Review & Revision Process

### 4.1 Self-Review Protocol
- Review each `#ChapterSection` against its stated `keyPoints`
- Check that all `#ContentElement` items have been incorporated
- Ensure all claims have appropriate evidence from your Zettelkasten
- Create `#EditingNote` nodes for any issues identified with:
  - `type` (Content, Structure, Style, Citation, Factual, Theological)
  - `status: Open`
  - `comment` detailing the issue
  - `relatedTo` linking to the relevant section

### 4.2 Revision Workflow
- Review all `#EditingNote` nodes for a chapter
- Sort by `type` to address similar issues together
- Update each `#EditingNote` to "Addressed" when changes are made
- When returning to Scrivener or text editor, keep Tana open with filtered view of editing notes

### 4.3 External Review Process
- When a `#BookChapter` is ready for external review:
  - Update status to "Review"
  - Create `#PublishingTask` for "External Review" with:
    - Appropriate `dueDate`
    - `priority` setting
    - `platform: General`
- When feedback is received, create `#EditingNote` nodes for each feedback item
- Process external feedback using the same revision workflow

## Phase 5: Content Integration & Completion

### 5.1 Chapter Finalization
- When all `#ChapterSection` nodes are marked "Final" and all `#EditingNote` items are "Resolved":
  - Update `#BookChapter` status to "Final"
  - Record final `wordCount`
  - Create required `#PublishingTask` items for publication

### 5.2 Substack Publication Process
- For chapters designated for Substack:
  - Create a `#PublishingTask` with `platform: Substack`
  - Export finalized content from Scrivener to Markdown
  - Schedule publication date in Substack
  - Update `publishedOnSubstack` date in `#BookChapter`

### 5.3 Book Assembly
- Create `#PublishingTask` items for final book assembly with `platform: General`
- Ensure all `#BookChapter` items are in "Final" status
- Follow your established EPUB/book formatting guidelines

## Appendix: Transition Commands & Shortcuts

### Tana Search Queries
- Find relevant Zettelkasten notes: `#claim AND #primitive-biblicism`
- View all open editing notes: `#EditingNote AND status::Open`
- Find unused research: `#evidence NOT tag:used AND #practical-atheism`

### Cross-Platform Integration
- Tana → Scrivener: Export section outlines as OPML
- Scrivener → Tana: Update word counts after writing sessions
- Tana → Things 3: Create tasks with deep links back to Tana nodes
- Things 3 → Tana: Use `thingsURL` property to link back to task