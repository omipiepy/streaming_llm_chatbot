from typing import AsyncGenerator
import httpx
import json
from app.providers.base import BaseProvider
from app.core.config import settings
from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse
from app.core.logger import setup_logging, get_logger

setup_logging()

logger = get_logger(__name__)
logger.info("Ollama provider initialized")


class OllamaProvider(BaseProvider):

    async def generate(self, prompt: ChatRequest) -> str:
        result = ""
        async for token in self.stream(prompt):
            result += token.content
        return result

    async def stream(self, prompt: ChatRequest) -> AsyncGenerator[ChatResponse, None]:

        
        url = f"{settings.ollama_api_url}/api/generate"

        payload =  {
            "model": settings.ollama_model_name,
            "prompt": prompt.prompt,
            "stream": True
        }
        logger.info(f"Sending request to Ollama: {payload}")

        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream("POST", url, json=payload) as r:
                async for line in r.aiter_lines():
                    if not line:
                        continue

                    data = json.loads(line)

                    token = data.get("response", "")

                    if token:
                        if prompt.thinking:
                            print(token, end="", flush=True) 

                        yield ChatResponse(
                            content=token,
                            done=False
                        )
                        

                    if data.get("done"):
                        yield ChatResponse(content="", done=True)
                        break
    logger.info("Finished streaming response from Ollama")