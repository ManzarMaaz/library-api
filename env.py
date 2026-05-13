import os
from dotenv import load_dotenv
from app.database import Base
from app.models import User, Book
from alembic import context

load_dotenv()

config = context.config

config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))

target_metadata = Base.metadata