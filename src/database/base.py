import asyncio
import os
import sys

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine

from langchain_postgres.vectorstores import PGVector
from langchain.vectorstores.pgvector import DistanceStrategy

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from models.embeddings import get_embedding_function
from settings import Settings

settings = Settings()

COLLECTION_NAME = "materias"


if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def get_vectorstore(settings = settings, async_mode: bool = False) -> PGVector:
    """
    Cria e retorna uma instância do PGVector configurada para ser síncrona ou assíncrona.

    :param settings: Instância de configurações contendo informações do banco de dados.
    :param async_mode: Define se o vectorstore será configurado para modo assíncrono.
    :return: Instância configurada do PGVector.
    """
    embeddings = get_embedding_function()

    if async_mode:
        engine = create_async_engine(str(settings.db_url))
    else:
        engine = create_engine(str(settings.db_url))

    vectorstore = PGVector(
        embeddings=embeddings,
        collection_name=COLLECTION_NAME, 
        connection=engine,
        use_jsonb=True,
        distance_strategy=DistanceStrategy.COSINE,
        async_mode=async_mode,
        
    )
    
    return vectorstore
