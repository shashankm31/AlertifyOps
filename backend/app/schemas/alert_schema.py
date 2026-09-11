from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AlertCreate(BaseModel):
    event_id: str
    source: str
    device: str
    status: str
    alert_type: str
    severity: str
    message: str
    status: str
    timestamp: datetime
    
    
class AlertResponse(BaseModel):
    id: int
    event_id: str
    device: str
    status: str
    alert_type: str
    severity: str
    message: str
    status: str
    timestamp: datetime
    
model_config = ConfigDict(from_attributes = True)