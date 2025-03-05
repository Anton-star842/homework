import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@pytest.mark.django_db
def test_register_user(api_client):
    response = api_client.post("/api/auth/register/", {"username": "newuser", "password": "password123"})
    assert response.status_code == 201
    assert User.objects.filter(username="newuser").exists()


@pytest.mark.django_db
def test_login_user(api_client, create_user):
    user = create_user("testuser", "password123")
    response = api_client.post("/api/auth/login/", {"username": "testuser", "password": "password123"})
    assert response.status_code == 200
    assert "token" in response.data


@pytest.mark.django_db
def test_access_protected_route(api_client, create_user):
    user = create_user("testuser", "password123")
    token = Token.objects.get(user=user)

    api_client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = api_client.get("/api/protected-route/")

    assert response.status_code == 200
