from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌟 کانال VIP"), KeyboardButton(text="🛠 پشتیبانی")],
        [KeyboardButton(text="👤 حساب کاربری"), KeyboardButton(text="🎁 قرعه‌کشی")],
        [KeyboardButton(text="🎓 آموزش‌های رایگان"), KeyboardButton(text="📢 سیگنال‌های رایگان")],
        [KeyboardButton(text="🗓 تقویم اقتصادی امروز")],
    ],
    resize_keyboard=True,
    input_field_placeholder="یک گزینه را انتخاب کنید…"
)

vip_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 خرید/تمدید اشتراک", callback_data="vip:buy")],
    [InlineKeyboardButton(text="📈 نتایج VIP", url="https://t.me/your_vip_results")]
])

free_inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="عضویت در کانال رایگان", url="https://t.me/your_free_channel")],
    [InlineKeyboardButton(text="اینستاگرام ما", url="https://instagram.com/yourbrand")]
])
