from pydantic import BaseModel, field_validator

class ChatRequest(BaseModel):
    prompt:str
    provider: str | None = None
    thinking: bool = False
    timeout: int 

    @field_validator("prompt")
    @classmethod
    def validate_prompt(cls, v):
        if not v or not v.strip():
            raise ValueError("prompt cannot be empty")
        return v.strip()
    
    @field_validator("timeout")
    @classmethod
    def validate_timeout(cls, v):
        if v < 1:
            raise ValueError("timeout too small (min 1s)")
        if v > 120:
            raise ValueError("timeout too large (max 120s)")

        return v
