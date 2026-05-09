<div align="center">

# 💎 Gemini SEO: The Production-Grade SEO Suite

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/AgriciDaniel/gemini-seo)
[![Gemini CLI](https://img.shields.io/badge/Engine-Gemini_CLI-orange.svg)](https://github.com/google/gemini-cli)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)

**The world's first Gemini-native SEO automation suite.**  
*Orchestrating 27+ parallel agents for technical audits, visual UX, E-E-A-T, and AI-Search Optimization (GEO).*

[Quick Start](#-quick-start) • [Command Reference](#-command-reference) • [Architecture](#-architecture) • [AEO/GEO](#-the-future-of-search-aeo--geo)

</div>

---

## 🚀 Why Gemini SEO?

Legacy SEO tools are blind. They read HTML, but they don't *see* the page. **Gemini SEO** is built from the ground up for the multimodal era, combining deep deterministic crawling with Gemini's advanced vision and long-context capabilities.

- **Vision-First Audits**: Playwright-powered screenshots analyzed by Gemini for ATF visibility and CLS.
- **Agentic Orchestration**: 17 autonomous sub-agents working in parallel, not sequential scripts.
- **Deep E-E-A-T**: Scoring based on the September 2025 Google Quality Rater Guidelines.
- **Future-Proof**: Dedicated workflows for AI Overviews, Perplexity, and `llms.txt`.

---

## 🛠️ Architecture: The Orchestrator

Gemini SEO doesn't just "run scripts." It acts as a Senior Architect, delegating to specialized specialists based on the business type (SaaS, Local, E-com, Publisher).

```mermaid
graph TD
    User([User Prompt]) --> Main[Gemini SEO Orchestrator]
    Main --> Detect{Site Type Detection}
    Detect --> SaaS[SaaS Mode]
    Detect --> Local[Local SEO Mode]
    Detect --> Ecom[E-commerce Mode]
    Detect --> Pub[Publisher Mode]
    
    Main --> Parallel[Parallel Execution Engine]
    Parallel --> T[seo-technical]
    Parallel --> C[seo-content]
    Parallel --> V[seo-visual]
    Parallel --> G[seo-geo]
    Parallel --> R[seo-reddit]
    
    T & C & V & G & R --> Report[Master Reporting Engine]
    Report --> Final[/output/full/MASTER-REPORT.md]
```

---

## 🕹️ Full Command Guide & Usage

Gemini SEO provides a suite of 30+ commands. Here is how to use the most important ones:

### 🌟 Mega Commands (Flagships)

#### 1. `/seo full <url>`
**What it does:** Runs all 27 specialists in parallel. This is a "360-degree" audit.  
**Use case:** When you first start working on a client site and need to find every single issue (Technical, Content, E-E-A-T, Backlinks, Schema).  
**Output:** A master report in `output/full/MASTER-REPORT.md` with prioritized action items.

#### 2. `/seo launch <niche or url>`
**What it does:** Generates a complete SEO foundation for a brand new website.  
**Use case:** Starting a new niche site or SaaS. It builds your keyword strategy, sitemap, content calendar, and schema pack from scratch.  
**Output:** 15+ files in `output/launch/` covering every phase of a site launch.

---

### 🚀 Advanced Features (New)

#### 3. `/seo wp <url>`
**What it does:** Connects to your WordPress backend via MCP. It checks for "hidden" SEO debt like slow plugins, database bloat, and orphaned media.  
**Setup:** You must provide a WordPress Application Password in `~/.config/gemini-seo/wordpress.json`.  
**Value:** Finds why your site is slow or buggy from the *inside*.

#### 4. `/seo links <url>`
**What it does:** Analyzes your internal link architecture. It calculates "Link Juice" flow and finds "Orphaned Pages" (pages with no internal links).  
**Value:** Helps you rank your important pages faster by suggesting where to add internal links.

#### 5. `/seo decay <url>`
**What it does:** Connects to Google Search Console to find "Decaying Content"—pages that used to get traffic but are now dropping.  
**Value:** Prevents traffic loss by telling you exactly which pages need an update.

#### 6. `/seo pov <url>`
**What it does:** Performs a "Multi-LLM" audit. It shows you how Perplexity, ChatGPT, and Gemini "see" your page.  
**Value:** Essential for **AEO (Answer Engine Optimization)**. Ensures your site is the #1 source for AI answers.

#### 7. `/seo outreach <topic>`
**What it does:** Scans your niche for top journalists and bloggers, then generates personalized email pitches.  
**Value:** Automates the hardest part of SEO: Link Building and PR.

---

### 🛠️ Core Specialists

| Command | Category | What it checks |
|:---|:---|:---|
| `/seo technical` | Technical | Robots.txt, Sitemap, Canonical tags, Security headers, 404s. |
| `/seo content` | Quality | E-E-A-T, Reading level, AI-content detection, Keyword density. |
| `/seo schema` | Structured | Validates JSON-LD and suggests missing Schema (FAQ, Product, etc). |
| `/seo performance`| Speed | Core Web Vitals (LCP, INP, CLS) using PageSpeed data. |
| `/seo visual` | UX | Mobile-friendliness and Above-the-Fold (ATF) visual hierarchy. |
| `/seo geo` | Future | Optimization for Generative Engines (AI Overviews). |
| `/seo reddit` | Signals | Brand mentions on Reddit and community sentiment analysis. |

---

## 🔌 MCP Setup Guide (Must Read)

To unlock the full power of Gemini SEO, configure these integrations in `~/.config/gemini-seo/`:

### 1. WordPress (Authenticated Audit)
Create an **Application Password** in your WP Profile, then add it to `wordpress.json`:
```json
{
  "wp_url": "https://yoursite.com",
  "wp_user": "admin",
  "wp_app_password": "xxxx xxxx xxxx xxxx"
}
```

### 2. Google Search Console (Decay & Indexing)
Place your `google-apis.json` (Service Account Key) in the config folder to enable `/seo decay` and automatic indexing.

### 3. DataForSEO / Firecrawl
These allow for live SERP data and JS-rendered crawling. Add your API keys to `dataforseo.json` and `firecrawl.json`.

---

## 🖼️ How Visual Audits Work
When you run `/seo visual`, Gemini SEO uses **Playwright** to take a real screenshot of your site. It then sends this image to Gemini's vision model to analyze:
1. Is the "Buy" or "Subscribe" button visible without scrolling?
2. Is the font too small on mobile?
3. Does the layout shift (CLS) during loading?

---

## 🛡️ Best Practices
- **For deep audits:** Use `/seo full`. It takes 3-5 minutes but saves you hours of manual work.
- **For new content:** Use `/seo pov` before you publish to ensure AI search engines will cite you.
- **For regular maintenance:** Run `/seo drift baseline` every month to catch SEO regressions.


---

## 💎 Flagship Workflows

### 1. MEGA COMMAND: `/seo full <url>`
The ultimate audit. This command triggers the entire agent fleet to deliver a professional-grade report in under 5 minutes.

- **Parallel specialists**: Technical, Content, Schema, Images, Sitemap, Performance, Visual, Local, Maps, Backlinks, Cluster, E-commerce, Hreflang, Competitor, SXO, AEO, Reddit, Video, and Drift Baseline.
- **Artifacts**: 
  - `MASTER-SEO-REPORT.md`: The combined intelligence.
  - `SUMMARY.json`: Normalized health scores (0-100).
  - `ACTION-PLAN.md`: Critical > High > Medium prioritization.
  - `COMPETITOR-GAP.md`: Comparison vs. top 5 SERP leaders.

### 2. MEGA COMMAND: `/seo launch <url or niche>`
Zero-to-ready pipeline for startups and new projects.

- **Phase 1 (Strategy)**: 30-keyword target list + intent mapping.
- **Phase 2 (Architecture)**: Hub-and-spoke URL design.
- **Phase 3 (Content)**: 90-day content calendar + H1-H3 structures.
- **Phase 4 (Setup)**: `robots.txt`, `sitemap.xml`, and technical foundation.
- **Phase 5 (Schema Pack)**: Pre-generated JSON-LD for Organization, FAQ, and Product.

---

## 🤖 The Future of Search: AEO & GEO

AI-powered search engines (Gemini, Perplexity, ChatGPT) require a new kind of optimization.

- **The Nugget Principle**: We audit your content to ensure direct answers are in the first 100 words.
- **Entity Clarity**: Clearly define concepts to improve model indexing.
- **llms.txt Management**: Automated generation and validation of `llms.txt` for AI crawlers.
- **Citability Score**: A unique 0-100 metric measuring how likely an AI model is to cite your page.

---

## 🖼️ Multimodal Vision Audits

Powered by **Playwright Chromium**, Gemini SEO "sees" your website exactly as your users do.

- **Visual CLS Detection**: Identify layout shifts that automated scripts miss.
- **ATF Analysis**: Is your value proposition visible on mobile without scrolling?
- **Cognitive UX**: Analysis of visual hierarchy and CTA effectiveness.

---

## ⚙️ Technical Deep Dive

- **Python Engine**: Python 3.10+ deterministic runners with `requests`, `bs4`, and `pandas`.
- **Crawl Parameters**: Max 500 pages (customizable), 1s delay, full robots.txt respect.
- **Quality Gates**: Built-in hooks to fail audits if critical thin content or canonical loops are found.
- **Site-Map Memory**: Shared `.seo-cache/` enables cross-agent intelligence.

---

## 📦 Installation & Setup

### Requirements
- **Gemini CLI** (latest)
- **Python 3.10+**
- **Node.js 18+**

### One-Line Install (Recommended)

**Linux/Mac:**
```bash
bash install.sh
```

**Windows (PowerShell):**
```powershell
.\install.ps1
```

### Manual Configuration
API keys for **DataForSEO**, **Google Search Console**, and **Firecrawl** should be placed in `~/.config/gemini-seo/`.

---

## 🛡️ Security & Quality Standards

- **SSRF Protection**: All fetch scripts validate URLs to block private/internal IP crawling.
- **Rate Limiting**: Intelligent back-off logic for 429 responses.
- **Compliance**: Adheres to Google's September 2025 E-E-A-T and CWV thresholds.

---

## 🗺️ Roadmap

- [ ] **v2.1**: Ahrefs/Semrush API Integration.
- [ ] **v2.2**: Automated SEO-optimized Image Generation (Gemini ImageGen).
- [ ] **v2.3**: Real-time GSC Indexing API Automation.

---

<div align="center">

**Built for the future of Search. Driven by Gemini.**  
*Created by Muhammad Usman Ali (dotusman) & The Gemini CLI Community.*

</div>
