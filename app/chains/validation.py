from langchain.chains import LLMChain, TransformChain
from app.core.config import llm
from app.prompts.validation_prompt import validation_prompt, validation_parser

validation_chain = LLMChain(
    llm=llm,
    prompt=validation_prompt,
    output_key="validation_raw"
)

def transform_validation(inputs: dict) -> dict:
    parsed = validation_parser.parse(inputs["validation_raw"])
    is_character = str(parsed["is_character"]).lower() == "true"
    return {
        "is_character": is_character,
        "character_description": inputs["user_input"] if is_character else None,
        "error_message": None if is_character else "Please describe a character with a name, traits, and a conflict."
    }

validation_transform = TransformChain(
    input_variables=["validation_raw", "user_input"],
    output_variables=["is_character", "character_description", "error_message"],
    transform=transform_validation
)
