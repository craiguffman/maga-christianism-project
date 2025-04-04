# 20250404170000_content_classification_framework
[Store as: #creation/tool/index/content_classification_framework v1.0]
[Related: #creation/tool/index/project_reference_index, #creation/tool/index/comprehensive_taxonomy]

---
title: "Content Classification Framework"
date: 2025-04-04
type: index
status: complete
tags:
  - content
  - organization
  - workflow
  - tana
  - dropbox
  - platforms
  - substack
---

# Content Classification Framework v1.0

This framework establishes a three-class system for organizing all project content based on storage location, formatting requirements, and intended use. It provides clear guidelines for ensuring content is optimally formatted for its destination while maintaining cross-platform consistency.

## Classification Overview

All project content is classified into one of three categories:

### Class A: Tana-Bound Tools
- **Definition**: Content that lives primarily within the Tana knowledge management system
- **Purpose**: Project organization, knowledge management, and workflow orchestration
- **Examples**: Knowledge objects, tool indices, reference documents, workflows, tracking systems
- **Format Requirements**: Tana-optimized with consistent tagging and metadata

### Class B: Dropbox-Bound References
- **Definition**: Content stored in the project's Dropbox structure but not bound to a specific platform
- **Purpose**: Research storage, source materials, analysis documents, collaborative drafts
- **Examples**: Source analyses, thematic syntheses, draft chapters, research notes
- **Format Requirements**: Standard markdown with consistent directory structure and metadata

### Class C: Platform-Optimized Content
- **Definition**: Content specifically formatted for publication on external platforms
- **Purpose**: Public-facing content tailored to specific platform requirements
- **Examples**: Substack posts, EPUB chapters, YouTube scripts, Lexicon entries
- **Format Requirements**: Platform-specific formatting with appropriate visual elements and styling

## Implementation Guidelines

### Class A: Tana-Bound Tools

#### Storage Location
- **Primary**: Tana knowledge management system
- **Backup**: Exported markdown files in Dropbox `/tools/tana_exports/`

#### Formatting Requirements
- **File Naming**: `YYYYMMDDHHMM_descriptive_name.md`
- **Storage Tag**: `#creation/tool/[type]/[name]` or `#knowledge/[type]/[name]`
- **Required Metadata**:
  - Title
  - Creation date
  - Type
  - Status
  - Related resources
  - Version

#### Content Structure
- **Header**: Consistent header with storage tags and metadata
- **Body**: Structured content with clear headings and organization
- **Footer**: Version history and related resources

#### Creation Workflow
1. Draft initial content in Claude using artifact-based approach
2. Review and refine structure and content
3. Import into Tana with appropriate tagging
4. Export backup to Dropbox repository

### Class B: Dropbox-Bound References

#### Storage Location
- **Primary**: Dropbox directory structure
- **Secondary**: GitHub repository for version control

#### Formatting Requirements
- **File Naming**: `descriptive-name-v1-0.md` (hyphenated, lowercase)
- **Directory Structure**: `/[content_type]/[category]/[subcategory]/`
- **Required Metadata**:
  - Title
  - Creation date
  - Type
  - Status
  - Related resources
  - Version

#### Content Structure
- **Header**: YAML or markdown frontmatter with metadata
- **Body**: Content organized with markdown headings and structures
- **References**: Consistent citation format for references
- **Footer**: Version history

#### Creation Workflow
1. Draft content in Claude using artifact-based approach
2. Review and refine in VSCode
3. Save to appropriate Dropbox directory
4. Commit to GitHub repository for version tracking
5. Reference in Tana as needed with appropriate tags

### Class C: Platform-Optimized Content

#### Storage Location
- **Primary**: Platform-specific (Substack, Amazon KDP, YouTube)
- **Backup**: Dropbox `/content/[platform]/[content_type]/`

#### Formatting Requirements
- **Substack**:
  - HTML-enhanced markdown
  - Platform-specific metadata
  - SEO optimization
  - Standardized header images
  - Consistent internal linking structure
  
- **EPUB**:
  - Scrivener-optimized formatting
  - Structural markup for chapters and sections
  - Standardized styling
  - Cover images and front matter
  
- **YouTube**:
  - Descript-formatted scripts
  - Timing markers
  - Visual cue notations
  - SEO-optimized descriptions

#### Content Structure
- **Platform-specific headers**
- **Standardized introductions**
- **Optimized body content**
- **Platform-appropriate calls to action**
- **Cross-platform references**

#### Creation Workflow
1. Draft content in Claude using artifact-based approach
2. Refine in appropriate tool (VSCode for Substack, Scrivener for EPUB, Descript for YouTube)
3. Apply platform-specific formatting and enhancements
4. Review for platform optimization
5. Publish to platform
6. Store backup in Dropbox with consistent naming and organization

## Cross-Class Integration

### Referencing System
- **Class A → Class B**: Reference Dropbox paths using standardized format
- **Class A → Class C**: Reference published URLs using standardized format
- **Class B → Class A**: Reference Tana objects using standardized tags
- **Class B → Class C**: Reference published URLs using standardized format
- **Class C → Class A**: Not typically referenced directly
- **Class C → Class B**: Reference source materials using standardized format

### Content Flow
1. **Research Phase**: Primarily Class B (Dropbox-bound references)
2. **Organization Phase**: Primarily Class A (Tana-bound tools)
3. **Creation Phase**: Transformation from Class B to Class C
4. **Publication Phase**: Primarily Class C (Platform-optimized content)
5. **Integration Phase**: Cross-referencing across all classes

## Content Conversion Guidelines

### Class B → Class C Conversion
- **Substack Conversion**:
  - Add HTML enhancements for Substack rendering
  - Incorporate standardized header images
  - Add internal links to lexicon entries
  - Structure for optimal readability on Substack
  
- **EPUB Conversion**:
  - Restructure for chapter flow
  - Add appropriate front and back matter
  - Standardize formatting for e-readers
  - Incorporate cross-references and navigation
  
- **YouTube Conversion**:
  - Adapt written content for spoken delivery
  - Add timing markers and visual cues
  - Incorporate presentation notes
  - Develop accompanying visual elements

### Class A → Class B Conversion
- Extract relevant content from Tana
- Structure as standalone documents
- Add appropriate contextual information
- Format for collaborative use

### Class B → Class A Conversion
- Extract key insights and structures
- Format with appropriate Tana tags
- Integrate into knowledge graph
- Create appropriate relationships to other knowledge objects

## Version Control

### Class A
- Version tracked within Tana using version nodes
- Export updated versions to Dropbox with version number in filename

### Class B
- Version tracked in GitHub repository
- Version numbers in filenames
- Detailed commit messages for changes

### Class C
- Platform-specific version management
- Backup copies in Dropbox with version numbers
- Change history documented in accompanying reference files

## Implementation Timeline

1. **Phase 1: Documentation** (Week 1)
   - Create this framework document
   - Update README and related indices
   - Develop templates for each class
   
2. **Phase 2: Classification** (Week 2)
   - Audit existing content and classify
   - Restructure storage locations as needed
   - Update metadata and formatting
   
3. **Phase 3: Workflow Integration** (Week 3)
   - Develop Claude prompts for each class
   - Create conversion workflows
   - Test cross-class referencing
   
4. **Phase 4: Full Implementation** (Week 4)
   - Apply framework to all new content
   - Convert existing content as needed
   - Train team on implementation

## Version History

v1.0 - 2025-04-04 - Initial content classification framework
