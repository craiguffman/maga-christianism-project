#!/usr/bin/env python3
"""
Tana-Readwise Integration Script

This script integrates Readwise exports (Markdown) with Tana exports (Markdown)
to organize highlights according to the structure defined in Tana.

Usage:
    python tana_readwise_integration.py \
        --readwise-file path/to/readwise_export.md \
        --tana-file path/to/tana_export.md \
        --output-dir path/to/output_directory

Updated to handle Tana-specific highlight formats including square-bracketed text,
atomic notes, synthesis notes, permanent notes, and thesis statements.
"""

import argparse
import os
import re
import sys
from datetime import datetime

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Integrate Readwise exports with Tana organization')
    parser.add_argument('--readwise-file', required=True, help='Path to Readwise export Markdown file')
    parser.add_argument('--tana-file', required=True, help='Path to Tana export markdown file')
    parser.add_argument('--output-dir', required=True, help='Path to output directory')
    return parser.parse_args()

def load_readwise_highlights(file_path):
    """Load highlights from a Readwise export markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    
    # Find the Highlights section
    highlights_section_match = re.search(r'### Highlights\n(.*)', markdown_text, re.DOTALL)
    
    highlights = []
    if highlights_section_match:
        highlights_text = highlights_section_match.group(1)
        
        # Parse each highlight with the new pattern
        highlight_matches = re.findall(r'- (.*?)\s*\(.*?\)', highlights_text, re.DOTALL)
        
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
            # Try alternative pattern: Look for a section that seems to be a structure
            alt_pattern = re.compile(r'- (Book \w+: .*?)\n((?:\s+- .*\n)+)', re.MULTILINE)
            alt_matches = alt_pattern.findall(content)
            
            if alt_matches:
                # Manually build structure from matched sections
                hierarchy = []
                for book_title, sections in alt_matches:
                    # Add book level
                    hierarchy.append({
                        'path': [book_title.strip()],
                        'text': book_title.strip()
                    })
                    
                    # Process sections
                    section_lines = sections.split('\n')
                    for line in section_lines:
                        if not line.strip():
                            continue
                        
                        # Extract section name, removing any Tana links
                        section_text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', line).strip()
                        if section_text.startswith('- '):
                            section_text = section_text[2:].strip()
                            
                        # Add to hierarchy with full path
                        if section_text:
                            hierarchy.append({
                                'path': [book_title.strip(), section_text],
                                'text': section_text
                            })
                
                print(f"Extracted {len(hierarchy)} structural elements from Tana export (alternative method)")
                return hierarchy
            
            print("Error: Could not find 'Structural Order' or alternative structure in Tana export")
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
            
            # Remove leading dash if present
            if text.startswith('-'):
                text = text[1:].strip()
                
            # Clean up any Tana links in the text
            text = re.sub(r'\[([^\]]+)\]\(.*?\)', r'\1', text)
            
            # Adjust the current path based on indent level
            if indent > prev_indent:
                current_path.append(text)
            elif indent == prev_indent:
                if current_path:  # Check to prevent errors with empty path
                    current_path.pop()
                current_path.append(text)
            else:
                # Go back up the tree to the appropriate level
                steps_back = (prev_indent - indent) // 2 + 1  # Assuming 2 spaces per indent level
                if len(current_path) >= steps_back:  # Check to prevent errors
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
        
        # Pattern 1: Find highlights in square brackets with Tana links
        highlights_pattern = re.compile(r'\[(.*?)\]\(https://app\.tana\.inc\?nodeid=.*?\)')
        highlight_matches = highlights_pattern.findall(content)
        highlights = [{'type': 'highlight', 'content': h.strip()} for h in highlight_matches]
        
        # Pattern 2: Find atomic notes with the SN(A)CK tag - using underscore pattern
        atomic_pattern = re.compile(r'(.*?)\s+#atomic_note_-_SN\(A\)CK', re.DOTALL)
        atomic_matches = atomic_pattern.findall(content)
        atomic_notes = [{'type': 'atomic_note', 'content': n.strip()} for n in atomic_matches]
        
        # Pattern 3: Find synthesis notes - using underscore pattern
        synthesis_pattern = re.compile(r'(.*?)\s+#synthesis_note_-_SN\(A\)CK', re.DOTALL)
        synthesis_matches = synthesis_pattern.findall(content)
        synthesis_notes = [{'type': 'synthesis_note', 'content': n.strip()} for n in synthesis_matches]
        
        # Pattern 4: Find permanent notes - using underscore pattern
        permanent_pattern = re.compile(r'(.*?)\s+#permanent_note_-_SN\(A\)CK', re.DOTALL)
        permanent_matches = permanent_pattern.findall(content)
        permanent_notes = [{'type': 'permanent_note', 'content': n.strip()} for n in permanent_matches]
        
        # Pattern 5: Find "Thesis" highlights which are often important
        thesis_pattern = re.compile(r'\[Thesis #\d+:(.*?)\]', re.DOTALL)
        thesis_matches = thesis_pattern.findall(content)
        thesis_notes = [{'type': 'thesis', 'content': t.strip()} for t in thesis_matches]
        
        # Combine all notes
        all_notes = highlights + atomic_notes + synthesis_notes + permanent_notes + thesis_notes
        
        print(f"Extracted {len(highlights)} highlights, {len(atomic_notes)} atomic notes, "
              f"{len(synthesis_notes)} synthesis notes, {len(permanent_notes)} permanent notes, "
              f"and {len(thesis_notes)} thesis statements from Tana export")
        
        return all_notes, []  # Return all as "highlights" for simplicity
    except Exception as e:
        print(f"Error extracting highlights from Tana export: {e}")
        sys.exit(1)

def categorize_highlights(readwise_highlights, tana_structure, tana_highlights):
    """Categorize both Readwise and Tana highlights according to Tana structure."""
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
    
    # Add "Uncategorized" category
    if "Uncategorized" not in categories:
        categories["Uncategorized"] = {
            'title': "Uncategorized",
            'path': ["Uncategorized"],
            'highlights': []
        }
    
    # First, categorize Tana highlights
    # These are already in the Tana structure so they're easier to match
    for highlight in tana_highlights:
        # For each highlight, find the best matching category
        best_match = None
        best_match_score = 0
        
        for path_key, category in categories.items():
            # Calculate a matching score 
            # For Tana highlights, we can use a more sophisticated approach
            path_text = ' '.join(category['path']).lower()
            highlight_text = highlight['content'].lower()
            
            # Try to find exact section references
            section_mentions = any(p.lower() in highlight_text for p in category['path'])
            
            # Calculate word overlap
            path_words = set(path_text.split())
            highlight_words = set(highlight_text.split())
            overlap = len(path_words.intersection(highlight_words))
            
            # Calculate score: section mentions are stronger signals
            score = overlap + (10 if section_mentions else 0)
            
            if score > best_match_score:
                best_match_score = score
                best_match = path_key
        
        # Assign to best match or Uncategorized
        target_category = categories.get(best_match) if best_match_score > 0 else categories["Uncategorized"]
        target_category['highlights'].append({
            'text': highlight['content'],
            'type': highlight['type'],
            'source': 'tana'
        })
    
    # Then, categorize Readwise highlights
    for highlight in readwise_highlights:
        highlight_text = highlight.get('text', '')
        if not highlight_text:
            continue
            
        best_match = None
        best_match_score = 0
        
        for path_key, category in categories.items():
            # Calculate a simple matching score based on word overlap
            category_words = set(' '.join(category['path']).lower().split())
            highlight_words = set(highlight_text.lower().split())
            overlap = len(category_words.intersection(highlight_words))
            
            if overlap > best_match_score:
                best_match_score = overlap
                best_match = path_key
        
        # Assign to best match or Uncategorized
        target_category = categories.get(best_match) if best_match_score > 0 else categories["Uncategorized"]
        target_category['highlights'].append({
            'text': highlight_text,
            'source': 'readwise'
        })
    
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
                source_tag = f"[{highlight.get('source', 'unknown')}]" if 'source' in highlight else ""
                type_tag = f"[{highlight.get('type', 'highlight')}]" if 'type' in highlight else ""
                tags = f"{source_tag} {type_tag}".strip()
                
                f.write(f"### {highlight.get('text', '')}  \n")
                if tags:
                    f.write(f"*Tags: {tags}*\n\n")
                if 'note' in highlight and highlight['note']:
                    f.write(f"*Note: {highlight['note']}*\n\n")
                f.write("---\n\n")
    
    print(f"Output files written to {output_dir}")

def create_safe_filename(text, max_length=100):
    """Convert text to a safe filename with a maximum length."""
    # Remove invalid characters and replace spaces with underscores
    safe = re.sub(r'[^\w\s-]', '', text).strip().lower()
    safe = re.sub(r'[-\s]+', '_', safe)
    
    # Truncate to max_length, ensuring it doesn't cut off mid-word
    if len(safe) > max_length:
        safe = safe[:max_length].rsplit('_', 1)[0]
    
    return safe

def main():
    """Main function."""
    args = parse_arguments()
    
    # Load data
    readwise_highlights = load_readwise_highlights(args.readwise_file)
    tana_structure = parse_tana_export(args.tana_file)
    tana_highlights, _ = extract_highlights_from_tana(args.tana_file)
    
    if not tana_structure:
        print("No structure found in Tana export. Exiting.")
        sys.exit(1)
    
    # Categorize highlights
    categories = categorize_highlights(readwise_highlights, tana_structure, tana_highlights)
    
    # Write output files
    write_output_files(categories, args.output_dir, [], [])
    
    print("Integration completed successfully!")

if __name__ == "__main__":
    main()