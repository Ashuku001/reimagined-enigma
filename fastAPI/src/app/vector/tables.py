from piccolo.table import Table
from piccolo.columns import ForeignKey, JSON, JSONB, Boolean, Decimal, Integer, Varchar, Text,  Boolean, Float, Date, Bytea, Timestamp
from datetime import datetime
from pgvector.peewee import VectorField
from app.vector.column import Vector

class Merchant(Table, tablename="Merchants"): 
    business_name= Varchar()
    username= Varchar(unique=True)
    password= Varchar()
    email= Varchar()
    whatsapp_phone_number= Varchar()
    
class BotVectorStore(Table, tablename="BotVectorStores"):
    merchantId=ForeignKey(Merchant)
    original=Text()
    vector=Bytea()
    createdAt = Timestamp(default=datetime.now(), null=False)
    updatedAt = Timestamp(default=datetime.now(), null=False)
    
class LangchainPgCollection(Table, tablename="langchain_pg_collection"):
    name = Varchar()
    cmetadata = Varchar()
    
class LangChainPgEmbedding(Table, tablename="langchain_pg_embedding"):
    collection_id = ForeignKey(LangchainPgCollection)
    embedding =  Vector(dimensions=1536)
    document = Text()
    cmetadata = Varchar()