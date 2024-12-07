# Використовуємо базовий образ Ubuntu
FROM ubuntu:latest

# Оновлюємо систему і встановлюємо Python
RUN apt-get update && apt-get install -y python3 python3-pip && apt-get clean

# Оновлюємо pip
RUN python3 -m pip install --no-cache-dir --upgrade pip

# Встановлюємо робочу директорію
WORKDIR /src

# Копіюємо файли
COPY . /src

# Встановлюємо залежності з requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Відкриваємо порт для Flask
EXPOSE 5000

# Запускаємо Flask сервер
CMD ["python3", "dz4_flask.py"]

