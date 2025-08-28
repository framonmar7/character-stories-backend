from langchain.prompts import PromptTemplate

story_prompt = PromptTemplate(
    input_variables=["character_description", "eneatype_number", "eneatype_explanation"],
    template="""
The character is: {character_description}
They have been identified with Enneagram type {eneatype_number}.

Enneagram details:
{eneatype_explanation}

Write a deep and creative story about this character,
including their childhood, motivations, fears, and how these affect their relationships.
The story must remain psychologically consistent with the Enneagram type.
"""
)
