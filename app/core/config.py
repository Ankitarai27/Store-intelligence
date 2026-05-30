from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Store Intelligence API"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    log_level: str = "INFO"

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "store_intelligence"
    postgres_user: str = "postgres"
    postgres_password: str = "postgres"

    database_url: str = Field(
        default=(
            "postgresql+psycopg://"
            "postgres:postgres@localhost:5432/store_intelligence"
        )
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()