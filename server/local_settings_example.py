import os
import sys
from .settings import BASE_DIR

DEBUG = True
TESTING = sys.argv[1:2] == ['test']

SITE_URL = "http://localhost:8007"

ALLOWED_HOSTS = ['localhost', '*']
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SWAGGER_SETTINGS = {
    'LOGIN_URL': '{}/admin/login'.format(SITE_URL),
    'LOGOUT_URL': '{}/admin/logout'.format(SITE_URL),
    'SECURITY_DEFINITIONS': {
        "api_key": {
            "type": "apiKey",
            "name": "authorization",
            "in": "header"
        },
        "basic": {
            "type": "basic"
        }
    },
}
