import pytest


@pytest.mark.django_db
def test_filter_courses_by_teacher(api_client, create_user, create_course):
    teacher_1 = create_user("teacher1", "password", is_staff=True)
    teacher_2 = create_user("teacher2", "password", is_staff=True)
    create_course("Math", teacher_1)
    create_course("Physics", teacher_2)

    api_client.force_authenticate(user=teacher_1)
    response = api_client.get("/api/courses/?teacher=teacher1")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Math"
