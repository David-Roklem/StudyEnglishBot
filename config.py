from aiogram import Bot, Router
from aiogram import Dispatcher
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)
    bot_token: str


settings = Settings()
