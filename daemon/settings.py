from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SCRAPER_API_KEY: str
    SCRAPER_API_URL: str

    class Config:
        env_file = ".env"

settings = Settings()