---
name: gemini-seo
description: "Tier 4 SEO Analysis Suite for Gemini CLI. Multimodal visual audits, technical SEO, E-E-A-T, AEO/GEO, and direct code implementation. Ported from AgriciDaniel/claude-seo with Gemini-native enhancements."
---

# Gemini SEO: Advanced SEO Suite

**Gemini SEO** is a high-performance SEO analysis and optimization toolset. It leverages Gemini's long context window and native multimodal (vision) capabilities to provide audits that go beyond standard HTML parsing.

## 🚀 Quick Reference

| Command | Action |
|---------|--------|
| `/seo audit <url>` | Full website audit (Technical, Content, Visual, Schema) |
| `/seo visual <url>` | Multimodal audit of layout, CLS, and "Above the Fold" content |
| `/seo technical <url>` | Deep technical check (Robots, Sitemaps, Indexing, CWV) |
| `/seo eeat <url>` | Content quality and authoritativeness assessment |
| `/seo geo <url>` | Optimization for AI Search (Gemini Overviews, ChatGPT) |
| `/seo schema <url>` | JSON-LD detection, validation, and generation |
| `/seo fix <url>` | **Gemini Exclusive**: Propose and apply direct code fixes for SEO issues |

## 🛠️ Specialized Workflows

### 1. Multimodal Visual Audit
Unlike other SEO tools, Gemini SEO uses `scripts/capture_screenshot.py` to see what the user sees.
- **Visual CLS**: Identify elements causing layout shifts.
- **Above the Fold**: Analyze if the primary value proposition and CTA are visible without scrolling.
- **Mobile UX**: Validate font sizes, tap targets, and responsiveness visually.

### 2. Deep Technical Audit
Uses `scripts/fetch_page.py` and `scripts/parse_html.py` to analyze:
- **Crawlability**: robots.txt blocks, canonical loops, 404s.
- **Performance**: CWV (LCP, INP, CLS) thresholds via `references/cwv-thresholds.md`.
- **Indexing**: Meta robots, sitemap coverage.

### 3. E-E-A-T & AEO
Evaluates content against the latest Google Quality Rater Guidelines (Sept 2025).
- **Experience**: Does the content show first-hand testing or usage?
- **Expertise**: Are author bios and credentials present and valid?
- **AI Readiness (GEO)**: Is the content structured for LLM citation? (Nugget principle, entity clarity).

## 🤖 Sub-Agent Delegation
For complex audits, Gemini SEO spawns specialized sub-agents:
- `seo-technical`: Focuses on infra and crawlability.
- `seo-content`: Focuses on E-E-A-T and semantic richness.
- `seo-visual`: Focuses on layout and UX (Multimodal).
- `seo-schema`: Focuses on structured data.

## 📁 Shared Context & Cache
All data is stored in `.seo-cache/` to allow cross-turn analysis and "Site Map Memory".

## 📜 Guiding Principles
- **Evidence Over Guesses**: Never hallucinate crawl data. If a script fails, report the failure.
- **Actionable Fixing**: Don't just report a missing `alt` tag; offer the `replace` tool call to fix it.
- **Vision-First**: If a site is live, always try a visual audit first.

## 📊 Scoring
Weighted aggregate (0-100) based on:
- Technical SEO (25%)
- Content Quality (25%)
- Visual/UX (20%)
- Performance (15%)
- Schema/AEO (15%)
