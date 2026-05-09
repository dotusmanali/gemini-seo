import sys
import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Capture SEO Baseline")
    parser.add_argument("url")
    args = parser.parse_args()
    print(f"📸 Capturing baseline for {args.url}...")
    os.makedirs(".seo-cache", exist_ok=True)
    baseline = {"url": args.url, "title": "Mock Title", "canonical": args.url}
    with open(".seo-cache/baseline.json", "w") as f:
        json.dump(baseline, f)
    print("✅ Baseline captured.")

if __name__ == "__main__":
    main()
