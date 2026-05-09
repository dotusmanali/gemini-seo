---
name: seo
description: "Main SEO Orchestrator. Coordinates all 27 specialized SEO sub-skills and 17 agents. Handles /seo full and /seo launch mega-commands."
---

# Gemini SEO Orchestrator

**Role:** High-level router and coordinator for the Gemini SEO suite.

## 🕹️ Command Routing Table

| Command | Specialists Running | Est. Time |
|---------|---------------------|-----------|
| `/seo launch <url/niche>` | 8-phase generation pipeline | 5-10 min |
| `/seo full <url>` | All 20+ specialists parallel | 3-5 min |
| `/seo wp <url>` | **NEW: Deep WordPress authenticated audit via MCP** | 2-4 min |
| `/seo audit <url>` | Core 8 specialists | 1-2 min |
| `/seo links <url>` | **NEW: AI Internal Link Grapher & juice analysis** | 1-2 min |
| `/seo decay <url>` | **NEW: Content Decay & Cannibalization Detector** | 1-2 min |
| `/seo pov <url>` | **NEW: Multi-LLM POV (Perplexity vs GPT-4o search)** | 1-2 min |
| `/seo outreach <url>`| **NEW: Automated PR & Journalist Outreach generator** | 1-2 min |
| `/seo report <url>` | **NEW: Generates an Interactive HTML visual report** | 10 sec |
| `/seo page <url>` | Single page deep dive | 30 sec |
| All other `/seo` commands | Single specialist | 15-30 sec |

## 🚀 Mega Commands

### `/seo full <url>`
Runs every specialist on an existing website and generates a master report in `output/full/`.
1. **Intelligence**: Detect site type (SaaS, E-com, etc.).
2. **Execution**: Run all 20+ specialists in parallel.
3. **Consolidation**: Combine results into `MASTER-SEO-REPORT.md` and `SUMMARY.json`.

### `/seo launch <url or niche>`
Zero-to-ready foundation for new websites. Generates Strategy, Architecture, Content, Technical, and Schema packs in `output/launch/`.

## 🛠️ Global Orchestration Rules
1. **Auto-Detect**: Determine business type (SaaS, E-commerce, Local, Publisher) from homepage signals.
2. **Parallelism**: Use `scripts/run_all_workflows.py` to trigger parallel agents.
3. **Caching**: Store evidence in `.seo-cache/` for cross-turn context.
4. **Reporting**: All reports must include a **Health Score (0-100)** and prioritized **Action Plan**.

## 📁 Shared Storage
- **Cache**: `.seo-cache/`
- **Full Audits**: `output/full/`
- **Launch Files**: `output/launch/`
- **Single Commands**: `output/[command-name]/`
