from pydantic import BaseModel, ConfigDict

class AlertCreate(BaseModel):
    device: str
    status: str
    
class AlertResponse(BaseModel):
    id: int
    device: str
    status: str
    
model_config = ConfigDict(from_attributes = True)