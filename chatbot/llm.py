
import os
from dotenv import load_dotenv


load_dotenv()

from langchain_mistralai import ChatMistralAI

api_key = os.getenv("MISTRAL_API_KEY")
model_name = os.getenv("MISTRAL_MODEL", 'codestral-2508')




if not api_key:
    raise ValueError("MISTRAL_API_KEY is missing from environment variables")

llm = ChatMistralAI(
    model=model_name,
    api_key=api_key,
    temperature=0.7,
    max_retries=2,
    timeout=30
)


