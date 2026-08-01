from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Alert(Base):
    
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key = True)
    
    device = Column(String, nullable = False)
    status = Column(String, nullable = False)