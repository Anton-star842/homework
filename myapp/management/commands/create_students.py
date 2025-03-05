import requests
from django.core.management.base import BaseCommand
from myapp.models import Student, CustomUser
from myapp.tasks import send_password_reset_email
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode

class Command(BaseCommand):
    help = 'Create students from the Reqres API and send password reset emails'

    def handle(self, *args, **kwargs):
        response = requests.get('https://reqres.in/api/users')
        users = response.json().get('data', [])

        for user_data in users:
            # Перевірка, чи є вже користувач з таким email
            if CustomUser.objects.filter(email=user_data['email']).exists():
                self.stdout.write(self.style.WARNING(f"User with email {user_data['email']} already exists"))
                continue

            # Створення нового користувача, якщо такого немає
            user = CustomUser.objects.create_user(
                username=user_data['email'],
                email=user_data['email'],
                password='temporarypassword',  # Set a temporary password
            )
            student = Student.objects.create(
                user=user,
                full_name=user_data['first_name'] + " " + user_data['last_name'],
                email=user_data['email'],
            )
            self.stdout.write(self.style.SUCCESS(f"Created student: {student.full_name}"))

            # Генерація посилання для скидання пароля
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(user.pk.encode())
            reset_link = f'http://localhost:8000/reset/{uid}/{token}/'

            # Надсилання листа
            send_password_reset_email.delay(user.email, reset_link)
            self.stdout.write(self.style.SUCCESS(f"Sent password reset email to {user.email}"))
