from datetime import datetime


def normalize_solarwinds_alert(payload: dict) -> dict:
    return {
        "event_id": payload.get("event_id"),
        "source": "SolarWinds",
        "device": payload.get("device"),
        "alert_type": payload.get("alert_type"),
        "severity": payload.get("severity"),
        "message": payload.get("message"),
        "status": payload.get("status", "Open"),
        "timestamp": datetime.fromisoformat(payload["timestamp"])
    }