import os

from pydantic import Field, model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False
    SMTP_HOST: str = Field("smtp.gmail.com", env=["SMTP_HOST"])   
    SMTP_PORT: int = Field(587, env=["SMTP_PORT"])
    SMTP_USERNAME: str = Field("", env=["SMTP_USERNAME"])
    SMTP_PASSWORD: str = Field("", env=["SMTP_PASSWORD"])
    SMTP_FROM_EMAIL: str = Field("", env=["SMTP_USERNAME"])
    SMTP_FROM_NAME: str = "Saifullah Khan"
    SMTP_USE_TLS: bool = True
    SMTP_USE_SSL: bool = False

    @model_validator(mode="after")
    def validate_smtp_security(self):
        if self.SMTP_USE_TLS and self.SMTP_USE_SSL:
            raise ValueError("SMTP_USE_TLS and SMTP_USE_SSL cannot both be true")
        return self

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
