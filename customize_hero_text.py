import os

path = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\index.html"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace main loader text attributes
content = content.replace('loader-text-1="Rebel"', 'loader-text-1="Genius"')
content = content.replace('loader-text-2="Entrepreneur"', 'loader-text-2="Tech Preneur"')
content = content.replace('loader-text-3="Disruptor"', 'loader-text-3="AI Architect"')
content = content.replace('loader-text-4="Designer"', 'loader-text-4="Fullstack Dev"')

# Replace hero title lists
content = content.replace('Rebel<br/>', 'Genius<br/>')
content = content.replace('Entrepreneur<br/>', 'Tech Preneur<br/>')
content = content.replace('Disruptor<br/>', 'AI Architect<br/>')
content = content.replace('Designer<br/>', 'Fullstack Dev<br/>')

# Replace the passion text
content = content.replace(
    'My passion is creating meaningful products for the world that solves real problems, delights users and exceeds expectations.',
    'My passion is building production-grade, secure, local-first AI systems that solve real workflow gaps, automate business processes, and exceed expectations.'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("[OK] Hero text and categories customized successfully in index.html!")
