from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain_core.runnables import RunnablePassthrough

from models.llm import get_llm_model
from database.base import get_vectorstore


def create_rag_chain():
    vectorstore = get_vectorstore(async_mode=True)
    retriever = vectorstore.as_retriever()
    llm = get_llm_model()

    message = """
    Você é um assistente virtual. A partir de agora responda apenas em português do Brasil.

    Contexto:
    {context}

    Pergunta: {question}

    Responda à pergunta acima utilizando apenas o contexto fornecido. Se não conseguir identificar a resposta, responda "Não sei."
    """

    prompt = ChatPromptTemplate.from_messages([("human", message)])
    rag_chain = {
        "context": retriever,
        "question": RunnablePassthrough(),
    } | prompt | llm | StrOutputParser()

    return rag_chain
