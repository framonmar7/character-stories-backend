from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

validation_schema = [
    ResponseSchema(
        name="is_character",
        description="true if it is a character description, false otherwise"
    )
]

validation_parser = StructuredOutputParser.from_response_schemas(validation_schema)
validation_instructions = validation_parser.get_format_instructions()

validation_prompt = PromptTemplate(
    input_variables=["user_input"],
    partial_variables={"format_instructions": validation_instructions},
    template="""
Analyze the following text and answer whether it corresponds to a character description.
A character description must include at least: identity (name or role), some traits,
and a conflict or difficulty.

Text: {user_input}

Respond only in this format:
{format_instructions}
"""
)
