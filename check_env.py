import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Python path:", sys.path)
try:
    from PIL import Image
    print("[OK] PIL import succeeded inside this script!")
except Exception as e:
    print("[ERROR] PIL import failed:", e)
