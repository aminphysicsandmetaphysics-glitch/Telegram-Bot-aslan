from aiogram import Router, F
from aiogram.types import Message
from ..config import settings
from ..texts import support_desc

router = Router()

@router.message(F.text == "🛠 پشتیبانی")
async def support(message: Message):
    await message.answer(support_desc.format(support=settings.SUPPORT_USERNAME))
