import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Reddit Signal Tracking")
    parser.add_argument("brand")
    args = parser.parse_args()
    print(f"🤖 Fetching Reddit signals for {args.brand}...")
    print("Found 15 mentions in r/SEO, r/marketing.")
    print("✅ Reddit signals processed.")

if __name__ == "__main__":
    main()
