from app.integrations.alert_normalizer import normalize_alert

def normalize_gcp_alert(payload: dict) -> dict:
    
    return normalize_alert(
        
        event_id = payload["event_id"],
        source = "GCP Monitoring",
        device = payload["resource_id"],
        alert_type = payload["alert_name"],
        severity = payload.get("severity", "Warning"),
        message = payload.get("reason", ""),
        status = payload.get("state", "OPEN"),
        timestamp = payload["timestamp"]
    )
    
    
if __name__ == "__main__":
    test_payload = {
        "event_id": "GCP-001",
        "resource_id": "vm-test-001",
        "alert_name": "HighDiskUsage",
        "severity": "Warning",
        "reason": "Disk utilization above 85%",
        "state": "OPEN",
        "timestamp": "2026-09-24T05:00:00"
    }
    
    result = normalize_gcp_alert(test_payload)
    print(result)   