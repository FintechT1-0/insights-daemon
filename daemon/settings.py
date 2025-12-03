from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SCRAPER_API_KEY: str
    SCRAPER_API_URL: str
    PROXIED: bool
    DELAY: int

    class Config:
        env_file = ".env"

settings = Settings()