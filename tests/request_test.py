import pytest
from unittest.mock import AsyncMock

from app.providers.ollama import OllamaProvider
from app.schemas.request import ChatRequest
from app.schemas.response import ChatResponse


@pytest.mark.asyncio
async def test_generate_with_mock(monkeypatch):

    provider = OllamaProvider()

    async def fake_stream(prompt):
        yield ChatResponse(content="Hello", done=False)
        yield ChatResponse(content=" World", done=True)

    monkeypatch.setattr(provider, "stream", fake_stream)

    result = await provider.generate(ChatRequest(prompt="Hello"))

    assert result == "Hello World"