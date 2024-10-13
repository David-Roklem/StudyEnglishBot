import os
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode  # aiogram 3
from aiogram.client.default import DefaultBotProperties
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
# from aiogram.contrib.fsm_storage.memory import MemoryStorage


load_dotenv(find_dotenv())

# storage = MemoryStorage()
bot = Bot(os.getenv('TELEGRAM_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher()
