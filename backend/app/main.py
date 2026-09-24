from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.alert_routes import router
from app.api.auth_routes import router as auth_router
from app.api.cloudwatch_routes import router as cloudwatch_router
from app.api.azure_monitor_routes import router as azure_router
from app.api.gcp_monitoring_routes import router as gcp_router

from app.database.database import Base, engine
from app.models.alert_model import Alert
from app.models.user_model import User
from app.models.incident_model import Incident

    
# Create FastAPI appliocation   
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    
allow_origins = ["http://localhost:5173", "http://127.0.0.1:5173"],
allow_credentials = True,
allow_methods = ["*"],
allow_headers = ["*"],
)

Base.metadata.create_all(bind = engine)

app.include_router(router)

app.include_router(auth_router)

app.include_router(cloudwatch_router)

app.include_router(azure_router)

app.include_router(gcp_router)


#Home API
@app.get("/")
def home():
    return {"message": "Welcome to AlertifyOps"}


#Health check API
@app.get("/health")
def health():
    return {"status": "Application is running"}


