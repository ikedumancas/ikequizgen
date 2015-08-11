from common import *

DEBUG = False

# Allow all host headers
ALLOWED_HOSTS = ['*']

FULL_DOMAIN_NAME = 'https://ikedumancas-doit.herokuapp.com'


# Parse database configuration from $DATABASE_URL
import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
DATABASES = {
	'default': dj_database_url.config()
}
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# if os.environ.get('HEROKU_ENV') is not None:
#     STATIC_ROOT = 'staticfiles'

STATIC_ROOT = 'staticfiles'
HTML_MINIFY = True