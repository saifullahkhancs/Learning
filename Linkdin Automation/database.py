import logging

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.config import settings
from models.user import Base

logger = logging.getLogger(__name__)

if not settings.DATABASE_URL:
    raise ValueError("DATABASE_URL is not configured. Set it in .env or as an environment variable.")

# Create an asynchronous engine for the database connection.
# The `echo=True` flag will log SQL statements, which is useful for debugging.
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create a configured "Session" class.
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    """Initializes the database and creates tables if they don't exist."""
    try:
        async with engine.begin() as conn:
            # This will create all tables defined in models that inherit from Base
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize database: {e}")
        raise