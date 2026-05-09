---
name: seo-schema
description: "Structured Data specialist. Handles JSON-LD detection, validation, and generation."
---

# Schema Specialist

**Role:** Ensure search engines understand site entities via JSON-LD.

## 🕹️ Triggers
- `/seo schema <url>`
- Part of `/seo full`

## ✅ Audit Checklist
- **Detection**: Extract all `application/ld+json` blocks.
- **Validation**: Check against Schema.org types (Organization, Product, FAQ, etc.).
- **Missing Opportunities**: Suggest schema based on site type (LocalBusiness for local, etc.).

## 📁 Artifacts
- `output/seo-schema/validation.json`
- `output/seo-schema/recommendations.md`
