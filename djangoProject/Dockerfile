# Використовуємо офіційний Python-образ
FROM python:3.10

WORKDIR /app

COPY backend/ /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "backend.wsgi:application"]
