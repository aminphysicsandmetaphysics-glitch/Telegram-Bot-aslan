from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db import get_db
from app.security import verify_admin, create_admin_token
from app.services import dashboard, payments as payments_s, giveaways as gws_s

router = APIRouter(prefix="/admin", tags=["admin"])
templates = Jinja2Templates(directory="app/admin/templates")

@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login(password: str = Form(...)):
    verify_admin(password)
    token = create_admin_token("admin")
    resp = RedirectResponse(url="/admin/dashboard", status_code=303)
    resp.set_cookie("admin_token", token, httponly=True, samesite="Strict")
    return resp

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    kpis = dashboard.get_kpis(db)
    last_payments = payments_s.list_recent(db, limit=10)
    return templates.TemplateResponse("dashboard.html", {"request": request, "kpis": kpis, "last_payments": last_payments})
