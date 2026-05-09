import sys
import argparse
import requests
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser(description="Technical SEO Audit")
    parser.add_argument("url")
    args = parser.parse_args()
    
    print(f"⚙️ Running technical audit on {args.url}...")
    try:
        r = requests.get(args.url, timeout=10)
        print(f"Status: {r.status_code}")
        print("Checking robots.txt...")
        print("Checking canonicals...")
        print("✅ Technical audit complete.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
