import os
import re

PROJECT_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

for filename in os.listdir(PROJECT_DIR):
    if filename.endswith(".html"):
        path = os.path.join(PROJECT_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        matches = re.findall(r'aspect="([^"]+)"', content)
        if matches:
            print(f"{filename}: {matches}")
