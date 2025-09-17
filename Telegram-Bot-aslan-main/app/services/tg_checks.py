from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

async def is_member(bot: Bot, channel: str, user_id: int) -> bool:
    try:
        cm = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        return cm.status in ("member","administrator","creator")
    except TelegramBadRequest:
        return False
