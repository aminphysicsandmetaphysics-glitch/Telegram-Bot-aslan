from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from .config import settings
from .handlers import start, menu, vip, support, profile, free_content, calendar, giveaway

bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

def register_handlers():
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(vip.router)
    dp.include_router(support.router)
    dp.include_router(profile.router)
    dp.include_router(free_content.router)
    dp.include_router(calendar.router)
    dp.include_router(giveaway.router)
