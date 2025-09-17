from aiogram import Router, F
from aiogram.types import Message
from ..texts import free_desc
from ..keyboards import free_inline

router = Router()

@router.message(F.text.in_({"🎓 آموزش‌های رایگان", "📢 سیگنال‌های رایگان"}))
async def free_content(message: Message):
    await message.answer(free_desc, reply_markup=free_inline)
