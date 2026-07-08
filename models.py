from sqlalchemy import Column, Integer, String 
from database import Base

class Task(Base):
    
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key= True)
    
    task_title = Column(String, nullable = False)
    
    description = Column(String)
    
    assigned_to = Column(String)
    
    priority = Column(String)
    
    status = Column(String)
    
    due_date = Column(String)
    
    created_by = Column(String)
    
# this file only defines the structure of the table, and think of it as a blueprint