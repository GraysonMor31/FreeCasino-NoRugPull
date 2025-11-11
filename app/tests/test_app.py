from app.server.app import create_app

def test_root_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello" in response.data

def test_health_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/api/health")
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data["status"] == "200, OK"
    assert json_data["message"] == "Server is healthy"