from fastapi import APIRouter, HTTPException
from app.schemas.models import CharacterRequest, CharacterResponse
from app.chains.pipeline import graph
from app.api.responses import error_responses

router = APIRouter(prefix="/api")

@router.post("/generate", response_model=CharacterResponse, responses=error_responses)
def generate_character_story(req: CharacterRequest):
    result = graph.invoke({"user_input": req.description})

    if not result.get("is_character"):
        raise HTTPException(status_code=400, detail="Please describe a character with a name, traits, and a conflict.")

    try:
        return CharacterResponse(
            eneatype_number=result["eneatype_number"],
            character_story=result["character_story"],
        )
    except Exception:
        raise HTTPException(status_code=500, detail="OpenAI quota exceeded")
