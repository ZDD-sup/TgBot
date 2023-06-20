import json
import string

from aiogram import types, Dispatcher

from create_bot import dp


#@dp.message_handler()
async def del_mat(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}.intersection(set(json.load(open('mat.json')))) != set():
        await message.reply('Маты запрещены!')
        await message.delete()


'''*********************************************'''
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(del_mat)