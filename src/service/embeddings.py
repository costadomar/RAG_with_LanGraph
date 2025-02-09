import os
import sys
from typing import List

from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.base import get_vectorstore
from data.process_documents import load_documents_pdf, load_documents_docx
from utils.logging import get_logger
from settings import Settings

logger = get_logger(__name__)
settings = Settings()


class EmbeddingsService:
    def __init__(self, chunk_size: int = 800, chunk_overlap: int = 80):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def run(self):
        documents = self._load_documents()
        chunks = self._split_documents(documents)
        self._add_to_pgvector(chunks)

    def _load_documents(self) -> List[Document]:
        """Processa os Documentos e retorna uma lista de documentos."""
        return load_documents_pdf()

    def _split_documents(self, documents: List[Document]) -> List[Document]:
        """Divide documentos em chunks."""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )
        return text_splitter.split_documents(documents)

    def _calculate_chunk_ids(self, chunks: List[Document]) -> List[Document]:
        """Calcula IDs únicos para chunks."""
        last_page_id = None
        current_chunk_index = 0

        for chunk in chunks:
            source = chunk.metadata.get("source")
            page = chunk.metadata.get("page")
            current_page_id = f"{source}:{page}"

            if current_page_id == last_page_id:
                current_chunk_index += 1
            else:
                current_chunk_index = 0

            chunk_id = f"{current_page_id}:{current_chunk_index}"
            last_page_id = current_page_id
            chunk.metadata["id"] = chunk_id

        return chunks


    def _add_to_pgvector(self, chunks: List[Document]):
        """Adiciona documentos e embeddings ao banco de dados PostgreSQL."""
        chunks_with_ids = self._calculate_chunk_ids(chunks)
        db = get_vectorstore(async_mode=False)

        new_chunks = []
        for chunk in chunks_with_ids:
                new_chunks.append(chunk)

        if len(new_chunks):
            logger.info(f"Adding new documents: {len(new_chunks)}")
            new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
            db.add_documents(new_chunks, ids=new_chunk_ids)
        else:
            logger.info("✅ No new documents to add")

        logger.info("Finished adding new documents.")


if __name__ == "__main__":
    service = EmbeddingsService()
    service.run()
