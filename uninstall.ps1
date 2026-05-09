Write-Host "🗑️ Uninstalling gemini-seo..."

$gemini_path = Join-Path $env:USERPROFILE ".gemini"
$skills_path = Join-Path $gemini_path "skills"
$agents_path = Join-Path $gemini_path "agents"

Remove-Item -Path (Join-Path $skills_path "seo") -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path (Join-Path $agents_path "seo-*") -Force -ErrorAction SilentlyContinue

# Remove from GEMINI.md
$gemini_md = Join-Path $gemini_path "GEMINI.md"
if (Test-Path $gemini_md) {
    $content = Get-Content $gemini_md
    $content | Where-Object { $_ -notmatch "gemini-seo" } | Set-Content $gemini_md
}

Write-Host "✅ gemini-seo uninstalled."
