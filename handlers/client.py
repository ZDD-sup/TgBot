from aiogram import types, Dispatcher

from create_bot import bot
from data_base.sqlite_db import sql_read
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help'])
async def command_start(messeage: types.Message):
    try:
        await bot.send_message(messeage.from_user.id, 'Чем могу помочь?', reply_markup=kb_client)  # отвечает в личку на сообщение с группы
        await messeage.delete()
        # await message.answer(message.text) # отвечает на сообщение
        # await message.reply(message.text) # указывает на какое сообщение отвечает
    except:  # если пользователь не добовлялся к боту вылезит данное сообщение в группе
        await messeage.reply('Для общения с ботом лично, напишите ему:\nt.me/BusCard_bot')


# @dp.message_handler(commands=['Запись'])
async def command_schedule(message: types.Message):
    await bot.send_message(message.from_user.id, 'Фотограф напишет в свободное время, для утачнеиня всех деталей.\nУкажите ваш номер телефона без +7 или 8, это будет ваш уникальный код для поиска готовых фотографий в будующем.\nПример номера РФ:1112223344')


# @dp.message_handler(commands=['Фотографии'])
async def command_package_photo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Укажите ваш номер телефона для поиска фото\nПример: 1112223344')
    resulte = sql_read(message.text)
    await bot.send_photo(message.from_user.id, )

'''*********************************************'''
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_schedule, commands=['Запись'])
    dp.register_message_handler(command_package_photo, commands=['Фотографии'])
