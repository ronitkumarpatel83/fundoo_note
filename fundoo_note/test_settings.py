"""
Django test settings for fundooNotes project.
"""
from .settings import *

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fundoo_note',
        'USER': 'postgres',
        'PASSWORD': 'Ronit@12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

