from aiogram import Router, F
from aiogram.types import Message
from ..texts import vip_desc
from ..keyboards import vip_inline

router = Router()

@router.message(F.text == "🌟 کانال VIP")
async def vip(message: Message):
    await message.answer(vip_desc, reply_markup=vip_inline)
