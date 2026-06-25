import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
matches = re.findall(r'href=[\'\"]([^\'\"]*)[\'\"]', content)
social_urls = [m for m in matches if any(x in m for x in ['twitter', 'x.com', 'github', 'youtube', 'linkedin', 'mailto', 'linear.app'])]
print("SOCIAL URLS:", list(set(social_urls)))
