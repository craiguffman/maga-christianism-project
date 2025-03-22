import os
import json
from datetime import datetime

def add_source():
    """Add a new source to the collection with metadata"""
    
    # Get source information
    title = input("Enter source title: ")
    author = input("Enter author: ")
    source_type = input("Enter source type (book, article, transcript, personal): ")
    relevance = input("How is this source relevant to your project? ")
    
    # Create a source ID (simplified version)
    source_id = title.lower().replace(" ", "-")[:30]
    
    # Create the source record
    source = {
        "id": source_id,
        "title": title,
        "author": author,
        "type": source_type,
        "added_date": datetime.now().strftime("%Y-%m-%d"),
        "relevance": relevance,
        "notes": []
    }
    
    # Save the source metadata
    save_dir = os.path.join("sources", source_type + "s")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    filename = os.path.join(save_dir, f"{source_id}.json")
    with open(filename, "w") as f:
        json.dump(source, f, indent=4)
    
    print(f"Source '{title}' added successfully!")
    
    # Create a template file for notes
    notes_dir = os.path.join("synthesis", "source-summaries")
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
    
    notes_file = os.path.join(notes_dir, f"{source_id}-notes.md")
    with open(notes_file, "w") as f:
        f.write(f"# Notes on {title}\n\n")
        f.write(f"Author: {author}\n\n")
        f.write("## Key Insights\n\n")
        f.write("## Relevant Quotes\n\n")
        f.write("## Application to Project\n\n")
    
    print(f"Note template created at '{notes_file}'")

if __name__ == "__main__":
    add_source()