from pydantic import BaseModel

class CharacterRequest(BaseModel):
    description: str

class CharacterResponse(BaseModel):
    is_character: bool
    error_message: str | None = None
    eneatype_number: str | None = None
    character_story: str | None = None
