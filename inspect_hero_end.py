import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("Hero_container__inGFW")
if idx != -1:
    print("Found Hero_container__inGFW at:", idx)
    # Find next tags, for example the next div after the hero container
    print("=== Context after Hero_container__inGFW ===")
    # Let's write the first 5000 characters after the hero container starts to check where it ends.
    # We will write to a temp file because of encoding issues.
    with open("temp_hero_end.txt", "w", encoding="utf-8") as f_out:
        f_out.write(content[idx:idx + 10000])
    print("Saved to temp_hero_end.txt")
else:
    print("Not found")
