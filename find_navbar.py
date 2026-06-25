import sys, re
sys.stdout.reconfigure(encoding='utf-8')

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the navbar/header area in the body HTML
# Look for "Navigate to home" or "logoLink" or the nav element
patterns = [
    'Navigate to home',
    'logoLink',
    'logoItem',
    'Log in',
    'Sign up',
]

for pat in patterns:
    idx = content.find(pat)
    if idx != -1:
        start = max(0, idx - 300)
        end = min(len(content), idx + 300)
        print(f"=== '{pat}' found at pos {idx} ===")
        print(content[start:end])
        print()
    else:
        print(f"'{pat}' NOT found in HTML")
