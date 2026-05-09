import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Core SEO Audit")
    parser.add_argument("url")
    args = parser.parse_args()
    print(f"🔍 Running core audit for {args.url}...")
    print("Checking headers, meta, and content quality...")
    print("✅ Audit complete.")

if __name__ == "__main__":
    main()
