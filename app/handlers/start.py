from aiogram import Router, F
from aiogram.types import Message
from ..keyboards import main_kb
from ..texts import brand_title, welcome

router = Router()

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        welcome.format(brand=brand_title),
        reply_markup=main_kb
    )
