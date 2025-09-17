from sqlalchemy import String, Integer, BigInteger, Boolean, DateTime, ForeignKey, Numeric, UniqueConstraint, JSON, Column, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_id = Column(BigInteger, unique=True, index=True, nullable=False)
    username = Column(String(64), nullable=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    is_vip = Column(Boolean, default=False)
    vip_until = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    provider = Column(String(32), default="crypto")
    amount = Column(Numeric, nullable=True)
    currency = Column(String(10), default="USDT")
    status = Column(String(20), default="pending", index=True)
    tx_id = Column(String(200), index=True, nullable=True)
    meta = Column(JSON, default={})
    created_at = Column(DateTime, default=datetime.utcnow)

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    plan = Column(String(64))
    status = Column(String(32), default="active")
    started_at = Column(DateTime, default=datetime.utcnow)
    ends_at = Column(DateTime, nullable=True)

class Giveaway(Base):
    __tablename__ = "giveaways"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200))
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    starts_at = Column(DateTime, default=datetime.utcnow)
    ends_at = Column(DateTime, nullable=True)

class GiveawayTask(Base):
    __tablename__ = "giveaway_tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    giveaway_id = Column(Integer, ForeignKey("giveaways.id", ondelete="CASCADE"))
    task_type = Column(String(64))
    target = Column(String(400), nullable=True)
    weight = Column(Integer, default=1)
    is_required = Column(Boolean, default=True)

class GiveawayEntry(Base):
    __tablename__ = "giveaway_entries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    giveaway_id = Column(Integer, ForeignKey("giveaways.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    points = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    __table_args__ = (UniqueConstraint("giveaway_id", "user_id", name="uq_g_entry"),)
