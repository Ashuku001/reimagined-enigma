from piccolo.columns.column_types import Column
from piccolo.engine import engine_finder
from typing import List

class Vector(Column):
    value_type = list

    def __init__(self, dimensions: int, **kwargs):
        self.dimensions = dimensions
        super().__init__(**kwargs)

    @property
    def column_type(self) -> str:
        return f"vector({self.dimensions})"

    async def create(self):
        # Override to support pgvector creation syntax
        engine = engine_finder()
        if engine.dialect == "postgres":
            await engine.run_ddl("CREATE EXTENSION IF NOT EXISTS vector;")
        await super().create()

    def to_python_value(self, value) -> List[float]:
        # Convert database value to Python list
        return [float(i) for i in value[1:-1].split(",")]

    def to_db_value(self, value: List[float]) -> str:
        # Convert Python list to database format
        return f"({','.join(map(str, value))})"
