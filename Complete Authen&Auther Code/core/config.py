
import os

from pydantic_settings import BaseSettings
from pydantic import model_validator


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False
    # It's crucial to set a strong, secret key in your environment.
    # You can generate one with: openssl rand -hex 32
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    PASSWORD_RESET_TOKEN_EXPIRE_MINUTES: int = 30
    # check whether the url is given in
    PASSWORD_RESET_URL: str = os.environ.get("PASSWORD_RESET_URL")
    BACKEND_CORS_ORIGINS: str = os.environ.get("BACKEND_CORS_ORIGINS")
    SMTP_HOST: str | None = None
    SMTP_PORT: int = 587
    SMTP_USERNAME: str | None = None
    SMTP_PASSWORD: str | None = None
    SMTP_FROM_EMAIL: str | None = None
    SMTP_FROM_NAME: str = "LinkeFlow"
    SMTP_USE_TLS: bool = True
    SMTP_USE_SSL: bool = False

    @model_validator(mode="after")
    def validate_smtp_security(self):
        if self.SMTP_USE_TLS and self.SMTP_USE_SSL:
            raise ValueError("SMTP_USE_TLS and SMTP_USE_SSL cannot both be true")
        return self

    @property
    def cors_origins(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.BACKEND_CORS_ORIGINS.split(",")
            if origin.strip()
        ]

    class Config:
        env_file = ".env"


settings = Settings()
