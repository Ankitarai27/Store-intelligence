"""
PROMPT:
Create a FastAPI health endpoint test using pytest and TestClient.

CHANGES MADE:
Adjusted assertions to match the Store Intelligence API response structure.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["service"] == "store-intelligence-api"
    assert "timestamp" in body
    assert body["version"] == "0.1.0"