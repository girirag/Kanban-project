from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os
from datetime import datetime

app = FastAPI(title="Kanban Board API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174", "http://localhost:3000", "http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: int
    text: str
    column: str

class TaskCreate(BaseModel):
    text: str
    column: str = "Planning"

class TaskUpdate(BaseModel):
    text: Optional[str] = None
    column: Optional[str] = None

# In-memory storage for now (will be replaced with Firebase)
tasks_db = []
next_id = 1

# Try to load existing tasks from file
TASKS_FILE = "tasks_backup.json"

def load_tasks():
    global tasks_db, next_id
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                data = json.load(f)
                tasks_db = data.get('tasks', [])
                next_id = data.get('next_id', 1)
                print(f"Loaded {len(tasks_db)} tasks from backup")
    except Exception as e:
        print(f"Error loading tasks: {e}")
        tasks_db = []
        next_id = 1

def save_tasks():
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump({
                'tasks': tasks_db,
                'next_id': next_id,
                'last_updated': datetime.now().isoformat()
            }, f, indent=2)
    except Exception as e:
        print(f"Error saving tasks: {e}")

# Load tasks on startup
load_tasks()

@app.get("/")
async def root():
    return {
        "message": "Kanban Board API is running",
        "tasks_count": len(tasks_db),
        "firebase_status": "connecting..."
    }

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    try:
        return [Task(**task) for task in tasks_db]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tasks: {str(e)}")

@app.post("/tasks", response_model=Task)
async def create_task(task: TaskCreate):
    global next_id
    try:
        new_task = {
            "id": next_id,
            "text": task.text,
            "column": task.column
        }
        
        tasks_db.append(new_task)
        next_id += 1
        save_tasks()
        
        print(f"Created task: {new_task}")
        return Task(**new_task)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating task: {str(e)}")

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    try:
        # Find the task
        task_index = None
        for i, task in enumerate(tasks_db):
            if task['id'] == task_id:
                task_index = i
                break
        
        if task_index is None:
            raise HTTPException(status_code=404, detail="Task not found")
        
        # Update the task
        if task_update.text is not None:
            tasks_db[task_index]['text'] = task_update.text
        if task_update.column is not None:
            tasks_db[task_index]['column'] = task_update.column
        
        save_tasks()
        
        print(f"Updated task {task_id}: {tasks_db[task_index]}")
        return Task(**tasks_db[task_index])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating task: {str(e)}")

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    try:
        # Find and remove the task
        task_index = None
        for i, task in enumerate(tasks_db):
            if task['id'] == task_id:
                task_index = i
                break
        
        if task_index is None:
            raise HTTPException(status_code=404, detail="Task not found")
        
        deleted_task = tasks_db.pop(task_index)
        save_tasks()
        
        print(f"Deleted task {task_id}: {deleted_task}")
        return {"message": f"Task {task_id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting task: {str(e)}")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "tasks_count": len(tasks_db),
        "firebase_connected": False,  # Will be True when Firebase is connected
        "storage": "file_backup"
    }

# Firebase integration (will be activated when service account is available)
firebase_db = None

def init_firebase():
    global firebase_db
    try:
        if os.path.exists("firebase-service-account.json"):
            import firebase_admin
            from firebase_admin import credentials, firestore
            
            cred = credentials.Certificate("firebase-service-account.json")
            firebase_admin.initialize_app(cred)
            firebase_db = firestore.client()
            
            print("✅ Firebase initialized successfully")
            return True
    except Exception as e:
        print(f"Firebase initialization failed: {e}")
    return False

# Try to initialize Firebase on startup
firebase_connected = init_firebase()

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Kanban Board API...")
    print("📊 API Documentation: http://localhost:8001/docs")
    print("🔥 Firebase Status:", "Connected" if firebase_connected else "Using file backup")
    uvicorn.run(app, host="0.0.0.0", port=8001)