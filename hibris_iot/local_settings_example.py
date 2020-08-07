import os
import sys

PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True
TESTING = sys.argv[1:2] == ['test']

SITE_URL = "http://localhost:8000"
FRONT_URL = "http://localhost:3000"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

ALLOWED_HOSTS = ['localhost', '*']
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = (
#     'localhost:4200',
#     'localhost:8000'
# )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iot',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(PROJECT_PATH, 'database.sqlite'),
    # }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

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

PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgH3mThhm29POg2LCv2r9ZPumx1D47Voxvej4QRKEiqjyRJUWDlBf
qbSaYhwb7RUAghmiM8mWgNFnbR3S+YX8m5KdOKnc2Bwy5HzP/B/A9GFfjke21vn1
sA/d0XD41KKQhGsDU6ZOTX49mALexJ5Y/etpOgIEaDKqef85qs/LITe1AgMBAAEC
gYAmhs6JKxjEJSMRmtTm0aoQVEYUIkjH3Abofuey2fpwnsqb8Mbqk4ukJ8Y0IduY
HLKzU26TlsnOyt6aTNBszxNwCVU3CtJMUNLwSMWocYW9T3NHBfa1zrF1PoMY+rV2
MM06shUe+t+dOWXUvxTOtMGSuCVraQwruwZcgGl/G1kk1QJBALqcBN3k6Hp6L/mg
jdjTHMgrpBkxV6ZHDJYVuLyFP5JApC9/FWM0CHjjCZwoqX9nUh4hMdOVd7TRDqgW
Gl4fYEcCQQCstx03GTONiOIqL31xPEFLq1D/kecEu2/BtdQq6y78VPbyd+rseHE/
3Khr1S8nHmK9YRgAA/roxCXTo6ZW9YIjAkApsQXdVXEjO/1P9jD6yl/Z0PY+sql0
etczCPNXGyYS1OJZwjjTCyMBbygMfYEw97J/DMeHEBPIkBSINTf642OtAkADARxs
/O88owjsGu9frOCl5FEAYRVXq7sB75vFM1oZ4ZB6H0Pi4SV3KutzFL5BO/ITwUCd
n3QZ4G+YAty93n9pAkEAuLHIee+YXaSM7lhiXrECc3cMkQ6Q/ntHuW7uyxh4TSbv
sOY71TsJ+nLQNE3DhK6HuzTrXvxGL8G+aDyWfsR7lQ==
-----END RSA PRIVATE KEY-----'''.encode("utf-8")

PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgH3mThhm29POg2LCv2r9ZPumx1D4
7Voxvej4QRKEiqjyRJUWDlBfqbSaYhwb7RUAghmiM8mWgNFnbR3S+YX8m5KdOKnc
2Bwy5HzP/B/A9GFfjke21vn1sA/d0XD41KKQhGsDU6ZOTX49mALexJ5Y/etpOgIE
aDKqef85qs/LITe1AgMBAAE=
-----END PUBLIC KEY-----'''.encode("utf-8")

ALLOWED_PUBLIC_KEYS = [
    PUBLIC_KEY
]

CELERY_TASK_ALWAYS_EAGER = True  # For production always False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
