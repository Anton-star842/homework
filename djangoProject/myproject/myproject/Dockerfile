# Використовуємо офіційний образ Python
FROM python:3.12-slim

# Встановлюємо змінні середовища
ENV PYTHONUNBUFFERED 1

# Створюємо директорію для проєкту
RUN mkdir /app
WORKDIR /app

# Копіюємо файли проєкту до контейнера
COPY . /app/

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Відкриваємо порт 8000 для доступу
EXPOSE 8000

# Команда для запуску сервера
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
