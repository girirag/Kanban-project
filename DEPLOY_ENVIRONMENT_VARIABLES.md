# Deploy Environment Variables Guide

## Current Setup Overview

### Backend (Render)
- **Platform**: Render
- **URL**: https://backend-kanban-board-q2ft.onrender.com
- **Environment Variables**: Already configured
- **Firebase Credentials**: Added as Secret File ✅

### Frontend (Not Yet Deployed)
- **API URL**: Configured to use Render backend
- **Environment Variables**: Ready for deployment

---

## Environment Variables Summary

### Frontend Environment Variables

#### Development (.env.local)
```bash
VITE_API_URL=http://localhost:8001
```

#### Production (.env.production)
```bash
VITE_API_URL=https://backend-kanban-board-q2ft.onrender.com
```

### Backend Environment Variables (Already on Render)

#### Current Render Configuration
- `PORT` - Auto-set by Render
- `PYTHON_VERSION=3.11.0`
- Secret File: `firebase-service-account.json` ✅

---

## Deploy Frontend to Firebase Hosting

### Prerequisites
```bash
npm install -g firebase-tools
firebase login
```

### Step 1: Initialize Firebase Hosting
```bash
cd firstApp
firebase init hosting
```

Select:
- Use existing project: `firstapp-ddec4`
- Public directory: `build`
- Configure as single-page app: `Yes`
- Set up automatic builds: `No`

### Step 2: Configure Environment Variables for Firebase Hosting

Firebase Hosting doesn't use traditional environment variables. Instead, the variables are built into the app at build time.

**Option A: Use .env.production (Recommended)**

The `.env.production` file is already configured and will be used automatically during build:

```bash
# .env.production
VITE_API_URL=https://backend-kanban-board-q2ft.onrender.com
```

**Option B: Set at Build Time**

```bash
VITE_API_URL=https://backend-kanban-board-q2ft.onrender.com npm run build
```

### Step 3: Build and Deploy
```bash
# Build the app (uses .env.production automatically)
npm run build

# Deploy to Firebase Hosting
firebase deploy --only hosting
```

Your app will be live at:
```
https://firstapp-ddec4.web.app
https://firstapp-ddec4.firebaseapp.com
```

---

## Deploy Frontend to Vercel (Alternative)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Deploy with Environment Variables
```bash
cd firstApp

# Set environment variable
vercel env add VITE_API_URL production

# When prompted, enter:
https://backend-kanban-board-q2ft.onrender.com

# Deploy
vercel --prod
```

Or use Vercel Dashboard:
1. Go to https://vercel.com/
2. Import your GitHub repository
3. Add environment variable:
   - Name: `VITE_API_URL`
   - Value: `https://backend-kanban-board-q2ft.onrender.com`
4. Deploy

---

## Deploy Frontend to Netlify (Alternative)

### Step 1: Install Netlify CLI
```bash
npm install -g netlify-cli
```

### Step 2: Build and Deploy
```bash
cd firstApp

# Build
npm run build

# Deploy
netlify deploy --prod

# Set environment variable in Netlify Dashboard
# Site settings > Environment variables
# VITE_API_URL = https://backend-kanban-board-q2ft.onrender.com
```

---

## Environment Variables Reference

### All Environment Variables in This Project

#### Frontend Variables
| Variable | Value | Where Used | Status |
|----------|-------|------------|--------|
| `VITE_API_URL` | `https://backend-kanban-board-q2ft.onrender.com` | Frontend API calls | ✅ Configured |

#### Backend Variables (Render)
| Variable | Value | Where Used | Status |
|----------|-------|------------|--------|
| `PORT` | Auto-set by Render | Server port | ✅ Auto-configured |
| `PYTHON_VERSION` | `3.11.0` | Python runtime | ✅ Set on Render |

#### Firebase Credentials (Render Secret File)
| File | Status |
|------|--------|
| `firebase-service-account.json` | ✅ Added to Render |

---

## Firebase Configuration Files

### firebase.json (Already Created)
```json
{
  "hosting": {
    "public": "build",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  }
}
```

### .firebaserc (Create This)
```json
{
  "projects": {
    "default": "firstapp-ddec4"
  }
}
```

---

## Quick Deploy Commands

### Deploy to Firebase Hosting
```bash
cd firstApp
npm run build
firebase deploy --only hosting
```

### Deploy to Vercel
```bash
cd firstApp
vercel --prod
```

### Deploy to Netlify
```bash
cd firstApp
npm run build
netlify deploy --prod
```

---

## Verify Deployment

After deploying, test your frontend:

1. **Open the deployed URL**
2. **Check API connection**:
   - Open browser console
   - Create a task
   - Check for API calls to: `https://backend-kanban-board-q2ft.onrender.com`

3. **Test functionality**:
   - Create tasks
   - Move tasks between columns
   - Delete tasks
   - Refresh page (tasks should persist)

---

## Environment Variable Best Practices

### ✅ Do:
- Use `.env.production` for production builds
- Use `.env.local` for local development
- Keep `.env.example` for documentation
- Add `.env` files to `.gitignore`

### ❌ Don't:
- Commit `.env` files with real values
- Hardcode API URLs in source code
- Use development URLs in production

---

## Troubleshooting

### Frontend can't connect to backend
- Check `VITE_API_URL` is set correctly
- Verify backend is running: `curl https://backend-kanban-board-q2ft.onrender.com/health`
- Check browser console for CORS errors

### Environment variable not working
- Rebuild the app: `npm run build`
- Clear browser cache
- Check variable name starts with `VITE_`

### Firebase deploy fails
- Run `firebase login` again
- Check project ID: `firebase use firstapp-ddec4`
- Verify build directory exists: `ls build/`

---

## Current Status

✅ Backend deployed on Render with Firebase
✅ Environment variables configured
✅ Frontend ready for deployment
⏳ Frontend not yet deployed (choose platform above)

## Next Steps

1. Choose deployment platform (Firebase Hosting, Vercel, or Netlify)
2. Follow the deployment steps above
3. Test the deployed application
4. Update GitHub README with live URLs