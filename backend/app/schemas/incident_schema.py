from pydantic import BaseModel, ConfigDict
from datetime import datetime

class IncidentBase(BaseModel):
    id: int
    title: str
    severity: str
    status: str
    device: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)