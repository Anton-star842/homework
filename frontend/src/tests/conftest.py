import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from myapp.models import Course, Homework, Grade
from rest_framework.authtoken.models import Token
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoProject.settings'


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    def make_user(username, password, is_staff=False):
        user = User.objects.create_user(username=username, password=password, is_staff=is_staff)
        Token.objects.create(user=user)
        return user
    return make_user


@pytest.fixture
def create_course(db):
    def make_course(name, teacher):
        return Course.objects.create(name=name, teacher=teacher)
    return make_course


@pytest.fixture
def create_homework(db):
    def make_homework(course, student):
        return Homework.objects.create(course=course, student=student, status="pending")
    return make_homework


@pytest.fixture
def create_grade(db):
    def make_grade(homework, teacher, value):
        return Grade.objects.create(homework=homework, teacher=teacher, value=value)
    return make_grade


