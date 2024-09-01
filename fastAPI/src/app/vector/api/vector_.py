from datetime import datetime
import json
from fastapi.routing import APIRouter
from fastapi import File
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # to create embeddings
import tempfile
from dotenv import load_dotenv
from app.vector.repository.botvectorstore import BotVectorStoreRepository
from app.execute_sql import execute_sql


router = APIRouter()
load_dotenv()

@router.post("/pdf")
async def add_vector( merchantId: int, file: bytes = File(...)):
    # read pdf into a document
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(file)
        temp_file.flush()
        loader = PyPDFLoader(temp_file.name)
        document = loader.load()
    
    # split document into paragraph
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(document)
    
    # GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
    # covert paragraps into embeddings
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    for chunk in chunks:
        vectors = embeddings.embed_query(chunk.page_content)
        json_data = json.dumps(vectors)
        blob_data = json_data.encode('utf-8')
        
        # store the vectors into a database
        repo = BotVectorStoreRepository()
        response = await repo.add_vector(details={"original": chunk.page_content, "vector": blob_data, "merchantId": merchantId, "createdAt":datetime.now(), "updatedAt":datetime.now()})

    return {"success": response}

@router.get("/vectors")
async def get_vector( merchantId: int, query: str):
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    vectors = embeddings.embed_query(query)
    sql = ""
    result = await execute_sql(vectors)
    return result
