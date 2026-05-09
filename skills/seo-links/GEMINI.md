---
name: seo-links
description: "AI Internal Link Grapher. Crawls the site to build a map of internal links, identifies orphaned pages, calculates 'link juice' flow, and suggests optimal anchor text for new internal links."
---

# 🕸️ AI Internal Link Grapher

**Role:** Site Architecture & Link Flow Optimizer
**Trigger:** `/seo links <url>`

## 🕵️‍♂️ Audit Checklist
- [ ] **Orphaned Pages:** Identify pages with 0 incoming internal links.
- [ ] **Click Depth:** Find pages that take > 3 clicks to reach from the homepage.
- [ ] **Link Juice Distribution:** Identify high-authority pages that should be linking to priority targets.
- [ ] **Anchor Text Cannibalization:** Check if the same anchor text is pointing to different URLs.
- [ ] **Opportunity Mapping:** Suggest 10 new internal links with exact source URL, target URL, and suggested anchor text.

## 📦 Artifacts
- **Output:** `output/seo-links/internal-link-graph.md`
- **Data:** `output/seo-links/link-matrix.json`