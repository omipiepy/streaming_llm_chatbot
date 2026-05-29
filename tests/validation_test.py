import pytest
from pydantic import ValidationError

from app.schemas.request import ChatRequest


def test_chat_request_valid():
    req = ChatRequest(prompt="hello")
    assert req.prompt == "hello"
