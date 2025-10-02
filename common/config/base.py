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
    RABBITMQ_USER: str = config("RABBITMQ_USER")
    RABBITMQ_PASSWORD: str = config("RABBITMQ_PASSWORD")
    RABBITMQ_HOST: str = config("RABBITMQ_HOST")
    RABBITMQ_PORT: str = config("RABBITMQ_PORT")
    RABBITMQ_URL: str = (
        f"amqp://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}"
    )

    model_config = ConfigDict(env_file=".env", extra="ignore")


settings = Settings()
