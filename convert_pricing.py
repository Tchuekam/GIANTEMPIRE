import os, glob, re

root_dir = r'c:\Users\CLINIC\.gemini\antigravity-ide\scratch\apple-clone'
# Pattern to match dollar amounts like $999, $1,099, $42.91
pattern = re.compile(r'\$([0-9]{1,3}(?:,?[0-9]{3})*(?:\.[0-9]{2})?)')

EXCHANGE_RATE = 600

def replacer(match):
    # Get the number part
    num_str = match.group(1)
    # Remove commas
    clean_num = num_str.replace(',', '')
    try:
        # Convert to float
        val = float(clean_num)
        # Convert to FCFA
        fcfa_val = val * EXCHANGE_RATE
        # Format FCFA with commas and no decimals
        fcfa_str = f"{int(fcfa_val):,} FCFA"
        return fcfa_str
    except ValueError:
        return match.group(0)

count = 0
for filepath in glob.glob(os.path.join(root_dir, '**', '*.*'), recursive=True):
    if filepath.endswith(('.html', '.js', '.json', '.txt')):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = pattern.sub(replacer, content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1
        except Exception as e:
            pass

print(f'Converted prices to FCFA in {count} files.')
