FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Системні залежності
RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Python-пакети
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо проєкт
COPY . .

# Робимо скрипт виконуваним (він у /app/)
RUN chmod +x /app/wait-for-db.sh

EXPOSE 8000

# Робоча директорія — mysite
WORKDIR /app/mysite

# ВИДАЛЕНО: 'python manage.py migrate' з CMD. 
# Запускаємо лише runserver, міграції виконаємо через docker-compose.yml
CMD ["sh", "-c", "/app/wait-for-db.sh python manage.py runserver 0.0.0.0:8000"]
