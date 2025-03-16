import os
import re
import json
from datetime import datetime

def parse_tana_export(tana_md_path):
    """Extract chapter structure, atomic notes, and synthesis notes from Tana export"""
    with open(tana_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the book structure from "Structural Order"
    structure_pattern = r'- \*\*Structural Order\*\*:([\s\S]*?)(?=\n  - \S|\Z)'
    structure_match = re.search(structure_pattern, content)
    
    book_structure = {}
    if structure_match:
        structure_text = structure_match.group(1).strip()
        # Parse the nested structure
        book_structure = parse_nested_structure(structure_text)
    
    # Extract atomic notes
    atomic_note_pattern = r'(.*?) \(Book.*?\) #atomic_note_-_SN\(A\)CK([\s\S]*?)(?=\n        -|\Z)'
    atomic_notes = re.findall(atomic_note_pattern, content)
    
    parsed_atomic_notes = []
    for note_text, note_content in atomic_notes:
        # Clean up the note text
        note_text = note_text.strip()
        
        # Try to extract section information
        section_match = re.search(r'\(([^,]+), __', note_text)
        section = section_match.group(1) if section_match else "Uncategorized"
        
        parsed_atomic_notes.append({
            'text': note_text,
            'content': note_content,
            'section': section
        })
    
    # Extract synthesis notes
    synthesis_note_pattern = r'(.*?) \(Book.*?\) #synthesis_note-SN\(A\)CK([\s\S]*?)(?=\n        -|\Z)'
    synthesis_notes = re.findall(synthesis_note_pattern, content)
    
    parsed_synthesis_notes = []
    for note_text, note_content in synthesis_notes:
        # Clean up the note text
        note_text = note_text.strip()
        
        # Try to extract section information
        section_match = re.search(r'\(([^,]+), __', note_text)
        section = section_match.group(1) if section_match else "Uncategorized"
        
        parsed_synthesis_notes.append({
            'text': note_text,
            'content': note_content,
            'section': section
        })
    
    return {
        'structure': book_structure,
        'atomic_notes': parsed_atomic_notes,
        'synthesis_notes': parsed_synthesis_notes
    }

def extract_readwise_highlights(markdown_path):
    """Extract highlights from a Readwise markdown export"""
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match highlight pattern based on your format
    highlight_pattern = r'- (.*?)(?=\n-|\n\n|\Z)'
    matches = re.findall(highlight_pattern, content, re.DOTALL)
    
    highlights = []
    for match in matches:
        # Skip metadata lines like "**Tags:**"
        if match.strip().startswith('**Tags:**'):
            continue
            
        # Extract the highlight text
        highlight_text = match.strip()
        
        # Extract location if available
        location_match = re.search(r'\(\[Location (\d+)\]', highlight_text)
        location = int(location_match.group(1)) if location_match else 0
        
        # Extract tags if available
        tag_match = re.search(r'\*\*Tags:\*\* (#\w+)', highlight_text)
        tags = [tag_match.group(1)] if tag_match else []
        
        # Clean the highlight text (remove location and tags info)
        clean_text = re.sub(r'\(\[Location.*?\)\)', '', highlight_text)
        clean_text = re.sub(r'\s+- \*\*Tags:\*\*.*', '', clean_text)
        
        highlights.append({
            'text': clean_text.strip(),
            'location': location,
            'tags': tags
        })
    
    # Sort highlights by location
    highlights.sort(key=lambda x: x['location'])
    
    return highlights

def parse_nested_structure(text, indent=0):
    """Parse indented structure text into a nested dictionary"""
    lines = text.split('\n')
    structure = {}
    current_key = None
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Count leading spaces to determine indentation level
        spaces = len(line) - len(line.lstrip())
        level = spaces // 2  # Assuming 2 spaces per indentation level
        
        if level == indent:
            # This is a section at current level
            current_key = line.strip()
            structure[current_key] = {}
        elif level > indent and current_key:
            # This belongs to a subsection
            if not isinstance(structure[current_key], dict):
                structure[current_key] = {}
            
            # Gather all lines at this indentation or deeper for recursive parsing
            sub_lines = [line]
            i = lines.index(line) + 1
            while i < len(lines):
                next_line = lines[i]
                if not next_line.strip():
                    i += 1
                    continue
                next_spaces = len(next_line) - len(next_line.lstrip())
                next_level = next_spaces // 2
                if next_level >= level:
                    sub_lines.append(next_line)
                    i += 1
                else:
                    break
            
            sub_structure = parse_nested_structure('\n'.join(sub_lines), level)
            structure[current_key].update(sub_structure)
    
    return structure

def flatten_structure(structure, prefix=""):
    """Convert nested structure to flat list of sections with their full paths"""
    flat_sections = []
    
    for key, value in structure.items():
        section_path = f"{prefix}{key}" if prefix else key
        flat_sections.append(section_path)
        
        if isinstance(value, dict) and value:
            nested_sections = flatten_structure(value, f"{section_path} > ")
            flat_sections.extend(nested_sections)
    
    return flat_sections

def assign_highlights_to_sections(highlights, flat_sections, locations_file=None):
    """Assign highlights to book sections based on location ranges"""
    section_ranges = {}
    
    # If a locations file exists, load it
    if locations_file and os.path.exists(locations_file):
        with open(locations_file, 'r') as f:
            section_ranges = json.load(f)
    else:
        # Otherwise, define section ranges interactively
        print("\n=== DEFINING LOCATION RANGES FOR CHAPTERS ===")
        print("For each book section, you'll need to provide the location range.")
        print("This will help organize highlights into the correct sections.")
        
        for section in flat_sections:
            print(f"\nSection: {section}")
            try:
                start = int(input("  Enter starting location: "))
                end = int(input("  Enter ending location: "))
                section_ranges[section] = (start, end)
            except ValueError:
                print("  Skipping this section (invalid input)")
        
        # Save the ranges for future use
        if locations_file:
            with open(locations_file, 'w') as f:
                json.dump(section_ranges, f, indent=2)
    
    # Assign highlights to sections
    organized_highlights = {section: [] for section in flat_sections}
    organized_highlights["Uncategorized"] = []
    
    for highlight in highlights:
        location = highlight['location']
        if location == 0:
            organized_highlights["Uncategorized"].append(highlight)
            continue
        
        assigned = False
        for section, (start, end) in section_ranges.items():
            if start <= location <= end:
                organized_highlights[section].append(highlight)
                assigned = True
                break
        
        if not assigned:
            organized_highlights["Uncategorized"].append(highlight)
    
    return organized_highlights

def save_integrated_notes(source_id, structure, organized_highlights, atomic_notes, synthesis_notes):
    """Create integrated notes document with highlights and notes organized by chapter structure"""
    output_file = f'synthesis/source-summaries/{source_id}-integrated.md'
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w') as f:
        f.write(f"# Integrated Notes: {source_id}\n")
        f.write(f"*Generated on {datetime.now().strftime('%Y-%m-%d')}*\n\n")
        
        # Flatten the structure for easier processing
        flat_sections = flatten_structure(structure)
        
        # Process each section
        for section in flat_sections:
            f.write(f"## {section}\n\n")
            
            # Add highlights for this section
            if section in organized_highlights and organized_highlights[section]:
                f.write("### Highlights\n\n")
                for highlight in organized_highlights[section]:
                    f.write(f"> {highlight['text']}\n\n")
                    if highlight['tags']:
                        f.write(f"**Tags**: {', '.join(highlight['tags'])}\n\n")
            
            # Add atomic notes for this section
            section_atomic_notes = [note for note in atomic_notes if note['section'] == section]
            if section_atomic_notes:
                f.write("### Atomic Notes\n\n")
                for note in section_atomic_notes:
                    f.write(f"**{note['text']}**\n\n")
            
            # Add synthesis notes for this section
            section_synthesis_notes = [note for note in synthesis_notes if note['section'] == section]
            if section_synthesis_notes:
                f.write("### Synthesis Notes\n\n")
                for note in section_synthesis_notes:
                    f.write(f"**{note['text']}**\n\n")
            
            f.write("\n---\n\n")
        
        # Add uncategorized content
        f.write("## Uncategorized Content\n\n")
        
        if "Uncategorized" in organized_highlights and organized_highlights["Uncategorized"]:
            f.write("### Highlights\n\n")
            for highlight in organized_highlights["Uncategorized"]:
                f.write(f"> {highlight['text']}\n\n")
                if highlight['tags']:
                    f.write(f"**Tags**: {', '.join(highlight['tags'])}\n\n")
        
        # Add uncategorized notes
        uncategorized_atomic = [note for note in atomic_notes if note['section'] == "Uncategorized"]
        if uncategorized_atomic:
            f.write("### Atomic Notes\n\n")
            for note in uncategorized_atomic:
                f.write(f"**{note['text']}**\n\n")
        
        uncategorized_synthesis = [note for note in synthesis_notes if note['section'] == "Uncategorized"]
        if uncategorized_synthesis:
            f.write("### Synthesis Notes\n\n")
            for note in uncategorized_synthesis:
                f.write(f"**{note['text']}**\n\n")
    
    print(f"Integrated notes saved to {output_file}")

def write_structure_to_file(structure, file_path):
    """Save the book structure to a file"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, 'w') as f:
        f.write("# Book Structure\n\n")
        write_nested_structure(f, structure)
    
    print(f"Book structure saved to {file_path}")

def write_nested_structure(file, structure, level=0):
    """Write nested structure to file with proper indentation"""
    for key, value in structure.items():
        file.write('  ' * level + f"- {key}\n")
        if isinstance(value, dict) and value:
            write_nested_structure(file, value, level + 1)

def main():
    print("===== Tana and Readwise Integration Tool =====")
    
    # Get source ID
    source_id = input("Enter the source ID (e.g., ages-of-american-capitalism): ")
    
    # Get Tana export path
    tana_path = input("Enter path to Tana export file: ")
    if not os.path.exists(tana_path):
        print(f"Error: Tana file not found at {tana_path}")
        return
    
    # Get Readwise export path
    readwise_path = input("Enter path to Readwise export file: ")
    if not os.path.exists(readwise_path):
        print(f"Error: Readwise file not found at {readwise_path}")
        return
    
    # Parse Tana export for structure and notes
    print("\nParsing Tana export for structure and notes...")
    tana_data = parse_tana_export(tana_path)
    
    # Parse Readwise export for highlights
    print("Parsing Readwise export for highlights...")
    highlights = extract_readwise_highlights(readwise_path)
    
    # Save the book structure
    structure_file = f'sources/books/{source_id}/{source_id}-structure.md'
    write_structure_to_file(tana_data['structure'], structure_file)
    
    # Flatten the structure for highlight organization
    flat_sections = flatten_structure(tana_data['structure'])
    print(f"\nFound {len(flat_sections)} sections in the book structure")
    print(f"Found {len(highlights)} highlights from Readwise")
    print(f"Found {len(tana_data['atomic_notes'])} atomic notes")
    print(f"Found {len(tana_data['synthesis_notes'])} synthesis notes")
    
    # Define location ranges for sections and organize highlights
    locations_file = f'sources/books/{source_id}/{source_id}-locations.json'
    organized_highlights = assign_highlights_to_sections(highlights, flat_sections, locations_file)
    
    # Save integrated notes
    save_integrated_notes(
        source_id, 
        tana_data['structure'], 
        organized_highlights, 
        tana_data['atomic_notes'], 
        tana_data['synthesis_notes']
    )
    
    print("\nIntegration complete!")

if __name__ == "__main__":
    main()