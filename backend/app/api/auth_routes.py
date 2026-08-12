from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserResponse
from app.core.security import hash_password

router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)