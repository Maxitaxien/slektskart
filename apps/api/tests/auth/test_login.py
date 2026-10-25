from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_correct_credentials():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "login-success@example.com",
            "password": "123",
            "display_name": "login-success"
        }
    )

    assert response.status_code == 201

    response = client.post(
        "/api/auth/login",
        json={
            "email": "login-success@example.com",
            "password": "123"
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["token_type"] == "bearer"
    assert isinstance(body["access_token"], str)
    assert body["access_token"]

def test_incorrect_credentials():
    response = client.post(
        "/api/auth/register",
        json={
            "email": "login-wrong-password@example.com",
            "password": "123",
            "display_name": "wrong-password"
        }
    )

    assert response.status_code == 201

    response = client.post(
        "/api/auth/login",
        json={
            "email": "nonexistentemail@example.com",
            "password": "123"
        }
    )

    assert response.status_code == 401

    response = client.post(
        "/api/auth/login",
        json={
            "email": "login-wrong-password@example.com",
            "password": "incorrect"
        }
    )

    assert response.status_code == 401
