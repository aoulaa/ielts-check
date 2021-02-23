from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_photo_admin = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Send to admin📤", callback_data='admin_photo'),
            InlineKeyboardButton(text="Cancel❌", callback_data='cancel')
        ],

    ], resize_keyboard=True)

post_text = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Send to admin📤", callback_data='admin_msg'),
            InlineKeyboardButton(text="Cancel❌", callback_data='cancel')
        ],

    ], resize_keyboard=True)

reply_photo = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Confirm✅", callback_data='confirm_photo'),
            InlineKeyboardButton(text="Cancel❌", callback_data='cancel_admin')
        ],
    ], resize_keyboard=True)

reply_1 = InlineKeyboardMarkup(
    row_width=2,

    inline_keyboard=[
        [
            InlineKeyboardButton(text="Confirm✅", callback_data='confirm'),
            InlineKeyboardButton(text="Cancel❌", callback_data='cancel_admin')
        ],
    ], resize_keyboard=True)
