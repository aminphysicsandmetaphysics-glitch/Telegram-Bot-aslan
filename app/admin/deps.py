from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from . import views
from ..config import settings

bearer = HTTPBearer(auto_error=False)

def get_token_from_cookie(request: Request):
    token = request.cookies.get("admin_token")
    if token:
        return token
    # fallback to Authorization header
    auth = request.headers.get("Authorization")
    if auth and auth.lower().startswith("bearer "):
        return auth.split(" ",1)[1]
    return None

def require_admin_token(token: str = Depends(get_token_from_cookie)):
    if not token:
        raise HTTPException(status_code=401, detail="Missing admin token")
    try:
        jwt.decode(token, settings.ADMIN_JWT_SECRET, algorithms=["HS256"])
        return True
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired admin token")
