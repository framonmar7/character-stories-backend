from fastapi import APIRouter, HTTPException
from openai import AuthenticationError, RateLimitError, APIConnectionError, APIStatusError
from app.schemas.models import CharacterRequest, CharacterResponse
from app.chains.pipeline import graph
from app.api.responses import error_responses

router = APIRouter(
    prefix="/api",
    tags=["Endpoints"]
)

@router.get("/", include_in_schema=False)
def index():
    return {
        "message": "Welcome to the Character Stories API",
        "endpoints": {
            "generate_character_story": "/api/generate"
        },
        "docs": "/docs"
    }

@router.post("/generate", response_model=CharacterResponse, responses=error_responses)
def generate_character_story(req: CharacterRequest):
    try:
        result = graph.invoke({"user_input": req.description})
    except AuthenticationError:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")
    except RateLimitError:
        raise HTTPException(status_code=429, detail="You exceeded your current quota")
    except (APIConnectionError, APIStatusError):
        raise HTTPException(status_code=503, detail="OpenAI service temporarily unavailable")
    except Exception:
        raise HTTPException(status_code=500, detail="Unexpected internal error")

    if not result.get("is_character"):
        raise HTTPException(status_code=400, detail="Please describe a character with a name, traits, and a conflict")

    return CharacterResponse(
        eneatype_number=result["eneatype_number"],
        character_story=result["character_story"],
    )
