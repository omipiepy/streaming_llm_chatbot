import asyncio
import httpx
from app.providers.factory import get_provider

from app.schemas.request import ChatRequest
from app.utils.retry import retry_async
from app.utils.timer import run_with_timeout


class ChatService:
    async def chat(self, prompt: ChatRequest) -> str:

        timeout_seconds = 30
        provider = get_provider(prompt.provider)
        async def task():
            return await provider.generate(prompt)

        return await retry_async(
            lambda: run_with_timeout(task(), timeout_seconds),
            max_attempts=3,
            delay=2
        )