from django.core.management.base import BaseCommand
import requests
from myapp.models import CustomUser
from myapp.tasks import send_password_reset_link  # Імпортуємо Celery таску

class Command(BaseCommand):
    help = 'Fetch users from external API and create them'

    def handle(self, *args, **kwargs):
        response = requests.get("https://reqres.in/api/users")
        users = response.json()["data"]
        for user_data in users:
            user = CustomUser.objects.create(
                username=user_data["first_name"],
                email=user_data["email"],
                password="defaultpassword123"  # Ви можете додати логіку для генерації паролів
            )
            # Викликаємо Celery таску для відправлення e-mail
            send_password_reset_link.delay(user.id)
        self.stdout.write(self.style.SUCCESS("Users created and reset links sent"))
