from typing import AsyncGenerator
import json
import httpx

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
            "key": settings.gemini_api_key,
            "alt": "sse"
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

            logger.info(f"Streaming Request URL: {url}")

            async with client.stream(
                "POST",
                url,
                params=params,
                json=payload
            ) as response:

                response.raise_for_status()

                async for line in response.aiter_lines():

                    if not line:
                        continue


                    if line.startswith("data: "):
                        line = line.removeprefix("data: ")
                    try:
                        data = json.loads(line)

                        candidates = data.get("candidates", [])

                        if not candidates:
                            continue

                        parts = (
                            candidates[0]
                            .get("content", {})
                            .get("parts", [])
                        )

                        if not parts:
                            continue

                        text = parts[0].get("text", "")
                        if prompt.thinking:
                            print(text, end="", flush=True)
                        if text:
                            yield ChatResponse(
                                content=text,
                                done=False
                            )

                    except json.JSONDecodeError:
                        continue

                yield ChatResponse(
                    content="",
                    done=True
                )