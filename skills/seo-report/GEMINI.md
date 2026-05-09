---
name: seo-report
description: "Interactive HTML Report Generator. Compiles audit JSON data into a beautiful, shareable HTML report mimicking high-end PDF audits."
---

# 📊 SEO Report Generator

**Role:** Report Presentation Engine
**Trigger:** `/seo report <url>`

## 🕵️‍♂️ Action Checklist
- [ ] **Ingest Data:** Read combined output JSONs from `.seo-cache/` or `/output/full/SUMMARY.json`.
- [ ] **Compile Template:** Inject data into the Tailwind-powered HTML template.
- [ ] **Save Artifact:** Output a standalone HTML file that can be opened in any browser or printed to PDF natively.

## 📦 Artifacts
- **Output:** `output/report/[url]_audit_report.html`