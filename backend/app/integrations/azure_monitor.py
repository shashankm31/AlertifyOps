from app.integrations.alert_normalizer import normalize_alert

def normalize_azure_alert(payload: dict) -> dict:
    return normalize_alert(
        event_id = payload["event_id"],
        source = "Azure Monitor",
        device = payload["resource_id"],
        alert_type = payload["alert_name"],
        severity = payload.get("severity", "Warning"),
        message = payload.get("reason", ""),
        status = payload.get("state", "Fired"),
        timestamp = payload["timestamp"]
    )
    
    

if __name__ == "__main__":
    test_payload = {
        "event_id": "AZ-001",
        "resource_id": "vm-test-001",
        "alert_name": "HighMemory",
        "severity": "Warning",
        "reason": "Memory utilization above 85%",
        "state": "Fired",
        "timestamp": "2026-09-24T03:00:00"
    }
    
    result = normalize_azure_alert(test_payload)
    print(result)