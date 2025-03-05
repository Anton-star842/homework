FROM python:3.11

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли вимог
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект
COPY . /app

# Встановлюємо змінну середовища для Django
ENV DJANGO_SETTINGS_MODULE=myapp.settings

# Команда для запуску Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myapp.wsgi:application"]
