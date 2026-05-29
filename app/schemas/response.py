from pydantic import BaseModel, field_validator

class ChatResponse(BaseModel):
    content: str
    done: bool

    @field_validator("content")
    @classmethod
    def validate_content(cls, v):
        if not v or not v.strip():
            raise ValueError("content cannot be empty")
        return v