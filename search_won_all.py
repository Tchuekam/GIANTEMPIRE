import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def main():
    pages = ["index.html", "life.html", "loves.html", "work.html", "thoughts.html", "contact.html"]
    for page in pages:
        path = os.path.join(PROJECT_DIR, page)
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        matches = re.findall(r'.{0,40}[Ww][Oo][Nn].{0,40}', content)
        if matches:
            print(f"\nMatches in {page}:")
            for m in matches:
                print(repr(m))

if __name__ == "__main__":
    main()
