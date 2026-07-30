from pydantic import BaseModel

class AlertCreate(BaseModel):
    device: str
    status: str