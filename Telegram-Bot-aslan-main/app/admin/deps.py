from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from .settings import ADMIN_JWT_SECRET  # از config موجود می‌گیری

security = HTTPBearer(auto_error=False)

def require_admin(request: Request):
    token = request.cookies.get("admin_token")
    if not token:
        raise HTTPException(status_code=302, headers={"Location": "/admin/login"})
    try:
        payload = jwt.decode(token, ADMIN_JWT_SECRET, algorithms=["HS256"])
        if payload.get("role") != "admin":
            raise HTTPException(status_code=403)
    except JWTError:
        raise HTTPException(status_code=302, headers={"Location": "/admin/login"})
    return True
