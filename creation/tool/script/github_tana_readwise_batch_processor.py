#!/usr/bin/env python3
"""
Tana-Readwise Batch Processor with GitHub Integration

Processes multiple Tana/Readwise files and updates tracking in GitHub repository.
"""

import os
import sys
import glob
import re
import argparse
import base64
import requests

# GitHub repository details
GITHUB_REPO = "craiguffman/maga-christianism-project"
GITHUB_BRANCH = "main"
TRACKING_FILE_PATH = "project-docs/sources-tracking.md"

def get_github_token():
    """Retrieve GitHub personal access token from environment."""
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        raise ValueError("GitHub token not found. Set GITHUB_TOKEN environment variable.")
    return token

def read_processed_sources():
    """Read processed sources from GitHub-hosted tracking file."""
    token = get_github_token()
    
    # GitHub API endpoint for getting file content
    url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{TRACKING_FILE_PATH}?ref={GITHUB_BRANCH}"
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3.raw"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        content = response.text
        
        # Extract processed sources
        processed = []
        match = re.search(r"## Already Processed.*?## ", content, re.DOTALL)
        if match:
            section = match.group(0).replace("## Already Processed", "").replace("## ", "")
            for line in section.strip().split("\n"):
                if line.startswith("- "):
                    processed.append(line[2:].strip())
        
        return processed, content
    except Exception as e:
        print(f"Error reading tracking file: {e}")
        sys.exit(1)

def update_github_tracking_file(existing_content, newly_processed):
    """Update the tracking file on GitHub."""
    token = get_github_token()
    
    # Find the already processed section
    already_processed_section = re.search(r"## Already Processed.*?## ", existing_content, re.DOTALL)
    if already_processed_section:
        # Add new entries to the section
        new_section = "## Already Processed\n"
        old_section = already_processed_section.group(0).replace("## Already Processed", "").replace("## ", "")
        
        # Extract existing entries
        existing_entries = [line[2:].strip() for line in old_section.strip().split("\n") if line.startswith("- ")]
        
        # Add existing entries
        for entry in existing_entries:
            new_section += f"- {entry}\n"
        
        # Add new entries
        for entry in newly_processed:
            if entry not in existing_entries:
                new_section += f"- {entry}\n"
        
        new_section += "\n## "
        
        # Replace old section with new section
        updated_content = existing_content.replace(already_processed_section.group(0), new_section)
        
        # GitHub API endpoint for updating file
        url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{TRACKING_FILE_PATH}"
        
        # Get the current file's SHA
        get_url = f"{url}?ref={GITHUB_BRANCH}"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        try:
            get_response = requests.get(get_url, headers=headers)
            get_response.raise_for_status()
            file_info = get_response.json()
            current_sha = file_info['sha']
            
            # Prepare payload for update
            payload = {
                "message": "Update processed sources",
                "content": base64.b64encode(updated_content.encode('utf-8')).decode('utf-8'),
                "sha": current_sha,
                "branch": GITHUB_BRANCH
            }
            
            # Send update request
            update_response = requests.put(url, headers=headers, json=payload)
            update_response.raise_for_status()
            
            print("Successfully updated tracking file on GitHub")
        
        except Exception as e:
            print(f"Error updating tracking file: {e}")
            sys.exit(1)

def extract_highlights_from_file(file_path, verbose=False):
    """
    Extract highlights and notes from file, supporting different tag formats.
    (Existing method from previous script)
    """
    # [Previous extract_highlights_from_file implementation remains the same]
    # ... (copy the entire method from the previous script)

def extract_content_blocks(content, verbose=False):
    """
    Process content into logical blocks for better extraction.
    (Existing method from previous script)
    """
    # [Previous extract_content_blocks implementation remains the same]
    # ... (copy the entire method from the previous script)

def clean_block_content(block):
    """
    Clean the content by removing all tag patterns.
    (Existing method from previous script)
    """
    # [Previous clean_block_content implementation remains the same]
    # ... (copy the entire method from the previous script)

def write_output_files(output_dir, file_highlights, verbose=False):
    """Write highlights to output files."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Write a file with all highlights
    output_file = os.path.join(output_dir, "extracted_highlights.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Extracted Highlights\n\n")
        for highlight in file_highlights:
            f.write(f"## {highlight.get('type', 'highlight')}\n\n")
            f.write(f"{highlight['content']}\n\n")
    
    if verbose:
        print(f"Wrote {len(file_highlights)} highlights to {output_file}")

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Process Tana/Readwise files')
    parser.add_argument('target', help='Directory or file to process')
    parser.add_argument('--output-dir', default='processed_highlights', 
                        help='Output directory for processed highlights')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    return parser.parse_args()

def main():
    """Main function to process files."""
    # Parse arguments
    args = parse_arguments()
    
    # Get list of already processed files and existing content
    processed_sources, existing_content = read_processed_sources()
    
    # Get list of files to process
    if os.path.isdir(args.target):
        files_to_process = glob.glob(os.path.join(args.target, "*.md"))
    else:
        files_to_process = [args.target]
    
    # Filter out already processed files
    files_to_process = [f for f in files_to_process if os.path.basename(f) not in processed_sources]
    
    # Process each file
    newly_processed = []
    all_highlights = []
    for file_path in files_to_process:
        try:
            # Extract highlights from the file
            file_highlights, _ = extract_highlights_from_file(file_path, args.verbose)
            
            # Add highlights to the collection
            all_highlights.extend(file_highlights)
            
            # Add file to processed sources
            newly_processed.append(os.path.basename(file_path))
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Write output files if we have highlights
    if all_highlights:
        write_output_files(args.output_dir, all_highlights, args.verbose)
    
    # Update tracking file on GitHub
    if newly_processed:
        update_github_tracking_file(existing_content, newly_processed)
    
    print(f"Processed {len(newly_processed)} new files")
    print(f"Total highlights extracted: {len(all_highlights)}")

if __name__ == "__main__":
    main()
