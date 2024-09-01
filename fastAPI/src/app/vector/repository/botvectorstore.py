from typing import  List, Dict, Any
from app.vector.tables  import  Merchant, BotVectorStore
from fastapi import HTTPException
from datetime import datetime

class BotVectorStoreRepository:    
    async def get_all_vectors(self, merchantId: int) -> List[BotVectorStore]:
        return await BotVectorStore.select(BotVectorStore.original,
                                           BotVectorStore.vector).output(nested=True).where(
                                               BotVectorStore.merchantId == merchantId)
    
    async def add_vector(self, details: Dict[str, Any]):
        try:
            botVectorStore = BotVectorStore(**details)
            await BotVectorStore.insert(botVectorStore)
        except Exception as e:
            print(e)
            return False
        return True