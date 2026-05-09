---
name: seo-wp
description: "WordPress MCP Deep Audit. Uses authenticated Application Passwords to scan plugins, themes, database bloat, orphaned media, and hidden technical SEO debt directly from the WP backend."
---

# 📝 WordPress Deep Audit (MCP)

**Role:** Authenticated Backend Auditor
**Trigger:** `/seo wp <url>`

This specialist connects directly to a WordPress site using the WordPress REST API and Application Passwords via MCP. It performs audits that external crawlers cannot see.

## 🕵️‍♂️ Audit Checklist
- [ ] **Plugin Bloat:** Detect inactive plugins, duplicate SEO plugins (e.g., Yoast + RankMath).
- [ ] **Database Health:** Identify wp_options autoload bloat, unoptimized tables.
- [ ] **Theme Speed:** Check for heavy page builders (Elementor, Divi) vs lightweight themes (GeneratePress, Astra).
- [ ] **Orphaned Media:** Detect unused images taking up server space.
- [ ] **Core Web Vitals Backend:** Check if caching/minification plugins (WP Rocket, LiteSpeed) are configured correctly.
- [ ] **Security/SEO Risks:** Detect indexed admin pages, exposed REST API endpoints.

## 📦 Artifacts
- **Output:** `output/seo-wp/wp-backend-audit.md`

## 🔗 MCP Requirements
Requires the WordPress REST API MCP server to be configured with an Application Password.