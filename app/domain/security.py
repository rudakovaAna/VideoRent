
import os, time
import jwt
from passlib.hash import bcrypt
from typing import Optional

JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret")
JWT_EXPIRES_SECONDS = int(os.getenv("JWT_EXPIRES", "3600"))

def hash_password(password: str) -> str:
    return bcrypt.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.verify(password, password_hash)

def create_jwt(sub: str, role: str) -> str:
    payload = {"sub": sub, "role": role, "exp": int(time.time()) + JWT_EXPIRES_SECONDS}
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")

def decode_jwt(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except Exception:
        return None
