#!/usr/bin/env python3
"""
DEVONthink OPML Extractor for Dissertation Notes

This script extracts notes from DEVONthink OPML files, organizes them by key figures,
and splits them into manageable chunks that can be processed by AI assistants
or imported into other note-taking systems like Tana.

Usage:
    python devonthink_extractor.py input.opml [output_dir]

If output_dir is not specified, files will be saved in a directory named 
after the input file.
"""

import os
import sys
import xml.etree.ElementTree as ET
import json
from datetime import datetime
import re
import argparse
from pathlib import Path
from collections import defaultdict

# Maximum size for each chunk in characters
MAX_CHUNK_SIZE = 8000

# List of key figures to organize notes by
KEY_FIGURES = [
    "Hooker, Richard", 
    "Hauerwas, Stanley", 
    "Barth, Karl",
    "Augustine",
    "Balthasar, Hans Urs von",
    "Cary, Philip",
    "Lake, Peter",
    "Luther, Martin",
    "McIntosh, Mark",
    "Milbank, John",
    "Ockham, William",
    "Porter, Jean",
    "Shuger, Debora",
    "Tillich, Paul",
    "Webster, John",
    "Wells, Sam",
    "Williams, Rowan",
    "Woodard-Lehman, Derek",
    "Wright, N.T.",
    "Zagzeski, Linda"
]

# Alternative name formats to check
NAME_VARIANTS = {
    "Hooker, Richard": ["Richard Hooker", "Hooker", "Hooker Richard"],
    "Hauerwas, Stanley": ["Stanley Hauerwas", "Hauerwas", "Hauerwas Stanley"],
    "Barth, Karl": ["Karl Barth", "Barth", "Barth Karl"],
    "Augustine": ["St. Augustine", "Saint Augustine", "Augustine of Hippo"],
    "Balthasar, Hans Urs von": ["Hans Urs von Balthasar", "von Balthasar", "Balthasar", "Balthasar Hans Urs von"],
    "Cary, Philip": ["Philip Cary", "Cary", "Cary Philip"],
    "Lake, Peter": ["Peter Lake", "Lake", "Lake Peter"],
    "Luther, Martin": ["Martin Luther", "Luther", "Luther Martin"],
    "McIntosh, Mark": ["Mark McIntosh", "McIntosh", "McIntosh Mark"],
    "Milbank, John": ["John Milbank", "Milbank", "Milbank John"],
    "Ockham, William": ["William Ockham", "William of Ockham", "Ockham", "Ockham William"],
    "Porter, Jean": ["Jean Porter", "Porter", "Porter Jean"],
    "Shuger, Debora": ["Debora Shuger", "Debora K. Shuger", "Shuger", "Shuger Debora"],
    "Tillich, Paul": ["Paul Tillich", "Tillich", "Tillich Paul"],
    "Webster, John": ["John Webster", "Webster", "Webster John"],
    "Wells, Sam": ["Samuel Wells", "Sam Wells", "Wells", "Wells Sam"],
    "Williams, Rowan": ["Rowan Williams", "Williams", "Williams Rowan"],
    "Woodard-Lehman, Derek": ["Derek Woodard-Lehman", "Woodard-Lehman", "Woodard-Lehman Derek"],
    "Wright, N.T.": ["N.T. Wright", "N. T. Wright", "Nicholas Thomas Wright", "Tom Wright", "Wright", "Wright N.T."],
    "Zagzeski, Linda": ["Linda Zagzeski", "Zagzeski", "Zagzeski Linda"]
}

def parse_opml(opml_file):
    """Parse the OPML file and extract the outline structure"""
    try:
        tree = ET.parse(opml_file)
        root = tree.getroot()
        return root
    except ET.ParseError as e:
        print(f"Error parsing OPML file: {e}")
        sys.exit(1)

def extract_title(root):
    """Extract the title from the OPML file"""
    head = root.find('head')
    if head is not None:
        title_elem = head.find('title')
        if title_elem is not None:
            return title_elem.text
    return "Untitled"

def identify_figure_from_path(path):
    """
    Identify which key figure a note belongs to based on its path/hierarchy
    Returns the name of the figure or None if no match is found
    """
    path_lower = path.lower()
    
    # Check each key figure and their variants in the path
    for figure in KEY_FIGURES:
        # Check the main name in the path
        if figure.lower() in path_lower:
            return figure
        
        # Check name variants in the path
        if figure in NAME_VARIANTS:
            for variant in NAME_VARIANTS[figure]:
                if variant.lower() in path_lower:
                    return figure
    
    return None

def identify_figure(text, title, path):
    """
    Identify which key figure a note belongs to
    First tries to identify from path/hierarchy, then falls back to content analysis
    Returns the name of the figure or 'Other' if no match is found
    """
    # First try to identify based on path/hierarchy
    figure_from_path = identify_figure_from_path(path)
    if figure_from_path:
        return figure_from_path
    
    # If path doesn't provide a clear figure, analyze content
    # Combine title and the first few paragraphs of text for searching
    search_text = f"{title} {text[:500]}".lower()
    
    # Check each key figure and their variants
    for figure in KEY_FIGURES:
        # Check the main name
        if figure.lower() in search_text:
            return figure
        
        # Check name variants
        if figure in NAME_VARIANTS:
            for variant in NAME_VARIANTS[figure]:
                if variant.lower() in search_text:
                    return figure
    
    return "Other"

def process_outline(outline, parent_path=""):
    """
    Recursively process outline elements and extract notes
    Returns a list of note objects
    """
    notes = []
    
    # Extract information from the current outline element
    text = outline.get('text', '')
    title = outline.get('title', '')
    created = outline.get('created', '')
    modified = outline.get('modified', '')
    
    # If we have title content but no text, use the title as text
    if title and not text:
        text = title
    
    # Create the current path
    current_name = title if title else text.split('\n')[0][:50]  # Use first line of text if no title
    current_path = f"{parent_path}/{current_name}" if parent_path else current_name
    
    # Identify which figure this note belongs to using path first, then content
    figure = identify_figure(text, title, current_path)
    
    # Add the current note to the list if it has content
    if text:
        notes.append({
            'path': current_path,
            'title': title,
            'text': text,
            'created': created,
            'modified': modified,
            'figure': figure
        })
    
    # Process child outlines
    for child in outline.findall('outline'):
        notes.extend(process_outline(child, current_path))
    
    return notes

def split_large_notes(notes, max_size=MAX_CHUNK_SIZE):
    """Split notes that exceed the maximum size into multiple chunks"""
    chunked_notes = []
    
    for note in notes:
        text = note['text']
        # If the note is within the size limit, keep it as is
        if len(text) <= max_size:
            chunked_notes.append(note)
            continue
        
        # Split the note into paragraphs
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = []
        current_size = 0
        
        for paragraph in paragraphs:
            paragraph_size = len(paragraph) + 2  # +2 for the newlines
            
            # If adding this paragraph would exceed the limit, start a new chunk
            if current_size + paragraph_size > max_size and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [paragraph]
                current_size = paragraph_size
            else:
                current_chunk.append(paragraph)
                current_size += paragraph_size
        
        # Add the last chunk if there's any content left
        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))
        
        # Create a new note for each chunk
        for i, chunk in enumerate(chunks):
            chunked_note = note.copy()
            chunked_note['text'] = chunk
            chunked_note['path'] = f"{note['path']} (part {i+1}/{len(chunks)})"
            chunked_note['title'] = f"{note['title']} (part {i+1}/{len(chunks)})" if note['title'] else None
            chunked_notes.append(chunked_note)
    
    return chunked_notes

def save_notes(notes, output_dir):
    """Save notes to files in the specified directory, organized by key figure"""
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Group notes by figure
    notes_by_figure = defaultdict(list)
    for note in notes:
        notes_by_figure[note['figure']].append(note)
    
    # Mapping to keep track of filenames for the index
    file_mapping = {}
    total_count = 0
    
    # Process each figure group
    for figure, figure_notes in notes_by_figure.items():
        # Create a directory for this figure if it's not "Other"
        figure_dir = output_dir
        if figure != "Other":
            figure_dir = os.path.join(output_dir, re.sub(r'[<>:"/\\|?*]', '_', figure))
            os.makedirs(figure_dir, exist_ok=True)
        
        # Save individual notes for this figure
        for i, note in enumerate(figure_notes):
            total_count += 1
            # Create a filename based on the path
            safe_path = re.sub(r'[<>:"/\\|?*]', '_', note['path'])
            filename = f"{total_count:04d}_{safe_path}.txt"
            filepath = os.path.join(figure_dir, filename)
            
            # Store the relative path for the index
            rel_path = os.path.relpath(filepath, output_dir)
            file_mapping[total_count] = {
                'note': note,
                'filename': rel_path
            }
            
            # Write the note content to the file
            with open(filepath, 'w', encoding='utf-8') as f:
                if note['title']:
                    f.write(f"# {note['title']}\n\n")
                f.write(note['text'])
            
            print(f"Saved note: {filepath}")
        
        # Create a figure-specific metadata file
        if figure != "Other":
            fig_metadata_file = os.path.join(figure_dir, f"{figure}_metadata.json")
            with open(fig_metadata_file, 'w', encoding='utf-8') as f:
                json.dump(figure_notes, f, indent=2)
    
    # Save a complete metadata file with all notes information
    metadata_file = os.path.join(output_dir, "metadata.json")
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(notes, f, indent=2)
    
    print(f"Saved metadata: {metadata_file}")
    
    # Create a master index file for easier navigation
    index_file = os.path.join(output_dir, "index.md")
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# Dissertation Notes Index\n\n")
        
        # Create a section for each figure
        current_figure = None
        for i in range(1, total_count + 1):
            note = file_mapping[i]['note']
            filename = file_mapping[i]['filename']
            
            # Add a header if we're starting a new figure
            if note['figure'] != current_figure:
                current_figure = note['figure']
                f.write(f"\n## {current_figure}\n\n")
            
            path_display = note['path']
            f.write(f"{i}. [{path_display}]({filename})\n")
    
    print(f"Created index: {index_file}")
    
    # Create separate index files for key figures
    for figure in notes_by_figure:
        if figure != "Other" and notes_by_figure[figure]:
            figure_dir = os.path.join(output_dir, re.sub(r'[<>:"/\\|?*]', '_', figure))
            figure_index = os.path.join(figure_dir, "index.md")
            
            with open(figure_index, 'w', encoding='utf-8') as f:
                f.write(f"# {figure} Notes\n\n")
                
                for i in range(1, total_count + 1):
                    if i in file_mapping and file_mapping[i]['note']['figure'] == figure:
                        note = file_mapping[i]['note']
                        # Use a relative path from the figure directory
                        local_filename = os.path.basename(file_mapping[i]['filename'])
                        path_display = note['path']
                        f.write(f"{i}. [{path_display}]({local_filename})\n")
            
            print(f"Created figure index: {figure_index}")

def create_import_guide(output_dir, original_file, title, figure_counts):
    """Create a guide for how to use the extracted files"""
    guide_file = os.path.join(output_dir, "README.md")
    with open(guide_file, 'w', encoding='utf-8') as f:
        f.write(f"# {title} - Dissertation Notes Extraction Guide\n\n")
        f.write(f"Original file: {original_file}\n")
        f.write(f"Extracted on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Organization\n\n")
        f.write("Notes have been organized by key figures in your dissertation:\n\n")
        
        # List the figures and their note counts
        for figure, count in figure_counts.items():
            if figure != "Other":
                safe_figure = re.sub(r'[<>:"/\\|?*]', '_', figure)
                f.write(f"- [{figure}]({safe_figure}/index.md) - {count} notes\n")
        
        # List the "Other" category if it exists
        if "Other" in figure_counts:
            f.write(f"- Other - {figure_counts['Other']} notes\n")
        
        f.write("\n## Contents\n\n")
        f.write("1. Individual note files (.txt) organized in directories by figure\n")
        f.write("2. metadata.json - Complete metadata for all notes\n")
        f.write("3. index.md - A navigable master index of all notes\n")
        f.write("4. Figure-specific indexes in each figure's directory\n\n")
        
        f.write("## Using These Files\n\n")
        
        f.write("### For Your Book Research:\n")
        f.write("- Navigate to the directory of the key figure you're researching\n")
        f.write("- Upload individual .txt files to AI assistants as needed\n")
        f.write("- Upload the figure's index.md to provide context about available materials\n\n")
        
        f.write("### Working with AI Assistants:\n")
        f.write("- For specific inquiries about a figure, upload the figure's directory contents\n")
        f.write("- For broader research questions, use the master index.md to identify relevant files\n")
        f.write("- Start with smaller, focused uploads and add more context as needed\n\n")
        
        f.write("### Future Tana Integration:\n")
        f.write("- The metadata.json file contains all hierarchical information needed for a Tana import\n")
        f.write("- Each note includes its original path, creation date, and modification date\n")
        f.write("- Figure assignments can be used to organize notes in Tana workspaces\n")
    
    print(f"Created guide: {guide_file}")

def main():
    parser = argparse.ArgumentParser(description='Extract and organize dissertation notes from DEVONthink OPML files')
    parser.add_argument('opml_file', help='Path to the OPML file')
    parser.add_argument('output_dir', nargs='?', help='Directory to save extracted notes (optional)')
    args = parser.parse_args()
    
    opml_file = args.opml_file
    
    # If no output directory is specified, create one based on the input filename
    if args.output_dir:
        output_dir = args.output_dir
    else:
        base_name = os.path.splitext(os.path.basename(opml_file))[0]
        output_dir = f"{base_name}_extracted"
    
    print(f"Processing {opml_file}...")
    root = parse_opml(opml_file)
    title = extract_title(root)
    print(f"Title: {title}")
    
    # Process the outlines
    body = root.find('body')
    if body is None:
        print("Error: No body element found in OPML file")
        sys.exit(1)
    
    notes = []
    for outline in body.findall('outline'):
        notes.extend(process_outline(outline))
    
    print(f"Found {len(notes)} notes")
    
    # Split large notes into smaller chunks
    chunked_notes = split_large_notes(notes)
    print(f"After chunking: {len(chunked_notes)} notes")
    
    # Count notes by figure
    figure_counts = defaultdict(int)
    for note in chunked_notes:
        figure_counts[note['figure']] += 1
    
    # Print figure distribution
    print("\nNotes distribution by figure:")
    for figure, count in sorted(figure_counts.items()):
        print(f"  {figure}: {count} notes")
    
    # Save the notes to files, organized by figure
    save_notes(chunked_notes, output_dir)
    
    # Create a guide for using the extracted files
    create_import_guide(output_dir, opml_file, title, figure_counts)
    
    print(f"\nExtraction complete. Files saved to {output_dir}")
    print(f"Notes are organized in directories by key figures.")
    
    # Provide specific usage instructions
    print("\nTo use with AI assistants:")
    print("1. Navigate to a specific figure's directory (e.g., 'Wells_Sam')")
    print("2. Upload individual text files or the figure's index.md")
    print("3. Ask questions related to that figure's work and ideas")
    
    print("\nFor comprehensive queries:")
    print("1. Start with the master index.md to identify relevant notes")
    print("2. Upload specific notes based on your research needs")

if __name__ == "__main__":
    main()
