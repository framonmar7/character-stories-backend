import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
MODEL_NAME = os.getenv("MODEL_NAME")

if not OPENAI_API_KEY or not MODEL_NAME:
    raise RuntimeError("Missing required environment variables.")

llm = ChatOpenAI(model=MODEL_NAME)
