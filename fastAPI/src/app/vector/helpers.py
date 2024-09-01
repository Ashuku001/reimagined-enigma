from tempfile import NamedTemporaryFile
from fastapi import HTTPException
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
import os

load_dotenv()

async def get_pdf_chunks(file):
    # read pdf into a document
    with NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(await file.read())
        temp_file_path = temp_file.name
        # temp_file.flush()
    try:
        loader = PyPDFLoader(temp_file_path)
        document = loader.load()
    finally:
        os.remove(temp_file_path)
    
    # split document into paragraph
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(document) 
    
    return chunks


def create_embeddings(chunks,COLLECTION_NAME):
    CONNECTION = f"postgresql+psycopg2://{os.getenv('PG_USERNAME')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}"
    vector_store = PGVector.from_documents(
        embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001'),
        documents=chunks,
        collection_name=COLLECTION_NAME,
        connection=CONNECTION,
        use_jsonb=True,
        create_extension=True
    )
    return vector_store

async def pg_vectorstore(COLLECTION_NAME):
    CONNECTION = f"postgresql+psycopg2://{os.getenv('PG_USERNAME')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}"
    vector_store = PGVector(
        embeddings=GoogleGenerativeAIEmbeddings(model='models/embedding-001'),
        collection_name=COLLECTION_NAME,
        connection=CONNECTION,
        use_jsonb=True,
        create_extension=True
    )
    
    return vector_store

def get_embedding(query):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
    try:
        print (query)
        return embeddings.embed_query(query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"message": "An internal error occured"})