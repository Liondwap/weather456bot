import math
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='6014725046:AAHEK6sr5uLIuyiyTw_5wq1qLO-Z07Re2Ik')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message):
   await bot.send_message(message.chat.id, "Введите название города и я пришлю сводку погоды")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        city_name = message.text
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ru&units=metric&appid=e9bfd242705adb91d8a937787ff94285")
        data = response.json()
        city = data["name"]
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        await message.reply(f"Погода в городе: {city}\nТемпература: {cur_temp}°C \n"
                                f"Влажность: {humidity}%\nДавление: {math.ceil(pressure / 1.333)} мм.рт.ст\n"
                                f"Хорошего дня!")
    except:
        await message.reply("ошибка(!")






if __name__ == "__main__":
 executor.start_polling(dp)
