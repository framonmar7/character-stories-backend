from fastapi import APIRouter, HTTPException
from app.schemas.models import CharacterRequest, CharacterResponse
from app.chains.pipeline import graph

router = APIRouter(prefix="/api")

@router.post("/generate", response_model=CharacterResponse)
def generate_character_story(req: CharacterRequest):
    result = graph.invoke({"user_input": req.description})

    if not result.get("is_character"):
        raise HTTPException(status_code=400, detail=result.get("error_message"))

    return CharacterResponse(**result)
