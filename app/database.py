import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import ssl  # Add this import

Base = declarative_base()

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Pass the connect_args with the ssl context to the engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, 
    echo=True,
    connect_args={"ssl": ssl_context} # Force SSL here, not in the URL
)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with async_session() as session:
        yield session