from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.alert_schema import AlertCreate, AlertResponse
from app.database.database import get_db
from app.models.alert_model import Alert
from app.core.security import get_current_user
from app.integrations.solarwinds import normalize_solarwinds_alert
from app.services.alert_deduplication import is_duplicate
from app.services.alert_correlation import find_related_incident
from app.models.incident_model import Incident
from app.schemas.incident_schema import IncidentUpdate


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
    
    # 1. Normalize Solarwinds alert
    normalized_alert = normalize_solarwinds_alert(payload)
    
    #2. Check for duplicate alert
    existing_alert = db.query(Alert).filter(
        Alert.event_id == normalized_alert['event_id']
    ).first()
    
    if existing_alert:
            return {
                "message": "Duplicate alert detected",
                "alert_id": existing_alert.id 
            }
    
    #3. Find an existing open incident for this device
    related_incident = find_related_incident(db, normalized_alert)
    
    #4. Create a new incident if none exists
    if not related_incident:
        new_incident = Incident(
            title = f"{normalized_alert['device']} issue",
            severity = normalized_alert["severity"],
            status = "Open",
            device = normalized_alert["device"],
            created_at = normalized_alert["timestamp"]
        )
        db.add(new_incident)
        db.commit()
        db.refresh(new_incident)
        
        related_incident = new_incident
        
    #5. Connect the alert to the incident
    normalized_alert["incident_id"] = related_incident.id
    
    #6. Save the alert
    db_alert = Alert(
        event_id = normalized_alert["event_id"],
        source = normalized_alert["source"],
        device = normalized_alert["device"],
        alert_type = normalized_alert["alert_type"],
        severity = normalized_alert["severity"],
        message = normalized_alert["message"],
        status = normalized_alert["status"],
        timestamp = normalized_alert["timestamp"],
        incident_id = normalized_alert["incident_id"]
    )
    
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    
    return {
        "message": "SolarWinds alert received",
        "alert_id": db_alert.id,
        "incident_id": related_incident.id
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

@router.put("/incidents/{incident_id}")
def update_incident(
    incident_id: int,
    incident: IncidentUpdate,
    db: Session = Depends(get_db)
):
    db_incident = db.query(Incident).filter(Incident.id == incident_id).first()
    
    if db_incident is None:
        return {
            "message": "Incident not found"
        }
        
    db_incident.status = incident.status
    
    db.commit()
    db.refresh(db_incident)
    
    return {
        "message": "Incident updated successfully",
        "incident_id": db_incident.id,
        "status": db_incident.status
    }