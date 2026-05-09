# 💎 Gemini SEO: The Ultimate Command Guide

This guide explains every command in the Gemini SEO suite, what it does, and how to use it effectively.

---

## 🌟 MEGA COMMANDS

### `/seo full <url>`
*   **Description**: The "God Mode" of SEO audits. It spawns 27 parallel agents to analyze every aspect of a website.
*   **What it does**: 
    *   Crawls the site (Technical, Content, Images).
    *   Checks E-E-A-T signals.
    *   Validates all Schema.
    *   Analyzes visual UX on mobile/desktop.
    *   Checks Reddit mentions and Social signals.
*   **When to use**: Onboarding a new client or performing a quarterly deep-dive audit.
*   **Output**: `output/full/MASTER-SEO-REPORT.md`

### `/seo launch <url or niche>`
*   **Description**: The "Zero-to-Hero" pipeline. It builds the SEO foundation for a brand-new website.
*   **Phases**:
    1.  **Keyword Strategy**: 30 high-intent keywords clustered by topic.
    2.  **Architecture**: URL structure and internal link mapping.
    3.  **Content Plan**: 90-day calendar with H1/H2/H3 structures.
    4.  **Tech Pack**: robots.txt, sitemap, and security headers.
    5.  **Schema Pack**: Complete JSON-LD templates.
*   **When to use**: Before you write the first line of code for a new project.

---

## 📝 WORDPRESS & BACKEND (MCP)

### `/seo wp <url>`
*   **Description**: Deep, authenticated audit of your WordPress site.
*   **What it does**: 
    *   Scans active/inactive plugins for security risks and bloat.
    *   Checks if your theme is slowing down the site.
    *   Finds orphaned media files in `wp-content/uploads`.
    *   Checks Database health (autoload bloat).
*   **Prerequisite**: Requires WP Application Password in `wordpress.json`.

---

## 🤖 AI & GENERATIVE SEARCH (AEO/GEO)

### `/seo pov <url>`
*   **Description**: Multi-LLM Perspective Audit.
*   **What it does**: Shows you exactly how Perplexity, ChatGPT, and Gemini Search interpret your page.
*   **Value**: Ensures your content is "AI-ready" and likely to be cited as a source.

### `/seo geo <url>`
*   **Description**: Generative Engine Optimization.
*   **What it does**: Optimizes for Google AI Overviews. Checks for "Answer-First" formatting and nugget-based content delivery.

---

## 🕸️ ARCHITECTURE & DATA

### `/seo links <url>`
*   **Description**: AI Internal Link Grapher.
*   **What it does**: Visualizes how "Link Juice" flows through your site. Finds pages that are "orphaned" or hidden deep in the architecture.

### `/seo decay <url>`
*   **Description**: Content Decay Detector.
*   **What it does**: Connects to Google Search Console to find pages that are losing traffic.
*   **Action**: Tells you whether to update, delete, or merge the page.

---

## ✉️ LINK BUILDING & PR

### `/seo outreach <topic>`
*   **Description**: Automated Digital PR.
*   **What it does**: Finds journalists writing about your topic and drafts personalized emails using AI that sound like they were written by a human.

---

## 🛠️ CORE SPECIALISTS

*   `/seo technical`: Crawlability and Indexability audit.
*   `/seo content`: E-E-A-T and Readability check.
*   `/seo schema`: JSON-LD validation and generation.
*   `/seo images`: Alt text and compression audit.
*   `/seo performance`: Core Web Vitals audit.
*   `/seo local`: GBP and NAP citation audit.
*   `/seo reddit`: Brand sentiment on forums.
*   `/seo competitor`: Gap analysis vs Top 5 SERP leaders.
