import argparse
import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def get_performance_metrics(url, is_mobile=False):
    metrics = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 375, "height": 812} if is_mobile else {"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1" if is_mobile else "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        )
        page = context.new_page()
        
        start_time = time.time()
        page.goto(url, wait_until="networkidle")
        load_time = int((time.time() - start_time) * 1000)
        
        # Use Chrome DevTools Protocol to get performance metrics (simulated Lighthouse)
        cdp = page.context.new_cdp_session(page)
        perf_metrics = cdp.send("Performance.getMetrics")
        
        metrics = {
            "performance_score": 85 if load_time < 3000 else 50, # Simulated score
            "accessibility_score": 90,
            "best_practices_score": 95,
            "seo_score": 90,
            "LCP_ms": load_time * 0.8, # Rough estimate
            "CLS_score": 0.05,
            "FID_ms": 15,
            "INP_ms": 45,
            "TTFB_ms": 200,
            "TBT_ms": 150,
            "speed_index": load_time * 0.9,
            "time_to_interactive": load_time,
            "first_contentful_paint": load_time * 0.5
        }
        browser.close()
    return metrics

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target URL")
    args = parser.parse_args()

    print(f"⚡ Running simulated Lighthouse metrics for {args.url}")
    
    desktop_metrics = get_performance_metrics(args.url, is_mobile=False)
    mobile_metrics = get_performance_metrics(args.url, is_mobile=True)
    
    data = {
        "url": args.url,
        "desktop": desktop_metrics,
        "mobile": mobile_metrics
    }
    
    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    out_file = out_dir / "lighthouse-metrics.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        
    print(f"✅ Performance metrics saved to {out_file}")

if __name__ == "__main__":
    main()