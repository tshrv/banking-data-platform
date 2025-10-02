import subprocess
from typing import AsyncGenerator

import pytest_asyncio
from loguru import logger
from sqlmodel.ext.asyncio.session import AsyncSession

from common.clients.db import engine


@pytest_asyncio.fixture(scope="session", autouse=True, loop_scope="session")
def manage_migrations():
    """Run Alembic migrations before tests and downgrade afterwards"""
    logger.debug("Database migrations upgrade started")
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    logger.debug("Database migrations upgrade complete")
    yield
    logger.debug("Database migrations downgrade started")
    subprocess.run(["alembic", "downgrade", "base"], check=True)
    logger.debug("Database migrations downgrade complete")


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def session() -> AsyncGenerator[AsyncSession, None]:
    """A function scoped database session that initiates rollback after every test function"""
    async with AsyncSession(engine) as session:
        async with session.begin():
            logger.debug("Database session started")
            yield session
            logger.debug("Database session rollback started")
            await session.rollback()  # rollback all operations performed in the session
            logger.debug("Database session rollback complete")
            logger.debug("Database session complete")
