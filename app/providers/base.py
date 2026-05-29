from abc import ABC, abstractmethod
from typing import AsyncGenerator

from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse

class BaseProvider(ABC):
    @abstractmethod
    async def generate(self, prompt: ChatRequest) -> str:
        pass

    @abstractmethod
    def stream(self, prompt: ChatRequest) -> AsyncGenerator[ChatResponse, None]:
        pass