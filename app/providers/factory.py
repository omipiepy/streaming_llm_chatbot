from app.core.config import settings
from app.providers.gemini import GeminiProvider
from app.providers.ollama import OllamaProvider

def get_provider(name: str | None = None):
  
    if name == "gemini":
        return GeminiProvider()
    if name == "ollama":
        return OllamaProvider()

    raise ValueError(f"Unknown provider: {name}")