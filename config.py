import os
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode  # aiogram 3
from aiogram.client.default import DefaultBotProperties
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pydantic_settings import BaseSettings, SettingsConfigDict


# load_dotenv(find_dotenv())

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)

    bot_token: str


settings = Settings()

# storage = MemoryStorage()
bot = Bot(settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher()
