import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from data.config import group_username
from keyboards.default.buttons import academ_tasks_button, menu, general_tasks_button
from keyboards.inline.inline_buttons import reply_photo, reply_1

from loader import bot, dp
from states.st import Data


@dp.callback_query_handler(text="admin_photo")
async def send_to_admin(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.copy_to(group_username[0], reply_markup=reply_photo)

    await call.message.delete_reply_markup()
    await call.message.answer('Your task has been sent to admins')


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer(cache_time=20)

    await call.message.delete_reply_markup()
    await call.message.answer('You cancelled the post.❗\n you can send another post',
                              reply_markup=academ_tasks_button)


@dp.callback_query_handler(text="cancel_admin")
async def cancel_admin(call: CallbackQuery, state: FSMContext):

    user_id = re.findall(r'%[1-9].+%', call.message.html_text)
    user_id = user_id[0][1:-1]
    await call.answer(cache_time=20)
    await call.message.answer(hbold('you cancelled the post, leave a comment, why❗'))

    await call.message.delete_reply_markup()
    await Data.data1.set()
    await state.update_data(
        {"user_id": user_id}
    )


@dp.message_handler(state=Data.data1)
async def send_comment(message: types.Message, state: FSMContext):

    data = await state.get_data()
    id_user = data.get("user_id")
    comment = message.text
    text = hbold('Your post was cancelled dut to❗')
    await bot.send_message(id_user, f'{text}\n\n{comment}',
                           reply_markup=menu)
    id_1 = await bot.get_chat(id_user)
    username = f"@{id_1.username}"
    await message.answer(f'comment has been delivered to {username}')
    await state.finish()


@dp.callback_query_handler(text="admin_msg")
async def send_to_admin(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.copy_to(group_username[0], reply_markup=reply_1)
    await call.message.delete_reply_markup()
    await call.message.answer('Your essay has been sent to admins wait for confirmation.✅')


@dp.message_handler(text='General IELTS📑')
async def general_ielts(message: types.Message):
    await message.answer('choose type of task',
                         reply_markup=general_tasks_button)
