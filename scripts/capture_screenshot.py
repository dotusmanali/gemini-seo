import asyncio
import sys
import os
from playwright.async_api import async_playwright

async def capture(url, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 GeminiSEO/2.0"
        )
        page = await context.new_page()
        try:
            await page.goto(url, timeout=60000, wait_until="networkidle")
            # Wait a bit for animations to settle
            await asyncio.sleep(2)
            await page.screenshot(path=output_path, full_page=False)
            print(f"Screenshot saved to {output_path}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python capture_screenshot.py [url] [output_path]")
        sys.exit(1)
    
    url = sys.argv[1]
    output = sys.argv[2]
    asyncio.run(capture(url, output))
