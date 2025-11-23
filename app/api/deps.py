
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from sqlalchemy.orm import Session
from app.infra.db import get_session_maker
from app.domain.security import decode_jwt

security = HTTPBearer(auto_error=False)

def get_db():
    SessionLocal = get_session_maker()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(security)) -> Optional[dict]:
    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")
    payload = decode_jwt(token.credentials)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return payload

def require_role(role: str):
    def checker(payload: dict = Depends(get_current_user)):
        if payload.get("role") != role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return payload
    return checker
