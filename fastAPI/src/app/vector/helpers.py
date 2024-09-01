from tempfile import NamedTemporaryFile
from fastapi import HTTPException
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_postgres import PGVector
from langchain_postgres.vectorstores import PGVector
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

from app.vector.models import CustomPGVector

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
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80)
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
    # vector_store = CustomPGVector.from_documents_with_fk(
    #     embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001'),
    #     documents=chunks,  # Your document chunks
    #     collection_name=COLLECTION_NAME,  # The name of your collection
    #     connection=CONNECTION,  # Database connection object
    #     fk_column="merchantId",  # FK column name in the vector table
    #     fk_reference="Merchants(id)"  # Reference to the external table and column
    # )

    return vector_store

def pg_vectorstore():
    CONNECTION = f"postgresql+psycopg2://{os.getenv('PG_USERNAME')}:{os.getenv('PG_PASSWORD')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}"
    vector_store = PGVector.from_existing_index(
        embedding=GoogleGenerativeAIEmbeddings(model='models/embedding-001'),
        connection=CONNECTION,
        # collection_name="langchain_pg_embedding",
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
    
def question_answer_chain():
    
    # initialize gemini model
    gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", 
                                    temprature=0, 
                                    max_tokens=100)
    # create a prompt template
    prompt_template = ("""
            You are AI powered chatbot designed to provide 
            information and assistance for customers based on the context
            provided to you only. Do not make anything up.
            Only use the context you are provided otherwise say 
            you dont know and request more information from the customer's question. 
            Don't make it obvious that you are a chatbot.
            
            context: {context} 
            Question: {question}
            """)
    
    return gemini_llm, prompt_template
    

def rag_chain():
    qa_chain = question_answer_chain()
    vector_store = pg_vectorstore()
    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': 10})
    rag_chain = create_retrieval_chain(retriever, qa_chain)