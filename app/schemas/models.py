from pydantic import BaseModel

class CharacterRequest(BaseModel):
    description: str

class CharacterResponse(BaseModel):
    eneatype_number: str
    character_story: str
