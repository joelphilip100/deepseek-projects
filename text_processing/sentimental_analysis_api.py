from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from sentimental_analysis import analyze_sentiment

app = FastAPI()


class SentimentalAnalysisRequest(BaseModel):
    prompt: str = Field(..., max_length=500, description="The input text to analyze sentiment")


class SentimentalAnalysisResponse(BaseModel):
    sentiment: str


@app.post("/analyze-sentiment/", response_model=SentimentalAnalysisResponse, summary="Analyze sentiment of text")
async def analyze_sentiment_api(request: SentimentalAnalysisRequest):
    if not request.prompt.strip():
        raise HTTPException(status_code=400, detail="Text is required")

    sentiment = analyze_sentiment(request.prompt)
    return {"sentiment": sentiment}
