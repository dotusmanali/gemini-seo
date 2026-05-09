import os
import json
import sys

def main():
    print("🪝 Pre-audit hook: Initializing environment...")
    os.makedirs("output", exist_ok=True)
    os.makedirs(".seo-cache", exist_ok=True)
    print("✅ Pre-audit complete.")

if __name__ == "__main__":
    main()
