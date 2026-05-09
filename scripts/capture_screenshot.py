import argparse
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

def capture_and_analyze(url):
    print(f"📸 Capturing visual intelligence for {url}")
    
    out_dir = Path("outputs/screenshots")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    full_path = out_dir / "full_page.png"
    atf_path = out_dir / "atf_800px.png"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.goto(url, wait_until="networkidle")
        
        page.screenshot(path=str(atf_path))
        page.screenshot(path=str(full_path), full_page=True)
        
        # Analyze ATF using JS
        analysis = page.evaluate("""() => {
            const atfElements = Array.from(document.querySelectorAll('*')).filter(el => {
                const rect = el.getBoundingClientRect();
                return rect.top < 800 && rect.width > 0 && rect.height > 0;
            });
            
            const hasH1 = atfElements.some(el => el.tagName === 'H1');
            const hasButton = atfElements.some(el => el.tagName === 'BUTTON' || (el.tagName === 'A' && el.className.includes('btn')));
            
            return {
                hero_has_text: hasH1,
                hero_has_cta: hasButton,
                atf_content_density: atfElements.length > 50 ? "high" : "medium",
                estimated_cls_risk: document.querySelectorAll('img:not([width])').length > 0 ? "high" : "low",
                visual_hierarchy_score: hasH1 ? 8 : 4
            };
        }""")
        
        browser.close()
        return analysis

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target URL")
    args = parser.parse_args()

    analysis = capture_and_analyze(args.url)
    analysis["url"] = args.url
    
    out_dir = Path("outputs")
    out_file = out_dir / "visual-analysis.json"
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(analysis, f, indent=2)
        
    print(f"✅ Visual analysis complete. Saved to {out_file} and outputs/screenshots/")

if __name__ == "__main__":
    main()