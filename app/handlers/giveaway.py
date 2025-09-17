from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ..config import settings
from ..services.tg_checks import is_member
from ..db import get_db
from sqlalchemy.orm import Session
from ..models import Giveaway, GiveawayTask, GiveawayEntry

router = Router()

@router.message(F.text == "🎁 قرعه‌کشی")
async def gw_entry(message: Message):
    db_gen = get_db()
    db: Session = next(db_gen)
    try:
        user_id = message.from_user.id
        gw = db.query(Giveaway).filter_by(is_active=True).order_by(Giveaway.id.desc()).first()
        if not gw:
            return await message.answer("در حال حاضر قرعه‌کشی فعالی وجود ندارد.")

        sponsor_channels = [x.strip() for x in (settings.SPONSOR_CHANNELS or "").split(",") if x.strip()]
        ok_channels = []
        for ch in sponsor_channels:
            if await is_member(message.bot, ch, user_id):
                ok_channels.append(ch)

        entry = db.query(GiveawayEntry).filter_by(giveaway_id=gw.id, user_id=user_id).first()
        if not entry:
            entry = GiveawayEntry(giveaway_id=gw.id, user_id=user_id)
            db.add(entry)
        entry.done = (len(ok_channels) == len(sponsor_channels)) if sponsor_channels else True
        entry.score = len(ok_channels)
        db.commit()

        txt = f"🎁 {gw.title}\nوضعیت تسک‌ها:\n"
        for ch in sponsor_channels:
            tick = "✅" if ch in ok_channels else "❌"
            txt += f"{tick} عضویت در {ch}\n"
        kb = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="🔄 بررسی دوباره", callback_data=f"gw:recheck:{gw.id}")
        ]])
        await message.answer(txt, reply_markup=kb)
    finally:
        try:
            next(db_gen)
        except StopIteration:
            pass
