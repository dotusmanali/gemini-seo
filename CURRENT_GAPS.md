# CURRENT_GAPS.md

## Analysis of Current Gemini SEO vs. Enterprise Standards

After reviewing the current state of `gemini-seo` and comparing it to the benchmark data found in the `forexguru.pk` audit outputs, here is the brutally honest assessment of our current system's weaknesses:

### 1. Lighthouse Metrics (Performance)
**Gap:** `crawl_site.py` and current performance agents rely on basic HTTP requests and external APIs (if configured). It does *not* natively capture local Lighthouse metrics (LCP, CLS, FID, INP, TTFB) using a headless browser. 
**Verdict:** **WEAK.**

### 2. Node-Level DOM Parsing
**Gap:** Current crawling extracts basic tags (Title, Meta, H1). It does *not* parse the full DOM tree to analyze elements in the Above-The-Fold (ATF) zone, font sizes, Y-positions, or color contrast ratios.
**Verdict:** **WEAK.**

### 3. Visual Intelligence (ATF Scoring)
**Gap:** We have a screenshot capability (`capture_screenshot.py`), but it lacks deterministic ATF scoring. It does not output structured JSON analyzing `hero_has_text`, `hero_has_cta`, `atf_content_density`, or visual hierarchy based on font scales.
**Verdict:** **WEAK.**

### 4. Master Consolidation Engine
**Gap:** Our `post-audit.py` merges text, but it does not produce a highly structured, data-driven `SUMMARY.json` with exact categorizations (Critical, High, Medium, Quick Wins) and category scoring (0-100 per category) that translates directly into an `ACTION-PLAN.md` with targeted timeframes.
**Verdict:** **WEAK.**

### 5. Parallel Execution and Unified Reporting
**Gap:** While we have 27+ specialists, the underlying data they process is shallow. The agents are making assumptions rather than working off a deeply unified, metric-rich dataset (`crawl-all.json`, `lighthouse-metrics.json`, `homepage-parse.json`).
**Verdict:** **WEAK.**

---

## The Upgrade Plan

To make `gemini-seo` truly powerful and distinct from `claude-seo` and `codex-seo`, we must upgrade the core engine. We will retain our 27-specialist architecture but feed them **Enterprise-Grade Data**. 

We will build:
1.  `run_lighthouse.py`: Native Core Web Vitals extraction via Playwright.
2.  `parse_dom.py`: Deep node-level parser for the homepage.
3.  **Upgraded** `capture_screenshot.py`: Visual hierarchy scoring.
4.  **Upgraded** `crawl_site.py`: Deep link and directive extraction.
5.  **Upgraded** `post-audit.py`: The ultimate consolidation engine to feed our HTML report generator.