import time
from argon2 import PasswordHasher
import jwt
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .config import settings

ph = PasswordHasher()
bearer = HTTPBearer()

def verify_admin(password: str):
    if not settings.ADMIN_PASSWORD_HASH:
        raise HTTPException(status_code=500, detail="Admin password not set")
    try:
        ph.verify(settings.ADMIN_PASSWORD_HASH, password)
        return True
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid credentials")

def create_admin_token(username: str):
    payload = {"sub": username, "exp": int(time.time()) + settings.ADMIN_JWT_EXPIRE_MIN*60}
    return jwt.encode(payload, settings.ADMIN_JWT_SECRET, algorithm="HS256")

def require_admin(token: HTTPAuthorizationCredentials = Depends(bearer)):
    try:
        jwt.decode(token.credentials, settings.ADMIN_JWT_SECRET, algorithms=["HS256"])
        return True
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
