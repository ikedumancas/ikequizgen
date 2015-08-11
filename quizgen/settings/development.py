import os
from .common import *
DEBUG = True

ALLOWED_HOSTS = []


FULL_DOMAIN_NAME = 'http://localhost:8000'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# if os.environ.get('HEROKU_ENV') is not None:
#     STATIC_ROOT = 'staticfiles'

STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")
HTML_MINIFY = False