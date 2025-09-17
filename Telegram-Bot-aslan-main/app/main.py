from fastapi import FastAPI, Request, HTTPException
from aiogram.types import Update
from .config import settings
from .bot import bot, dp, register_handlers
from .admin.views import router as admin_router
from fastapi.staticfiles import StaticFiles
from app.admin.views import router as admin_router

app.mount("/static", StaticFiles(directory="app/admin/static"), name="static")
app.include_router(admin_router)

register_handlers()

@app.on_event("startup")
async def on_startup():
    if settings.BASE_URL:
        url = settings.BASE_URL.rstrip("/") + settings.WEBHOOK_PATH
        await bot.set_webhook(url, secret_token=settings.WEBHOOK_SECRET)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.session.close()

@app.post(settings.WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != settings.WEBHOOK_SECRET:
        raise HTTPException(status_code=401, detail="Invalid secret")
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}
