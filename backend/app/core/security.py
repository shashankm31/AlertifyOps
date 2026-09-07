from passlib.context import CryptContext
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/login")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    return jwt.encode(data, SECRET_KEY, algorithm = ALGORITHM)  #jwt.encode(payload, key, algorithm = "HS256")

def verify_access_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
    return payload

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = verify_access_token(token)
        return payload
    except Exception:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid or expired token")



