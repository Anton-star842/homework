import json
import requests
from django.core.management.base import BaseCommand
from myapp.models import CustomUser


class Command(BaseCommand):
    help = 'Імпортує користувачів з API reqres.in'

    def handle(self, *args, **kwargs):
        # Завантажуємо дані користувачів з API
        url = 'https://reqres.in/api/users?page=1'
        response = requests.get(url)

        if response.status_code == 200:
            users_data = response.json()['data']
            # Імпортуємо кожного користувача
            for user_data in users_data:
                # Перевіряємо, чи є вже користувач з таким email
                if not CustomUser.objects.filter(username=user_data['email']).exists():
                    user = CustomUser.objects.create_user(
                        username=user_data['email'],
                        email=user_data['email'],
                        password='temporarypassword',  # Тимчасовий пароль
                    )
                    self.stdout.write(self.style.SUCCESS(f"Користувач {user.username} був успішно доданий."))
                else:
                    self.stdout.write(self.style.WARNING(f"Користувач з email {user_data['email']} вже існує."))
        else:
            self.stdout.write(self.style.ERROR('Не вдалося отримати дані з API.'))
