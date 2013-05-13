import os as _os

APPLICATION_NAME = 'memerchant'

DEBUG = True

BASE_PATH = _os.path.abspath(
    _os.path.join(_os.path.dirname(__file__), '..', '..')
)

TEMPLATES = {
    'DIRS': [_os.path.join(BASE_PATH, 'templates')],
    'TMP_DIR': '/tmp/{}'.format(APPLICATION_NAME),
    'STATIC_DIR': _os.path.join(BASE_PATH, 'static'),
}

SECRET_KEY = (
    '\xd9\x80\xb1\x1c\xda\x02\xb8H\xfbD\xab\xb4\'@\xa1K\\RL\xaed\xb3!\xb0'
)

DUMMY_DATA = True

DEFAULT_USERS = [
]

# custom

DOMAIN_URI = 'http://memerchant.herokuapp.com'

BALANCED_SECRET = 'd04d94eebb6911e2a260026ba7c1aba6'

DB_URI = 'sqlite://'
DB_DEBUG = False

MAIL_DEBUG = True
MAIL_FROM = ('MeMerchant', 'support@example.com')
MAIL_SERVER = 'smtp.mailgun.org'
MAIL_USERNAME = 'user@mailgun.org'
MAIL_PASSWORD = 'password'
MAIL_PORT = 587

GITHUB_URL = 'https://github.com/Malms425/memerchant'
