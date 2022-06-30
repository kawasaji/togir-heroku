import os
from flask import Flask, request
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.exceptions

API_TOKEN = '5430684434:AAFaGBTHBzBNoOllEFRiqHaN0RUD6Agt3Yg'
# API_URL = f'https://togir-bot.herokuapp.com/{API_TOKEN}'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# server = Flask(__name__)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("/ok")

@dp.message_handler(commands=['ok'])
async def start(message: types.Message):
    await message.reply("/start ok")


# @server.route('/' + API_TOKEN, methods=['POST'])
# def get_message():
#     json_string = request.get_data().decode('utf-8')
#     update = aiogram.types.Update.as_json(json_string)
#     bot.get_updates([update])
#     return '!', 200
#
# @server.route('/')
# def webhook():
#     bot.delete_webhook()
#     bot.set_webhook(url=API_URL)
#     return  '!', 200
#
# if __name__ == '__main__':
#     server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)