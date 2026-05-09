Write-Host "Installing WordPress MCP Server dependencies..."
pip install mcp httpx
$configDir = "$env:USERPROFILE\.config\gemini-seo"
New-Item -ItemType Directory -Force -Path $configDir | Out-Null
$configFile = "$configDir\wordpress.json"

if (-Not (Test-Path $configFile)) {
    $template = @{
        wp_url = ""
        wp_user = ""
        wp_app_password = ""
    }
    $template | ConvertTo-Json | Set-Content -Path $configFile
    Write-Host "Created config template at $configFile"
}
Write-Host "Done!"
