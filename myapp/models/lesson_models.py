# myapp/models/lesson_models.py
from django.db import models
from .course_models import Course
from .user_models import User

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="lessons_taught")

    def __str__(self):
        return self.title
