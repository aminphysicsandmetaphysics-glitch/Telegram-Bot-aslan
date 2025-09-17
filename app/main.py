from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from app.admin.views import router as admin_router
from app.config import settings
from app.db import Base, engine
from app.handlers import start, vip, giveaway
from aiogram import Bot, Dispatcher
from aiogram.types import Update

# create tables (simple auto-create)
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/admin/static"), name="static")
app.include_router(admin_router)

# include aiogram handlers: we will use webhook route
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

# register aiogram routers
dp.include_router(start.router)
dp.include_router(vip.router)
dp.include_router(giveaway.router)

@app.post(settings.WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    # verify secret token header if you set it (Telegram sends header "X-Telegram-Bot-Api-Secret-Token")
    secret = request.headers.get("x-telegram-bot-api-secret-token")
    if settings.WEBHOOK_SECRET and secret != settings.WEBHOOK_SECRET:
        return {"detail":"Unauthorized"}
    data = await request.json()
    update = Update.parse_obj(data)
    await dp.feed_update(bot, update)
    return {"ok": True}
