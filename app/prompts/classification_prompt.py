from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from app.core.eneatypes import eneatype_details

classification_schema = [
    ResponseSchema(
        name="eneatype_number",
        description="Enneagram type number (1-9)"
    )
]

classification_parser = StructuredOutputParser.from_response_schemas(classification_schema)
classification_instructions = classification_parser.get_format_instructions()

eneatypes_text = "\n".join([f"{num}: {desc}" for num, desc in eneatype_details.items()])

classification_prompt = PromptTemplate(
    input_variables=["character_description"],
    partial_variables={"format_instructions": classification_instructions, "eneatypes_text": eneatypes_text},
    template="""
Analyze the following character and decide which of the 9 Enneagram types fits best.

Enneagram types:
{eneatypes_text}

Character description: {character_description}

Respond only in this format:
{format_instructions}
"""
)
