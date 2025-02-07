from langchain.document_loaders import PyPDFDirectoryLoader, word_document
from langchain.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain_community.document_loaders import Docx2txtLoader
from utils.logging import get_logger
from settings import Settings


logger = get_logger(__name__)
settings = Settings()


def load_documents_pdf():
    document_loader = PyPDFDirectoryLoader(settings.data_path)
    
    return document_loader.load()

def load_documents_docx():
    document_loader = Docx2txtLoader(f"{settings.data_path}/01_0201ARP01e02-20181ºtrimestre.docx")
    
    return document_loader.load()
