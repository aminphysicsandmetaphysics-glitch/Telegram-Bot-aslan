from fastapi import APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from ..security import verify_admin, create_admin_token, require_admin

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/login", response_class=HTMLResponse)
def login_form():
    return """
    <form method="post" style="margin:2rem;font-family:sans-serif">
      <h2>Admin Login</h2>
      <input name="password" type="password" placeholder="Password" style="padding:.5rem"/>
      <button style="padding:.5rem 1rem">Login</button>
    </form>
    """

@router.post("/login")
def login(password: str = Form(...)):
    verify_admin(password)
    token = create_admin_token("admin")
    resp = RedirectResponse(url="/admin/dashboard", status_code=302)
    resp.set_cookie("adm", token, httponly=True, samesite="Strict")
    return resp

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(auth=Depends(require_admin)):
    return "<h1>Admin Dashboard</h1><p>Stats coming soon…</p>"
