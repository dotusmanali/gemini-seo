Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "🚀 Installing gemini-seo..." -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan

# Check Python
if (!(Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python 3.10+ is required but not installed." -ForegroundColor Red
    exit 1
}

# Check Node
if (!(Get-Command node -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Node.js 18+ is required but not installed." -ForegroundColor Red
    exit 1
}

# Create directories
$gemini_path = Join-Path $env:USERPROFILE ".gemini"
$skills_path = Join-Path $gemini_path "skills"
$agents_path = Join-Path $gemini_path "agents"
$config_path = Join-Path $env:APPDATA "gemini-seo"

if (!(Test-Path $skills_path)) { New-Item -Path $skills_path -ItemType Directory }
if (!(Test-Path $agents_path)) { New-Item -Path $agents_path -ItemType Directory }
if (!(Test-Path $config_path)) { New-Item -Path $config_path -ItemType Directory }

# Copy skills and agents
Copy-Item -Path "skills\*" -Destination $skills_path -Recurse -Force
Copy-Item -Path "agents\*" -Destination $agents_path -Recurse -Force

# Create venv
$venv_path = Join-Path $skills_path "seo\.venv"
python -m venv $venv_path
& "$venv_path\Scripts\activate.ps1"
pip install -r requirements.txt

# Playwright
$confirm = Read-Host "Do you want to install Playwright Chromium? (y/n)"
if ($confirm -eq "y") {
    playwright install chromium
}

# Global GEMINI.md reference
$gemini_md = Join-Path $gemini_path "GEMINI.md"
if (!(Test-Path $gemini_md)) {
    "# Gemini CLI Personal Settings" | Out-File $gemini_md -Encoding utf8
}
$content = Get-Content $gemini_md
if ($content -notmatch "gemini-seo") {
    Add-Content $gemini_md "- [[skills/seo/GEMINI.md]] # gemini-seo suite"
}

# Credential templates
'{"username": "", "password": ""}' | Out-File (Join-Path $config_path "dataforseo.json") -Encoding utf8
'{"client_id": "", "client_secret": "", "refresh_token": ""}' | Out-File (Join-Path $config_path "google-apis.json") -Encoding utf8

Write-Host "✅ gemini-seo installed successfully!" -ForegroundColor Green
Write-Host "Try: /seo launch mybusiness.com" -ForegroundColor Green
