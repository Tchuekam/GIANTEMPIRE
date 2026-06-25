import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def main():
    path = os.path.join(PROJECT_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Let's find the exact text in index.html around hero image
    match = re.search(r'<div[^>]*class="[^"]*hero__img[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)
    if match:
        print("FOUND HERO__IMG DIV CONTENT:")
        print(match.group(0))
    else:
        print("hero__img div not found")
        
    # Let's search for the text "WON J. YOU" or "WON" in index.html
    large_text = re.findall(r'<div[^>]*class="[^"]*f-1190[^"]*"[^>]*>.*?</div>', content)
    print("\nLarge text elements (loader/f-1190):")
    for elem in large_text:
        print(elem)
        
    hero_text = re.findall(r'<div[^>]*class="[^"]*f-750[^"]*"[^>]*>.*?</div>', content)
    print("\nHero text elements (f-750):")
    for elem in hero_text:
        print(elem[:200])

if __name__ == "__main__":
    main()
