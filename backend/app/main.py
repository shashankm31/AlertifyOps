from fastapi import FastAPI
from app.api.alerts import router

    
# Create FastAPI appliocation   
app = FastAPI()

app.include_router(router)



#Home API
@app.get("/")
def home():
    return {"message": "Welcome to AlertifyOps"}


#Health check API
@app.get("/health")
def health():
    return {"status": "Application is running"}


