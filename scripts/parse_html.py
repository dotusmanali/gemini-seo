#!/usr/bin/env python3
"""
Parse HTML and extract SEO-relevant elements.
Ported and enhanced for Gemini CLI.
"""

import argparse
import json
import os
import re
import sys
from typing import Optional
from urllib.parse import urljoin, urlparse

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 required. Install with: pip install beautifulsoup4")
    sys.exit(1)

def parse_html(html: str, base_url: Optional[str] = None) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    result = {
        "title": None,
        "meta_description": None,
        "meta_robots": None,
        "canonical": None,
        "h1": [],
        "h2": [],
        "h3": [],
        "images": [],
        "links": {"internal": [], "external": []},
        "schema": [],
        "open_graph": {},
        "twitter_card": {},
        "word_count": 0,
        "hreflang": [],
    }

    title_tag = soup.find("title")
    if title_tag:
        result["title"] = title_tag.get_text(strip=True)

    for meta in soup.find_all("meta"):
        name = meta.get("name", "").lower()
        property_attr = meta.get("property", "").lower()
        content = meta.get("content", "")
        if name == "description":
            result["meta_description"] = content
        elif name == "robots":
            result["meta_robots"] = content
        if property_attr.startswith("og:"):
            result["open_graph"][property_attr] = content
        if name.startswith("twitter:"):
            result["twitter_card"][name] = content

    canonical = soup.find("link", rel="canonical")
    if canonical:
        result["canonical"] = canonical.get("href")

    for link in soup.find_all("link", rel="alternate"):
        hreflang = link.get("hreflang")
        if hreflang:
            result["hreflang"].append({"lang": hreflang, "href": link.get("href")})

    for tag in ["h1", "h2", "h3"]:
        for heading in soup.find_all(tag):
            text = heading.get_text(strip=True)
            if text:
                result[tag].append(text)

    for img in soup.find_all("img"):
        src = img.get("src", "")
        if base_url and src:
            src = urljoin(base_url, src)
        result["images"].append({
            "src": src,
            "alt": img.get("alt"),
            "width": img.get("width"),
            "height": img.get("height"),
            "loading": img.get("loading"),
        })

    if base_url:
        base_domain = urlparse(base_url).netloc
        for a in soup.find_all("a", href=True):
            href = a.get("href", "")
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            full_url = urljoin(base_url, href)
            parsed = urlparse(full_url)
            link_data = {"href": full_url, "text": a.get_text(strip=True)[:100], "rel": a.get("rel", [])}
            if parsed.netloc == base_domain:
                result["links"]["internal"].append(link_data)
            else:
                result["links"]["external"].append(link_data)

    for script in soup.find_all("script", type="application/ld+json"):
        try:
            schema_data = json.loads(script.string)
            if isinstance(schema_data, dict) and "@graph" in schema_data:
                result["schema"].extend(schema_data["@graph"])
            elif isinstance(schema_data, list):
                result["schema"].extend(schema_data)
            else:
                result["schema"].append(schema_data)
        except:
            pass

    # Simplified word count
    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r"\b\w+\b", text)
    result["word_count"] = len(words)

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse HTML for Gemini SEO")
    parser.add_argument("file", nargs="?", help="HTML file to parse")
    parser.add_argument("--url", "-u", help="Base URL")
    args = parser.parse_args()
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        html = sys.stdin.read()
    print(json.dumps(parse_html(html, args.url), indent=2))
