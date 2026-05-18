import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

pytestmark = pytest.mark.anyio

async def test_api_docs_are_online():
    test_transport = ASGITransport(app=app)
    async with AsyncClient(transport=test_transport, base_url="http://test") as ac:
        response = await ac.get("/docs")
    
    assert response.status_code == 200