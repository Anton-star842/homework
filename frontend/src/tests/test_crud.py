import pytest


@pytest.mark.django_db
def test_create_course(api_client, create_user):
    teacher = create_user("teacher", "password", is_staff=True)

    api_client.force_authenticate(user=teacher)
    response = api_client.post("/api/courses/", {"name": "Biology"})

    assert response.status_code == 201
    assert response.data["name"] == "Biology"


@pytest.mark.django_db
def test_update_course(api_client, create_user, create_course):
    teacher = create_user("teacher", "password", is_staff=True)
    course = create_course("History", teacher)

    api_client.force_authenticate(user=teacher)
    response = api_client.patch(f"/api/courses/{course.id}/", {"name": "World History"})

    assert response.status_code == 200
    assert response.data["name"] == "World History"


@pytest.mark.django_db
def test_delete_course(api_client, create_user, create_course):
    teacher = create_user("teacher", "password", is_staff=True)
    course = create_course("Chemistry", teacher)

    api_client.force_authenticate(user=teacher)
    response = api_client.delete(f"/api/courses/{course.id}/")

    assert response.status_code == 204
