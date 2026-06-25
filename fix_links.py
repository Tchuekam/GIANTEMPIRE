import os
import re

PROJECT_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"
pages = ["index.html", "life.html", "loves.html", "work.html", "thoughts.html", "contact.html"]

def fix_all_links():
    for page in pages:
        path = os.path.join(PROJECT_DIR, page)
        if not os.path.exists(path):
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace absolute links to pages
        # /work -> work.html
        # /life -> life.html
        # /loves -> loves.html
        # /thoughts -> thoughts.html
        # /contact -> contact.html
        content = re.sub(r'href="/work([^"]*)"', r'href="work.html\1"', content)
        content = re.sub(r'href="/life([^"]*)"', r'href="life.html\1"', content)
        content = re.sub(r'href="/loves([^"]*)"', r'href="loves.html\1"', content)
        content = re.sub(r'href="/thoughts([^"]*)"', r'href="thoughts.html\1"', content)
        content = re.sub(r'href="/contact([^"]*)"', r'href="contact.html\1"', content)
        
        # Replace thoughts articles (which we don't have, so point to thoughts.html)
        content = re.sub(r'href="/thoughts/[^"]+"', 'href="thoughts.html"', content)
        
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"[OK] Cleaned links in {page}")

if __name__ == "__main__":
    fix_all_links()
