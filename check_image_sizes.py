import os
from PIL import Image

IMAGES_DIR = r"c:\Users\CLINIC\.gemini\antigravity-ide\scratch\portfolio-clone\images"

for filename in os.listdir(IMAGES_DIR):
    if filename.lower().endswith((".webp", ".png", ".jpg", ".jpeg")):
        path = os.path.join(IMAGES_DIR, filename)
        try:
            img = Image.open(path)
            w, h = img.size
            aspect = w / h
            print(f"{filename}: {w}x{h} (Aspect: {aspect:.5f})")
        except Exception as e:
            print(f"Error reading {filename}: {e}")
