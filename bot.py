from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

bot = Bot(os.getenv('TELEGRAM_TOKEN'))

dp = Dispatcher(bot)


async def on_startup(_):
    print("2translate has started!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
