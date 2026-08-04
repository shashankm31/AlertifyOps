from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.alert_schema import AlertCreate, AlertResponse
from app.database.database import get_db
from app.models.alert_model import Alert


router = APIRouter()

@router.post("/alerts", response_model = AlertResponse)
def create_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db)
):  
    db_alert = Alert(
        device = alert.device,
        status = alert.status
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    
    return db_alert

@router.get("/alerts", response_model = list[AlertResponse])
def get_alerts(
    db: Session = Depends(get_db)
):
    alerts = db.query(Alert).all()
    return alerts


    