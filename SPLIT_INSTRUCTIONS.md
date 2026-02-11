# Instructions for Splitting and Uploading to GitHub

Your project has been split into two separate directories:

## 📁 Directory Structure

```
projects/
├── firstApp/              (original project - can be archived)
├── kanban-frontend/       (new frontend repository)
└── kanban-backend/        (new backend repository)
```

## 🚀 Quick Setup

### Option 1: Automated Setup (Recommended)

Run the setup script from your current directory:
```bash
setup-github-repos.bat
```

This will initialize both git repositories and show you the next steps.

### Option 2: Manual Setup

#### Backend Repository

1. Navigate to backend directory:
```bash
cd ..\kanban-backend
```

2. Initialize git and commit:
```bash
git init
git add .
git commit -m "Initial commit: Kanban backend API"
```

3. Create a new repository on GitHub named `kanban-backend`

4. Push to GitHub:
```bash
git remote add origin https://github.com/girirag/kanban-backend.git
git branch -M main
git push -u origin main
```

#### Frontend Repository

1. Navigate to frontend directory:
```bash
cd ..\kanban-frontend
```

2. Initialize git and commit:
```bash
git init
git add .
git commit -m "Initial commit: Kanban frontend"
```

3. Create a new repository on GitHub named `kanban-frontend`

4. Push to GitHub:
```bash
git remote add origin https://github.com/girirag/kanban-frontend.git
git branch -M main
git push -u origin main
```

## 📝 What's Included

### Backend (`kanban-backend`)
- FastAPI application
- Firebase integration
- All Python dependencies
- Setup scripts
- Documentation
- `.gitignore` (excludes `__pycache__`, `.env`, `firebase-service-account.json`)

### Frontend (`kanban-frontend`)
- SvelteKit application
- All source files
- Static assets
- Configuration files
- Dependencies
- `.gitignore` (excludes `node_modules`, `.svelte-kit`, `.env`)

## ⚠️ Important Notes

1. **Firebase Credentials**: The `firebase-service-account.json` file is excluded from git. You'll need to add it manually to the backend directory after cloning.

2. **Environment Variables**: Create `.env` files in each repository as needed (they're gitignored).

3. **Update Repository Links**: After creating the GitHub repositories, update the README files with the correct repository URLs.

4. **Backend URL**: Update the API URL in `kanban-frontend/src/lib/api.ts` to point to your deployed backend.

## 🔗 Repository URLs

After creating on GitHub, your repositories will be at:
- Backend: `https://github.com/girirag/kanban-backend`
- Frontend: `https://github.com/girirag/kanban-frontend`

## 🧹 Cleanup (Optional)

After successfully pushing both repositories, you can archive or delete the original `firstApp` directory.
