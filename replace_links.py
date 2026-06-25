import os, glob, re

root_dir = r'c:\Users\CLINIC\.gemini\antigravity-ide\scratch\apple-clone'
pattern = re.compile(r'https?://(?:[a-zA-Z0-9-]+\.)*apple\.com(?:[a-zA-Z0-9.-]*)(?:/[^\s"\'<>]*)?')
count = 0

for filepath in glob.glob(os.path.join(root_dir, '**', '*.*'), recursive=True):
    if filepath.endswith(('.html', '.js', '.json', '.txt', '.css')):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'apple.com' in content:
                new_content = pattern.sub('#', content)
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
        except Exception as e:
            pass
print(f'Replaced links with regex in {count} files.')
