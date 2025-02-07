from langchain.embeddings import OllamaEmbeddings


def get_embedding_function():
    
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    return embeddings
