from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(case_sensitive=False, env_file=".env")
    bot_token: str
    admin_id: int

    # Database config
    # DB_HOST: str
    # DB_NAME: str
    # DB_PORT: str
    # DB_USER: str
    # DB_PASS: str
    IS_ECHO: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    DB_URL: str = Field('', validation_alias='DB_URL')

    def __init__(self, **data):
        super().__init__(**data)
        self.DB_URL = self.__construct_db_url()

    def __construct_db_url(self) -> str:
        return (f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
                f"localhost:5433/{self.POSTGRES_DB}")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings


settings = get_settings()
