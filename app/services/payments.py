from app.models import Payment
from sqlalchemy import desc

def list_recent(db, limit=10):
    return db.query(Payment).order_by(desc(Payment.created_at)).limit(limit).all()
