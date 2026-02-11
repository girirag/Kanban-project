<script lang="ts">
  import { dndzone } from 'svelte-dnd-action';
  import { onMount } from "svelte";
  import { apiService, type Task } from '../lib/api';

  const columns = ["Planning", "To Do", "In Progress", "In Review", "Done"];
  let newTask = '';
  let taskId = 1;
  let errorMessage = '';

  let board: Record<string, Task[]> = {};
  columns.forEach(col => board[col] = []);

  let originalBoardState: Record<string, Task[]> = {};
  let isDragging = false;
  let apiConnected = false;

  function getAllTaskNames(): string[] {
    return Object.values(board).flat().map(task => task.text.toLowerCase().trim());
  }

  function loadFromLocalStorage() {
    try {
      const savedTasks = localStorage.getItem('kanban-tasks');
      if (savedTasks) {
        const tasks = JSON.parse(savedTasks) as Task[];
        columns.forEach(col => board[col] = []);
        tasks.forEach(task => {
          if (board[task.column]) {
            board[task.column].push(task);
          }
        });
        if (tasks.length > 0) {
          taskId = Math.max(...tasks.map(t => t.id)) + 1;
        }
        board = { ...board };
      }
    } catch (error) {
      console.error('Error loading from localStorage:', error);
    }
  }

  function saveToLocalStorage() {
    try {
      const allTasks = Object.values(board).flat();
      localStorage.setItem('kanban-tasks', JSON.stringify(allTasks));
    } catch (error) {
      console.error('Error saving to localStorage:', error);
    }
  }

  onMount(async () => {
    loadFromLocalStorage();
    await connectToAPI();
  });

  async function connectToAPI() {
    try {
      console.log('Attempting to connect to API...');
      const healthCheck = await apiService.healthCheck();
      console.log('API Health Check:', healthCheck);
      apiConnected = healthCheck.status === 'healthy';
      
      if (apiConnected) {
        errorMessage = '';
        const tasks = await apiService.getTasks();
        console.log('Tasks loaded from API:', tasks);
        
        columns.forEach(col => board[col] = []);
        tasks.forEach(task => {
          if (board[task.column]) {
            board[task.column].push(task);
          }
        });
        
        if (tasks.length > 0) {
          taskId = Math.max(...tasks.map(t => t.id)) + 1;
        }
        
        board = { ...board };
        saveToLocalStorage();
      }
    } catch (error) {
      console.error('API connection failed:', error);
      apiConnected = false;
      errorMessage = 'API connection failed - using offline mode. Click "Retry Connection" to try again.';
    }
  }

  async function addTask() {
    const trimmedTask = newTask.trim();
    if (!trimmedTask) {
      errorMessage = 'Task name cannot be empty';
      setTimeout(() => errorMessage = '', 3000);
      return;
    }
    const existingNames = getAllTaskNames();
    if (existingNames.includes(trimmedTask.toLowerCase())) {
      errorMessage = 'Task name already exists';
      setTimeout(() => errorMessage = '', 3000);
      return;
    }
    
    if (apiConnected) {
      try {
        const newTaskData = await apiService.createTask({
          text: trimmedTask,
          column: "Planning"
        });
        
        board["Planning"] = [...board["Planning"], newTaskData];
        board = { ...board };
        saveToLocalStorage();
        
        console.log('Task created via API:', newTaskData);
      } catch (error) {
        console.error('API create failed:', error);
        const newItem: Task = {
          id: taskId++,
          text: trimmedTask,
          column: "Planning"
        };
        board["Planning"] = [...board["Planning"], newItem];
        board = { ...board };
        saveToLocalStorage();
        errorMessage = 'API save failed - saved locally';
        setTimeout(() => errorMessage = '', 3000);
      }
    } else {
      const newItem: Task = {
        id: taskId++,
        text: trimmedTask,
        column: "Planning"
      };
      board["Planning"] = [...board["Planning"], newItem];
      board = { ...board };
      saveToLocalStorage();
    }
    newTask = '';
  }

  function handleConsider(event: CustomEvent, column: string) {
    const { items } = event.detail;
    if (!isDragging) {
      isDragging = true;
      originalBoardState = {};
      columns.forEach(col => {
        originalBoardState[col] = [...board[col]];
      });
    }
    board[column] = items;
  }

  async function handleFinalize(event: CustomEvent, column: string) {
    const { items } = event.detail;
    const movedTask = items.find((item: Task) => item.column !== column);
    if (!movedTask) {
      board[column] = items;
      isDragging = false;
      originalBoardState = {};
      return;
    }
    const originalColumn = movedTask.column;
    const fromIndex = columns.indexOf(originalColumn);
    const toIndex = columns.indexOf(column);
    const canMoveForwardOneStep = toIndex === fromIndex + 1;
    const canMoveBackwardOneStep = toIndex === fromIndex - 1;
    const canMoveFromDone = originalColumn === "Done";
    
    if (canMoveForwardOneStep || canMoveBackwardOneStep || canMoveFromDone) {
      movedTask.column = column;
      board[column] = items;
      board[originalColumn] = board[originalColumn].filter(task => task.id !== movedTask.id);
      
      if (apiConnected) {
        try {
          await apiService.updateTask(movedTask.id, { column: column });
          console.log('Task updated via API:', movedTask.id);
        } catch (error) {
          console.error('API update failed:', error);
        }
      }
      saveToLocalStorage();
    } else {
      const restoredBoard: Record<string, Task[]> = {};
      columns.forEach(col => {
        restoredBoard[col] = [...originalBoardState[col]];
      });
      board = restoredBoard;
      board = { ...board };
      setTimeout(() => {
        board = { ...restoredBoard };
      }, 10);
    }
    isDragging = false;
    originalBoardState = {};
  }

  async function deleteTask(taskId: number, column: string, event?: Event) {
    event?.stopPropagation();
    
    if (apiConnected) {
      try {
        await apiService.deleteTask(taskId);
        console.log('Task deleted via API:', taskId);
      } catch (error) {
        console.error('API delete failed:', error);
      }
    }
    
    board[column] = board[column].filter(task => task.id !== taskId);
    board = { ...board };
    saveToLocalStorage();
  }
</script>

<style>
  .board-container {
    background: 
      linear-gradient(45deg, rgba(71, 85, 105, 0.1) 25%, transparent 25%), 
      linear-gradient(-45deg, rgba(71, 85, 105, 0.1) 25%, transparent 25%), 
      linear-gradient(45deg, transparent 75%, rgba(71, 85, 105, 0.1) 75%), 
      linear-gradient(-45deg, transparent 75%, rgba(71, 85, 105, 0.1) 75%),
      linear-gradient(135deg, #334155 0%, #475569 25%, #64748b 50%, #475569 75%, #334155 100%);
    background-size: 60px 60px, 60px 60px, 60px 60px, 60px 60px, 100% 100%;
    background-position: 0 0, 0 30px, 30px -30px, -30px 0px, 0 0;
    min-height: 100vh;
    padding: 2rem;
    position: relative;
  }
  
  .board-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
      linear-gradient(45deg, transparent 40%, rgba(148, 163, 184, 0.1) 50%, transparent 60%),
      linear-gradient(-45deg, transparent 40%, rgba(148, 163, 184, 0.1) 50%, transparent 60%);
    background-size: 120px 120px;
    pointer-events: none;
  }
  
  .board-wrapper {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    max-width: 1400px;
    margin: 0 auto;
  }
  
  .board-header {
    display: flex;
    align-items: center;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid #f1f5f9;
  }
  
  .board-title {
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }
  
  .board-icon {
    width: 40px;
    height: 40px;
    background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
  }
  
  .board-name {
    font-size: 1.75rem;
    font-weight: 700;
    color: #1e293b;
    margin: 0;
  }
  
  .add-task-section {
    margin-bottom: 2rem;
    display: flex;
    gap: 0.75rem;
    align-items: center;
  }
  
  .task-input {
    flex: 1;
    max-width: 400px;
    padding: 0.75rem 1rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-size: 0.95rem;
    transition: border-color 0.2s;
  }
  
  .task-input:focus {
    outline: none;
    border-color: #3b82f6;
  }
  
  .add-btn {
    padding: 0.75rem 1.5rem;
    background: #3b82f6;
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s;
  }
  
  .add-btn:hover {
    background: #2563eb;
  }
  
  .kanban {
    display: flex;
    gap: 0.75rem;
    width: 100%;
  }
  
  .column {
    flex: 1;
    min-width: 0;
    border-radius: 12px;
    padding: 0;
    min-height: 500px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    border: 1px solid rgba(255,255,255,0.2);
  }
  
  .column:nth-child(1) {
    background: linear-gradient(180deg, #bfdbfe 0%, #93c5fd 100%);
  }
  .column:nth-child(2) {
    background: linear-gradient(180deg, #fed7aa 0%, #fdba74 100%);
  }
  .column:nth-child(3) {
    background: linear-gradient(180deg, #bbf7d0 0%, #86efac 100%);
  }
  .column:nth-child(4) {
    background: linear-gradient(180deg, #e9d5ff 0%, #d8b4fe 100%);
  }
  .column:nth-child(5) {
    background: linear-gradient(180deg, #fecaca 0%, #fca5a5 100%);
  }
  
  .column-header {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid rgba(255,255,255,0.3);
    background: rgba(255,255,255,0.1);
    border-radius: 12px 12px 0 0;
  }
  
  .column-title {
    font-size: 0.9rem;
    font-weight: 600;
    color: #374151;
    margin: 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  
  .dnd-zone {
    padding: 0.75rem 1rem;
    min-height: 400px;
  }
  
  .task {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 0.75rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    cursor: grab;
    border-left: 4px solid #3b82f6;
    transition: all 0.2s;
    position: relative;
  }
  
  .task:hover {
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
    transform: translateY(-1px);
  }
  
  .task:active {
    cursor: grabbing;
  }
  
  .task-content {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 0.5rem;
  }
  
  .task-text {
    flex: 1;
    font-size: 0.9rem;
    line-height: 1.4;
    color: #374151;
    font-weight: 500;
  }
  
  .task-meta {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 0.75rem;
    padding-top: 0.75rem;
    border-top: 1px solid #f1f5f9;
  }
  
  .task-id {
    font-size: 0.75rem;
    color: #6b7280;
    font-weight: 600;
  }
  
  .task-priority {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #10b981;
  }
  
  .delete-btn {
    background: #ef4444;
    color: white;
    border: none;
    border-radius: 4px;
    padding: 0.25rem 0.5rem;
    font-size: 0.7rem;
    cursor: pointer;
    opacity: 0;
    transition: opacity 0.2s;
    position: absolute;
    top: 0.5rem;
    right: 0.5rem;
  }
  
  .task:hover .delete-btn {
    opacity: 1;
  }
  
  .delete-btn:hover {
    background: #dc2626;
  }
  
  .error-message {
    color: #ef4444;
    font-size: 0.875rem;
    margin-top: 0.5rem;
    padding: 0.5rem;
    background: #fef2f2;
    border-radius: 6px;
    border-left: 4px solid #ef4444;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
  }
  
  .retry-btn {
    padding: 0.5rem 1rem;
    background: #3b82f6;
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 0.875rem;
    cursor: pointer;
    white-space: nowrap;
  }
  
  .retry-btn:hover {
    background: #2563eb;
  }
  
  .connection-status {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-size: 0.875rem;
    margin-left: auto;
  }
  
  .connection-status.connected {
    background: #d1fae5;
    color: #065f46;
  }
  
  .connection-status.disconnected {
    background: #fee2e2;
    color: #991b1b;
  }
  
  .status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
  }
  
  .status-dot.connected {
    background: #10b981;
  }
  
  .status-dot.disconnected {
    background: #ef4444;
  }
</style>

<div class="board-container">
  <div class="board-wrapper">
    <div class="board-header">
      <div class="board-title">
        <div class="board-icon">📋</div>
        <h1 class="board-name">Project Board</h1>
      </div>
      <div class="connection-status {apiConnected ? 'connected' : 'disconnected'}">
        <div class="status-dot {apiConnected ? 'connected' : 'disconnected'}"></div>
        {apiConnected ? 'Connected to Firebase' : 'Offline Mode'}
      </div>
    </div>

    <div class="add-task-section">
      <input
        bind:value={newTask}
        placeholder="What needs to be done?"
        class="task-input"
        on:keydown={(e) => e.key === 'Enter' && addTask()}
      />
      <button
        on:click={addTask}
        class="add-btn"
      >
        Add Task
      </button>
    </div>

    {#if errorMessage}
      <div class="error-message">
        {errorMessage}
        {#if !apiConnected}
          <button class="retry-btn" on:click={connectToAPI}>Retry Connection</button>
        {/if}
      </div>
    {/if}

    <div class="kanban">
      {#each columns as column}
        <div class="column">
          <div class="column-header">
            <h3 class="column-title">{column}</h3>
          </div>
          <div
            class="dnd-zone"
            use:dndzone={{ items: board[column], flipDurationMs: 300 }}
            on:consider={(event) => handleConsider(event, column)}
            on:finalize={(event) => handleFinalize(event, column)}
          >
            {#each board[column] as task (task.id)}
              <div class="task">
                <div class="task-content">
                  <div class="task-text">{task.text}</div>
                  {#if column === "Done"}
                    <button
                      class="delete-btn"
                      on:click={(e) => deleteTask(task.id, column, e)}
                      title="Delete task"
                    >
                      ✕
                    </button>
                  {/if}
                </div>
                <div class="task-meta">
                  <span class="task-id">TASK-{task.id}</span>
                  <div class="task-priority"></div>
                </div>
              </div>
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>
</div>