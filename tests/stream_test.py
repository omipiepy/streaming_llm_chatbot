import pytest
from app.providers.ollama import OllamaProvider
from app.schemas.request import ChatRequest


@pytest.mark.asyncio
async def test_stream_response():
    provider = OllamaProvider()

    chunks = []

    async for chunk in provider.stream(ChatRequest(prompt="Hello")):
        chunks.append(chunk)

        assert hasattr(chunk, "content")
        assert hasattr(chunk, "done")

    # must return something
    assert len(chunks) > 0

    # last chunk should be done=True OR at least one done flag exists
    assert any(c.done for c in chunks)