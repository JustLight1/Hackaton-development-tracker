"""Database config project"""
import os
from pathlib import Path

from dotenv import load_dotenv

from decouple import config

load_dotenv()

ENVIRONMENT = config('ENVIRONMENT')
BASE_DIR = Path(__file__).resolve().parent.parent


if ENVIRONMENT == 'testing':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif ENVIRONMENT == 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME':  os.getenv('POSTGRES_DB', 'django'),
            'USER':  os.getenv('POSTGRES_USER', 'django'),
            'PASSWORD':  os.getenv('POSTGRES_PASSWORD', 'django_password'),
            'HOST': os.getenv('DB_HOST', '127.0.0.1'),
            'PORT':  os.getenv('DB_PORT', 5432),
        }
    }
