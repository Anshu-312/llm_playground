import time
from openrouter import OpenRouter
from typing import Tuple
from app.core.config import settings

client = OpenRouter(api_key=settings.openrouter_api_key)

def generate_completion(
        system_prompt:str,
        user_prompt:str,
        temperature:float,
        max_tokens:int
) -> Tuple[str, int, int, int]:
    
    start_time = time.time()
    response = client.chat.send(
        model=settings.openrouter_model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    latency_ms = int((time.time()-start_time) * 1000)

    return (
        response.choices[0].message.content,
        response.usage.prompt_tokens,
        response.usage.completion_tokens,
        latency_ms,
    )