from fastapi import FastAPI
from pydantic import BaseModel

class Alert(BaseModel):
    device: str
    status: str
    
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to AlertifyOps"}


@app.get("/health")
def health():
    return {"status": "Application is running"}


#sending a POST request as /alerts to create an alert 
@app.post("/alerts")
def create_Alert():     #Function FastAPI to create an alert
    return {
        "id": 101,
        "device": "Router-R1",
        "status": "Down"
    }
    
    