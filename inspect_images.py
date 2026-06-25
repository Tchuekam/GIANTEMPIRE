import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def inspect_page(filename):
    path = os.path.join(PROJECT_DIR, filename)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    print(f"\n--- IMAGES IN {filename} ---")
    imgs = re.findall(r'<img[^>]+>', content)
    for img in imgs:
        src = re.search(r'src="([^"]+)"', img)
        src_val = src.group(1) if src else "No src"
        cls = re.search(r'class="([^"]+)"', img)
        cls_val = cls.group(1) if cls else "No class"
        alt = re.search(r'alt="([^"]+)"', img)
        alt_val = alt.group(1) if alt else "No alt"
        print(f"Tag: {img[:80]}...\n  src: {src_val}\n  class: {cls_val}\n  alt: {alt_val}")

inspect_page("index.html")
inspect_page("life.html")
inspect_page("loves.html")
inspect_page("work.html")
