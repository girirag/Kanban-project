Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setting up separate GitHub repositories" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$backendPath = Join-Path (Split-Path -Parent $scriptPath) "kanban-backend"
$frontendPath = Join-Path (Split-Path -Parent $scriptPath) "kanban-frontend"

# Initialize Backend
Write-Host "Step 1: Initialize Backend Repository" -ForegroundColor Yellow
Write-Host "----------------------------------------"
if (Test-Path $backendPath) {
    Push-Location $backendPath
    git init
    git add .
    git commit -m "Initial commit: Kanban backend API"
    Write-Host "Backend repository initialized!" -ForegroundColor Green
    Pop-Location
} else {
    Write-Host "ERROR: Backend directory not found at $backendPath" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Initialize Frontend
Write-Host "Step 2: Initialize Frontend Repository" -ForegroundColor Yellow
Write-Host "----------------------------------------"
if (Test-Path $frontendPath) {
    Push-Location $frontendPath
    git init
    git add .
    git commit -m "Initial commit: Kanban frontend"
    Write-Host "Frontend repository initialized!" -ForegroundColor Green
    Pop-Location
} else {
    Write-Host "ERROR: Frontend directory not found at $frontendPath" -ForegroundColor Red
    exit 1
}
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Create two new repositories on GitHub:"
Write-Host "   - kanban-backend"
Write-Host "   - kanban-frontend"
Write-Host ""
Write-Host "2. For BACKEND, run these commands:" -ForegroundColor Yellow
Write-Host "   cd ..\kanban-backend"
Write-Host "   git remote add origin https://github.com/girirag/kanban-backend.git"
Write-Host "   git branch -M main"
Write-Host "   git push -u origin main"
Write-Host ""
Write-Host "3. For FRONTEND, run these commands:" -ForegroundColor Yellow
Write-Host "   cd ..\kanban-frontend"
Write-Host "   git remote add origin https://github.com/girirag/kanban-frontend.git"
Write-Host "   git branch -M main"
Write-Host "   git push -u origin main"
Write-Host ""

Read-Host "Press Enter to exit"
