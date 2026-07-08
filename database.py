from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from dotenv import load_dotenv
load_dotenv()
# import the function that can read a .env file , i .e open the new file and load all of its variables , into the memory

DATABASE_URL = os.getenv("DATABASE_URL")
# here, we are connecting to a PostgreSQL database hosted on the cloud (Neon)

# note: click "Show Password" and copy the complete connection string

engine = create_engine(DATABASE_URL)
# engine is responsible for connecting FastAPI with the cloud PostgreSQL database

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

def get_db():
    
    db = SessionLocal()
    
    try:
        
        yield db
        
    finally:
        
        db.close()