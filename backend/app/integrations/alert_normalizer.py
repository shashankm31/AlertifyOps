from datetime import datetime

def normalize_alert (
    event_id: str,
    source: str,
    device: str,
    alert_type: str,
    severity: str,
    message: str,
    status: str,
    timestamp: str
) -> dict:
    
    
    return {
        "event_id": event_id,
        "source": source,
        "device": device,
        "alert_type": alert_type,
        "severity": severity,
        "message": message,
        "status": status,
        "timestamp": datetime.fromisoformat(timestamp)
    }
    

if __name__ == "__main__":
    result = normalize_alert(
        event_id = "TEST-001",
        source = "SolarWinds",
        device = "Router-01",
        alert_type = "Interface Down",
        severity = "Critical",
        message = "GigabitEthernet0/1 is down",
        status = "Open",
        timestamp = "2026-09-21T04:00:00" 
    )
    
    print(result)