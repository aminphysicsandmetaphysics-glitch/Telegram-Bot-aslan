from aiogram import Router, F
from aiogram.types import Message
from ..texts import calendar_loading, calendar_empty
from ..config import settings
from ..services.calendar_api import fetch_today_events, render_events_fa

router = Router()

@router.message(F.text == "🗓 تقویم اقتصادی امروز")
async def calendar_today(message: Message):
    await message.answer(calendar_loading)
    events = await fetch_today_events(settings.CALENDAR_API_KEY)
    text = render_events_fa(events)
    if not text:
        text = calendar_empty + "\n\n(برای فعال‌سازی، CALENDAR_API_KEY رو در env تنظیم کن.)"
    await message.answer(text)
