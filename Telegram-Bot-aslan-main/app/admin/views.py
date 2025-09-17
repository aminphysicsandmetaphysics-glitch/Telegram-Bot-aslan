from fastapi import APIRouter, Depends, Form, Request, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db import get_db
from .deps import require_admin
from app import services

router = APIRouter(prefix="/admin", tags=["admin"])
templates = Jinja2Templates(directory="app/admin/templates")

@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    kpis = services.dashboard.get_kpis(db)
    last_payments = services.payments.list_recent(db, limit=10)
    return templates.TemplateResponse("dashboard.html", {"request": request, "kpis": kpis, "last_payments": last_payments})

@router.get("/users", response_class=HTMLResponse)
def users_list(request: Request, q: str = "", page: int = 1, db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    data = services.users.search(db, q=q, page=page, page_size=20)
    return templates.TemplateResponse("users_list.html", {"request": request, **data, "q": q})

@router.post("/signals/create")
def create_signal(title: str = Form(...), body: str = Form(...), market: str = Form(""), is_vip: bool = Form(True),
                  db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    services.signals.create(db, title=title, body=body, market=market, is_vip=is_vip)
    return RedirectResponse("/admin/signals", status_code=303)

@router.get("/giveaways", response_class=HTMLResponse)
def giveaways_page(request: Request, db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    gws = services.giveaways.list(db)
    return templates.TemplateResponse("giveaways.html", {"request": request, "gws": gws})

@router.post("/giveaways/create")
def giveaways_create(title: str = Form(...), description: str = Form(""), db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    services.giveaways.create(db, title, description)
    return RedirectResponse("/admin/giveaways", status_code=303)

@router.post("/giveaways/{gw_id}/tasks/add")
def giveaway_task_add(gw_id: int, task_type: str = Form(...), target: str = Form(""), weight: int = Form(1),
                      is_required: bool = Form(True), db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    services.giveaways.add_task(db, gw_id, task_type, target, weight, is_required)
    return RedirectResponse(f"/admin/giveaways?focus={gw_id}", status_code=303)

@router.get("/settings", response_class=HTMLResponse)
def settings_page(request: Request, db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    settings = services.settings.all(db)
    channels = services.settings.channels(db)
    socials = services.settings.socials(db)
    return templates.TemplateResponse("settings.html", {"request": request, "settings": settings, "channels": channels, "socials": socials})

@router.post("/settings/save")
def settings_save(key: str = Form(...), value: str = Form(...), db: Session = Depends(get_db), _: bool = Depends(require_admin)):
    services.settings.upsert(db, key, value)
    return RedirectResponse("/admin/settings", status_code=303)
