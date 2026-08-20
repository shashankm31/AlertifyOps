from passlib.context import CryptContext
from jose import jwt

pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    return jwt.encode(data, SECRET_KEY, algorithm = ALGORITHM)  #jwt.encode(payload, key, algorithm = "HS256")

def verify_access_token(token: str) -> dict:
    payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
    return payload


