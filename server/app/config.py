from os.path import join, dirname

from pydantic_settings import SettingsConfigDict, BaseSettings


# todo: Make prettier
DOTENV = join(dirname(dirname(dirname(__file__))), ".env")


class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_HOST: str

    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()
