import sqlite3
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.buttons import menu_main
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name_user=name)
    except sqlite3.IntegrityError as err:
        print(err)

    await message.answer('You are in main menu. '
                         'Choose type of essay you want to send',
                         reply_markup=menu_main)


@dp.message_handler(text='⬅back', state="*")
async def go_back_to_post_menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('Choose type of IELTS task',
                         reply_markup=menu_main)


@dp.message_handler(text='⬅bаck', state="*")
async def go_back_to_menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('You are in main menu',
                         reply_markup=menu_main)


@dp.message_handler(Command(['restart', 'help']), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer('if something went wrong press /start')


