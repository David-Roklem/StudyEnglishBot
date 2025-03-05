import os
from functools import lru_cache
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(case_sensitive=False)
    bot_token: str

    # Database config
    DB_HOST: str
    DB_NAME: str
    DB_PORT: str
    DB_USER: str
    DB_PASS: str
    IS_ECHO: str

    DB_URL: str = Field('', validation_alias='DB_URL')

    # other configs
    bot_token: str
    admin_id: int

    # class Config:
    #     extra = 'ignore'
    #     BASE_DIR = Path(__file__).resolve().parent.parent
    #     env_file = os.path.join(BASE_DIR, '.env')

    def __init__(self, **data):
        super().__init__(**data)
        self.DB_URL = self.__construct_db_url()

    def __construct_db_url(self) -> str:
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings


settings = get_settings()
