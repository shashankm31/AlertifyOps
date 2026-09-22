from app.integrations.alert_normalizer import normalize_alert

def normalize_cloudwatch_alert(payload: dict) -> dict:
    return normalize_alert(
        event_id = payload["event_id"],
        source = "AWS CloudWatch",
        device = payload["instance_id"],
        alert_type = payload["alarm_name"],
        severity = payload.get("severity", "Warning"),
        message = payload.get("reason", ""),
        status = payload.get("state", "ALARM"),
        timestamp = payload["timestamp"]     
    )


if __name__ == "__main__":
    test_payload = {
        "event_id": "CW-001",
        "instance_id": "i-12345",
        "alarm_name": "HighCPU",
        "severity": "Critical",
        "reason": "CPU utilization above 80%",
        "state": "ALARM",
        "timestamp": "2026-09-21T05:00:00"
    }
    
    result = normalize_cloudwatch_alert(test_payload)
    print(result)