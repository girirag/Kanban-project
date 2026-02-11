# Environment Variables - Complete Summary

## 📋 All Environment Variables in This Project

### Frontend Environment Variables

#### VITE_API_URL
- **Purpose**: Backend API endpoint URL
- **Type**: String (URL)
- **Required**: Yes
- **Default**: `https://backend-kanban-board-q2ft.onrender.com`

**Values by Environment:**
```bash
# Local Development (.env.local)
VITE_API_URL=http://localhost:8001

# Production (.env.production)
VITE_API_URL=https://backend-kanban-board-q2ft.onrender.com
```

**Where it's used:**
- File: `src/lib/api.ts`
- Line: `const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://backend-kanban-board-q2ft.onrender.com';`

---

### Backend Environment Variables (Render)

#### PORT
- **Purpose**: Server port number
- **Type**: Number
- **Required**: Yes (auto-set by Render)
- **Default**: `8001` (local), auto-assigned (Render)
- **Status**: ✅ Configured on Render

#### PYTHON_VERSION
- **Purpose**: Python runtime version
- **Type**: String
- **Required**: Recommended for Render
- **Value**: `3.11.0`
- **Status**: ✅ Set on Render

---

### Firebase Credentials (Backend - Render Secret File)

#### firebase-service-account.json
- **Purpose**: Firebase Admin SDK authentication
- **Type**: Secret File (JSON)
- **Required**: Yes (for Firebase integration)
- **Status**: ✅ Added to Render
- **Location**: Render Secret Files

**Contents:**
```json
{
  "type": "service_account",
  "project_id": "firstapp-ddec4",
  "private_key_id": "[YOUR_PRIVATE_KEY_ID]",
  "private_key": "[YOUR_PRIVATE_KEY]",
  "client_email": "firebase-adminsdk-xxxxx@firstapp-ddec4.iam.gserviceaccount.com",
  "client_id": "[YOUR_CLIENT_ID]",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xxxxx%40firstapp-ddec4.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

---

## 🚀 Deployment Status

### Backend (Render)
| Variable/File | Status | Platform |
|---------------|--------|----------|
| `PORT` | ✅ Auto-configured | Render |
| `PYTHON_VERSION` | ✅ Set to 3.11.0 | Render |
| `firebase-service-account.json` | ✅ Added as Secret File | Render |

**Backend URL**: https://backend-kanban-board-q2ft.onrender.com
**Firebase Status**: ✅ Connected

### Frontend (Not Yet Deployed)
| Variable | Status | Value |
|----------|--------|-------|
| `VITE_API_URL` | ✅ Configured | `https://backend-kanban-board-q2ft.onrender.com` |

**Deployment Options:**
- Firebase Hosting: `firebase deploy --only hosting`
- Vercel: `vercel --prod`
- Netlify: `netlify deploy --prod`

---

## 📝 Configuration Files

### .env.local (Local Development)
```bash
VITE_API_URL=http://localhost:8001
```

### .env.production (Production Build)
```bash
VITE_API_URL=https://backend-kanban-board-q2ft.onrender.com
```

### .env.example (Template)
```bash
# API Configuration
# For local development, use local backend
VITE_API_URL=http://localhost:8001

# For production, use Render backend (or leave empty to use default)
# VITE_API_URL=https://backend-kanban-board-q2ft.onrender.com
```

---

## 🔧 How to Deploy Environment Variables

### For Firebase Hosting

Environment variables are built into the app at build time:

```bash
# Build with production environment
npm run build

# Deploy to Firebase
firebase deploy --only hosting
```

The `.env.production` file is automatically used during `npm run build`.

### For Vercel

**Option 1: CLI**
```bash
vercel env add VITE_API_URL production
# Enter: https://backend-kanban-board-q2ft.onrender.com

vercel --prod
```

**Option 2: Dashboard**
1. Go to Vercel Dashboard
2. Select your project
3. Settings → Environment Variables
4. Add: `VITE_API_URL` = `https://backend-kanban-board-q2ft.onrender.com`
5. Redeploy

### For Netlify

**Option 1: CLI**
```bash
netlify env:set VITE_API_URL https://backend-kanban-board-q2ft.onrender.com
netlify deploy --prod
```

**Option 2: Dashboard**
1. Go to Netlify Dashboard
2. Site settings → Environment variables
3. Add: `VITE_API_URL` = `https://backend-kanban-board-q2ft.onrender.com`
4. Trigger redeploy

### For Render (Backend - Already Done)

**Environment Variables:**
1. Go to Render Dashboard
2. Select service: `backend-kanban-board-q2ft`
3. Environment tab
4. Add variables

**Secret Files:**
1. Go to Render Dashboard
2. Select service: `backend-kanban-board-q2ft`
3. Environment tab → Secret Files
4. Add file: `firebase-service-account.json`

---

## ✅ Verification Checklist

### Backend (Render)
- [x] PORT configured
- [x] PYTHON_VERSION set
- [x] Firebase credentials added
- [x] Backend deployed and live
- [x] Firebase connected
- [x] API endpoints working

### Frontend
- [x] VITE_API_URL configured in code
- [x] .env.production created
- [x] .env.local created for development
- [ ] Frontend deployed (pending)

---

## 🎯 Quick Reference

### Current URLs
- **Backend API**: https://backend-kanban-board-q2ft.onrender.com
- **API Docs**: https://backend-kanban-board-q2ft.onrender.com/docs
- **Health Check**: https://backend-kanban-board-q2ft.onrender.com/health
- **GitHub**: https://github.com/girirag/Kanban-project
- **Firebase Console**: https://console.firebase.google.com/project/firstapp-ddec4

### Deploy Commands
```bash
# Deploy to Firebase Hosting
npm run build && firebase deploy --only hosting

# Deploy to Vercel
vercel --prod

# Deploy to Netlify
npm run build && netlify deploy --prod
```

---

## 🔐 Security Notes

- ✅ Firebase credentials stored as Secret File (not in code)
- ✅ .env files in .gitignore
- ✅ No sensitive data in repository
- ✅ CORS configured on backend
- ✅ Firestore security rules in place

---

## 📚 Related Documentation

- `DEPLOY_ENVIRONMENT_VARIABLES.md` - Detailed deployment guide
- `RENDER_FIREBASE_SETUP.md` - Render Firebase setup
- `PROJECT_STATUS.md` - Overall project status
- `ENVIRONMENT_VARIABLES.md` - Complete environment variables reference