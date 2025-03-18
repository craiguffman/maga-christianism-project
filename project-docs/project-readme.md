# MAGA Christianism Research Project

## Project Overview
This repository manages a systematic research project exploring the theological and political dynamics of MAGA Christianism, with a focus on methodological rigor and comprehensive source analysis.

## Repository Structure

### Core Documents
- `consolidated-notes.md`: Central repository for research insights, source analyses, and thematic compilations
- `chapter-source-index.md`: Tracking document for chapter development and source integration
- `source_integration.py`: Python utility for managing research documentation

### Workflow

#### Source Analysis Integration
1. Analyze a new source
2. Update `source_integration.py` with source details
3. Run the script to automatically update:
   - Consolidated notes
   - Chapter source index
   - Source tracking metadata

#### Key Features
- Minimal manual updating
- Machine-readable format
- Supports incremental research process
- Flexible metadata tracking

## Setup Requirements
- Python 3.8+
- PyYAML library
- VSCode (recommended)
- Git version control

## Installation
```bash
# Clone the repository
git clone [your-repo-url]

# Install required dependencies
pip install pyyaml
```

## Usage
```bash
# Integrate a new source
python source_integration.py --source "Source Name" --chapter "Theological Framework"
```

## Ecosystem Integration
- GitHub for version control
- VSCode for editing
- Tana for knowledge management
- Things for task tracking

## Recommended Workflow
1. Conduct source analysis
2. Update markdown files
3. Commit changes to Git
4. Sync with Tana and Things

## Contribution Guidelines
- Follow markdown formatting
- Use consistent metadata
- Update source integration script as needed

## License
[Your Chosen License]

## Contact
[Your Contact Information]
