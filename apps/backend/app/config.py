from pydantic import (
    PostgresDsn, BaseModel,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

class Postgres(BaseModel):
    dsn: PostgresDsn

class GoogleSheet(BaseModel):
    id: str
    api_key: str

class Env(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", env_nested_delimiter="__")

    postgres: Postgres
    google_sheet: GoogleSheet

env = Env() # type: ignore
