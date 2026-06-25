import os
import re

PROJECT_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone"

for filename in os.listdir(PROJECT_DIR):
    if filename.endswith(".html"):
        path = os.path.join(PROJECT_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Find hero__img div and its inner img tag
        matches = re.finditer(r'<div[^>]*class="[^"]*hero__img[^"]*"[^>]*>(.*?)</div>', content, re.DOTALL)
        print(f"\n--- {filename} ---")
        found = False
        for m in matches:
            found = True
            print("Container HTML:")
            print(m.group(0).strip())
        if not found:
            print("No hero__img container found")
