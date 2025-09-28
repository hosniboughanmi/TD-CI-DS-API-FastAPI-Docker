import pytest
from httpx import AsyncClient
from app.main import app  # adapte le chemin si besoin

@pytest.mark.anyio
async def test_predict_success():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/predict", json={"features": [3.5, 1.2, 4.9]})
        assert resp.status_code == 200
        assert "predictions" in resp.json()

