import os
import json
import re
import markdown
from datetime import datetime

def parse_tana_export(tana_md_path):
    """Parse a markdown export from Tana containing atomic notes"""
    with open(tana_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into individual notes
    # Assuming each note starts with a heading (# or ## etc.)
    note_pattern = r'(#+\s+.+?\n)(.+?)(?=#+\s+|\Z)'
    notes = re.findall(note_pattern, content, re.DOTALL)
    
    parsed_notes = []
    for heading, content in notes:
        note = {
            'title': heading.strip('#').strip(),
            'content': content.strip(),
            'tags': []
        }
        
        # Extract tags from content
        tag_pattern = r'#(\w+[-\w]*)'
        tags = re.findall(tag_pattern, content)
        note['tags'] = tags
        
        parsed_notes.append(note)
    
    return parsed_notes

def integrate_notes_with_source(source_id, tana_notes):
    """Integrate Tana notes with your source in the project"""
    # Load source metadata
    source_path = f'sources/books/{source_id}.json'
    with open(source_path, 'r') as f:
        source = json.load(f)
    
    # Update the notes file
    notes_file = f'synthesis/source-summaries/{source_id}-notes.md'
    
    # Prepare content to append
    current_date = datetime.now().strftime("%Y-%m-%d")
    tana_section = f"\n## Atomic Notes (imported from Tana on {current_date})\n\n"
    
    for note in tana_notes:
        tana_section += f"### {note['title']}\n\n"
        tana_section += f"{note['content']}\n\n"
        if note['tags']:
            tana_section += f"**Tags**: {', '.join(['#'+tag for tag in note['tags']])}\n\n"
    
    # Append to the existing notes file
    with open(notes_file, 'a') as f:
        f.write(tana_section)
    
    print(f"Added {len(tana_notes)} notes from Tana to {notes_file}")

def main():
    print("Tana Notes Integrator")
    
    # Ask for the source ID
    source_id = input("Enter the source ID (e.g., ages-of-american-capitalism): ")
    
    # Ask for the path to the Tana export
    tana_export_path = input("Enter the path to your Tana markdown export: ")
    
    if os.path.exists(tana_export_path):
        tana_notes = parse_tana_export(tana_export_path)
        print(f"Found {len(tana_notes)} notes in the Tana export")
        
        integrate_notes_with_source(source_id, tana_notes)
        print("Integration complete!")
    else:
        print(f"Error: File {tana_export_path} not found")

if __name__ == "__main__":
    main()
