#!/bin/bash
echo "🗑️ Uninstalling gemini-seo..."

rm -rf ~/.gemini/skills/seo/
rm -rf ~/.gemini/agents/seo-*

# Remove from GEMINI.md
if [ -f ~/.gemini/GEMINI.md ]; then
    sed -i '/gemini-seo/d' ~/.gemini/GEMINI.md
fi

echo "✅ gemini-seo uninstalled."
