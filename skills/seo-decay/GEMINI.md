---
name: seo-decay
description: "Content Decay & Cannibalization Detector. Connects to Google Search Console to identify pages losing traffic over time and pages competing for the same keywords."
---

# 🍂 Content Decay Detector

**Role:** Traffic Retention Specialist
**Trigger:** `/seo decay <url>`

## 🕵️‍♂️ Audit Checklist
- [ ] **Content Decay:** Identify URLs that have lost > 20% traffic or impressions over the last 6 months.
- [ ] **Keyword Cannibalization:** Find queries where 2 or more URLs from the same domain are ranking.
- [ ] **Freshness Check:** Check "Last Modified" dates of declining content.
- [ ] **Revamp Strategy:** Suggest whether to Update, Merge, Redirect, or Delete decaying content.

## 📦 Artifacts
- **Output:** `output/seo-decay/content-decay-report.md`
- **Data:** `output/seo-decay/cannibalization-matrix.json`