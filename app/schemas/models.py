from pydantic import BaseModel, Field

class GenerateRequest(BaseModel):
    system_prompt: str = Field(..., min_length=1)
    user_prompt: str = Field(..., min_length=1)
    temperature: float = Field(0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(512, ge=1, le=2048)

class Usage(BaseModel):
    input_tokens: int
    output_tokens: int

class GenerateResponse(BaseModel):
    output: str
    usage: Usage
    latency_ms: int