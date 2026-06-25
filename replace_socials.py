import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Twitter, GitHub, YouTube
content = content.replace('https://x.com/linear', 'https://x.com/RTchuek88935')
content = content.replace('https://twitter.com/linear', 'https://x.com/RTchuek88935')
content = content.replace('https://github.com/linear', 'https://github.com/Tchuekam')
content = content.replace('https://www.youtube.com/@linear', 'https://www.youtube.com/@Giantech-Empire')
content = content.replace('https://youtube.com/@linear', 'https://www.youtube.com/@Giantech-Empire')

# Let's add LinkedIn, Email, Phone
# Find the YouTube li element to append the new links
yt_li = '<li class="Footer_sectionItem__lDqAK"><a class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/@Giantech-Empire">YouTube</a></li>'

new_links = """<li class="Footer_sectionItem__lDqAK"><a class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" target="_blank" rel="noopener noreferrer" href="https://www.linkedin.com/in/tchuekam-rostand/">LinkedIn</a></li><li class="Footer_sectionItem__lDqAK"><a class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" href="mailto:tchuekrostand@gmail.com">tchuekrostand@gmail.com</a></li><li class="Footer_sectionItem__lDqAK"><a class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" href="tel:+237659248952">+237659248952</a> / <a class="Footer_sectionLink__yuXh6 Link_root__cNtak Link_variant-dimmed__kvcr0" href="tel:+237653683174">+237653683174</a></li>"""

content = content.replace(yt_li, yt_li + new_links)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced social links in index.html")
