---
name: seo-pov
description: "Multi-LLM POV Audit. Analyzes a page from the perspective of different AI models (Perplexity, ChatGPT, Gemini, Claude) to ensure it ranks well in Answer Engines."
---

# 🤖 Multi-LLM POV Audit

**Role:** Generative Search Optimizer
**Trigger:** `/seo pov <url>`

## 🕵️‍♂️ Audit Checklist
- [ ] **Perplexity POV:** Does the page provide dense, verifiable facts and citations early on?
- [ ] **ChatGPT Search POV:** Is the content conversational and structured well for real-time extraction?
- [ ] **Gemini POV:** Are entities (Google Knowledge Graph) clearly defined using semantic HTML and Schema?
- [ ] **llms.txt Check:** Is the page machine-readable when stripped of CSS/JS?

## 📦 Artifacts
- **Output:** `output/seo-pov/multi-llm-audit.md`