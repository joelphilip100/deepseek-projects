from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from named_entity_extractor import extract_named_entities

app = FastAPI()


class NamedEntityRequest(BaseModel):
    text: str = Field(..., max_length=500, description="The input text to extract named entities")
    entities: str = Field(..., max_length=100, description="The named entities to extract")


class NamedEntityResponse(BaseModel):
    result: object


@app.post("/extract-named-entities", response_model=NamedEntityResponse, summary="Extract named entities from text")
async def extract_named_entities_api(request: NamedEntityRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text is required")

    result = extract_named_entities(request.text, request.entities, True)
    return {"result": result}
