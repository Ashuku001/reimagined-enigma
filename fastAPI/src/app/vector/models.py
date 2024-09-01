from app.vector.tables import Merchant, BotVectorStore
from langchain_community.vectorstores import PGVector
from typing import List, Any
from langchain.schema import Document


class CustomPGVector(PGVector):
    def _create_table_with_fk(self, connection, table_name, fk_column, fk_reference):
        with connection.cursor() as cursor:
            # Create the vector table with a foreign key reference
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                vector VECTOR, -- Assuming this is the vector type used by pgvector
                document JSONB, -- Assuming documents are stored in JSONB format
                {fk_column} INTEGER,  -- Foreign key column
                FOREIGN KEY ({fk_column}) REFERENCES {fk_reference}  -- Add FK constraint
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
    
    @classmethod
    def from_documents_with_fk(
        cls,
        embedding: Any,
        documents: List[Document],
        collection_name: str,
        connection,
        use_jsonb: bool = True,
        create_extension: bool = True,
        fk_column: str = "external_id",  # Name of the FK column
        fk_reference: str = "external_table(id)"  # Reference table and column
    ):
        # Create an instance of CustomPGVector
        vector_store = cls(
            embeddings=embedding,
            collection_name=collection_name,
            connection=connection,
            use_jsonb=use_jsonb
        )
    #     embeddings: Embeddings,
    # *,
    # connection: DBConnection | AsyncEngine | None = None,
    # embedding_length: int | None = None,
    # collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
    # collection_metadata: dict | None = None,
    # distance_strategy: DistanceStrategy = 

        # Optionally create pgvector extension if not exists
        if create_extension:
            with connection.cursor() as cursor:
                cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
                connection.commit()

        # Create the table with FK if needed
        vector_store._create_table_with_fk(
            connection=connection,
            table_name=collection_name,
            fk_column=fk_column,
            fk_reference=fk_reference
        )

        # Add documents to the vector store
        vector_store.add_documents(documents)

        return vector_store
