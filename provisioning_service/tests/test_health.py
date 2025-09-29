import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio(loop_scope="session")
async def test_health_check(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == status.HTTP_200_OK, "Health check failed"
    if response.status_code == status.HTTP_200_OK:
        data = response.json()
        assert data["status"] == "ok", "Invalid health check response"
