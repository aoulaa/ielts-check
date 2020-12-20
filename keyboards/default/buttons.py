from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Send your essays for checking📝')],
        [KeyboardButton(text='Tutorials👩🏻‍🏫'), KeyboardButton(text='Books📗')],

    ],
    resize_keyboard=True
)

# these buttons are main
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Academic IELTS📑'), KeyboardButton(text='General IELTS📑')],
        [KeyboardButton(text='⬅bаck')],

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


lessons_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⬅bаck')],
        [KeyboardButton(text='Band 9 IELTS Vocabulary')],
        [KeyboardButton(text='Academic Writing Task 1')],
        [KeyboardButton(text='Task 1 Top Tips for 8+')],
        [KeyboardButton(text='Task 1 Informal Letters')],
        [KeyboardButton(text='score 8+ in Writing Task 2')],
        [KeyboardButton(text='Task 2  8+ in Vocabulary')],
        [KeyboardButton(text='Task 2 TIPS YOU NEED TO KNOW')],
        [KeyboardButton(text='3 step introduction task 2')],
        [KeyboardButton(text='How to Plan Task 2')],
        [KeyboardButton(text='Complex IELTS Sentences')],
        [KeyboardButton(text='Task 2 - Super Strategy!')]

    ],
    one_time_keyboard=True,
    resize_keyboard=True
)


books_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='⬅bаck')],
        [KeyboardButton(text='Tahasoni Ebrahim master ielts task 1')],
        [KeyboardButton(text='Tahasoni Ebrahim master ielts task 2')],
        [KeyboardButton(text='High Impact IELTS-Book')],
        [KeyboardButton(text='Collins Writing for IELTS')],


    ],
    one_time_keyboard=True,
    resize_keyboard=True
)










