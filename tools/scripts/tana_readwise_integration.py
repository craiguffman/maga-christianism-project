#!/usr/bin/env python3
"""
Tana-Readwise Integration Script

This script integrates Readwise exports (JSON) with Tana exports (Markdown)
to organize highlights according to the structure defined in Tana.

Usage:
    python tana_readwise_integration.py \
        --readwise-file path/to/readwise_export.json \
        --tana-file path/to/tana_export.md \
        --output-dir path/to/output_directory

Updated to handle both #highlights and #highlight-SN(A)CK tags in Tana exports.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Integrate Readwise exports with Tana organization')
    parser.add_argument('--readwise-file', required=True, help='Path to Readwise export JSON file')
    parser.add_argument('--tana-file', required=True, help='Path to Tana export markdown file')
    parser.add_argument('--output-dir', required=True, help='Path to output directory')
    return parser.parse_args()

def load_readwise_highlights(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    # Find the Highlights section
    highlights_section_match = re.search(r'### Highlights\n\n(.*?)(?=\n#|\Z)', markdown_text, re.DOTALL)
    
    highlights = []
    if highlights_section_match:
        highlights_text = highlights_section_match.group(1)
        
        # Parse each highlight
        highlight_matches = re.findall(r'- (.*?)\s*\(\[Location \d+\].*?\)', highlights_text, re.DOTALL)
        
        for match in highlight_matches:
            # Clean up the highlight text
            highlight_text = match.strip().replace('\n', ' ')
            highlights.append({
                'text': highlight_text
            })
    
    print(f"Loaded {len(highlights)} highlights from {file_path}")
    return highlights

def parse_tana_export(file_path):
    """Parse Tana export markdown file to extract structural organization."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the Structural Order section within #Inspectional_Reading
        structural_pattern = re.compile(r'#Inspectional_Reading.*?\*\*Structural Order\*\*:(.*?)(?=\n#|\Z)', re.DOTALL)
        structural_match = structural_pattern.search(content)
        
        if not structural_match:
            print("Error: Could not find 'Structural Order' within '#Inspectional_Reading' in Tana export")
            return None
        
        structure_content = structural_match.group(1).strip()
        
        # Parse the structure into a hierarchy
        lines = structure_content.split('\n')
        hierarchy = []
        current_path = []
        prev_indent = -1
        
        for line in lines:
            if not line.strip():
                continue
                
            # Calculate indent level based on spaces/tabs
            indent = len(line) - len(line.lstrip())
            text = line.strip()
            
            # Adjust the current path based on indent level
            if indent > prev_indent:
                current_path.append(text)
            elif indent == prev_indent:
                current_path.pop()
                current_path.append(text)
            else:
                # Go back up the tree to the appropriate level
                steps_back = (prev_indent - indent) // 2 + 1  # Assuming 2 spaces per indent level
                current_path = current_path[:-steps_back]
                current_path.append(text)
            
            prev_indent = indent
            
            # Add to hierarchy
            hierarchy.append({
                'path': current_path.copy(),
                'text': text
            })
        
        print(f"Extracted {len(hierarchy)} structural elements from Tana export")
        return hierarchy
    except Exception as e:
        print(f"Error parsing Tana export: {e}")
        sys.exit(1)

def extract_highlights_from_tana(file_path):
    """Extract highlights and original notes from Tana export."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find both types of highlights: #highlights and #highlight-SN(A)CK
        highlights_pattern = re.compile(r'(#highlights|#highlight-SN\(A\)CK)(.*?)(?=\n#|\Z)', re.DOTALL)
        highlight_matches = highlights_pattern.findall(content)
        
        # Find original notes (atomic, synthesis, permanent)
        notes_pattern = re.compile(r'(#atomic notes|#synthesis notes|#permanent notes)(.*?)(?=\n#|\Z)', re.DOTALL)
        notes_matches = notes_pattern.findall(content)
        
        highlights = [{'type': h_type, 'content': h_content.strip()} for h_type, h_content in highlight_matches]
        notes = [{'type': n_type, 'content': n_content.strip()} for n_type, n_content in notes_matches]
        
        print(f"Extracted {len(highlights)} highlights and {len(notes)} original notes from Tana export")
        return highlights, notes
    except Exception as e:
        print(f"Error extracting highlights from Tana export: {e}")
        sys.exit(1)

def categorize_highlights(readwise_highlights, tana_structure):
    """Categorize Readwise highlights according to Tana structure."""
    # Create a dictionary to hold categorized highlights
    categories = {}
    
    # Initialize categories based on structure
    for item in tana_structure:
        path_key = ' > '.join(item['path'])
        if path_key not in categories:
            categories[path_key] = {
                'title': item['text'],
                'path': item['path'],
                'highlights': []
            }
    
    # Simple categorization based on keywords
    # (This is a basic approach - you might want to enhance this with NLP or other techniques)
    for highlight in readwise_highlights:
        highlight_text = highlight.get('text', '')
        if not highlight_text:
            continue
            
        best_match = None
        best_match_score = 0
        
        for path_key, category in categories.items():
            # Calculate a simple matching score based on word overlap
            category_words = set(path_key.lower().split())
            highlight_words = set(highlight_text.lower().split())
            overlap = len(category_words.intersection(highlight_words))
            
            if overlap > best_match_score:
                best_match_score = overlap
                best_match = path_key
        
        # If no good match, put in "Uncategorized"
        if best_match_score == 0:
            if "Uncategorized" not in categories:
                categories["Uncategorized"] = {
                    'title': "Uncategorized",
                    'path': ["Uncategorized"],
                    'highlights': []
                }
            categories["Uncategorized"]['highlights'].append(highlight)
        else:
            categories[best_match]['highlights'].append(highlight)
    
    return categories

def write_output_files(categories, output_dir, tana_highlights, tana_notes):
    """Write categorized highlights to output files."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create an index file
    index_path = os.path.join(output_dir, "00_index.md")
    with open(index_path, 'w', encoding='utf-8') as index_file:
        index_file.write("# Organized Highlights Index\n\n")
        index_file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        index_file.write("## Categories\n\n")
        for path_key, category in categories.items():
            if len(category['highlights']) > 0:
                safe_filename = create_safe_filename(category['title'])
                index_file.write(f"- [{category['title']}]({safe_filename}.md) ({len(category['highlights'])} highlights)\n")
        
        # Add Tana highlights and notes
        if tana_highlights:
            index_file.write("\n## Original Tana Highlights\n\n")
            for i, highlight in enumerate(tana_highlights):
                index_file.write(f"- {highlight['type']}: {highlight['content'][:50]}...\n")
        
        if tana_notes:
            index_file.write("\n## Original Tana Notes\n\n")
            for i, note in enumerate(tana_notes):
                index_file.write(f"- {note['type']}: {note['content'][:50]}...\n")
    
    # Write category files
    for path_key, category in categories.items():
        if len(category['highlights']) == 0:
            continue
            
        safe_filename = create_safe_filename(category['title'])
        file_path = os.path.join(output_dir, f"{safe_filename}.md")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            # Write header
            f.write(f"# {category['title']}\n\n")
            f.write(f"Path: {' > '.join(category['path'])}\n\n")
            f.write(f"Contains {len(category['highlights'])} highlights\n\n")
            
            # Write highlights
            f.write("## Highlights\n\n")
            for highlight in category['highlights']:
                f.write(f"### {highlight.get('text', '')}  \n")
                if 'note' in highlight and highlight['note']:
                    f.write(f"*Note: {highlight['note']}*\n\n")
                if 'location' in highlight:
                    f.write(f"*Location: {highlight['location']}*\n\n")
                if 'color' in highlight:
                    f.write(f"*Color: {highlight['color']}*\n\n")
                f.write("---\n\n")
    
    print(f"Output files written to {output_dir}")

def create_safe_filename(text):
    """Convert text to a safe filename."""
    # Remove invalid characters and replace spaces with underscores
    safe = re.sub(r'[^\w\s-]', '', text).strip().lower()
    safe = re.sub(r'[-\s]+', '_', safe)
    return safe

def main():
    """Main function."""
    args = parse_arguments()
    
    # Load data
    readwise_highlights = load_readwise_highlights(args.readwise_file)
    tana_structure = parse_tana_export(args.tana_file)
    tana_highlights, tana_notes = extract_highlights_from_tana(args.tana_file)
    
    if not tana_structure:
        print("No structure found in Tana export. Exiting.")
        sys.exit(1)
    
    # Categorize highlights
    categories = categorize_highlights(readwise_highlights, tana_structure)
    
    # Write output files
    write_output_files(categories, args.output_dir, tana_highlights, tana_notes)
    
    print("Integration completed successfully!")

if __name__ == "__main__":
    main()