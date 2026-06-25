import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def inspect_media():
    path = os.path.join(PROJECT_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Main Hero Image (hero-3)
    print("--- HERO IMG SEARCH ---")
    hero_imgs = re.findall(r'<img[^>]+hero-3[^>]+>', content)
    for img in hero_imgs:
        print(img)
        
    # Any image in hero__img
    print("\n--- HERO__IMG DIV CONTENT ---")
    hero_divs = re.findall(r'<div class="hero__img[^"]*">.*?</div>', content)
    for div in hero_divs:
        print(div)
        
    # 2. Other image tags on Home Page
    print("\n--- ALL OTHER IMGS ---")
    imgs = re.findall(r'<img[^>]+>', content)
    for img in imgs:
        if "logo.png" not in img:
            print(img[:120])
            
    # 3. Video tags on Home Page
    print("\n--- VIDEOS ---")
    vids = re.findall(r'<video[^>]*>.*?</video>', content)
    for vid in vids:
        print(vid[:200])
        
    # Background video sources
    sources = re.findall(r'<source[^>]+src="([^"]+)"', content)
    for src in sources:
        print("SOURCE SRC:", src)

inspect_media()
