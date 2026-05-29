from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import os
from app.core.logger import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)
load_dotenv()

class Settings(BaseSettings):
    ollama_api_url: str = os.getenv("OLLAMA_API_URL", "")
    ollama_model_name: str = os.getenv("OLLAMA_MODEL_NAME", "")
    gemini_api_url: str = os.getenv("GEMINI_API_URL", "")
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    gemini_model_name: str = os.getenv("GEMINI_MODEL_NAME", "")

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"                         
      )


settings = Settings()
logger.info(f"Configuration loaded for OllamaProvider")
logger.info(f"Configuration loaded for GeminiProvider")
