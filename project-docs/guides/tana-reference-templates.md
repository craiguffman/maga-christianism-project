# Tana Reference Templates for GitHub Documents

The following templates show how to create reference nodes in Tana that link to your GitHub-stored markdown documents. These templates follow the tagging system outlined in the Tana Tagging System Reference.

## Main Documentation Reference Structure

Create a top-level node in Tana for project documentation:

```
Project Documentation #workflow #reference
- Workflow Guides #workflow #reference #instruction
- Research Frameworks #research #reference #instruction
- Content Templates #content #template #reference
- Integration Guides #workflow #integration #reference
```

## Workflow Guides References

Under the "Workflow Guides" node, add references to your main workflow documents:

```
Unified Workflow Guide #workflow #reference #instruction #all
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/guides/unified-workflow.md
- Purpose: Comprehensive guide for the entire content creation process
- Last Updated: [date]
- Key Sections:
  - Research Phase #workflow #process #research
  - Content Planning #workflow #process #content
  - Draft Creation #workflow #process #content #draft
  - Publication #workflow #process #publication
```

```
Claude Deep Dive Guide #workflow #reference #instruction #claude
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/guides/claude-deep-dive.md
- Purpose: Advanced techniques for working with Claude AI
- Last Updated: [date]
- Key Commands:
  - Research Commands #claude #instruction #research
  - Content Development #claude #instruction #content
  - Analysis Frameworks #claude #instruction #analysis
```

## Research Framework References

Under the "Research Frameworks" node, add references to research methodology documents:

```
Theological Analysis Framework #research #reference #instruction #theology
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/frameworks/theological-analysis.md
- Purpose: Framework for analyzing theological content and claims
- Last Updated: [date]
- Key Components:
  - Historical Context #research #process #history
  - Textual Analysis #research #process #analysis
  - Denominational Comparison #research #process #comparison
```

```
Political Rhetoric Framework #research #reference #instruction #politics
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/frameworks/political-rhetoric.md
- Purpose: Framework for analyzing political speech and messaging
- Last Updated: [date]
- Key Components:
  - Audience Analysis #research #process #audience
  - Rhetorical Patterns #research #process #rhetoric
  - Emotional Appeals #research #process #analysis
```

## Content Template References

Under the "Content Templates" node, add references to your content templates:

```
Article Structure Template #content #template #article
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/templates/article-structure.md
- Purpose: Standard template for article content
- Last Updated: [date]
- Key Sections:
  - Introduction Framework #content #template #section
  - Argument Development #content #template #section
  - Conclusion Structure #content #template #section
```

```
Video Script Template #content #template #video
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/templates/video-script.md
- Purpose: Template for video script development
- Last Updated: [date]
- Key Components:
  - Opening Hook #content #template #section
  - Visual Description #content #template #visual
  - Narration Structure #content #template #narration
```

## Integration Guide References

Under the "Integration Guides" node, add references to tool integration guides:

```
Tana Tagging System #workflow #reference #syntax #tana
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/references/tana-tagging-system.md
- Purpose: Comprehensive tagging reference for Tana
- Last Updated: [date]
- Key Tag Categories:
  - Primary Tags #workflow #reference #syntax
  - Secondary Tags #workflow #reference #syntax
  - Content Type Tags #workflow #reference #syntax
  - Tool-Specific Tags #workflow #reference #syntax
```

```
VSCode-GitHub Integration #workflow #integration #vscode #github
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/guides/vscode-github-integration.md
- Purpose: Workflow for code editing and version control
- Last Updated: [date]
- Key Processes:
  - Cloning Repository #workflow #process #github
  - Committing Changes #workflow #process #github
  - Managing Branches #workflow #process #github
```

## Quick Reference Nodes

For frequently used commands or syntaxes, create direct nodes in Tana:

```
Claude Quick Commands #claude #reference #syntax
- Research: @claude research: [topic] #claude #instruction #research
- Analyze: @claude analyze: [text or document] #claude #instruction #analysis
- Draft: @claude draft: [description of needed content] #claude #instruction #content
- Feedback: @claude feedback: [your content] #claude #instruction #feedback
- Summarize: @claude summarize: [content to condense] #claude #instruction #summary
```

```
Common Tag Combinations #workflow #reference #syntax #tana
- Research Source: #research #source #[topic] 
- Content Draft: #content #draft #[content-type]
- Claude Instruction: #claude #instruction #[purpose]
- Workflow Process: #workflow #process #[tool]
```

## Project-Specific Research References

For your specific project, create reference nodes for key research areas:

```
MAGA Christianity Research Map #research #reference #maga #christianism
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/project-docs/research/maga-christianism-map.md
- Purpose: Overview of research areas and connections
- Last Updated: [date]
- Key Areas:
  - Historical Context #research #history #christianism
  - Theological Frameworks #research #theology #maga
  - Political Integration #research #politics #christianism
  - Media Representation #research #media #maga
```

## Working Files References

Create references to active working files:

```
Current Draft: Chapter 3 #content #inprogress #chapter
- URL: https://github.com/craiguffman/maga-christianism-project/blob/main/drafts/chapter-3-draft.md
- Status: In Progress #content #inprogress
- Due Date: [date]
- Claude Assistance: #claude #instruction #content
  - @claude feedback: Chapter 3 theological analysis
  - @claude revise: Chapter 3 section on religious nationalism
```

## Content Publication References

Track published content:

```
Published Articles #content #complete #article
- Article: "The Evolution of Religious Nationalism" #content #complete #article #christianism
  - URL: https://github.com/craiguffman/maga-christianism-project/blob/main/published/religious-nationalism-evolution.md
  - Published: [date]
  - Platform: Substack
- Article: "Theological Foundations of MAGA" #content #complete #article #maga #theology
  - URL: https://github.com/craiguffman/maga-christianism-project/blob/main/published/theological-foundations-maga.md
  - Published: [date]
  - Platform: EPUB
```

## Integration with Claude Workflow

Create a node specifically for Claude interaction tracking:

```
Claude Interactions #claude #reference
- Research Requests #claude #research
  - [Date]: Research on religious symbolism in campaigns #claude #research #symbolism
  - [Date]: Analysis of evangelical voting patterns #claude #research #politics
- Content Development #claude #content
  - [Date]: Outline for article on media representation #claude #outline #media
  - [Date]: Draft feedback on theological analysis #claude #feedback #theology
```
