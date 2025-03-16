import os
import json
import glob

def list_sources():
    """List all available sources"""
    sources = []
    
    # Search all source directories
    for source_type in ["books", "articles", "transcripts", "personal-notes"]:
        dir_path = os.path.join("sources", source_type)
        if os.path.exists(dir_path):
            json_files = glob.glob(os.path.join(dir_path, "*.json"))
            for json_file in json_files:
                with open(json_file, "r") as f:
                    source = json.load(f)
                    sources.append((source["id"], source["title"], source["author"]))
    
    # Print sources with numbers for selection
    for i, (id, title, author) in enumerate(sources, 1):
        print(f"{i}. {title} by {author}")
    
    return sources

def list_chapters():
    """List all chapters"""
    chapters = []
    
    # Get all chapter directories
    for part in ["part1-foundations", "part2-biblicism", "part3-atheism", "part4-apocalypticism"]:
        dir_path = os.path.join("chapters", part)
        if os.path.exists(dir_path):
            md_files = glob.glob(os.path.join(dir_path, "*.md"))
            for md_file in md_files:
                chapter_name = os.path.basename(md_file).replace(".md", "")
                chapters.append((md_file, chapter_name))
    
    # Print chapters with numbers for selection
    for i, (path, name) in enumerate(chapters, 1):
        print(f"{i}. {name}")
    
    return chapters

def connect_source_to_chapter():
    """Connect a source to a chapter"""
    print("Available sources:")
    sources = list_sources()
    
    if not sources:
        print("No sources found. Add sources first.")
        return
    
    source_num = int(input("\nSelect source number: "))
    source_id, source_title, source_author = sources[source_num-1]
    
    print("\nAvailable chapters:")
    chapters = list_chapters()
    
    if not chapters:
        print("No chapters found. Create chapter files first.")
        return
    
    chapter_num = int(input("\nSelect chapter number: "))
    chapter_path, chapter_name = chapters[chapter_num-1]
    
    relevance = input("\nDescribe how this source is relevant to this chapter: ")
    
    # Add the reference to the chapter file
    with open(chapter_path, "a") as f:
        f.write(f"\n## Source: {source_title}\n")
        f.write(f"Author: {source_author}\n")
        f.write(f"Relevance: {relevance}\n\n")
    
    print(f"Source '{source_title}' connected to chapter '{chapter_name}'")

if __name__ == "__main__":
    connect_source_to_chapter()