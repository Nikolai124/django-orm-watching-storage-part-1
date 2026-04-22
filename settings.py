from dotenv import load_dotenv
import os

load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.geenv('DJANGO_HOST_DB'),
        'PORT': os.getenv('DJANGO_PORT_DB'),
        'NAME': os.getenv('DJANGO_NAME_DB'),
        'USER': os.getenv('DJANGO_USER_DB'),
        'PASSWORD': os.getenv('DJANGO_PASSWORD_DB'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
