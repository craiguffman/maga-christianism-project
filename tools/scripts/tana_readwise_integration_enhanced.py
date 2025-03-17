#!/usr/bin/env python3

import argparse
import json
import os
import re
import sys
from datetime import datetime

# Define content type maps for both legacy and new systems
CONTENT_TYPE_MAP = {
    # Legacy system
    "#permanent_note": "note",
    "#claim": "note",
    "#question": "question",
    "#evidence": "note",
    "#quote": "quote",
    
    # New SN(A)CK system
    "#highlight": "highlight",
    "#summary": "note",
    "#note": "note",
    "#analysis": "note",
    "#connection": "note",
    "#key": "note"
}

# Define priority order for content types
CONTENT_TYPE_PRIORITY = [
    # New SN(A)CK system (higher priority)
    "#highlight",
    "#summary",
    "#note",
    "#analysis",
    "#connection",
    "#key",
    
    # Legacy system
    "#quote",
    "#evidence",
    "#claim",
    "#question",
    "#permanent_note"
]

def extract_tags(content):
    """Extract both legacy and SN(A)CK format tags from content."""
    # Pattern for both legacy tags and SN(A)CK format tags
    legacy_pattern = r'#[a-zA-Z0-9_/-]+'
    snack_pattern = r'#[a-zA-Z0-9_/-]+\s+SN\(A\)CK'
    
    # Combine patterns and find all matches
    all_tags = re.findall(legacy_pattern, content)
    
    # Add SNACK format tags if they exist
    snack_tags = re.findall(snack_pattern, content)
    
    # Return combined list of tags
    return list(set(all_tags + snack_tags))

def determine_content_type(tags):
    """Determine the content type based on tags from either system."""
    # Process tags to handle SN(A)CK format
    processed_tags = []
    for tag in tags:
        if "SN(A)CK" in tag:
            # Get the tag part before SN(A)CK
            base_tag = tag.split()[0]
            processed_tags.append(base_tag)
        else:
            processed_tags.append(tag)
    
    # Find all matching content type tags
    content_types = [tag for tag in processed_tags if tag in CONTENT_TYPE_MAP]
    
    # If multiple content types are found, use priority order
    if len(content_types) > 1:
        for content_type in CONTENT_TYPE_PRIORITY:
            if content_type in content_types:
                return CONTENT_TYPE_MAP[content_type]
    
    # If one content type is found, use it
    if len(content_types) == 1:
        return CONTENT_TYPE_MAP[content_types[0]]
    
    # Default to note if no content type tag is found
    return "note"

def clean_content(content):
    """Clean content by removing all tags."""
    # Replace legacy tags
    cleaned = re.sub(r'#[a-zA-Z0-9_/-]+', '', content)
    
    # Replace SN(A)CK format tags
    cleaned = re.sub(r'#[a-zA-Z0-9_/-]+\s+SN\(A\)CK', '', cleaned)
    
    return cleaned.strip()

def get_topic_tags(tags):
    """Get topic tags (non-content-type tags) from either system."""
    topic_tags = []
    
    for tag in tags:
        # Check if it's a SN(A)CK format tag
        if "SN(A)CK" in tag:
            base_tag = tag.split()[0]
            if base_tag not in CONTENT_TYPE_MAP:
                # Remove the # prefix
                topic_tags.append(base_tag[1:])
        elif tag not in CONTENT_TYPE_MAP:
            # Remove the # prefix
            topic_tags.append(tag[1:])
    
    return topic_tags

def expand_nested_tags(tags):
    """Expand hierarchical/nested tags."""
    expanded_tags = []
    
    for tag in tags:
        # Check if it's a hierarchical tag
        if '/' in tag:
            # Add the full tag
            expanded_tags.append(tag)
            
            # Add each level of the hierarchy
            parts = tag.split('/')
            current = ''
            
            for i, part in enumerate(parts):
                if i == 0:
                    current = part
                else:
                    current += '/' + part
                
                # Add each level if it's not already included
                if current != tag and current not in expanded_tags:
                    expanded_tags.append(current)
        else:
            # Non-hierarchical tag
            expanded_tags.append(tag)
    
    return expanded_tags

def process_content_blocks(content):
    """Process content into logical blocks handling multi-line and quotes."""
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
        
        # Check if this line has content tags
        has_tags = False
        for tag in extract_tags(trimmed_line):
            # For legacy tags
            if tag in CONTENT_TYPE_MAP:
                has_tags = True
                break
            
            # For SN(A)CK format
            if "SN(A)CK" in tag:
                base_tag = tag.split()[0]
                if base_tag in CONTENT_TYPE_MAP:
                    has_tags = True
                    break
        
        # If we find a line with content tags and it's not part of a block quote,
        # it might indicate the end of the current block
        if has_tags and not is_block_quote_line and len(current_block) > 1:
            # If the previous line didn't have tags, split here
            prev_line_has_tags = False
            if i > 0:
                for tag in extract_tags(lines[i-1]):
                    if tag in CONTENT_TYPE_MAP or (
                        "SN(A)CK" in tag and tag.split()[0] in CONTENT_TYPE_MAP
                    ):
                        prev_line_has_tags = True
                        break
            
            if not prev_line_has_tags:
                blocks.append('\n'.join(current_block[:-1]))
                current_block = [trimmed_line]
    
    # Don't forget the last block
    if current_block:
        blocks.append('\n'.join(current_block))
    
    return [block for block in blocks if block.strip()]

def parse_content_block(block):
    """Parse a content block into a Readwise-compatible object."""
    tags = extract_tags(block)
    content_type = determine_content_type(tags)
    highlight_text = clean_content(block)
    topic_tags = get_topic_tags(tags)
    expanded_tags = expand_nested_tags(topic_tags)
    
    return {
        "text": highlight_text,
        "tags": expanded_tags,
        "note": "",
        "location": 0,
        "location_type": "",
        "highlighted_at": datetime.now().isoformat(),
        "highlight_type": content_type
    }

def process_tana_file(file_path):
    """Process a Tana export file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process the content into blocks
        content_blocks = process_content_blocks(content)
        
        # Parse each block into a Readwise-compatible object
        highlights = [
            parse_content_block(block) for block in content_blocks if block.strip()
        ]
        
        return {"highlights": highlights}
    
    except Exception as e:
        print(f"Error processing file {file_path}: {str(e)}")
        sys.exit(1)

def save_readwise_json(data, output_path):
    """Save processed data to a JSON file for Readwise import."""
    try:
        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write the output file
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Successfully processed {len(data['highlights'])} highlights")
        print(f"Output written to: {output_path}")
    
    except Exception as e:
        print(f"Error saving output file: {str(e)}")
        sys.exit(1)

def integrate_tana_readwise(tana_file, readwise_file, output_dir):
    """Integrate Tana exports with Readwise format."""
    # Process the Tana file
    highlights_data = process_tana_file(tana_file or readwise_file)
    
    # Generate output filename
    filename = os.path.basename(tana_file or readwise_file)
    output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.json")
    
    # Save the output
    save_readwise_json(highlights_data, output_file)
    
    return output_file

def main():
    parser = argparse.ArgumentParser(description='Process Tana exports for Readwise integration')
    parser.add_argument('--tana-file', help='Path to the Tana export file')
    parser.add_argument('--readwise-file', help='Path to the file to be imported into Readwise')
    parser.add_argument('--output-dir', required=True, help='Output directory for processed files')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    
    args = parser.parse_args()
    
    if not args.tana_file and not args.readwise_file:
        print("Error: Either --tana-file or --readwise-file must be provided")
        parser.print_help()
        sys.exit(1)
    
    # Process the integration
    output_file = integrate_tana_readwise(args.tana_file, args.readwise_file, args.output_dir)
    
    print(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    main()