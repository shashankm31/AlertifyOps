from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.user_model import User
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.core.security import hash_password, verify_password
from fastapi import HTTPException


router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)


@router.post("/register", response_model = UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    
    hashed_password = hash_password(user.password)
    
    db_user = User(
        username = user.username,
        email = user.email,
        password = hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    
    db_user = db.query(User).filter(User.email == user.email).first()
    
    if not db_user:
        raise HTTPException(status_code = 401, detail = "User not found")
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code = 401, detail = "Password incorrect")
    
    return {
        "message": "Login successful",
        "username": db_user.username,
        "email": db_user.email
    }