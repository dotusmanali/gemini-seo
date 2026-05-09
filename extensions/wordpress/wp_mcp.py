import os
import json
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("WordPress SEO Auditor")

# Load config
CONFIG_FILE = os.path.expanduser("~/.config/gemini-seo/wordpress.json")

def get_wp_client():
    if not os.path.exists(CONFIG_FILE):
        raise ValueError(f"Configuration file not found at {CONFIG_FILE}. Please setup first.")
    
    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)
        
    url = config.get("wp_url", "").rstrip("/")
    user = config.get("wp_user", "")
    password = config.get("wp_app_password", "")
    
    if not all([url, user, password]):
        raise ValueError("Missing required configuration keys (wp_url, wp_user, wp_app_password)")
        
    # Basic Auth using Application Password
    auth = (user, password)
    return url, auth

@mcp.tool()
def get_plugins() -> str:
    """Fetch all installed WordPress plugins and their status."""
    url, auth = get_wp_client()
    api_url = f"{url}/wp-json/wp/v2/plugins"
    
    response = httpx.get(api_url, auth=auth)
    if response.status_code == 401:
        return "Authentication failed. Check your Application Password."
    response.raise_for_status()
    
    plugins = response.json()
    result = "WordPress Plugins:\n"
    for p in plugins:
        status = "🟢 Active" if p.get('status') == 'active' else "🔴 Inactive"
        result += f"- {p.get('name')} (v{p.get('version')}) - {status}\n"
    return result

@mcp.tool()
def get_theme_info() -> str:
    """Fetch the active WordPress theme information."""
    url, auth = get_wp_client()
    api_url = f"{url}/wp-json/wp/v2/themes?status=active"
    
    response = httpx.get(api_url, auth=auth)
    response.raise_for_status()
    
    themes = response.json()
    if not themes:
        return "No active theme found via REST API."
        
    theme = themes[0]
    return f"Active Theme: {theme.get('name')} (v{theme.get('version')})"

@mcp.tool()
def get_site_health() -> str:
    """Check if the REST API is accessible and authenticated."""
    try:
        url, auth = get_wp_client()
        response = httpx.get(f"{url}/wp-json/", auth=auth)
        if response.status_code == 200:
            return f"✅ Successfully connected and authenticated to {url}"
        return f"❌ Connection failed. Status code: {response.status_code}"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
