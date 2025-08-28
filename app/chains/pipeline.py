from langchain.chains import SequentialChain
from app.chains.validation import validation_chain, validation_transform
from app.chains.classification import classification_chain, classification_transform
from app.chains.story import story_chain

full_chain = SequentialChain(
    chains=[
        validation_chain,
        validation_transform,
        classification_chain,
        classification_transform,
        story_chain
    ],
    input_variables=["user_input"],
    output_variables=["is_character", "error_message", "eneatype_number", "character_story"],
    verbose=True
)
