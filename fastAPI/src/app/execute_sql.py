from piccolo.engine import engine_finder

# Get the database engine
engine = engine_finder()

# Execute raw SQL
async def execute_sql(query):
    result = await engine.run_query(query)
    return result