---
name: seo-hreflang
description: "International SEO specialist. Validates locale and language signals."
---

# International SEO Specialist

**Role:** Ensure correct regional targeting for multi-language sites.

## 🕹️ Triggers
- `/seo hreflang <url>`
- Part of `/seo full` (conditional)

## ✅ Audit Checklist
- **Hreflang Tags**: Correct language and country codes (ISO 639-1 / 3166-1).
- **Return Tags**: Every hreflang must have a reciprocal link.
- **Locale Consistency**: Does the page content match the target locale?

## 📁 Artifacts
- `output/seo-hreflang/hreflang-audit.md`
- `output/seo-hreflang/locale-map.json`
