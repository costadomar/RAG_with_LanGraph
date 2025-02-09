from langchain.embeddings import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings

from settings import Settings

settings = Settings()

def get_embedding_function():
    
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=settings.open_ai_api_key)
    
    return embeddings
