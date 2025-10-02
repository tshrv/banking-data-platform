from decouple import config
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_DB: str = config("POSTGRES_DB")
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = config("POSTGRES_HOST")
    POSTGRES_PORT: str = config("POSTGRES_PORT")
    POSTGRES_URL: str = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    model_config = ConfigDict(env_file=".env", extra="ignore")


settings = Settings()
