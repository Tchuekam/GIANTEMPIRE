import re
import os

PROJECT_DIR = r"C:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

def main():
    path = os.path.join(PROJECT_DIR, "index.html")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all words containing "won" or "you" (case insensitive)
    matches = re.findall(r'.{0,40}[Ww][Oo][Nn].{0,40}', content)
    print("Matches for 'WON':")
    for m in matches:
        print(repr(m))

if __name__ == "__main__":
    main()
