import pytest


def test_health_ok(client):
    response = client.get("/api/v1/health")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "ok"



def test_health_with_message(client):
    response = client.get("/api/v1/health/?message=привет%20мир")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "привет мир"


def test_post_health(client):
    response = client.post(
        "/api/v1/health/",
        json={"status": "ok", "message": "All good"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["message"] == "All good"
    assert "id" in data
    assert "timestamp" in data