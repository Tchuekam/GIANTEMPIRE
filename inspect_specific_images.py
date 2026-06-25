import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def inspect_site_images(filename):
    path = os.path.join(PROJECT_DIR, filename)
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all images hosted on the primary Webflow project cdn
    site_imgs = set(re.findall(r'https://cdn\.prod\.website-files\.com/644918964e907d2eeb9e57a0/[^\s"\'>]+', content))
    print(f"\nSite-level Webflow Assets in {filename}:")
    for img in sorted(site_imgs):
        print(img)

for page in ["index.html", "life.html", "loves.html", "work.html", "contact.html"]:
    inspect_site_images(page)
