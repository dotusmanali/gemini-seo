---
name: seo-audit
description: "Full SEO audit orchestration. Coordinates technical, content, visual, and schema agents."
---

# Full SEO Audit Workflow

When triggered via `/seo audit <url>`:

1. **Phase 1: Intelligence Gathering**
   - Run `python scripts/fetch_page.py <url>` to get raw HTML and headers.
   - Run `python scripts/parse_html.py` on the result to extract SEO elements.
   - Run `python scripts/capture_screenshot.py <url> .seo-cache/desktop.png` for visual analysis.

2. **Phase 2: Specialized Analysis**
   - **Technical**: Load `references/technical-checklist.md` and `references/cwv-thresholds.md`. Check indexability, sitemaps, and robots.txt.
   - **Content**: Load `references/eeat-framework.md`. Evaluate experience, expertise, and authority signals.
   - **Visual**: Use Gemini's vision capability to analyze `.seo-cache/desktop.png`. Focus on Above the Fold (ATF), CLS, and CTA visibility.
   - **Schema**: Validate existing JSON-LD and suggest missing blocks (Organization, LocalBusiness, etc.).

3. **Phase 3: Scoring & Action Plan**
   - Calculate category scores.
   - Generate `SEO-HEALTH-REPORT.md` with:
     - Health Score (0-100)
     - Executive Summary
     - Critical Fixes (High impact, Low effort)
     - Long-term Strategy
     - AEO/GEO readiness score.

4. **Phase 4: Implementation (Gemini Specific)**
   - Offer to fix technical issues immediately using the `replace` tool.
   - Example: "I found a missing alt tag on your logo. Would you like me to fix it now?"
