from sqlalchemy import Column, Integer, String, DateTime
from app.database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Alert(Base):
    
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key = True)
    
    device = Column(String, nullable = False)     #Router-01
    source = Column(String, nullable = False)     #SolarWinds
    alert_type = Column(String, nullable = False) #Interface Down
    severity = Column(String, nullable = False)   #Critical
    message = Column(String, nullable = False)    #GigabitEthernet0/1 is down
    status = Column(String, nullable = False)     #Open
    timestamp = Column(DateTime, nullable = False)  #When alert occurred
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=True)  #Foreign key to incidents table