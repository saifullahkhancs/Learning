from sqlalchemy.ext.asyncio import AsyncSession
from database import async_session


async def get_db() -> AsyncSession:
    """Dependency to get an async database session."""
    async with async_session() as session:
        yield session
