from typing import TypedDict
from langgraph.graph import StateGraph, END
from app.chains.validation import validation_chain, validation_transform
from app.chains.classification import classification_chain, classification_transform
from app.chains.story import story_chain

class CharacterState(TypedDict, total=False):
    user_input: str
    is_character: bool
    character_description: str
    eneatype_number: str
    eneatype_explanation: str
    character_story: str

def validate_node(state: CharacterState) -> CharacterState:
    result = validation_chain.invoke({"user_input": state["user_input"]})
    result = validation_transform.invoke({**result, "user_input": state["user_input"]})
    return {**state, **result}

def classify_node(state: CharacterState) -> CharacterState:
    result = classification_chain.invoke(
        {"character_description": state["character_description"]}
    )
    result = classification_transform.invoke(result)
    return {**state, **result}

def story_node(state: CharacterState) -> CharacterState:
    result = story_chain.invoke({
        "character_description": state["character_description"],
        "eneatype_number": state["eneatype_number"],
        "eneatype_explanation": state["eneatype_explanation"],
    })
    return {**state, **result}

workflow = StateGraph(CharacterState)

workflow.add_node("validate", validate_node)
workflow.add_node("classify", classify_node)
workflow.add_node("story", story_node)
workflow.set_entry_point("validate")

workflow.add_conditional_edges(
    "validate",
    lambda state: "classify" if state.get("is_character") else "end",
    {"classify": "classify", "end": END},
)

workflow.add_edge("classify", "story")
workflow.add_edge("story", END)

graph = workflow.compile()
