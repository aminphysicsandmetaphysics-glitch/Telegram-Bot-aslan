from sqlalchemy import String, Integer, BigInteger, Boolean, DateTime, ForeignKey, UniqueConstraint, JSON
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[str | None] = mapped_column(String(64), nullable=True)
    is_vip: Mapped[bool] = mapped_column(Boolean, default=False)
    vip_until: Mapped[datetime | None]

class Subscription(Base):
    __tablename__ = "subscriptions"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    plan_name: Mapped[str] = mapped_column(String(50))
    days: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(Integer)
    paid_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    expires_at: Mapped[datetime]
    provider: Mapped[str] = mapped_column(String(20))
    tx_ref: Mapped[str] = mapped_column(String(100), index=True)

class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    provider: Mapped[str] = mapped_column(String(20))
    amount: Mapped[int] = mapped_column(Integer)
    currency: Mapped[str] = mapped_column(String(10))
    status: Mapped[str] = mapped_column(String(20), index=True)  # pending/paid/failed
    tx_ref: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    meta: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

class Giveaway(Base):
    __tablename__ = "giveaways"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    description: Mapped[str | None] = mapped_column(String(500))
    ends_at: Mapped[datetime]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

class GiveawayTask(Base):
    __tablename__ = "giveaway_tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    giveaway_id: Mapped[int] = mapped_column(ForeignKey("giveaways.id", ondelete="CASCADE"))
    kind: Mapped[str] = mapped_column(String(30))
    payload: Mapped[dict] = mapped_column(JSON)
    is_required: Mapped[bool] = mapped_column(Boolean, default=True)

class GiveawayEntry(Base):
    __tablename__ = "giveaway_entries"
    id: Mapped[int] = mapped_column(primary_key=True)
    giveaway_id: Mapped[int] = mapped_column(ForeignKey("giveaways.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    score: Mapped[int] = mapped_column(Integer, default=0)
    __table_args__ = (UniqueConstraint("giveaway_id","user_id", name="uq_g_entry"),)
