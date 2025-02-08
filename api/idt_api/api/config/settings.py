from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Influencer Discount Tracker API"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()