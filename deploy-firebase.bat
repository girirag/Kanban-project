@echo off
echo ========================================
echo Deploying Kanban Board to Firebase
echo ========================================
echo.

echo Step 1: Building the application...
call npm run build
if %errorlevel% neq 0 (
    echo Build failed!
    pause
    exit /b 1
)

echo.
echo Step 2: Deploying to Firebase Hosting...
call firebase deploy --only hosting

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Deployment Successful!
    echo ========================================
    echo.
    echo Your app is live at:
    echo https://firstapp-ddec4.web.app
    echo https://firstapp-ddec4.firebaseapp.com
    echo.
) else (
    echo.
    echo ========================================
    echo Deployment Failed!
    echo ========================================
    echo.
    echo Make sure you're logged in: firebase login
    echo.
)

pause