from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from grammar_check import check_grammar

app = FastAPI()


class GrammarCheckRequest(BaseModel):
    prompt: str = Field(..., max_length=500, description="The input text to check grammar")


class GrammarCheckResponse(BaseModel):
    corrected_text: str
    suggestions: list[str]


@app.post("/check-grammar/", response_model=GrammarCheckResponse, summary="Check grammar of text")
async def check_grammar_api(request: GrammarCheckRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Text is required")

    corrected_text, suggestions = check_grammar(request.prompt, True)
    return {"corrected_text": corrected_text, "suggestions": suggestions}
