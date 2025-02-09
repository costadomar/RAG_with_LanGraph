from langchain.tools.retriever import create_retriever_tool

from database.base import get_vectorstore


def retriever_tool():

    vectorstore = get_vectorstore(async_mode=True)
    retriever = vectorstore.as_retriever()
    
    retriever_tool = create_retriever_tool(
            retriever,
            "retriever",
            "buscar e retornar informações sobre os documentos.",
        )
    return retriever_tool
