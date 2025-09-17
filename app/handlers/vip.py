from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ..config import settings

router = Router()

@router.message(F.text == "🌟 کانال VIP")
async def vip(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💳 خرید/تمدید اشتراک", callback_data="vip:buy")],
        [InlineKeyboardButton(text="📈 نتایج VIP", url=f"https://t.me/{settings.VIP_RESULTS_CHANNEL.strip('@')}")]
    ])
    await message.answer("پلن VIP را انتخاب کنید:", reply_markup=kb)
