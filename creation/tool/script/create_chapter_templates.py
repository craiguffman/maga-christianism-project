import os

# Chapter structure based on your outline
chapters = {
    "part1-foundations": [
        "introducing-crisis-maga-christianism",
        "trinitarian-foundation-christian-identity",
        "knowledge-of-god",
        "formation-of-virtue"
    ],
    "part2-biblicism": [
        "ramist-realism",
        "scriptures-authority-reconsidered",
        "priority-of-the-particular",
        "appeals-to-timeless-absolutes"
    ],
    "part3-atheism": [
        "reinhold-niebuhr-american-pragmatism",
        "christ-as-supreme-exemplar",
        "practices-vs-principles",
        "church-as-alternative-community"
    ],
    "part4-apocalypticism": [
        "justification-theory-discontents",
        "friend-enemy-distinctions",
        "fear-of-other-vs-love-of-neighbor",
        "third-way-christian-humanism"
    ]
}

def create_chapter_templates():
    """Create template files for all chapters"""
    for part, section_chapters in chapters.items():
        # Create part directory if it doesn't exist
        part_dir = os.path.join("chapters", part)
        if not os.path.exists(part_dir):
            os.makedirs(part_dir)
        
        # Create each chapter file
        for chapter in section_chapters:
            chapter_path = os.path.join(part_dir, f"{chapter}.md")
            
            # Only create if it doesn't exist
            if not os.path.exists(chapter_path):
                with open(chapter_path, "w") as f:
                    title = chapter.replace("-", " ").title()
                    f.write(f"# {title}\n\n")
                    f.write("## Chapter Overview\n\n")
                    f.write("## Key Arguments\n\n")
                    f.write("## Sources to Incorporate\n\n")
                    f.write("## Personal Reflection\n\n")
                
                print(f"Created template for '{title}'")

if __name__ == "__main__":
    create_chapter_templates()