from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="RAG_"
    )

    llm_api_key: SecretStr          # obligatoire : pas de défaut
    log_level: str = "INFO"
    chunk_size: int = 800
    max_file_mb: int = 50
@lru_cache
def get_settings()-> Settings:
    return Settings()
