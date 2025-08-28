from langchain.chains import LLMChain, TransformChain
from app.core.config import llm
from app.prompts.classification_prompt import classification_prompt, classification_parser
from app.core.eneatypes import eneatype_details

classification_chain = LLMChain(
    llm=llm,
    prompt=classification_prompt,
    output_key="classification_raw"
)

def transform_classification(inputs: dict) -> dict:
    parsed = classification_parser.parse(inputs["classification_raw"])
    eneatype_number = parsed["eneatype_number"]
    return {
        "eneatype_number": eneatype_number,
        "eneatype_explanation": eneatype_details.get(eneatype_number, "")
    }

classification_transform = TransformChain(
    input_variables=["classification_raw"],
    output_variables=["eneatype_number", "eneatype_explanation"],
    transform=transform_classification
)
