from app.models import Giveaway, GiveawayTask, GiveawayEntry
from sqlalchemy.orm import Session

def list_giveaways(db: Session):
    return db.query(Giveaway).order_by(Giveaway.id.desc()).all()

def create_giveaway(db: Session, title: str, description: str = ""):
    gw = Giveaway(title=title, description=description)
    db.add(gw); db.commit(); db.refresh(gw); return gw

def add_task(db: Session, gw_id: int, task_type: str, target: str, weight:int=1, is_required:bool=True):
    t = GiveawayTask(giveaway_id=gw_id, task_type=task_type, target=target, weight=weight, is_required=is_required)
    db.add(t); db.commit(); db.refresh(t); return t

def list_entries(db: Session, gw_id: int):
    return db.query(GiveawayEntry).filter_by(giveaway_id=gw_id).all()
