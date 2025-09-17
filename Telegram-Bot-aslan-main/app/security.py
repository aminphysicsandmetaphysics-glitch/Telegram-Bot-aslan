import time, jwt
from argon2 import PasswordHasher
from fastapi import HTTPException, Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from .config import settings

ph = PasswordHasher()
bearer = HTTPBearer(auto_error=False)

def verify_admin(password: str):
    if not settings.ADMIN_PASSWORD_HASH:
        raise HTTPException(500, "Admin password not set")
    try:
        ph.verify(settings.ADMIN_PASSWORD_HASH, password)
        return True
    except Exception:
        raise HTTPException(401, "Invalid credentials")

def create_admin_token(username: str):
    payload = {"sub": username, "exp": int(time.time()) + 60*int(settings.ADMIN_JWT_EXPIRE_MIN)}
    return jwt.encode(payload, settings.ADMIN_JWT_SECRET, algorithm="HS256")

def require_admin(request: Request, token: HTTPAuthorizationCredentials = Depends(bearer)):
    raw = token.credentials if token else request.cookies.get("adm")
    if not raw:
        raise HTTPException(401, "Missing token")
    try:
        jwt.decode(raw, settings.ADMIN_JWT_SECRET, algorithms=["HS256"])
        return True
    except Exception:
        raise HTTPException(401, "Invalid or expired token")
