# FastAPI Backend Setup Instructions

## 🔥 Firebase Configuration Required

To complete the setup, you need to configure Firebase:

### 1. Get Firebase Service Account Key
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project: **firstapp-ddec4**
3. Go to **Project Settings** (gear icon)
4. Click **Service Accounts** tab
5. Click **Generate new private key**
6. Download the JSON file
7. Rename it to `firebase-service-account.json`
8. Place it in the `backend` folder

### 2. Update Firestore Security Rules
Make sure your Firestore rules allow read/write access:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true;
    }
  }
}
```

### 3. Start the Backend Server
```bash
cd backend
python main.py
```

The API will be available at: http://localhost:8000

### 4. API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 5. Test the Integration
1. Start the FastAPI backend (port 8000)
2. Start the Svelte frontend (port 5173/5174)
3. The frontend will automatically connect to the API

## ✅ What's Working Now

- ✅ FastAPI backend with Firebase integration
- ✅ RESTful API endpoints for tasks
- ✅ CORS configured for frontend
- ✅ Frontend updated to use API instead of direct Firebase
- ✅ Offline mode with localStorage fallback
- ✅ All drag & drop functionality preserved