# myapp/models/user_models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Розширення стандартної моделі User
    is_teacher = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
