from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

main_callback_data = CallbackData("cars", "cartime")


get_reservation = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="go_anketa")
        ],
        [
            InlineKeyboardButton(text="🔙Ortga", callback_data="back_to_services")
        ]
    ]
)


time_control_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Dushanba: 9:00 - 10:00", callback_data=main_callback_data.new(cartime="Dushanba 9-10")),
            InlineKeyboardButton(text="Chorshanba: 10:00 - 11:00", callback_data=main_callback_data.new(cartime="Chorshanba 10-11")),
        ],
        [
            InlineKeyboardButton(text="Juma: 11:00 - 12:00", callback_data=main_callback_data.new(cartime="Juma 11-12")),
            InlineKeyboardButton(text="Shanba: 13:00 - 14:00", callback_data=main_callback_data.new(cartime="Shanba 13-14")),
        ],

    ]
)


confirm_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❌Bekor qilish", callback_data="cancel"),
            InlineKeyboardButton(text="✅Tasdiqlash", callback_data="confirm"),
        ],


    ]
)