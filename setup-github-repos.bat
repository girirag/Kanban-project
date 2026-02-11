@echo off
setlocal

echo ========================================
echo Setting up separate GitHub repositories
echo ========================================
echo.

echo Current directory: %CD%
echo.

echo Step 1: Initialize Backend Repository
echo ----------------------------------------
pushd "%~dp0..\kanban-backend"
if errorlevel 1 (
    echo ERROR: Could not navigate to kanban-backend directory
    pause
    exit /b 1
)

git init
if errorlevel 1 (
    echo ERROR: git init failed
    popd
    pause
    exit /b 1
)

git add .
git commit -m "Initial commit: Kanban backend API"
echo Backend repository initialized!
popd
echo.

echo Step 2: Initialize Frontend Repository
echo ----------------------------------------
pushd "%~dp0..\kanban-frontend"
if errorlevel 1 (
    echo ERROR: Could not navigate to kanban-frontend directory
    pause
    exit /b 1
)

git init
if errorlevel 1 (
    echo ERROR: git init failed
    popd
    pause
    exit /b 1
)

git add .
git commit -m "Initial commit: Kanban frontend"
echo Frontend repository initialized!
popd
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo.
echo 1. Create two new repositories on GitHub:
echo    - kanban-backend
echo    - kanban-frontend
echo.
echo 2. For BACKEND, run these commands:
echo    cd ..\kanban-backend
echo    git remote add origin https://github.com/girirag/kanban-backend.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. For FRONTEND, run these commands:
echo    cd ..\kanban-frontend
echo    git remote add origin https://github.com/girirag/kanban-frontend.git
echo    git branch -M main
echo    git push -u origin main
echo.

pause
