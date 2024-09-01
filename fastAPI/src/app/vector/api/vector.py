
from fastapi.routing import APIRouter
from fastapi import File, UploadFile, HTTPException
from dotenv import load_dotenv
from app.vector.repository.langchainPgEmbedding import LangchainPgEmbeddingRepo, LangchainPgCollectionRepo
from app.vector.helpers import get_embedding, create_embeddings, get_pdf_chunks


router = APIRouter()
load_dotenv()

@router.post("/pdf")
async def add_vector( merchantId: int, file: UploadFile = File(...)):
    chunks = await get_pdf_chunks(file)
    
    try:
        create_embeddings(chunks, file.filename)
        return {"success": True}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"message": "failed to create embeddings for your pdf file"})
    
@router.get("/embedding")
async def get_docs():
    repo = LangchainPgEmbeddingRepo()
    try:
        response = await repo.get_docs()
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"message": "Failed to retrieve embedded documents."})
    
@router.get("/collection")
async def get_docs():
    repo = LangchainPgCollectionRepo()
    try:
        response = await repo.get_collection()
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"message": "Failed to retrieve embedded documents."})
    
@router.post("/completion")
async def completion(query: str):
    embeddings = get_embedding(query)
    try:
        return embeddings
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail={"message": "Failed to retrieve embedded documents."})