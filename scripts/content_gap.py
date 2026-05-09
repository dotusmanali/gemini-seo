import argparse
import json
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def extract_entities(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Simple entity extraction based on high-frequency nouns/keywords
        text = soup.get_text()
        words = re.findall(r'\w+', text.lower())
        # Filter common stopwords (simplified)
        stopwords = {'the', 'a', 'an', 'and', 'in', 'on', 'to', 'for', 'of', 'with', 'is', 'are', 'was', 'were'}
        keywords = [w for w in words if len(w) > 4 and w not in stopwords]
        return set([k[0] for k in Counter(keywords).most_common(20)])
    except:
        return set()

def main():
    parser = argparse.ArgumentParser(description="Semantic Content Gap Analyzer")
    parser.add_argument("--url", required=True, help="Your URL")
    parser.add_argument("--competitors", nargs='+', required=True, help="List of competitor URLs")
    args = parser.parse_args()

    print(f"🧠 Analyzing Semantic Content Gap for {args.url} vs {len(args.competitors)} competitors...")
    
    my_entities = extract_entities(args.url)
    all_comp_entities = set()
    
    for comp_url in args.competitors:
        print(f"🕵️ Analyzing competitor: {comp_url}")
        all_comp_entities.update(extract_entities(comp_url))
    
    gap = all_comp_entities - my_entities
    
    results = {
        "my_url": args.url,
        "competitors": args.competitors,
        "common_topics": list(my_entities.intersection(all_comp_entities)),
        "missing_topics": list(gap)[:10], # Top 10 missing
        "content_strategy_score": 100 - (len(gap) * 2)
    }
    
    out_dir = "outputs"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/content-gap.json", "w") as f:
        json.dump(results, f, indent=2)
        
    print(f"\n✅ Analysis complete! Found {len(gap)} missing semantic entities.")
    print(f"Top Gaps: {', '.join(list(gap)[:5])}")
    print(f"Results saved to outputs/content-gap.json")

if __name__ == "__main__":
    main()