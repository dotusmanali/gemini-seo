#!/bin/bash
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Installing gemini-seo..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3.10+ is required but not installed."
    exit 1
fi

# Check Node
if ! command -v node &> /dev/null; then
    echo "❌ Node.js 18+ is required but not installed."
    exit 1
fi

# Create directories
mkdir -p ~/.gemini/skills/
mkdir -p ~/.gemini/agents/
mkdir -p ~/.config/gemini-seo/

# Copy skills and agents
cp -r skills/* ~/.gemini/skills/
cp -r agents/* ~/.gemini/agents/

# Create venv
python3 -m venv ~/.gemini/skills/seo/.venv
source ~/.gemini/skills/seo/.venv/bin/activate
pip install -r requirements.txt

# Playwright
read -p "Do you want to install Playwright Chromium? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    playwright install chromium
fi

# Global GEMINI.md reference
GEMINI_MD=~/.gemini/GEMINI.md
if [ ! -f "$GEMINI_MD" ]; then
    echo "# Gemini CLI Personal Settings" > "$GEMINI_MD"
fi
if ! grep -q "gemini-seo" "$GEMINI_MD"; then
    echo "- [[skills/seo/GEMINI.md]] # gemini-seo suite" >> "$GEMINI_MD"
fi

# Credential templates
cat <<EOF > ~/.config/gemini-seo/dataforseo.json
{
    "username": "",
    "password": ""
}
EOF

cat <<EOF > ~/.config/gemini-seo/google-apis.json
{
    "client_id": "",
    "client_secret": "",
    "refresh_token": ""
}
EOF

echo "✅ gemini-seo installed successfully!"
echo "Try: /seo launch mybusiness.com"
