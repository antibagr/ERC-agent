from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env.local",
        env_file_encoding="utf-8",
        case_sensitive=True
    )
    
    # App Settings
    APP_NAME: str = "AI Bot"
    DEBUG: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "postgresql+asyncpg://botuser:botpass@localhost:5432/botdb"
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # LLM API Keys
    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""
    GROQ_API_KEY: str = ""
    
    # PydanticAI Settings
    PYDANTIC_AI_MODEL: str = "openai:gpt-4"
    PYDANTIC_AI_RETRIES: int = 2
    
    # Logfire (optional observability)
    LOGFIRE_TOKEN: str = ""
    
    # Security
    SECRET_KEY: str = "change-me-in-production"
    
settings = Settings()
