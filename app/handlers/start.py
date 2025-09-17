from aiogram import Router, F
from aiogram.types import Message
from ..keyboards import main_kb
from ..texts import WELCOME

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(WELCOME, reply_markup=main_kb)
