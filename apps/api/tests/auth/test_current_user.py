from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_current_user():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "current@example.com",
            "password": "123",
            "display_name": "current"
        }
    )

    assert response.status_code == 201

    response = client.post(
        "/api/auth/login",
        json={
            "email": "current@example.com",
            "password": "123"
        }
    )

    assert response.status_code == 200

    body = response.json()
    token = body["access_token"]

    response = client.get(
        "/api/auth/me",
        headers = {
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["email"] == "current@example.com"
    assert body["display_name"] == "current"
    assert body["is_active"] is True
    assert body["email_verified"] is False
    assert "password" not in body
    assert "password_hash" not in body

    # once again with invalid token:
    response = client.get(
        "/api/auth/me",
        headers = {
            "Authorization": f"Bearer INVALID"
        }
    )

    assert response.status_code == 401