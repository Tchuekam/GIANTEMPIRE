import os
try:
    from PIL import Image, ImageOps, ImageFilter
    print("[OK] Pillow is installed")
except ImportError:
    print("[WARNING] Pillow is NOT installed")
