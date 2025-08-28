from langchain.chains import LLMChain
from app.core.config import llm
from app.prompts.story_prompt import story_prompt

story_chain = LLMChain(
    llm=llm,
    prompt=story_prompt,
    output_key="character_story"
)
