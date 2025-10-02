from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from typing_extensions import AsyncGenerator

from common.config import settings

engine = create_async_engine(settings.POSTGRES_URL, echo=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Create an async session object for configured SQL database"""
    async with AsyncSession(engine) as session:
        async with session.begin():  # transaction auto-commit on close
            logger.debug("session started")
            yield session
            logger.debug("session closed")
