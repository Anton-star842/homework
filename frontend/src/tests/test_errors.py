import pytest


@pytest.mark.django_db
def test_access_denied_for_unauthorized_users(api_client):
    response = api_client.get("/api/protected-route/")
    assert response.status_code == 401  # Неавторизований доступ


@pytest.mark.django_db
def test_error_on_wrong_login(api_client):
    response = api_client.post("/api/auth/login/", {"username": "wronguser", "password": "wrongpass"})
    assert response.status_code == 400
    assert "non_field_errors" in response.data
