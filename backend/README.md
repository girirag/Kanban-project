# Kanban Board FastAPI Backend

This is the FastAPI backend for the Kanban Board application.

## Setup

### 1. Install Python Dependencies
```bash
cd backend
python setup.py
```

Or manually:
```bash
pip install -r requirements.txt
```

### 2. Configure Firebase
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project
3. Go to Project Settings > Service Accounts
4. Click "Generate new private key"
5. Save the downloaded file as `firebase-service-account.json` in the backend folder

### 3. Environment Configuration (Optional)
Copy `.env.example` to `.env` and configure if needed:
```bash
cp .env.example .env
```

### 4. Run the Server
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

On Windows, you can also use:
```bash
run.bat
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task
- `GET /health` - Health check

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Features

- ✅ RESTful API for task management
- ✅ Firebase Firestore integration
- ✅ CORS enabled for frontend
- ✅ Automatic task ID generation
- ✅ Error handling and validation
- ✅ Health check endpoint