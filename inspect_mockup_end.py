import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\giantech_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Search for Frame_wrapper___hKDg or Bleed_root__EzNZN after index 142142
idx_bleed = content.find("Bleed_root__EzNZN")
if idx_bleed != -1:
    # Let's find the closing tags and the next sibling
    # The mockup is very large, let's find the text that comes after the mockup.
    # What are the headings again?
    # - "A new species of product tool."
    idx_next_heading = content.find("A new species of product tool.")
    print("Found 'A new species of product tool.' at:", idx_next_heading)
    if idx_next_heading != -1:
        # Write context around the transition between the mockup and the next section
        with open("temp_mockup_end.txt", "w", encoding="utf-8") as f_out:
            f_out.write(content[idx_next_heading - 1500:idx_next_heading + 1000])
        print("Saved transition context to temp_mockup_end.txt")
else:
    print("Bleed_root__EzNZN not found")
