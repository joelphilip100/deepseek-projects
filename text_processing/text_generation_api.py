from typing import Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from text_generation import generate_text

app = FastAPI()


class TextGenerationRequest(BaseModel):
    prompt: str = Field(..., max_length=100, description="The input prompt to generate text")
    word_limit: int = Field(ge=50, le=500, default=50, description="The number of words to generate")
    language: Literal["English", "Hindi", "Spanish"] = Field(default="English", description="The language of the generated text")


class TextGenerationResponse(BaseModel):
    summary: str


@app.post("/generate/", response_model=TextGenerationResponse, summary="Generate text from prompt")
async def generate(request: TextGenerationRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt is required")

    summary = generate_text(request.prompt, request.word_limit, request.language)
    return {"summary": summary}
