import re

html_path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files\index.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace brand name globally (capitalized Linear)
content, count_capital = re.subn(r'\bLinear\b', 'GianTecH', content)
print(f"Replaced {count_capital} occurrences of capitalized '\\bLinear\\b' with 'GianTecH'.")

# 2. Replace linear.app domains
content, count_domain = re.subn(r'\blinear\.app\b', 'giantech.app', content)
print(f"Replaced {count_domain} occurrences of 'linear.app' with 'giantech.app'.")

# 3. Replace static.linear.app and webassets.linear.app
content, count_static = re.subn(r'\bstatic\.linear\.app\b', 'static.giantech.app', content)
content, count_webassets = re.subn(r'\bwebassets\.linear\.app\b', 'webassets.giantech.app', content)
print(f"Replaced {count_static} static.linear.app and {count_webassets} webassets.linear.app occurrences.")

# 4. Save file
with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Saved index.html.")
