from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from loader import dp

share_contact = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamni kiriting", request_contact=True)
        ]
    ],
    resize_keyboard=True
)
#
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Asosiy menyu📜')
        ],
        [
            KeyboardButton(text='Biz haqimizda📃')
        ]
    ],
    resize_keyboard=True
)







