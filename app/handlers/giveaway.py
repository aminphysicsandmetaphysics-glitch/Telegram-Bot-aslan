from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ..config import settings
from ..db import get_db
from sqlalchemy.orm import Session
from ..models import Giveaway, GiveawayTask, GiveawayEntry, User
from ..services.giveaways import list_giveaways

router = Router()

@router.message(F.text == "🎁 قرعه‌کشی")
async def gw_entry(message: Message):
    db = next(get_db())
    gw = db.query(Giveaway).filter_by(is_active=True).order_by(Giveaway.id.desc()).first()
    if not gw:
        await message.answer("در حال حاضر قرعه‌کشی فعالی وجود ندارد.")
        return
    tasks = db.query(GiveawayTask).filter_by(giveaway_id=gw.id).all()
    # Here we do simple check: only check channel membership automatically
    sponsor_channels = settings.SPONSOR_CHANNELS.split(",") if settings.SPONSOR_CHANNELS else []
    ok = []
    # try membership checks (best-effort)
    for ch in sponsor_channels:
        ch = ch.strip()
        try:
            cm = await message.bot.get_chat_member(chat_id=ch, user_id=message.from_user.id)
            ok.append((ch, cm.status in ("member","administrator","creator")))
        except Exception:
            ok.append((ch, False))
    # save entry
    entry = db.query(GiveawayEntry).filter_by(giveaway_id=gw.id, user_id=message.from_user.id).first()
    if not entry:
        entry = GiveawayEntry(giveaway_id=gw.id, user_id=message.from_user.id)
        db.add(entry)
    entry.points = sum(1 for _,v in ok if v)
    entry.created_at = entry.created_at
    db.commit()
    txt = f"🎁 {gw.title}\n\nنتایج بررسی:\n"
    for ch,okv in ok:
        txt += f"{'✅' if okv else '❌'} عضویت در {ch}\n"
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🔄 بررسی دوباره", callback_data=f"gw:recheck:{gw.id}")]])
    await message.answer(txt, reply_markup=kb)
