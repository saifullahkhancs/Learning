from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.config import settings
from models.user import Base

# Create an asynchronous engine for the database connection.
# The `echo=True` flag will log SQL statements, which is useful for debugging.
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create a configured "Session" class.
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    """Initializes the database and creates tables if they don't exist."""
    async with engine.begin() as conn:
        # This will create all tables defined in models that inherit from Base
        await conn.run_sync(Base.metadata.create_all)