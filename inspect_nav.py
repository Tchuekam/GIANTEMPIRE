import re

with open(r'c:\Users\CLINIC\.gemini\antigravity-ide\scratch\apple-clone\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'(<ul[^>]*globalnav-list[^>]*>.*?</ul>)', content, re.DOTALL)
if m:
    nav_html = m.group(1)
    items = re.findall(r'<li[^>]*class="([^"]*globalnav-[^"]*)"[^>]*>.*?</li>', nav_html, re.DOTALL)
    for i, cls in enumerate(items):
        print(f'Item {i}: {cls}')
else:
    print("globalnav-list not found")
