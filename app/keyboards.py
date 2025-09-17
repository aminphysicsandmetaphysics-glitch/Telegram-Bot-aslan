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
