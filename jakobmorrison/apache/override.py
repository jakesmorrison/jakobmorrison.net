#override.py

from jakobmorrison.settings import *

DEBUG = True
ALLOWED_HOSTS = ['www.jakobmorrison.net', '192.241.228.71']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': "/root/database/db.sqlite3",
    }
}

