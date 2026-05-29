from typing import AsyncGenerator
import json
import httpx
from app.utils.retry import retry_async
from app.core.config import settings
from app.core.logger import setup_logging, get_logger
from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse


setup_logging()
logger = get_logger(__name__)
logger.info("Gemini provider initialized")  

class GeminiProvider:

    async def generate(self, prompt: ChatRequest) -> str:
        result = ""

        async for chunk in self.stream(prompt):
            result += chunk.content

        return result

    async def stream(
        self,
        prompt: ChatRequest
    ) -> AsyncGenerator[ChatResponse, None]:

        url = (
            f"{settings.gemini_api_url}/"
            f"{settings.gemini_model_name}:generateContent"
        )

        params = {
            "key": settings.gemini_api_key
        }

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt.prompt}
                    ]
                }
            ]
        }


        async with httpx.AsyncClient(timeout=None) as client:
            response = await client.post(
                url,
                params=params,
                json=payload
            )

            async with httpx.AsyncClient(timeout=None) as client:

                response = await client.post(
                    url,
                    params=params,
                    json=payload
                )

                data = response.json()

                candidates = data.get("candidates", [])

                if not candidates:
                    return

                parts = (
                    candidates[0]
                    .get("content", {})
                    .get("parts", [])
                )

                if not parts:
                    return

                text = parts[0].get("text", "")

                if text:
                    if prompt.thinking:
                        print(text, end="", flush=True)

                    yield ChatResponse(
                        content=text,
                        done=False
                    )

                yield ChatResponse(
                    content="",
                    done=True
                )