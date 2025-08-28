from fastapi import APIRouter
from app.schemas.models import CharacterRequest, CharacterResponse
from app.chains.pipeline import full_chain

router = APIRouter(prefix="/api")

@router.post("/generate", response_model=CharacterResponse)
def generate_character_story(req: CharacterRequest):
    result = full_chain({"user_input": req.description})
    return CharacterResponse(**result)
