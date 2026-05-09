import argparse
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path

def crawl(start_url, max_depth=3):
    visited = set()
    queue = [(start_url, 0)]
    results = []
    
    print(f"🕷️ Starting deep crawl for {start_url} (Max Depth: {max_depth})")
    
    while queue:
        current_url, depth = queue.pop(0)
        
        if current_url in visited or depth > max_depth:
            continue
            
        visited.add(current_url)
        print(f"Crawling [{depth}]: {current_url}")
        
        try:
            start_time = time.time()
            response = requests.get(current_url, timeout=10)
            load_time = int((time.time() - start_time) * 1000)
            
            page_data = {
                "url": current_url,
                "status": response.status_code,
                "page_load_time_ms": load_time
            }
            
            if response.status_code == 200 and 'text/html' in response.headers.get('Content-Type', ''):
                soup = BeautifulSoup(response.text, 'html.parser')
                
                title = soup.title.string if soup.title else ""
                page_data["title"] = title.strip() if title else ""
                page_data["title_length"] = len(page_data["title"])
                page_data["title_pixel_width"] = page_data["title_length"] * 7 # Estimate
                
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                page_data["meta_description"] = meta_desc['content'] if meta_desc and meta_desc.has_attr('content') else ""
                page_data["meta_description_length"] = len(page_data["meta_description"])
                
                canonical = soup.find('link', rel='canonical')
                page_data["canonical_url"] = canonical['href'] if canonical and canonical.has_attr('href') else ""
                
                robots = soup.find('meta', attrs={'name': 'robots'})
                page_data["robots_directive"] = robots['content'] if robots and robots.has_attr('content') else ""
                
                h1s = soup.find_all('h1')
                page_data["h1_count"] = len(h1s)
                page_data["h1_text"] = [h1.get_text(strip=True) for h1 in h1s]
                
                page_data["h2_list"] = [h2.get_text(strip=True) for h2 in soup.find_all('h2')]
                page_data["h3_list"] = [h3.get_text(strip=True) for h3 in soup.find_all('h3')]
                
                text_content = soup.get_text(separator=' ')
                page_data["word_count"] = len(text_content.split())
                
                links = soup.find_all('a', href=True)
                internal_links = [l['href'] for l in links if l['href'].startswith('/') or start_url in l['href']]
                external_links = [l['href'] for l in links if l['href'].startswith('http') and start_url not in l['href']]
                
                page_data["internal_links_count"] = len(internal_links)
                page_data["external_links_count"] = len(external_links)
                
                images = soup.find_all('img')
                page_data["image_count"] = len(images)
                page_data["images_missing_alt"] = len([img for img in images if not img.get('alt')])
                
                schemas = soup.find_all('script', type='application/ld+json')
                page_data["has_schema"] = len(schemas) > 0
                schema_types = []
                for s in schemas:
                    try:
                        s_data = json.loads(s.string)
                        if isinstance(s_data, dict):
                            schema_types.append(s_data.get('@type', 'Unknown'))
                        elif isinstance(s_data, list):
                            for item in s_data:
                                if isinstance(item, dict):
                                    schema_types.append(item.get('@type', 'Unknown'))
                    except:
                        pass
                page_data["schema_types_found"] = schema_types
                
                page_data["open_graph_present"] = soup.find('meta', property=lambda x: x and x.startswith('og:')) is not None
                page_data["twitter_card_present"] = soup.find('meta', attrs={'name': lambda x: x and x.startswith('twitter:')}) is not None
                
                # Queue internal links
                if depth < max_depth:
                    for link in internal_links:
                        full_url = urljoin(start_url, link)
                        if full_url not in visited:
                            queue.append((full_url, depth + 1))
                            
            results.append(page_data)
            
        except Exception as e:
            print(f"❌ Error crawling {current_url}: {e}")
            results.append({"url": current_url, "status": "ERROR", "error": str(e)})

    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--depth", type=int, default=3, help="Crawl depth")
    args = parser.parse_args()

    results = crawl(args.url, args.depth)
    
    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    out_file = out_dir / "crawl-all.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"pages": results}, f, indent=2)
        
    print(f"\n✅ Crawl complete. Processed {len(results)} pages. Saved to {out_file}")

if __name__ == "__main__":
    main()