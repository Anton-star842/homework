from __future__ import absolute_import, unicode_literals

# Це дозволяє Django завантажити ваш об'єкт celery при старті проекту.
from myapp.celery import app as celery_app

__all__ = ('celery_app',)
