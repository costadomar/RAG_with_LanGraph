from langchain_community.llms.ollama import Ollama
from langchain_openai import ChatOpenAI

from settings import Settings

settings = Settings()

def get_llm_model():
    
    # llm = Ollama(model="mistral")
    llm = ChatOpenAI(model= 'gpt-4o-mini', api_key=settings.open_ai_api_key)
    
    return llm
