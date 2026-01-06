# LLM Playground

Lightweight FastAPI service for experimenting with LLM prompts via OpenRouter.

**Status:** Prototype

**Contents:**
- `app/main.py` — FastAPI app exposing the `/generate` endpoint
- `app/services/llm_client.py` — OpenRouter client wrapper
- `app/core/config.py` — environment-backed settings
- `app/schemas/models.py` — request/response Pydantic models

## Overview

LLM Playground is a minimal, local HTTP API that makes it easy to prototype prompt engineering workflows against OpenRouter-compatible LLMs. It accepts a `system_prompt` and `user_prompt`, forwards them to the configured model, and returns the generated text along with token usage and latency.

## Features

- Simple single endpoint API for quick experiments
- Uses `openrouter` client and reads credentials from environment
- Typed request/response models with `pydantic`

## Requirements

- Python 3.10+
- See `requirements.txt` for runtime dependencies

## Quickstart

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Create a `.env` file in the project root (or set env vars in your environment):

```
OPENROUTER_API_KEY=sk-...
OPENROUTER_MODEL=gpt-4o-mini
```

3. Run the server locally:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4. Try the API (example `curl`):

```bash
curl -s -X POST http://localhost:8000/generate \
	-H "Content-Type: application/json" \
	-d '{"system_prompt":"You are a helpful assistant.","user_prompt":"Summarize the benefits of unit testing.","temperature":0.7,"max_tokens":200}'
```

## API

POST /generate

Request model (`GenerateRequest`):
- `system_prompt` (str): system role instructions
- `user_prompt` (str): user query
- `temperature` (float): sampling temperature (0.0–2.0)
- `max_tokens` (int): maximum tokens for the response

Response model (`GenerateResponse`):
- `output` (str): generated text
- `usage` (object): `input_tokens` and `output_tokens`
- `latency_ms` (int): round-trip time in milliseconds

The API is implemented in `app/main.py` and uses `app/services/llm_client.py` to call OpenRouter.

## Configuration

Configuration is handled by `pydantic-settings`. Put values in a `.env` file or export them:

- `OPENROUTER_API_KEY` — API key for OpenRouter
- `OPENROUTER_MODEL` — model id to use

See `app/core/config.py` for details.

## Development notes

- The `generate_completion` function in `app/services/llm_client.py` returns a tuple: `(output, prompt_tokens, completion_tokens, latency_ms)`.
- Errors in `app/main.py` are surfaced as `HTTP 500` and the stacktrace is printed to the server console for debugging.

## Contributing

Contributions are welcome. Open an issue or PR with a clear description of the change.

## License

This project is provided under the terms of the repository `LICENSE` file.

## Contact

If you have questions, open an issue or contact the maintainer.
