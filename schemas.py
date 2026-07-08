from pydantic import BaseModel

class TaskSchema(BaseModel):
    
    task_title: str
    
    description: str
    
    assigned_to: str
    
    priority: str
    
    status: str
    
    due_date: str
    
    created_by: str
    
    