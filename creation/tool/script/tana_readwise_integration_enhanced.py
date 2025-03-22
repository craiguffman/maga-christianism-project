#!/usr/bin/env python3
"""
Tana-Readwise Integration Script

This script integrates Readwise exports (Markdown) with Tana exports (Markdown)
to organize highlights according to the structure defined in Tana.

Usage:
    python tana_readwise_integration_enhanced_fixed.py \
        --readwise-file path/to/file.md \
        --output-dir path/to/output_directory \
        --verbose

Updated to handle multiple Tana tagging formats:
1. Modern Tana formats (SN(A)CK system): #highlight_-_SN(A)CK, etc.
2. Legacy Tana formats: #permanent_note, #claim, #question, etc.
3. Older legacy formats: #highlight_-_22-3, #claim_(Tanarian_Brain), etc.
"""

import argparse
import os
import re
import sys
from datetime import datetime

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Process Tana exports for organization')
    parser.add_argument('--readwise-file', required=True, help='Path to file to process')
    parser.add_argument('--tana-file', help='Path to Tana export markdown file (optional)')
    parser.add_argument('--output-dir', required=True, help='Path to output directory')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    return parser.parse_args()

def verbose_log(message, verbose_mode=False):
    """Log messages when in verbose mode."""
    if verbose_mode:
        print(f"[INFO] {message}")

def load_readwise_highlights(file_path):
    """Load highlights from a Readwise export markdown file."""
    try:
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
    except Exception as e:
        print(f"Error loading highlights from {file_path}: {e}")
        return []

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
            
            print("Warning: Could not find 'Structural Order' or alternative structure in Tana export.")
            print("Using flat structure for organization.")
            return [{'path': ['Content'], 'text': 'Content'}]
        
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
        print("Using default flat structure.")
        return [{'path': ['Content'], 'text': 'Content'}]

def extract_highlights_from_file(file_path, verbose=False):
    """Extract highlights and notes from file, supporting different tag formats."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        all_notes = []
        
        # Process content into logical blocks for better extraction
        blocks = extract_content_blocks(content, verbose)
        
        if verbose:
            print(f"Found {len(blocks)} content blocks in the file")
        
        legacy_count = 0
        modern_count = 0
        older_legacy_count = 0
        
        # Process each block to find various tag types
        for block in blocks:
            # 1. Check for older legacy format (e.g., #highlight_-_22-3)
            older_legacy_match = re.search(r'#(highlight|claim|permanent_note|fleeting_note|quote|evidence|question)(?:_-_\d+-\d+|\s*\([^)]+\)|_-_[^#\s]+)', block)
            if older_legacy_match:
                note_type = older_legacy_match.group(1)
                cleaned_content = clean_block_content(block)
                all_notes.append({
                    'type': note_type,
                    'content': cleaned_content
                })
                older_legacy_count += 1
                continue
            
            # 2. Check for modern SN(A)CK format
            modern_match = re.search(r'#(\w+)_-_SN\(A\)CK', block)
            if modern_match:
                note_type = modern_match.group(1)
                cleaned_content = clean_block_content(block)
                all_notes.append({
                    'type': note_type,
                    'content': cleaned_content
                })
                modern_count += 1
                continue
            
            # 3. Check for legacy format (#permanent_note, #claim, etc.)
            legacy_match = re.search(r'#(permanent_note|claim|question|evidence|quote)\b', block)
            if legacy_match:
                note_type = legacy_match.group(1)
                cleaned_content = clean_block_content(block)
                all_notes.append({
                    'type': note_type,
                    'content': cleaned_content
                })
                legacy_count += 1
                continue
            
            # 4. Find square bracketed highlights with Tana links
            highlights_pattern = re.compile(r'\[(.*?)\]\(https://app\.tana\.inc\?nodeid=.*?\)')
            highlight_matches = highlights_pattern.findall(block)
            if highlight_matches:
                for h in highlight_matches:
                    all_notes.append({
                        'type': 'highlight',
                        'content': h.strip()
                    })
                    modern_count += 1
        
        if verbose:
            print(f"Found {older_legacy_count} older legacy format notes (e.g., #highlight_-_22-3)")
            print(f"Found {modern_count} modern format notes (SN(A)CK system)")
            print(f"Found {legacy_count} legacy format notes (#permanent_note, etc.)")
        
        print(f"Extracted {len(all_notes)} total notes/highlights from file")
        
        return all_notes, []  # Return all as "highlights" for simplicity
    except Exception as e:
        print(f"Error extracting highlights from file: {e}")
        sys.exit(1)

def extract_content_blocks(content, verbose=False):
    """Process content into logical blocks for better extraction."""
    lines = content.split('\n')
    blocks = []
    current_block = []
    in_block_quote = False
    
    for i, line in enumerate(lines):
        trimmed_line = line.strip()
        
        # Skip empty lines
        if trimmed_line == '':
            # If we were building a block, finish it
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
                in_block_quote = False
            continue
        
        # Handle block quotes
        is_block_quote_line = trimmed_line.startswith('>')
        
        # Check if this is the start of a new block or continuation
        if (not current_block or 
            (is_block_quote_line and not in_block_quote) or 
            (not is_block_quote_line and in_block_quote)):
            # If we were building a block, finish it
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
            
            # Start a new block
            current_block.append(trimmed_line)
            in_block_quote = is_block_quote_line
        else:
            # Continue current block
            current_block.append(trimmed_line)
        
        # Check if this line has any content type tags
        has_tags = any(tag in trimmed_line for tag in [
            '#permanent_note', '#claim', '#question', '#evidence', '#quote', '#highlight', 
            '#summary', '#note', '#analysis', '#connection', '#key', 
            '#highlight_-_22-3', '#claim_(Tanarian_Brain)', '#fleeting_note_-_SN(A)CK'
        ])
        
        # If we find a line with tags and it's not part of a block quote,
        # it might indicate the end of the current block
        if has_tags and not is_block_quote_line and len(current_block) > 1:
            # If the previous line didn't have tags, split here
            prev_line_has_tags = i > 0 and any(tag in lines[i-1] for tag in [
                '#permanent_note', '#claim', '#question', '#evidence', '#quote', '#highlight', 
                '#summary', '#note', '#analysis', '#connection', '#key',
                '#highlight_-_22-3', '#claim_(Tanarian_Brain)', '#fleeting_note_-_SN(A)CK'
            ])
            
            if not prev_line_has_tags:
                blocks.append('\n'.join(current_block[:-1]))
                current_block = [trimmed_line]
    
    # Don't forget the last block
    if current_block:
        blocks.append('\n'.join(current_block))
    
    return [block for block in blocks if block.strip()]

def clean_block_content(block):
    """Clean the content by removing all tag patterns."""
    # Remove various tag formats
    cleaned = block
    
    # Remove regular tags
    cleaned = re.sub(r'#[a-zA-Z0-9_/-]+\b', '', cleaned)
    
    # Remove SN(A)CK format tags
    cleaned = re.sub(r'#[a-zA-Z0-9_/-]+\s+SN\(A\)CK', '', cleaned)
    
    # Remove older legacy format tags (#highlight_-_22-3, #claim_(Tanarian_Brain))
    cleaned = re.sub(r'#[a-zA-Z0-9_/-]+(?:_-_\d+-\d+|\([^)]+\))', '', cleaned)
    
    return cleaned.strip()

def categorize_highlights(file_highlights, tana_structure, tana_highlights):
    """Categorize highlights according to structure."""
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
    
    # Combine all highlights for processing
    all_highlights = file_highlights + tana_highlights
    
    # Categorize all highlights
    for highlight in all_highlights:
        # For each highlight, find the best matching category
        best_match = None
        best_match_score = 0
        
        for path_key, category in categories.items():
            # Calculate a matching score 
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
            'type': highlight.get('type', 'highlight'),
            'source': highlight.get('source', 'file')
        })
    
    return categories

def write_output_files(categories, output_dir, verbose=False):
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
                source_tag = f"[{highlight.get('source', 'file')}]" if 'source' in highlight else ""
                type_tag = f"[{highlight.get('type', 'highlight')}]" if 'type' in highlight else ""
                tags = f"{source_tag} {type_tag}".strip()
                
                f.write(f"### {highlight.get('text', '')}  \n")
                if tags:
                    f.write(f"*Tags: {tags}*\n\n")
                if 'note' in highlight and highlight['note']:
                    f.write(f"*Note: {highlight['note']}*\n\n")
                f.write("---\n\n")
    
    print(f"Output files written to {output_dir}")
    if verbose:
        print(f"Created index file: {index_path}")
        print(f"Created {sum(1 for _, cat in categories.items() if len(cat['highlights']) > 0)} category files")

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
    verbose = args.verbose
    
    # Load highlights from file
    file_highlights = []
    
    # Extract highlights and notes directly from the file
    file_highlights, _ = extract_highlights_from_file(args.readwise_file, verbose)
    
    # If Tana file is provided, use it for structure and additional highlights
    if args.tana_file:
        tana_structure = parse_tana_export(args.tana_file)
        tana_highlights, _ = extract_highlights_from_file(args.tana_file, verbose)
    else:
        # If no Tana file, use a simple flat structure and no additional highlights
        print("No Tana file provided. Using only file highlights with a flat structure.")
        tana_structure = [{'path': ['Content'], 'text': 'Content'}]
        tana_highlights = []
    
    # Categorize highlights
    categories = categorize_highlights(file_highlights, tana_structure, tana_highlights)
    
    # Write output files
    write_output_files(categories, args.output_dir, verbose)
    
    print("Integration completed successfully!")

if __name__ == "__main__":
    main()