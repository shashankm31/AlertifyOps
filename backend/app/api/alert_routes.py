from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.alert_schema import AlertCreate, AlertResponse
from app.database.database import get_db
from app.models.alert_model import Alert
from app.core.security import get_current_user
from app.integrations.solarwinds import normalize_solarwinds_alert

router = APIRouter()

@router.post("/alerts", response_model = AlertResponse)
def create_alert(
    alert: AlertCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):  
    db_alert = Alert(
        device = alert.device,
        status = alert.status,
        alert_type = alert.alert_type,
        severity = alert.severity,
        message = alert.message,
        timestamp = alert.timestamp,
        source = alert.source
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    
    return db_alert


@router.post("/integrations/solarwinds")
def solarwinds_webhook(
    payload: dict,
    db: Session = Depends(get_db)
):
    normalized_alert = normalize_solarwinds_alert(payload)
    
    db_alert = Alert(**normalized_alert)
    
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    
    return {
        "message": "SolarWinds alert received",
        "alert_id": db_alert.id
    }


@router.get("/alerts", response_model = list[AlertResponse])
def get_alerts(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
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

