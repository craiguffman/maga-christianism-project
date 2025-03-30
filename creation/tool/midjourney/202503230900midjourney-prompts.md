# Midjourney Prompts for Lexicon Header Images

## Base Lexicon Template Prompt

For all lexicon entries, start with this base prompt and then customize using the category variations below:

```
An elegant academic reference book opened to a dictionary entry, with a deep blue to medium blue gradient background, minimalist design, white typography, abstract connection nodes pattern in the corner, clean modern encyclopedia aesthetic --ar 3:1 --style raw --no text
```

## Category Variations

### Primary Concepts (Deep Blue)
For foundational terms like "Christianism" and "MAGA Christianism":

```
Add "--color #0A2463, #3E92CC" to the base prompt
```

### Historical Context (Blue-Purple)
For historical terms like "Christian Nationalism" and "Dominionism":

```
Add "--color #0A2463, #7251A3" to the base prompt
```

### Contemporary Movements (Blue-Teal)
For terms describing current phenomena like "Identity Synthesis":

```
Add "--color #0A2463, #2A9D8F" to the base prompt
```

## Optimization Tips

1. **Generate Multiple Options**: Always create 4-5 variations and select the cleanest, most abstract one
2. **Avoid Text**: Midjourney often creates gibberish text, so use the `--no text` parameter
3. **Maintain Consistency**: Use the same base image with color variations rather than generating completely different images for each entry
4. **Text Overlay**: After generating the image, add your text overlay in Canva or another design tool:
   - Title: "Christianism Lexicon"
   - Subtitle: "[Term Name]"
   - Optional: Small entry number in corner (e.g., "#01")

## Example Complete Prompt

```
An elegant academic reference book opened to a dictionary entry, with a deep blue to medium blue gradient background, minimalist design, white typography, abstract connection nodes pattern in the corner, clean modern encyclopedia aesthetic --ar 3:1 --style raw --no text --color #0A2463, #3E92CC
```

## Implementation Process

1. Generate the base image for each category (Primary, Historical, Contemporary)
2. Save each base image as a template
3. For each new lexicon entry:
   - Select the appropriate category template
   - Add text overlay in Canva with the specific term
   - Maintain consistent placement of all text elements
   - Export at 1200x400px resolution (optimal for Substack)

This approach creates a visually cohesive set of header images that immediately signal "reference content" to your readers while maintaining categorical distinctions through subtle color variations.
