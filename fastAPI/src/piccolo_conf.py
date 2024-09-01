from piccolo.engine.postgres import PostgresEngine
from dotenv import load_dotenv
from piccolo.conf.apps import AppRegistry
import os

load_dotenv()

DB = PostgresEngine(
    config={
        "database": os.getenv("PG_DB"),
        "user": os.getenv("PG_USERNAME"),
        "password": os.getenv("PG_PASSWORD"),
        "host": os.getenv("PG_HOST"),
        "port": os.getenv("PG_PORT"),
    }
)

APP_REGISTRY = AppRegistry(
    apps=[ 
          "piccolo_admin.piccolo_app", 
          "app.store_insights.piccolo_app", 
          "app.machine_learning.piccolo_app",
          "app.blog.piccolo_app",
          "app.vector.piccolo_app",
        ]
)
