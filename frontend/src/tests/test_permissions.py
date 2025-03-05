import pytest


@pytest.mark.django_db
def test_student_sees_only_their_courses(api_client, create_user, create_course):
    student = create_user("student", "password")
    teacher = create_user("teacher", "password", is_staff=True)
    course_1 = create_course("Math", teacher)
    course_2 = create_course("Physics", teacher)

    api_client.force_authenticate(user=student)
    response = api_client.get("/api/courses/")

    assert response.status_code == 200
    assert len(response.data) == 0  # Студент ще не записаний на курси


@pytest.mark.django_db
def test_teacher_sees_their_courses(api_client, create_user, create_course):
    teacher = create_user("teacher", "password", is_staff=True)
    course = create_course("Math", teacher)

    api_client.force_authenticate(user=teacher)
    response = api_client.get("/api/courses/")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Math"
