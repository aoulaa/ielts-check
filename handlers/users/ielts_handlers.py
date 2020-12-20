import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ContentType
from aiogram.utils.exceptions import BadRequest
from aiogram.utils.markdown import hitalic

from data.config import channels

from keyboards.default.buttons import academ_tasks_button, menu
from keyboards.inline.inline_buttons import admin_photo_admin, post_text
from loader import bot, dp, db
from states import PostData


@dp.message_handler(text='Send your essays for checking📝')
async def get_your_essay_check(message: types.Message):
    await message.answer('Choose type of IELTS task',
                         reply_markup=menu)


@dp.message_handler(text='Academic IELTS📑')
async def academic_ielts(message: types.Message):
    await message.answer('Choose type of task you want to post on channel',
                         reply_markup=academ_tasks_button)


@dp.message_handler(text='Task 1')
async def task_1(message: types.Message, state: FSMContext):
    await message.answer('Send photo of your task 🖼️')

    await state.set_state('photo_state')


@dp.message_handler(state='photo_state', content_types=ContentType.ANY)
async def catch_photo(message: types.message, state: FSMContext):
    if not message.photo:
        await message.answer('Send photo of your task 1')
    else:
        photo_id = message.photo[-1].file_id
        db.update_task_1_photo_id(task_1_photo_id=photo_id, id=message.from_user.id)
        await message.answer('Send the essay you have written')
        await state.set_state('text_state')


# task 1
@dp.message_handler(state='text_state')
async def ready_answer1(message: types.Message, state: FSMContext):
    try:
        task_writing = str(message.html_text)
        db.update_task_1_writing(task_1_writing=task_writing, id=message.from_user.id)
        user1 = db.select_user(id=message.from_user.id)
        msg_text = "\n".join(
            [
                f'%{user1[0]}%',
                hitalic(user1[2])
            ]
        )
        await message.answer_photo(photo=user1[4], caption=msg_text, reply_markup=admin_photo_admin)
        await state.finish()
    except BadRequest:
        await message.answer("Text is too long please do not go over the limit(180)❗\n\n "
                             "(if you have written over the limit, you can send the rest of "
                             "your essay in comments when your post is approved)")


# for posts with photo
@dp.callback_query_handler(text="confirm_photo")
async def confirm(call: CallbackQuery):
    await call.answer('You confirmed the post', show_alert=True)

    user = re.findall(r'%[1-9].+%', call.message.html_text)
    user = user[0][1:-1]
    id_1 = await bot.get_chat(user)
    username1 = f"@{id_1.username}"
    await call.message.answer(f'user posted the post: {username1}')
    if len(user) == 10:
        target_channel = channels[0]
        text = call.message.html_text
        photo = call.message.photo[-1].file_id
        text = text[12:]

        await bot.send_message(user, f'Admin confirmed the post {target_channel}.✅',
                               reply_markup=menu)
        await bot.send_photo(target_channel, photo=photo, caption=text)
        await call.message.delete_reply_markup()
    elif len(user) == 9:
        target_channel = channels[0]
        text = call.message.html_text
        photo = call.message.photo[-1].file_id
        text = text[11:]
        await bot.send_message(user, f'Admin confirmed the post {target_channel}.✅',
                               reply_markup=menu)
        await bot.send_photo(target_channel, photo=photo, caption=text)

        await call.message.delete_reply_markup()
    elif len(user) <= 8:
        target_channel = channels[0]
        text = call.message.html_text
        photo = call.message.photo[-1].file_id
        text = text[11:]
        await bot.send_message(user, f'Admin confirmed the post {target_channel}.✅',
                               reply_markup=menu)
        await bot.send_photo(target_channel, photo=photo, caption=text)

        await call.message.delete_reply_markup()


@dp.callback_query_handler(text="confirm")
async def confirm(call: CallbackQuery):
    await call.answer('You confirmed the post', show_alert=True)
    user = re.findall(r'%[1-9].+%', call.message.html_text)
    user = user[0][1:-1]
    id_1 = await bot.get_chat(user)
    username1 = f"@{id_1.username}"
    await call.message.answer(f'user posted the post: {username1}')
    if len(user) == 10:
        target_channel = channels[0]
        text = call.message.html_text
        text = text[12:]

        await bot.send_message(user, f'Admin confirmed the post {target_channel}.✅',
                               reply_markup=menu)
        await bot.send_message(target_channel, text)
        await call.message.delete_reply_markup()
    elif len(user) == 9:
        target_channel = channels[0]
        text = call.message.html_text
        text = text[11:]
        await bot.send_message(user, f'Admin confirmed the post {target_channel}.✅',
                               reply_markup=menu)
        await bot.send_message(target_channel, text)

        await call.message.delete_reply_markup()
    elif len(user) <= 8:
        target_channel = channels[0]
        text = call.message.html_text
        text = text[11:]
        await bot.send_message(user, f'Admin confirmed the post {target_channel}.✅',
                               reply_markup=menu)
        await bot.send_message(target_channel, text)

        await call.message.delete_reply_markup()


# post bez foto
# post dlya task 2
@dp.message_handler(text=(['Task 2', 'Tаsk 1']))
async def send_ready_post(message: types.message):
    await message.answer('Send your essay for checking', )

    await PostData.save.set()


@dp.message_handler(state=PostData.save)
async def ready_essay(message: types.Message, state: FSMContext):
    task_writing_1 = str(message.html_text)

    db.update_task_1_writing(task_1_writing=task_writing_1, id=message.from_user.id)
    user1 = db.select_user(id=message.from_user.id)

    msg_text = "\n".join(
        [f'%{user1[0]}%',
         hitalic(user1[2])
         ]
    )
    await message.answer(msg_text, reply_markup=post_text)
    await state.finish()
