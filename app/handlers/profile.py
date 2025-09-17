from aiogram import Router, F
from aiogram.types import Message
from ..texts import profile_desc

router = Router()

@router.message(F.text == "👤 حساب کاربری")
async def profile(message: Message):
    user = message.from_user
    await message.answer(profile_desc.format(
        name=(user.full_name or "نام ثبت نشده"),
        username=(user.username or "—"),
        uid=user.id
    ))
