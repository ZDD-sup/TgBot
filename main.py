from aiogram.utils import executor
from create_bot import dp
from handlers import client, admin, other
from data_base import sqlite_db

async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_baseid_start()
    sqlite_db.sql_photo_start()
'''******************************КЛИЕНТСКАЯ ЧАСТЬ*************************************'''
client.register_handlers_client(dp)


'''******************************АДМИНСКАЯ ЧАСТЬ**************************************'''
admin.register_handlers_admin(dp)


'''********************************ОБЩАЯ ЧАСТЬ****************************************'''
other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)