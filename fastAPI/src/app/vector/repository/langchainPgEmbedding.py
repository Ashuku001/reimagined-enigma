from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
import os

from app.vector.tables import LangChainPgEmbedding, LangchainPgCollection



load_dotenv()


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


class LangchainPgEmbeddingRepo:
    async def get_docs(self):
        return await LangChainPgEmbedding.select(
                LangChainPgEmbedding.document,
                LangChainPgEmbedding.embedding
            )
        
    async def get_similar(self, embedding):
        return await LangChainPgEmbedding.raw(f"SELECT document, (embedding <=> '{embedding}' ) as cosine_distance \
                                FROM langchain_pg_embedding \
                                ORDER BY cosine_distance \
                                LIMIT 5")
        
    
class LangchainPgCollectionRepo:
    async def get_collection(self):
        return await LangchainPgCollection.select(
                LangchainPgCollection.name,
            )