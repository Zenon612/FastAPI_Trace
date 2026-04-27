

def test_health_ok(client):
    response = client.get("/api/v1/health")
    data = response.json()
    assert response.status_code == 200
    assert data["status"] == "ok"
    assert "time" in data

def test_health_with_message(client):
    response = client.get("/api/v1/health/?message=привет%20мир")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "привет мир"