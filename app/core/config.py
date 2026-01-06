from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    openrouter_api_key: str = Field(..., env="OPENROUTER_API_KEY")
    openrouter_Model: str = Field(..., env="OPENROUTER_MODEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()