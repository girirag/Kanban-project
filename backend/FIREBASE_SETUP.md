# Firebase Setup Instructions

## Required: Firebase Service Account Setup

To enable Firebase integration, you need to add your Firebase service account credentials:

### Steps:

1. **Go to Firebase Console**: https://console.firebase.google.com/project/firstapp-ddec4/settings/serviceaccounts/adminsdk

2. **Generate Service Account Key**:
   - Click "Generate new private key"
   - Download the JSON file

3. **Add Credentials**:
   - Copy the downloaded JSON file to `backend/firebase-service-account.json`
   - The file should contain real credentials (not the example placeholders)

### File Structure:
```
backend/
├── firebase-service-account.json          # ← Add your real Firebase credentials here
├── firebase-service-account.json.example  # ← Template/example file
└── main.py
```

### Security Note:
- The `firebase-service-account.json` file is ignored by git for security
- Never commit real Firebase credentials to version control
- Use the `.example` file as a template

### Verification:
Once added, restart the backend server. You should see:
```
✅ Firebase initialized successfully
```

If you see errors, check that:
- The JSON file has valid syntax
- All placeholder values are replaced with real credentials
- The project_id matches: `firstapp-ddec4`