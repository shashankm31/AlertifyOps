from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.integrations.gcp_monitoring import normalize_gcp_alert
from app.models.alert_model import Alert
from app.models.incident_model import Incident
from app.services.alert_correlation import find_related_incident



router = APIRouter(
    prefix = "/integrations",
    tags = ["GCP Monitoring"]
)

@router.post("/gcp")
def gcp_webhook(
    payload: dict,
    db: Session = Depends(get_db)
):
    
    #1. Normalize GCP alert
    normalized_alert = normalize_gcp_alert(payload)
    
    #2. Check for duplicate event
    existing_alert = db.query(Alert).filter(
        Alert.event_id == normalized_alert["event_id"]
    ).first()
    
    
    if existing_alert:
        return {
            "message": "Duplicate alert detected",
            "alert_id": existing_alert.id
        }
        
    #3. Find existing open incident
    related_incident = find_related_incident(db, normalized_alert)
    
    #4. Create incident if none exists
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
        
    #5. Save alert and connect it to incident
        db_alert = Alert(
            
        event_id = normalized_alert["event_id"],
        source = normalized_alert["source"],
        device = normalized_alert["device"],
        alert_type = normalized_alert["alert_type"],
        severity = normalized_alert["severity"],
        message = normalized_alert["message"],
        status = normalized_alert["status"],
        timestamp = normalized_alert["timestamp"],
        incident_id = related_incident.id
    )
    
        db.add(db_alert)
        db.commit()
        db.refresh(db_alert)
        
        return {
            "message": "GCP alert processed",
            "alert_id": db_alert.id,
            "incident_id": related_incident.id
        }