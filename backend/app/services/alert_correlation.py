from app.models.incident_model import Incident


def find_related_incident(db, alert):
    return db.query(Incident).filter(
        Incident.device == alert["device"],
        Incident.status == "Open"
    ).first()