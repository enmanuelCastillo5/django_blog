from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblogcastillo.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd74gauu4qds9in',
        'USER': 'vvdiubraqnkqyq',
        'PASSWORD': '522a29ff1ee405f73134d913a2b5f2306f9bb986bfe350ff93b3422cad7a591a',
        'HOST': 'ec2-52-20-248-222.compute-1.amazonaws.com',
        'PORT': 5432
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')