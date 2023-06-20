from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

storage = MemoryStorage()

bot = Bot(config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
