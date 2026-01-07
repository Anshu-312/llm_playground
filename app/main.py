from fastapi import FastAPI, HTTPException
from app.schemas.models import GenerateRequest, GenerateResponse, Usage
from app.services.llm_client import generate_completion

app = FastAPI(title="LLM Playground API", version="0.1.0")

@app.post("/generate", response_model=GenerateResponse)
async def generate(req: GenerateRequest):
    try:
        output, in_tokens, out_tokens, latency = generate_completion(
            system_prompt=req.system_prompt,
            user_prompt=req.user_prompt,
            temperature=req.temperature,
            max_tokens=req.max_tokens
        )

        return GenerateResponse(
            output=output,
            usage=Usage(
                input_tokens=in_tokens,
                output_tokens=out_tokens,
            ),
            latency_ms=latency
        )
    except Exception as e:
        # No silent failures
        import traceback
        print(traceback.format_exc())  # This prints the full error to your terminal
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def home():
    return {"Welcome to the LLM Playground API!"}    