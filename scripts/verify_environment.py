import sys
import platform
import subprocess

def check_env():
    print("🔍 Verifying Environment...")
    
    # Python
    py_version = sys.version_info
    if py_version.major == 3 and py_version.minor >= 10:
        print(f"✅ Python {py_version.major}.{py_version.minor} detected.")
    else:
        print(f"❌ Python 3.10+ required. Found {py_version.major}.{py_version.minor}")

    # Node
    try:
        node_v = subprocess.check_output(["node", "-v"]).decode().strip()
        print(f"✅ Node.js {node_v} detected.")
    except:
        print("❌ Node.js not found.")

    # Playwright
    try:
        import playwright
        print("✅ Playwright library found.")
    except ImportError:
        print("❌ Playwright library missing.")

    print("\n🚀 System ready for gemini-seo.")

if __name__ == "__main__":
    check_env()
