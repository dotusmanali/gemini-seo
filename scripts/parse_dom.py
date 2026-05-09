import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

def parse_dom(url):
    print(f"🌳 Parsing DOM nodes for {url}")
    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto(url, wait_until="networkidle")
        
        # Inject JS to extract bounding boxes and styles
        nodes = page.evaluate("""() => {
            const elements = document.querySelectorAll('h1, h2, h3, p, a, button, img');
            const data = [];
            elements.forEach(el => {
                const rect = el.getBoundingClientRect();
                if (rect.width > 0 && rect.height > 0) {
                    const style = window.getComputedStyle(el);
                    data.push({
                        tag: el.tagName.toLowerCase(),
                        class: el.className,
                        id: el.id,
                        text_content: el.innerText.substring(0, 100).trim(),
                        font_size: style.fontSize,
                        color: style.color,
                        background_color: style.backgroundColor,
                        position_y: rect.top,
                        is_atf: rect.top < 800
                    });
                }
            });
            return data;
        }""")
        
        browser.close()
        return nodes

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target URL")
    args = parser.parse_args()

    nodes = parse_dom(args.url)
    
    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    out_file = out_dir / "homepage-parse.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"url": args.url, "nodes": nodes}, f, indent=2)
        
    print(f"✅ Extracted {len(nodes)} visible DOM nodes. Saved to {out_file}")

if __name__ == "__main__":
    main()