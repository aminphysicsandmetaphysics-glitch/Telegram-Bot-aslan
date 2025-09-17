from app.models import Giveaway, GiveawayTask, GiveawayEntry
from sqlalchemy.orm import Session

def list(db: Session):
    return db.query(Giveaway).order_by(Giveaway.id.desc()).all()

def create(db: Session, title: str, description: str):
    g = Giveaway(title=title, description=description, is_active=True)
    db.add(g); db.commit(); db.refresh(g); return g

def add_task(db: Session, gw_id: int, task_type: str, target: str, weight: int, is_required: bool):
    t = GiveawayTask(giveaway_id=gw_id, task_type=task_type, target=target, weight=weight, is_required=is_required)
    db.add(t); db.commit(); return t
