const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://backend-kanban-board-q2ft.onrender.com';

console.log('API Base URL:', API_BASE_URL);

export interface Task {
  id: number;
  text: string;
  column: string;
}

export interface TaskCreate {
  text: string;
  column?: string;
}

export interface TaskUpdate {
  text?: string;
  column?: string;
}

class ApiService {
  private async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const url = `${API_BASE_URL}${endpoint}`;
    console.log(`API Request: ${options.method || 'GET'} ${url}`);
    
    const config: RequestInit = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      mode: 'cors',
      ...options,
    };

    try {
      const response = await fetch(url, config);
      console.log(`API Response: ${response.status} ${response.statusText}`);
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      console.log(`API Data:`, data);
      return data;
    } catch (error) {
      console.error(`API request failed: ${endpoint}`, error);
      throw error;
    }
  }

  async getTasks(): Promise<Task[]> {
    return this.request<Task[]>('/tasks');
  }

  async createTask(task: TaskCreate): Promise<Task> {
    return this.request<Task>('/tasks', {
      method: 'POST',
      body: JSON.stringify(task),
    });
  }

  async updateTask(taskId: number, updates: TaskUpdate): Promise<Task> {
    return this.request<Task>(`/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(updates),
    });
  }

  async deleteTask(taskId: number): Promise<void> {
    await this.request(`/tasks/${taskId}`, {
      method: 'DELETE',
    });
  }

  async healthCheck(): Promise<{ status: string; firebase_connected: boolean }> {
    return this.request('/health');
  }
}

export const apiService = new ApiService();