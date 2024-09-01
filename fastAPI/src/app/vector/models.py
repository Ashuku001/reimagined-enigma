from app.vector.tables import Merchant, BotVectorStore
from piccolo_api.crud.serializers import create_pydantic_model

BotVectorStoreReq = create_pydantic_model(BotVectorStore)