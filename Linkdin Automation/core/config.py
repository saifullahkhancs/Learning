from pydantic_settings import BaseSettings
import os




class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    JWT_SECRET: str = ""
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"


settings = Settings()

if not settings.JWT_SECRET:
    raise ValueError(
        "JWT_SECRET is not configured. Set it in .env or as an environment variable. "
        "Refusing to start with an empty secret."
    )
