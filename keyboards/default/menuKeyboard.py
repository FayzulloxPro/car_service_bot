from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

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

main_menu = ReplyKeyboardMarkup(
    keyboard=[
       [
           KeyboardButton(text="Ro'yxatdan o'tish🗒")
       ],
       [
           KeyboardButton(text="Foydali ma'lumotlar"),
           KeyboardButton(text="Biz bilan bog'lanish☎️")
       ],
       [
           KeyboardButton(text="Orqaga↩️")
       ]
    ],
    resize_keyboard=True)

car_types = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            KeyboardButton(text="Tico🚙", callback_data="type1"),
            KeyboardButton(text="Matiz🚙", callback_data="type2"),
            KeyboardButton(text="Spark🚙", callback_data="type3")
        ],
        [
            KeyboardButton(text="Nexia1️⃣", callback_data="type4"),
            KeyboardButton(text="Nexia2️⃣", callback_data="type5"),
            KeyboardButton(text="Ravon🚙", callback_data="type6")
        ],
        [
            KeyboardButton(text="Cobalt🚙", callback_data="type7"),
            KeyboardButton(text="Lacetti🚙", callback_data="type8")
        ],
        [
            KeyboardButton(text="Captiva🚙", callback_data="type9"),
            KeyboardButton(text="Malibu🚙", callback_data="type10"),
            KeyboardButton(text="Trailblaizer🚙", callback_data="type11")
        ],
        [
            KeyboardButton(text="Ko'proq ma'lumot📕", url='https://uzautomotors.com/'),
            KeyboardButton(text="Orqaga↩️", callback_data="cancel")
        ]
    ]
)

about_us = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Markazimiz haqida⚒")
        ],
        [
            KeyboardButton(text="Bot haqida📑")
        ],
        [
            KeyboardButton(text="Orqaga↩️")
        ]
    ],
    resize_keyboard=True)

admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Buyurtmalarni ko'rish"),
            KeyboardButton(text="Vaqtlarni o'zgartirish")
        ]
    ],
    resize_keyboard=True
)


next = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="keyingisi")
        ]
    ], resize_keyboard=True
)


types = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tico"),
            KeyboardButton(text="Matiz"),
            KeyboardButton(text="Spark")
        ],
        [
            KeyboardButton(text="Nexia"),
            KeyboardButton(text="Nexia"),
            KeyboardButton(text="Ravon")
        ],
        [
            KeyboardButton(text="Cobalt"),
            KeyboardButton(text="Lacetti")
        ],
        [
            KeyboardButton(text="Captiva"),
            KeyboardButton(text="Malibu"),
            KeyboardButton(text="Trailblaizer")
        ],
        [
            KeyboardButton(text="Boshqa")
        ]
    ], resize_keyboard=True
)

times = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Dushanba 16:00'),
            KeyboardButton(text='Seshanba 14:30')

        ],
        [
            KeyboardButton(text='Chorshanba 10:00'),
            KeyboardButton(text='Payshanba 9:00')
        ]
    ],
    resize_keyboard=True
)



@dp.message_handler(text="Orqaga")
async def send_message(message: Message):
    await message.answer("Kerakli bo'limni tanlang👇", reply_markup=main_menu)

services = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1️⃣Dvigatel moyini almashtirish va filtrni almashtirish🛢")
        ],
        [
            KeyboardButton(text="2️⃣🔦Chiroqlar, shinalar, egzoz va tormoz va rul boshqaruvining ishlashini tekshirish⚙️")
        ],
        [
            KeyboardButton(text="3️⃣Dvigatelingiz eng yuqori holatda ishlashi uchun sozlanganligini taminlash🔩")
        ],
        [
            KeyboardButton(text="4️⃣Shlangi suyuqlik va sovutish suvi darajasini tekshirish🧯")
        ],
        [
            KeyboardButton(text="5️⃣Sovutish tizimini tekshirish (avtomobilingizdagi radiatorlardan nasoslar va shlanglargacha)🔧")
        ],
        [
            KeyboardButton(text="6️⃣To'xtatib turish tekshiruvlari⛓")
        ],
        [
            KeyboardButton(text="7️⃣Rul boshqaruvini tekislash🔧")
        ],
        [
            KeyboardButton(text="8️⃣Avtomobil akkumulyatorining holatini tekshirish🔋")
        ],
        [
            KeyboardButton(text="Boshqa turdagi service")
        ],

    ], resize_keyboard=True
)

