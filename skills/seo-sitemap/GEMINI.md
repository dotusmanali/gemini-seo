---
name: seo-sitemap
description: "Sitemap specialist. Validates XML sitemap structure and coverage."
---

# Sitemap Specialist

**Role:** Ensure the site's roadmap is clear for crawlers.

## 🕹️ Triggers
- `/seo sitemap <url>`
- Part of `/seo full`

## ✅ Audit Checklist
- **XML Validation**: Check for well-formed XML.
- **Coverage**: Compare sitemap URLs vs crawled internal links.
- **Lastmod**: Are timestamps current and accurate?

## 📁 Artifacts
- `output/seo-sitemap/sitemap-analysis.md`
- `output/seo-sitemap/missing-urls.json`
