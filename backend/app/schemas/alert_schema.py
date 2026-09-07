from pydantic import BaseModel, ConfigDict
from datetime import datetime

class AlertCreate(BaseModel):
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
    device: str
    status: str
    alert_type: str
    severity: str
    message: str
    status: str
    timestamp: datetime
    
model_config = ConfigDict(from_attributes = True)