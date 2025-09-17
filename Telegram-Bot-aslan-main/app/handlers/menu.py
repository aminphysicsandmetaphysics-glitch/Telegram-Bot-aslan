from aiogram import Router, F
from aiogram.types import Message
from ..keyboards import main_kb

router = Router()

@router.message(F.text.in_({"منو", "بازگشت", "منوی اصلی"}))
async def menu(message: Message):
    await message.answer("منوی اصلی:", reply_markup=main_kb)
