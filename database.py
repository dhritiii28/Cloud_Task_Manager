from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg2://neondb_owner:npg_AbUk38rsFoCu@ep-aged-pine-aoe987vk-pooler.c-2.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
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