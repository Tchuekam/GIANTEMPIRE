import os
import re

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Print hero section
hero_match = re.search(r'<div[^>]*class="[^"]*hero is--home[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>\s*</header>', content, re.DOTALL)
if hero_match:
    print("--- FINAL HERO SECTION ---")
    print(hero_match.group(0))
else:
    # fallback to printing name and title tags
    print("Hero container not matched exactly by regex. Printing parts:")
    name_match = re.search(r'<div[^>]*class="[^"]*hero__name[^"]*"[^>]*>.*?</div>', content, re.DOTALL)
    if name_match:
        print("Hero Name:", name_match.group(0))
    img_match = re.search(r'<div[^>]*class="[^"]*hero__img[^"]*"[^>]*>.*?</div>', content, re.DOTALL)
    if img_match:
        print("Hero Img Container:", img_match.group(0))
