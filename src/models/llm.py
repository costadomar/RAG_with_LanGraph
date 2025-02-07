from langchain_community.llms.ollama import Ollama
from langchain_groq import ChatGroq

from settings import Settings

settings = Settings()

def get_llm_model():
    
    # llm = Ollama(model="mistral")
    llm = ChatGroq(temperature=0.2, model_name="mixtral-8x7b-32768", api_key=settings.groq_api_key)
    
    return llm
