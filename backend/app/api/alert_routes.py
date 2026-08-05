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


@router.put("/alerts/{alert_id}", response_model = AlertResponse)
def update_alert(
    alert_id: int,
    alert: AlertCreate,
    db: Session = Depends(get_db)
):
    db_alert = db.query(Alert).filter(Alert.id == alert_id).first()
    
    if db_alert is None:
        return {"message": "Alert not found"}
    
    db_alert.device = alert.device
    db_alert.status = alert.status
    
    db.commit()
    db.refresh(db_alert)
    
    return db_alert


@router.delete("/alerts/{alert_id}")
def delete_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):
    db_alert = db.query(Alert).filter(Alert.id == alert_id).first()
    
    if db_alert is None:
        return {"message": "Alert not found"}
    
    db.delete(db_alert)
    db.commit()
    
    return {"message": "Alert deleted successfully"}
