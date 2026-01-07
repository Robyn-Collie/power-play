from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    GOOGLE_API_KEY: Optional[str] = None
    ENVIRONMENT: str = "development"
    LOG_LEVEL: str = "info"
    
    # MLB API Base URL
    MLB_API_BASE_URL: str = "https://statsapi.mlb.com/api/v1"
    
    # Look for .env in current dir OR in backend/ dir
    model_config = SettingsConfigDict(
        env_file=[".env", "backend/.env", "../.env"], 
        extra="ignore"
    )

settings = Settings()
