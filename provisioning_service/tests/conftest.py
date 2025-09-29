from typing import AsyncGenerator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from provisioning_service.main import app


@pytest_asyncio.fixture(scope="function", loop_scope="session")
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Async client from httpx"""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        yield client
