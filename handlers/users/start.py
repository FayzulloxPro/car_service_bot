import sqlite3
from keyboards.default.menuKeyboard import menu
from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, bot, db

@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    name = message.from_user.full_name
    #Foydalanuvchini bazaga qo'shamiz
    # try:
    #     db.add_user(id=message.from_user.id,
    #                 name=name)
    # except sqlite3.IntegrityError as err:
    #     await bot.send_message(chat_id=ADMINS[0], text=err)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name} \nBizni tanlaganingizdan xursandmiz😊 ")
    await message.answer(
        "👉Ro'yxatdan o'tish uchun asosiy menyuga o'ting📜\n \n👉Bizning avtoservice va mazkur bot haqida ma'lumot olish uchun Biz haqimizda bo'limiga o'ting📃",
        reply_markup=menu)
    # adminga xabar beramiz
    # count = db.count_users()[0]
    # msg = f"{message.from_user.full_name} bazaga qo'shildi. \nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)





# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
# from keyboards.default.menu import menu
# from loader import dp
# from utils.db_api import database as db
#
#
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     user = await db.get_user(user_id=message.from_user.id)
#     if user:
#         markup = await menu(user)
#         await message.answer(f"Salom, {message.from_user.full_name}!\n")
#         await message.answer("Car Service botiga xush kelibsiz", reply_markup=markup)
#     else:
#         user = await db.add_user(user_id=message.from_user.id, name=message.from_user.full_name)
#         markup = await menu(user)
#         await message.answer(f"Salom, {message.from_user.full_name}!\n")
#         await message.answer("Car Service botiga xush kelibsiz", reply_markup=markup)

