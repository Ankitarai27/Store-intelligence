from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["service"] == "store-intelligence-api"
    assert "database" in body
    assert "healthy" in body["database"]
    assert "message" in body["database"]
    assert "timestamp" in body
    assert body["version"] == "0.1.0"