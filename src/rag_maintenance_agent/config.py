from pydantic import SecretStr,Field,model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import Literal

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="RAG_"
    )

    llm_api_key: SecretStr          # obligatoire : pas de défaut
    log_level: Literal["DEBUG","INFO","WARNING","ERROR"] ="INFO"
    chunk_size:int = Field(default=800,gt=0)
    max_file_mb: int = Field(default=50,gt=0)
    chunk_overlap: int = Field(default=100,ge=0)

    @model_validator(mode="after")
    #Avec model_validator ver_che est executé automatiquement lors de la creation du settings pour validation des cohérance des valeurs
    def verifier_chevauchement(self):
        if self.chunk_overlap >= self.chunk_size:
            raise ValueError(
                "chunk_overlap doit être inférieur à chunk_size"
            )
        return self
@lru_cache
#évite de recréer les paramètres à chaque appel à get_settings()
def get_settings()-> Settings:
    return Settings()
