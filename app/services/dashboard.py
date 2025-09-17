from sqlalchemy import func, desc
from app.models import User, Payment

def get_kpis(db):
    total_users = db.query(func.count(User.id)).scalar() or 0
    vip_users = db.query(func.count(User.id)).filter(User.is_vip==True).scalar() or 0
    revenue_30d = db.query(func.coalesce(func.sum(Payment.amount), 0)).filter(Payment.status=='paid').scalar() or 0
    return {"total_users": total_users, "vip_users": vip_users, "revenue_30d": float(revenue_30d)}
