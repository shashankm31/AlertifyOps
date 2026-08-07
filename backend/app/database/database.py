from sqlalchemy import create_engine     #creates a Database Engine object
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


DATABASE_URL = "postgresql://postgres:alertify123@localhost:5432/alertifyops"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)    # Session is a temporary workspace where you perform database operations. Session gets the database connection from engine

db = SessionLocal()

Base = declarative_base()    # Declarative_base() is a function so returns a Class. Not an object. 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
