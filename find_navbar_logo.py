import re, os, sys

sys.stdout.reconfigure(encoding='utf-8')

files_dir = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\Linear – The system for product development_files"
for fname in sorted(os.listdir(files_dir)):
    if not fname.endswith('.js.download'):
        continue
    fpath = os.path.join(files_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    patterns = [
        r'LinearIcon',
        r'LinearLogo', 
        r'logo.*home',
        r'home.*logo',
        r'BrandMark',
        r'brandMark',
        r'Wordmark',
        r'wordmark',
    ]
    for pat in patterns:
        matches = list(re.finditer(pat, content, re.IGNORECASE))
        if matches:
            for m in matches[:3]:
                start = max(0, m.start()-100)
                end = min(len(content), m.end()+300)
                print(f"=== {fname} - '{pat}' at pos {m.start()} ===")
                print(content[start:end])
                print()
