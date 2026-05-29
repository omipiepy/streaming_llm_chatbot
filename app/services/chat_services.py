import asyncio
import httpx
from app.providers.factory import get_provider

from app.schemas.request import ChatRequest
from app.utils.retry import retry_async
from app.utils.timer import run_with_timeout
from app.core.logger import setup_logging, get_logger

setup_logging()

logger = get_logger(__name__)
logger.info("Chat service initialized")

class ChatService:
        async def chat(self, prompt: ChatRequest) -> str:

            provider = get_provider(prompt.provider)

            async def task():
                return await run_with_timeout(
                    provider.generate(prompt),
                    timeout=30
                )

            return await retry_async(
                task,
                max_attempts=3,
                delay=2
            )
        