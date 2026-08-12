from fastapi import FastAPI
from app.api.alert_routes import router
from app.api.auth_routes import router as auth_router

from app.database.database import Base, engine
from app.models.alert_model import Alert
from app.models.user_model import User

    
# Create FastAPI appliocation   
app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(router)

app.include_router(auth_router)


#Home API
@app.get("/")
def home():
    return {"message": "Welcome to AlertifyOps"}


#Health check API
@app.get("/health")
def health():
    return {"status": "Application is running"}


