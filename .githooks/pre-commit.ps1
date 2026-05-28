# QWAV Pre-Commit Hook — Structure Enforcement
# Runs enforce-structure.py before every commit.
# Set up by: git config --local core.hooksPath .githooks

Write-Host "🔍 QWAV Structure Check..." -ForegroundColor Cyan

$enforceScript = "scripts\enforce-structure.py"
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

if (Test-Path $enforceScript) {
    python $enforceScript --report-only
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "❌ Structure check FAILED. Fix violations before committing." -ForegroundColor Red
        Write-Host "   Run: python scripts/enforce-structure.py --fix" -ForegroundColor Yellow
        exit 1
    }
    Write-Host "✅ Structure check PASSED" -ForegroundColor Green
} else {
    Write-Host "⚠️  enforce-structure.py not found — skipping check" -ForegroundColor Yellow
}

exit 0
