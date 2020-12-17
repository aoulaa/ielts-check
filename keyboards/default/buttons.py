from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# these buttons are main
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Academic IELTS')],
        [KeyboardButton(text='General IELTS')],

    ],
    resize_keyboard=True
)

academ_tasks_button = ReplyKeyboardMarkup(
    keyboard=[

        [KeyboardButton(text='Task 1'), KeyboardButton(text='Task 2')],
        [KeyboardButton(text='⬅back')]


    ],
    one_time_keyboard=True,
    resize_keyboard=True
)

general_tasks_button = ReplyKeyboardMarkup(
    keyboard=[

        [KeyboardButton(text='Tаsk 1'), KeyboardButton(text='Task 2')],
        [KeyboardButton(text='⬅back')]


    ],
    one_time_keyboard=True,
    resize_keyboard=True
)