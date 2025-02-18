from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Influencer Discount Tracker API"
    DB_URL: str = "neo4j://localhost:7687"
    DB_USERNAME: str = "neo4j"
    DB_PASSWORD: str = ""
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    EXTENSION_ID: str = "lkompfalbaajhhgdeaegmnbgelpajlhh"

    class Config:
        env_file = ".env"

settings = Settings()