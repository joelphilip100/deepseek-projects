import fastapi

from text_summarizer import summarize_text

app = fastapi.FastAPI()


@app.get("/summarize/")
async def summarize(text: str):
    return {"summary": summarize_text(text)}
