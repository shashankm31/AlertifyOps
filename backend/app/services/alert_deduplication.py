def is_duplicate(existing_alerts, new_alert):
    for existing_alert in existing_alerts:
        if (
            existing_alert.device == new_alert.device
            and existing_alert.alert_type == new_alert.alert_type
            and existing_alert.status == new_alert.status
        ):
            return True
    return False      