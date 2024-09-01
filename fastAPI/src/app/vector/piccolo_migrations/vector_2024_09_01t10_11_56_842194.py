from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from app.vector.column import Vector
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import Bytea
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Text
from piccolo.columns.column_types import Timestamp
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.timestamp import TimestampCustom
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class LangchainPgCollection(
    Table, tablename="langchain_pg_collection", schema=None
):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class Merchant(Table, tablename="Merchants", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


ID = "2024-09-01T10:11:56:842194"
VERSION = "1.7.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="vector", description=DESCRIPTION
    )

    manager.add_table(
        class_name="Merchant", tablename="Merchants", schema=None, columns=None
    )

    manager.add_table(
        class_name="LangChainPgEmbedding",
        tablename="langchain_pg_embedding",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="BotVectorStore",
        tablename="BotVectorStores",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="LangchainPgCollection",
        tablename="langchain_pg_collection",
        schema=None,
        columns=None,
    )

    manager.add_column(
        table_class_name="Merchant",
        tablename="Merchants",
        column_name="business_name",
        db_column_name="business_name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
            
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Merchant",
        tablename="Merchants",
        column_name="username",
        db_column_name="username",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": True,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Merchant",
        tablename="Merchants",
        column_name="password",
        db_column_name="password",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Merchant",
        tablename="Merchants",
        column_name="email",
        db_column_name="email",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="Merchant",
        tablename="Merchants",
        column_name="whatsapp_phone_number",
        db_column_name="whatsapp_phone_number",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="LangChainPgEmbedding",
        tablename="langchain_pg_embedding",
        column_name="collection_id",
        db_column_name="collection_id",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": LangchainPgCollection,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="LangChainPgEmbedding",
        tablename="langchain_pg_embedding",
        column_name="embedding",
        db_column_name="embedding",
        column_class_name="Vector",
        column_class=Vector,
        params={
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
            'dimensions': 1536
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="LangChainPgEmbedding",
        tablename="langchain_pg_embedding",
        column_name="document",
        db_column_name="document",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="LangChainPgEmbedding",
        tablename="langchain_pg_embedding",
        column_name="cmetadata",
        db_column_name="cmetadata",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="BotVectorStore",
        tablename="BotVectorStores",
        column_name="merchantId",
        db_column_name="merchantId",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": Merchant,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="BotVectorStore",
        tablename="BotVectorStores",
        column_name="original",
        db_column_name="original",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="BotVectorStore",
        tablename="BotVectorStores",
        column_name="vector",
        db_column_name="vector",
        column_class_name="Bytea",
        column_class=Bytea,
        params={
            "default": b"",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="BotVectorStore",
        tablename="BotVectorStores",
        column_name="createdAt",
        db_column_name="createdAt",
        column_class_name="Timestamp",
        column_class=Timestamp,
        params={
            "default": TimestampCustom(
                year=2024, month=9, day=9, hour=10, second=56, microsecond=835053
            ),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="BotVectorStore",
        tablename="BotVectorStores",
        column_name="updatedAt",
        db_column_name="updatedAt",
        column_class_name="Timestamp",
        column_class=Timestamp,
        params={
            "default": TimestampCustom(
                year=2024, month=9, day=9, hour=10, second=56, microsecond=835053
            ),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="LangchainPgCollection",
        tablename="langchain_pg_collection",
        column_name="name",
        db_column_name="name",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="LangchainPgCollection",
        tablename="langchain_pg_collection",
        column_name="cmetadata",
        db_column_name="cmetadata",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 255,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    return manager
