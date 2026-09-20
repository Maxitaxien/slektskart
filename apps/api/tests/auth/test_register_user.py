from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_register_returns_safe_user():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "max@example.com",
            "password": "123",
            "display_name": "Max"
        }
    )

    assert response.status_code == 201

    body = response.json()
    assert body["email"] == "max@example.com"
    assert body["display_name"] == "Max"
    assert "id" in body
    assert "password" not in body
    assert "password_hash" not in body

def test_register_same_email_twice_fails():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "123",
            "display_name": "Test1",
        }
    )

    assert response.status_code == 201

    response = client.post(
        "/api/auth/register",
        json={
            "email": "test@example.com",
            "password": "123",
            "display_name": "Test2",
        }
    )

    assert response.status_code == 409
