# Manual Setup Steps - Copy and Paste These Commands

## Option 1: Using PowerShell (Recommended)

Open PowerShell in the current directory and run:
```powershell
.\setup-github-repos.ps1
```

If you get an execution policy error, run this first:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\setup-github-repos.ps1
```

## Option 2: Manual Commands

### Setup Backend Repository

Open Command Prompt or PowerShell and run these commands one by one:

```bash
cd C:\Users\Giriraghav Kishore\projects\kanban-backend
git init
git add .
git commit -m "Initial commit: Kanban backend API"
```

### Setup Frontend Repository

```bash
cd C:\Users\Giriraghav Kishore\projects\kanban-frontend
git init
git add .
git commit -m "Initial commit: Kanban frontend"
```

## Create GitHub Repositories

1. Go to https://github.com/new
2. Create a repository named `kanban-backend` (don't initialize with README)
3. Create another repository named `kanban-frontend` (don't initialize with README)

## Push Backend to GitHub

```bash
cd C:\Users\Giriraghav Kishore\projects\kanban-backend
git remote add origin https://github.com/girirag/kanban-backend.git
git branch -M main
git push -u origin main
```

## Push Frontend to GitHub

```bash
cd C:\Users\Giriraghav Kishore\projects\kanban-frontend
git remote add origin https://github.com/girirag/kanban-frontend.git
git branch -M main
git push -u origin main
```

## Verify

After pushing, visit:
- https://github.com/girirag/kanban-backend
- https://github.com/girirag/kanban-frontend

Both repositories should now be live with all your code!

## Troubleshooting

If you get authentication errors:
1. Make sure you're logged into GitHub
2. Use GitHub CLI: `gh auth login`
3. Or use a personal access token instead of password

If git is not recognized:
1. Install Git from https://git-scm.com/download/win
2. Restart your terminal after installation
