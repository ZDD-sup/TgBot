from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/Запись')
b3 = KeyboardButton('/Фотографии')
#b4 = KeyboardButton('/Контакт', request_contact=True, request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)