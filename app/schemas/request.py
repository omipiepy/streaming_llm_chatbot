from pydantic import BaseModel

class ChatRequest(BaseModel):
    prompt:str
    provider: str | None = None
    thinking: bool = False
