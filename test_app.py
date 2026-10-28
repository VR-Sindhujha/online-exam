
from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["version"] == "v1"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_quiz():
    client = app.test_client()
    response = client.get("/quiz")
    assert response.status_code == 200
    assert len(response.json) == 3
    assert "answer" not in response.json[0]
