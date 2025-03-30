# Hybrid Content Workflow Setup Guide

## Prerequisites
- Mac computer
- GitHub account
- Scrivener
- Python 3.8+
- Git
- Tana
- Visual Studio Code (optional)

## Step 1: GitHub Repository Setup

### Create Repository
1. Go to GitHub and create a new repository
   - Name: `maga-christianism-project`
   - Initialize with a README
   - Choose .gitignore (Python template)

### Clone Repository
```bash
# Open Terminal
cd ~/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub
git clone https://github.com/craiguffman/maga-christianism-project
cd maga-christianism-project
```

### Create Project Folder Structure
```bash
# Create project directories
mkdir -p "Common Life Politics/Markdown Exports" "Common Life Politics/drafts"
mkdir -p "MAGA Christianism/Markdown Exports" "MAGA Christianism/chapters"
mkdir -p "Untold America/Markdown Exports" "Untold America/essays"

# Commit initial structure
git add .
git commit -m "Initial project structure"
git push
```

## Step 2: Python Environment Setup

### Install Python Dependencies
```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Create a virtual environment
python3 -m venv content_workflow_env

# Activate virtual environment
source content_workflow_env/bin/activate

# Install required libraries
pip install PyYAML pyperclip
```

### Configure Python Script
1. Open the script in VS Code
2. Update base path:
```python
base_path = '/Users/craiguffman/Library/CloudStorage/Dropbox-Personal/Mac/Documents/GitHub/maga-christianism-project'
```

## Step 3: Scrivener Markdown Compilation

### Compilation Settings
1. Open Scrivener project
2. Go to File → Compile
3. Choose "Markdown" as the format
4. Configure Compilation Options:
   - Include Titles: Yes
   - Include Synopsis: Optional
   - Export Folder: Project's Markdown Exports folder

### Compilation Workflow
1. In Scrivener, select documents to export
2. File → Compile
3. Choose Markdown Export folder
4. Compile

## Step 4: Git Configuration

### SSH Key Setup (if not already done)
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Copy SSH key to clipboard
pbcopy < ~/.ssh/id_ed25519.pub

# Add to GitHub SSH keys
# (Paste copied key in GitHub Settings → SSH and GPG keys)
```

### Configure Git User
```bash
git config --global user.name "Craig Uffman"
git config --global user.email "your_email@example.com"
```

## Step 5: Tana Integration

### Tana Paste Setup
1. Install Tana Paste browser extension
2. Configure Tana workspace
3. Create project-specific supertags

## Step 6: Workflow Test Run

### Prepare Test Document
1. Open a Scrivener project
2. Write a sample document
3. Compile to Markdown in appropriate export folder

### Run Python Script
```bash
# Activate virtual environment
source content_workflow_env/bin/activate

# Run script
python3 project_manager.py
```

## Troubleshooting Checklist
- Verify file paths
- Check Python virtual environment
- Confirm Git configuration
- Validate Scrivener export settings

## Recommended Workflow
1. Write in Scrivener
2. Compile to Markdown
3. Run Python script
4. Review Git commit
5. Check Tana import

## Next Steps
- Customize metadata extraction
- Refine compilation settings
- Set up automated script running

## Getting Help
- Check script documentation
- Consult tool-specific support
- Reach out for workflow optimization

## Maintenance
- Regularly update dependencies
- Backup your repository
- Review and refine workflow periodically
```
