import os, glob, re

root_dir = r'c:\Users\CLINIC\.gemini\antigravity-ide\scratch\apple-clone'
# Match <a ... href="https://..." ...>
pattern = re.compile(r'(<a\s+[^>]*href=["\'])(https?://[^"\']*)(["\'])', re.IGNORECASE)

count = 0

def replace_link(match):
    prefix = match.group(1)
    url = match.group(2)
    suffix = match.group(3)
    
    # Check if URL is related to apple
    url_lower = url.lower()
    if 'apple' in url_lower or 'icloud' in url_lower or 'goldmansachs' in url_lower or 'itunes' in url_lower:
        return prefix + '#' + suffix
    return match.group(0)

for filepath in glob.glob(os.path.join(root_dir, '**', '*.html'), recursive=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(replace_link, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
    except Exception as e:
        pass

print(f'Replaced links in {count} HTML files.')
