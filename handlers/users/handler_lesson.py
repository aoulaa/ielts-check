
from aiogram import types
from aiogram.types import ContentType

from data.db_dict import ex_dict, book_dict

from keyboards.default.buttons import lessons_button, books_button
from loader import dp


@dp.message_handler(text='Tutorials👩🏻‍🏫')
async def tutorials(message: types.Message):
    await message.answer('Choose a lesson you want to watch',
                         reply_markup=lessons_button)


@dp.message_handler(text=ex_dict)
async def send_videos(message: types.message):
    video_data = ex_dict[message.text]
    await message.answer_video(video=video_data[0], caption=video_data[1])


@dp.message_handler(text='Books📗')
async def books(message: types.Message):
    await message.answer('Choose a book you want to read',
                         reply_markup=books_button)


@dp.message_handler(text=book_dict)
async def send_books(message: types.message):
    book_data = book_dict[message.text]
    await message.answer_document(document=book_data[0], caption=book_data[1])

#
# @dp.message_handler(content_types=ContentType.ANY)
# async def catch_pdf(message: types.message):
#
#     pdf = message.video.file_id
#     await message.answer(f'copy_id: {pdf}')