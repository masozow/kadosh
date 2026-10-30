FROM python:3.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=sistemakadosh.settings_demo

WORKDIR /app

# Librerías del sistema para compilar el driver de MySQL
RUN sed -i 's|deb.debian.org/debian-security|archive.debian.org/debian-security|g' /etc/apt/sources.list \
    && grep -q 'archive.debian.org/debian-security' /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends gcc pkg-config default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt mysqlclient==1.4.6

COPY . .
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["gunicorn", "sistemakadosh.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
