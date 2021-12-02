from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


costs_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="1️⃣", callback_data="cost1"),
        InlineKeyboardButton(text="2️⃣", callback_data="cost2"),
        InlineKeyboardButton(text="3️⃣", callback_data="cost3"),
        InlineKeyboardButton(text="4️⃣", callback_data="cost4")
    ],
    [
        InlineKeyboardButton(text="5️⃣", callback_data="cost5"),
        InlineKeyboardButton(text="6️⃣", callback_data="cost6"),
        InlineKeyboardButton(text="7️⃣", callback_data="cost7"),
        InlineKeyboardButton(text="8️⃣", callback_data="cost8")
        ],
    [
        InlineKeyboardButton(text="O'chirish", callback_data="delete2")
    ]
    ])

data_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Bekor qilish", callback_data="delete")
    ]
    ]
)

admin_confirm = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Rad etish", callback_data="reject")
    ]
    ]
)
