from typing import List
from pydantic import BaseSettings,field_validator
from dotenv import load_dotenv

class Settings(BaseSettings):
    DATABASE_URL: str

    ALLOWED_ORIGINS:str = ""

    API_PREFIX:str = "/api"

    DEBUG:bool = False

    OPENAI_API_KEY:str 

    @field_validator("ALLOWED_ORIGINS")
    def validate_alloewd_origins(cls, v:str) -> List[str]:
        return [origin.strip() for origin in v.split(",")] if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()
        