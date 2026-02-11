# Troubleshooting Guide

## Common Issues and Solutions

### Issue: "API connection failed - using offline mode"

**Symptoms:**
- Error message appears on the frontend
- Tasks don't persist after refresh
- Console shows API connection errors

**Solutions:**

#### 1. Check Backend Status
```bash
curl https://backend-kanban-board-q2ft.onrender.com/health
```

Expected response:
```json
{
  "status": "healthy",
  "firebase_connected": true,
  "storage": "firebase"
}
```

#### 2. Check CORS Configuration
The backend must allow requests from your frontend origin.

**Fixed in latest version**: CORS now allows all origins (`allow_origins=["*"]`)

If you see CORS errors in browser console:
- Check `backend/main.py` CORS configuration
- Ensure `allow_origins` includes your frontend URL or `"*"`

#### 3. Render Service Sleeping
Render free tier spins down after inactivity.

**Solution:**
- First request after sleep takes ~30 seconds
- Wait and refresh the page
- Consider upgrading to paid tier for always-on service

#### 4. Check Frontend API URL
Verify the API URL in `src/lib/api.ts`:
```typescript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://backend-kanban-board-q2ft.onrender.com';
```

#### 5. Clear Browser Cache
```
Ctrl + Shift + Delete (Windows)
Cmd + Shift + Delete (Mac)
```
Clear cache and reload.

---

### Issue: Tasks Not Persisting

**Symptoms:**
- Tasks disappear after page refresh
- Data doesn't sync across devices

**Solutions:**

#### 1. Check Firebase Connection
```bash
curl https://backend-kanban-board-q2ft.onrender.com/health
```

Look for: `"firebase_connected": true`

If `false`:
- Check Render Secret Files
- Verify `firebase-service-account.json` is added
- Check Render logs for Firebase errors

#### 2. Check Firestore Rules
Go to: https://console.firebase.google.com/project/firstapp-ddec4/firestore/rules

Rules should allow read/write:
```
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /kanban-tasks/{taskId} {
      allow read, write: if true;
    }
  }
}
```

#### 3. Verify Firestore Collection
Go to: https://console.firebase.google.com/project/firstapp-ddec4/firestore/data

- Collection should be named: `kanban-tasks`
- Documents should appear when you create tasks

---

### Issue: Frontend Won't Start

**Symptoms:**
- `npm run dev` fails
- Port already in use error

**Solutions:**

#### 1. Kill Existing Process
```bash
# Windows
netstat -ano | findstr :5173
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:5173 | xargs kill -9
```

#### 2. Use Different Port
```bash
npm run dev -- --port 3000
```

#### 3. Reinstall Dependencies
```bash
rm -rf node_modules package-lock.json
npm install
```

---

### Issue: Backend Won't Start Locally

**Symptoms:**
- `python main.py` fails
- Import errors
- Firebase initialization errors

**Solutions:**

#### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### 2. Check Python Version
```bash
python --version
```
Should be Python 3.11 or higher.

#### 3. Add Firebase Credentials
Ensure `backend/firebase-service-account.json` exists with valid credentials.

#### 4. Check Port Availability
```bash
# Windows
netstat -ano | findstr :8001

# Mac/Linux
lsof -i:8001
```

---

### Issue: Drag and Drop Not Working

**Symptoms:**
- Can't move tasks between columns
- Tasks snap back to original position

**Solutions:**

#### 1. Check Movement Rules
Tasks can only move:
- Forward one column
- Backward one column
- From "Done" to any column

#### 2. Clear Browser Cache
Old JavaScript may be cached.

#### 3. Check Console for Errors
Open browser DevTools (F12) and check for JavaScript errors.

---

### Issue: Firebase Deployment Fails

**Symptoms:**
- `firebase deploy` fails
- Authentication errors

**Solutions:**

#### 1. Login Again
```bash
firebase logout
firebase login
```

#### 2. Check Project
```bash
firebase use firstapp-ddec4
```

#### 3. Build First
```bash
npm run build
firebase deploy --only hosting
```

---

### Issue: Render Deployment Fails

**Symptoms:**
- Build fails on Render
- Service won't start

**Solutions:**

#### 1. Check Render Logs
- Go to Render Dashboard
- Click on your service
- Check "Logs" tab for errors

#### 2. Verify Build Command
Should be: `pip install -r requirements.txt`

#### 3. Verify Start Command
Should be: `uvicorn main:app --host 0.0.0.0 --port $PORT`

#### 4. Check Python Version
Environment variable: `PYTHON_VERSION=3.11.0`

---

## Testing Tools

### Test API Connection
Open in browser:
```
file:///path/to/firstApp/test-api-connection.html
```

### Test Backend Endpoints
```bash
# Health check
curl https://backend-kanban-board-q2ft.onrender.com/health

# Get tasks
curl https://backend-kanban-board-q2ft.onrender.com/tasks

# Create task
curl -X POST https://backend-kanban-board-q2ft.onrender.com/tasks \
  -H "Content-Type: application/json" \
  -d '{"text":"Test Task","column":"Planning"}'
```

### Check Frontend API URL
Open browser console on your app and run:
```javascript
console.log(import.meta.env.VITE_API_URL);
```

---

## Getting Help

### Check Logs

**Render Backend Logs:**
https://dashboard.render.com/ → Select service → Logs

**Browser Console:**
F12 → Console tab

**Firebase Console:**
https://console.firebase.google.com/project/firstapp-ddec4

### Useful Commands

```bash
# Check backend health
curl https://backend-kanban-board-q2ft.onrender.com/health

# Check if port is in use
netstat -ano | findstr :5173

# Restart frontend
npm run dev

# Rebuild frontend
npm run build

# Check git status
git status

# View recent commits
git log --oneline -5
```

---

## Quick Fixes Checklist

- [ ] Backend is running (check health endpoint)
- [ ] Firebase is connected (`firebase_connected: true`)
- [ ] CORS allows your origin
- [ ] Frontend API URL is correct
- [ ] Browser cache cleared
- [ ] No console errors
- [ ] Firestore rules allow read/write
- [ ] Service account credentials added to Render

---

## Contact & Resources

- **GitHub Repository**: https://github.com/girirag/Kanban-project
- **Backend API**: https://backend-kanban-board-q2ft.onrender.com
- **API Docs**: https://backend-kanban-board-q2ft.onrender.com/docs
- **Firebase Console**: https://console.firebase.google.com/project/firstapp-ddec4
- **Render Dashboard**: https://dashboard.render.com/