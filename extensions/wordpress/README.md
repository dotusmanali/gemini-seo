# WordPress MCP Server Setup

This MCP (Model Context Protocol) server allows Gemini CLI to securely connect to any WordPress site using the WordPress REST API and Application Passwords.

## Prerequisites
1.  Python 3.10+
2.  A WordPress site (v5.6+)
3.  An Administrator account on the WordPress site.

## Configuration on WordPress
1.  Log in to your WordPress Admin dashboard.
2.  Go to **Users > Profile**.
3.  Scroll down to **Application Passwords**.
4.  Enter a name (e.g., "Gemini SEO") and click **Add New Application Password**.
5.  **Copy the generated password** (you won't be able to see it again).

## Local Setup
1.  Run the install script for your platform:
    *   Linux/Mac: `./install.sh`
    *   Windows: `.\install.ps1`
2.  Open `~/.config/gemini-seo/wordpress.json` and add your credentials:

```json
{
  "wp_url": "https://yourwebsite.com",
  "wp_user": "your_username",
  "wp_app_password": "XXXX XXXX XXXX XXXX XXXX XXXX"
}
```

## Available MCP Tools
Once configured, the `/seo wp <url>` command will utilize this MCP to access:
*   `get_plugins`: List all active and inactive plugins.
*   `get_theme_info`: Check the active theme and its weight.
*   `check_wp_options`: Analyze database autoload bloat.
*   `get_orphaned_media`: Find unused uploads.
*   `get_site_health`: Fetch the native WP Site Health status.