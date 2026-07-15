from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Alert(BaseModel):
    device: str
    status: str
    
    
@router.post("/alerts")
def create_Alert(alert: Alert):
    return {
        "message": "Alert received successfully",
        "alert": alert  
    }