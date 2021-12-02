from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.menuKeyboard import main_menu
from keyboards.default.menuKeyboard import about_us
from handlers.users.informations import about_service
from handlers.users.informations import about_bot
from handlers.users.informations import contact_us, available_services
from keyboards.default.menuKeyboard import car_types, times, next, types, services
from keyboards.inline.inlineKeyboards import costs_menu, admin_confirm, data_confirm
from loader import dp
import logging
import typing
import time
ADMINS = [912429653, 1362961919]


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, ContentTypes, ReplyKeyboardRemove

from backend.models import Order

from keyboards.default.menu import menu, share_contact
from keyboards.inline.main_inline import main_callback_data, confirm_btn, get_reservation
from keyboards.default.menuKeyboard import types
from utils.db_api.database import get_user
from keyboards.inline.main_inline import time_control_btn
from loader import dp, bot

@dp.message_handler(text="Orqaga")
async def send_message(message: Message):
    await message.answer("Kerakli bo'limni tanlang👇", reply_markup=main_menu)


@dp.message_handler(text="Asosiy menyu📜")
async def send_message(message: Message):
    await message.answer("Kerakli bo'limni tanlang👇", reply_markup=main_menu)

@dp.message_handler(text="Biz haqimizda📃")
async def send_message(message: Message):
    await message.answer("Qanday ma'lumot kerak🧐", reply_markup=about_us)

@dp.message_handler(text="Orqaga↩️")
async def send_message(message: Message):
    await message.answer("Kerakli bo'limni tanlang👇", reply_markup=menu)

@dp.message_handler(text="Markazimiz haqida⚒")
async def send_message(message: Message):
    await message.answer(about_service)

@dp.message_handler(text="Bot haqida📑")
async def send_message(message: Message):
    await message.answer(about_bot)

@dp.message_handler(text="Foydali ma'lumotlar")
async def send_message(message: Message):
    await message.answer("Avtomobillar haqida bilib oling\n \n Qaysi avtomobil haqida bilishni xohlaysiz?", reply_markup=car_types)

@dp.message_handler(text="Biz bilan bog'lanish☎️")
async def send_message(message: Message):
    await message.answer(contact_us)

@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name} \nBizni tanlaganingizdan xursandmiz😊 ")
    await message.answer("👉Ro'yxatdan o'tish uchun asosiy menyuga o'ting📜\n \n👉Bizning avtoservice va mazkur bot haqida ma'lumot olish uchun Biz haqimizda bo'limiga o'ting📃", reply_markup=menu)

@dp.message_handler(text="Asosiy menyu📜")
async def send_message(message: Message):
    await message.answer("Kerakli bo'limni tanlang👇", reply_markup=main_menu)

@dp.message_handler(text="Biz haqimizda📃")
async def send_message(message: Message):
    await message.answer("Qanday ma'lumot kerak🧐", reply_markup=about_us)

@dp.message_handler(text="Orqaga↩️")
async def send_message(message: Message):
    await message.answer("Kerakli bo'limni tanlang👇", reply_markup=menu)

@dp.message_handler(text="Markazimiz haqida⚒")
async def send_message(message: Message):
    await message.answer(about_service)

@dp.message_handler(text="Bot haqida📑")
async def send_message(message: Message):
    await message.answer(about_bot)

@dp.message_handler(text="Foydali ma'lumotlar")
async def send_message(message: Message):
    await message.answer("Avtomobillar haqida bilib oling\n \n Qaysi avtomobil haqida bilishni xohlaysiz?", reply_markup=car_types)

@dp.message_handler(text="Biz bilan bog'lanish☎️")
async def send_message(message: Message):
    await message.answer(contact_us)


@dp.message_handler(text="Ro'yxatdan o'tish🗒")
async def send_link(message: Message):
    await message.answer("Service turini tanlang", reply_markup=services)

#
@dp.message_handler(text="1️⃣Dvigatel moyini almashtirish va filtrni almashtirish🛢")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="2️⃣🔦Chiroqlar, shinalar, egzoz va tormoz va rul boshqaruvining ishlashini tekshirish⚙️")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="3️⃣Dvigatelingiz eng yuqori holatda ishlashi uchun sozlanganligini taminlash🔩")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="4️⃣Shlangi suyuqlik va sovutish suvi darajasini tekshirish🧯")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="5️⃣Sovutish tizimini tekshirish (avtomobilingizdagi radiatorlardan nasoslar va shlanglargacha)🔧")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="6️⃣To'xtatib turish tekshiruvlari⛓")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="7️⃣Rul boshqaruvini tekislash🔧")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="8️⃣Avtomobil akkumulyatorining holatini tekshirish🔋")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)


@dp.message_handler(text="Boshqa turdagi service")
async def send_link(message: Message, state: FSMContext):
    message_id = (await message.answer(".", reply_markup=ReplyKeyboardRemove())).message_id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
    await message.answer("Mazkur xizmat narxi: $15\n"
                         "\n"
                         "Anketani to'ldiring va sizga qulay bo'lgan vaqtni tanlang", reply_markup=get_reservation)
    type_service = message.text

@dp.callback_query_handler(text="go_anketa")
async def start_anketa(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await call.message.delete()
    await call.message.answer("Iltimos to'liq ismingizni kiriting")
    await state.set_state("fullname")


@dp.callback_query_handler(text="back_to_services")
async def back_to_services_fun(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Servis turini tanlang", reply_markup=services)




@dp.message_handler(state="fullname")
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Iltimos telefon raqamingizni kiriting", reply_markup=share_contact)
    await state.set_state("phone")


@dp.message_handler(state="phone", content_types=ContentTypes.CONTACT)
async def get_car(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    await state.update_data(phone=phone)
    await message.answer("Avtomobil rusumini tanlang", reply_markup=types)
    await state.set_state("car_name")


@dp.message_handler(state="car_name")
async def car_type(message: Message, state: FSMContext):
    car_name = message.text
    await state.update_data(car_name=car_name)
    await message.answer("Avtomobil turi qabul qilindi")
    await message.answer("Iltimos qulay vaqtni tanlang", reply_markup=times)
    await state.set_state("cartime")


@dp.message_handler(state="cartime")
async def get_time_and_confirm(message: Message, state: FSMContext):
    cartime = message.text
    await state.update_data(cartime=cartime)
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    car_name = data.get("car_name")
    msg = "👇Quyidagi ma'lumotlar qabul qilindi👇:\n \n"
    msg += f"📑Ism: - {name}\n \n"
    msg += f"📲Telefon raqam: - {phone}\n \n"
    msg += f"🚘Avtmobil rusumi: - {car_name}\n \n"
    msg += f"🕰Vaqti: - {cartime}"
    await message.answer(f"{msg}\n \nBizning manzil:\nTurin Polytechnic University\n \nhttps://maps.app.goo.gl/XeRDnvGMDHdu5B5u9", reply_markup=data_confirm)


    car_order = Order()
    car_order.servic_type = "3️⃣Dvigatelingiz eng yuqori holatda ishlashi uchun sozlanganligini taminlash🔩"
    car_order.full_name = name
    car_order.phone_num = phone
    car_order.car_name = car_name
    car_order.cartime = cartime
    car_order.payment = False

    car_order.save()






    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, msg, reply_markup=admin_confirm)

        except Exception as err:
            logging.exception(err)


    time.sleep(15)
    await message.answer(f"{msg}\n \n \nSizga yuqoridagi xabarni eslatmoqchiman👆")

