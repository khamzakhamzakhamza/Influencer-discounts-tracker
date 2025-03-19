from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = "neo4j://localhost:7687"
    DB_USERNAME: str = "neo4j"
    DB_PASSWORD: str = ""
    ENVIRONMENT: str = "development"
    YOUTUBE_API_KEY: str = ""

    class Config:
        env_file = ".env"

settings = Settings()