import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_API_BASE: str = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    MAX_API_CALLS: int = int(os.getenv("MAX_API_CALLS", 1000))
    COST_LIMIT: float = float(os.getenv("COST_LIMIT", 100.0))
    
    @property
    def is_development(self) -> bool:
        return self.ENVIRONMENT == "development"
    
    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "production"

settings = Settings()
