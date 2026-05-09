#!/bin/bash
echo "Installing WordPress MCP Server dependencies..."
pip install mcp httpx
mkdir -p ~/.config/gemini-seo
if [ ! -f ~/.config/gemini-seo/wordpress.json ]; then
cat << EOF > ~/.config/gemini-seo/wordpress.json
{
  "wp_url": "",
  "wp_user": "",
  "wp_app_password": ""
}
EOF
echo "Created config template at ~/.config/gemini-seo/wordpress.json"
fi
echo "Done!"
