#!/bin/bash
# Перевіряємо, чи існує сокет
if [ ! -S /home/ubuntu/djangoProject/myproject/myproject.sock ]; then
  # Якщо сокет ще не існує, змінюємо права на папку, щоб можна було його створити
  mkdir -p /home/ubuntu/djangoProject/myproject
  touch /home/ubuntu/djangoProject/myproject/myproject.sock
  chmod 777 /home/ubuntu/djangoProject/myproject/myproject.sock
fi

# Запускаємо Gunicorn або сервер Django
exec "$@"
