from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards import admin_kb

from create_bot import bot

from data_base.sqlite_db import sql_add_p_command

ID = None

class FSMadmin(StatesGroup):
    photo = State()
    number = State()

#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message): # moderator
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Давайте поработаем', reply_markup = admin_kb.button_case_admin)
    await message.delete()

# Начало диолога об загрузки фотографий
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMadmin.photo.set()
        await message.reply('Загрузи фото')

#  @dp.message_handler(state="*", commands='отмена')
#  @dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
# Отмена загрузки
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('Ок!')

# Получаем с начало диолога фото и пишем в словарь
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMadmin.next()
        await message.reply('Теперь введи номер телефона без +7/8')

# Получаем номер телефона и записываем в словарь
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['number'] = message.text
        await sql_add_p_command(state)
        await state.finish()
        await message.reply('Надеюсь ему понравятся фотографии :)')


'''*********************************************'''
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMadmin.photo)
    dp.register_message_handler(load_name, state=FSMadmin.number)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)