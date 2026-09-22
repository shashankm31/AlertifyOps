from fastapi import APIRouter

from app.integrations.cloudwatch import normalize_cloudwatch_alert

router = APIRouter(
    prefix = "/integrations",
    tags = ["CloudWatch"]
)

@router.post("/cloudwatch")
def cloudwatch_webhook(payload: dict):
    
    normalized_alert = normalize_cloudwatch_alert(payload)
    
    return {
        "message": "CloudWatch alert received",
        "normalized_alert": normalized_alert
    }