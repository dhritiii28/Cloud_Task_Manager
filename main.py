from fastapi import FastAPI, Depends
from database import Base, engine, get_db
from sqlalchemy.orm import Session
from schemas import TaskSchema
from models import Task

Base.metadata.create_all(bind=engine)

#connects to Neon and checks whether the the "tasks "table exists, if not then creates it

# here, Base contains all database table definitions
# and engine, contains the cloud database connection

app = FastAPI()

@app.get("/")
def home():
    
    return{"message": "Welcome to Cloud Task Manager API"}

# this API tells that FastAPI is running and the application started successfully

@app.post("/create_task")
def create_task(task: TaskSchema, db: Session = Depends(get_db)):
    
    new_task = Task(task_title = task.task_title, description = task.description, assigned_to = task.assigned_to,
                    priority = task.priority, status = task.status, due_date = task.due_date,
                    created_by = task.created_by)
    
    db.add(new_task)
    
    db.commit()
    
    db.refresh(new_task)
    
    return{"message": "Task Created Successfully"}

# the data sent from Postman is first validated by the TaskSchema (Pydantic Schema), if it is valid, the values 
# are then copied into the Task model, which represents the database table, and finally stored in the database

@app.get("/tasks")
def view_tasks(db: Session = Depends(get_db)):
    
    tasks = db.query(Task).all()
    
    return tasks
