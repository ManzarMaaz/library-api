import os
from dotenv import load_dotenv

import sys

# Add the 'app' directory to Python's path so it can find your modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app.database import Base

from app.models import User, Book
from alembic import context

load_dotenv()

config = context.config

config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL"))

target_metadata = Base.metadata