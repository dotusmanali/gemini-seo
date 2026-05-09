import requests
from bs4 import BeautifulSoup
import sys
import json

def crawl_site(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        for a in soup.find_all('a', href=True):
            links.append(a['href'])
            
        return {
            "url": url,
            "status": response.status_code,
            "title": soup.title.string if soup.title else "No Title",
            "links_count": len(links),
            "meta_description": soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else "No Meta Description"
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crawl_site.py [url]")
        sys.exit(1)
    
    url = sys.argv[1]
    result = crawl_site(url)
    print(json.dumps(result, indent=2))
