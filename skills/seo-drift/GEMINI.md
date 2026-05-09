---
name: seo-drift
description: "SEO Drift specialist. Monitors changes in SEO elements over time."
---

# SEO Drift Specialist

**Role:** Detect regressions in SEO metadata and structure.

## 🕹️ Triggers
- `/seo drift baseline <url>`
- `/seo drift compare <url>`
- Part of `/seo full`

## ✅ Audit Checklist
- **Title/Meta Changes**: Has the optimized metadata been overwritten?
- **Canonical Changes**: Detect accidental changes to preferred URLs.
- **Schema Removal**: Check if structured data has disappeared.

## 📁 Artifacts
- `output/seo-drift/drift-report.md`
- `.seo-cache/baseline.json`
