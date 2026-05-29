from pydantic import BaseModel

class ChatResponse(BaseModel):
    content: str
    done: bool