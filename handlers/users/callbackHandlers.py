import logging
from keyboards.default.menuKeyboard import menu
from handlers.users.informations import tico, matiz, spark, nexia1, nexia2, ravon, cobalt, lacetti, captiva, malibu, trailblazer
from aiogram.types import Message, CallbackQuery

from loader import dp
a = ['cost1', 'cost2', 'cost3', 'cost4', 'cost5', 'cost6', 'cost7', 'cost8',]

for i in a:
    @dp.callback_query_handler(text=a)
    async def send_message(call: CallbackQuery):
        await call.answer("Mazkur xizmat narxi $15", cache_time=60, show_alert=True)


@dp.callback_query_handler(text="delete")
async def get_callback(call: CallbackQuery):
    await call.answer("Ma'lumotlar bekor qilindi", show_alert=True)
    await call.message.delete()


@dp.callback_query_handler(text="delete2")
async def send_message(call: CallbackQuery):
    await call.message.delete()

@dp.callback_query_handler(text="confirm")
async def send_message(call: CallbackQuery):
    await call.answer("Buyurtmangiz qabul qilindi", show_alert=True)

@dp.callback_query_handler(text="delete")
async def send_message(call: CallbackQuery):
    await call.answer("Ma'lumotlar bekor qilindi", show_alert=True)
    await call.message.delete()

@dp.callback_query_handler(text="cancel")
async def send_message(call: CallbackQuery):
    await call.answer("Kerakli bo'limni tanlang👇")
    await call.message.delete()


@dp.callback_query_handler(text="type1")
async def send_message(call: CallbackQuery):
    await call.answer(tico, show_alert=True)

@dp.callback_query_handler(text="type2")
async def send_message(call: CallbackQuery):
    await call.answer(matiz, show_alert=True)


@dp.callback_query_handler(text="type3")
async def send_message(call: CallbackQuery):
    await call.answer(spark, show_alert=True)

@dp.callback_query_handler(text="type4")
async def send_message(call: CallbackQuery):
    await call.answer(nexia1, show_alert=True)


@dp.callback_query_handler(text="type5")
async def send_message(call: CallbackQuery):
    await call.answer(nexia2, show_alert=True)


@dp.callback_query_handler(text="type6")
async def send_message(call: CallbackQuery):
    await call.answer(ravon, show_alert=True)

@dp.callback_query_handler(text="type7")
async def send_message(call: CallbackQuery):
    await call.answer(cobalt, show_alert=True)


@dp.callback_query_handler(text="type8")
async def send_message(call: CallbackQuery):
    await call.answer(lacetti, show_alert=True)

@dp.callback_query_handler(text="type9")
async def send_message(call: CallbackQuery):
    await call.answer(captiva, show_alert=True)

@dp.callback_query_handler(text="type10")
async def send_message(call: CallbackQuery):
    await call.answer(malibu, show_alert=True)

@dp.callback_query_handler(text="type11")
async def send_message(call: CallbackQuery):
    await call.answer(trailblazer, show_alert=True)


@dp.callback_query_handler(text="reject")
async def send_message(call: CallbackQuery):
    await call.answer("Buyurtma bekor qilindi", show_alert=True)
    await call.message.delete()
