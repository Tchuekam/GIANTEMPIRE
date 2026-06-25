import re
import os

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# find body and display the first 2000 characters
main_start = content.find("<main")
if main_start != -1:
    print("MAIN START:")
    print(content[main_start:main_start+8000])
else:
    print("No <main> tag found")
