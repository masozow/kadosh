"""
Configuración para correr el proyecto localmente / en Docker sin tocar settings.py.

- Si existe la variable DB_HOST usa MySQL (modo Docker).
- Si no existe, usa SQLite (db.sqlite3) y no necesitas instalar MySQL.
"""
import os

from .settings import *  # noqa: F401,F403
from .settings import BASE_DIR, MIDDLEWARE_CLASSES, SECRET_KEY

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

if os.environ.get('DB_HOST'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'kadosh'),
            'USER': os.environ.get('DB_USER', 'kadosh'),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'HOST': os.environ['DB_HOST'],
            'PORT': os.environ.get('DB_PORT', '3306'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

# Logs a la consola (docker logs) en vez de un archivo debug.log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'level': 'WARNING', 'class': 'logging.StreamHandler'}},
    'root': {'handlers': ['console'], 'level': 'WARNING'},
}

# WhiteNoise sirve los archivos estáticos (css/js) aunque DEBUG sea False
MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
) + tuple(m for m in MIDDLEWARE_CLASSES if m != 'django.middleware.security.SecurityMiddleware')

# Esta urlconf agrega la ruta para servir las imágenes subidas (/archivos/)
ROOT_URLCONF = 'sistemakadosh.urls_demo'
