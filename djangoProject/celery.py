from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Встановлюємо змінну середовища для налаштувань Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

app = Celery('myapp')

# Завантажуємо конфігурацію Celery з налаштувань Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматично шукаємо та реєструємо всі задачі
app.autodiscover_tasks()
