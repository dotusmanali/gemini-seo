import argparse
import sys
import subprocess
import requests
import os
from pathlib import Path

def check_python_version():
    if sys.version_info < (3, 9):
        print("❌ Error: Python 3.9+ is required.")
        sys.exit(1)
    print("✅ Python version 3.9+ confirmed.")

def install_dependencies():
    packages = ["requests", "playwright", "beautifulsoup4", "lxml"]
    print("📦 Checking and installing required packages...")
    for pkg in packages:
        try:
            __import__(pkg if pkg != "beautifulsoup4" else "bs4")
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    
    # Ensure playwright browsers are installed
    subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
    print("✅ All dependencies installed.")

def verify_url(url):
    try:
        print(f"🔍 Verifying target URL: {url}")
        response = requests.head(url, allow_redirects=True, timeout=10)
        response.raise_for_status()
        print("✅ Target URL is reachable.")
    except Exception as e:
        print(f"❌ Error: Cannot reach target URL: {e}")
        sys.exit(1)

def setup_directories():
    dirs = ["outputs", "outputs/screenshots"]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    print("✅ Output directories prepared.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target URL to audit")
    args = parser.parse_args()

    print("\n--- Pre-Audit Environment Check ---")
    check_python_version()
    install_dependencies()
    verify_url(args.url)
    setup_directories()
    print("-----------------------------------\n")

if __name__ == "__main__":
    main()