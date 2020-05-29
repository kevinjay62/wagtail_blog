from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["192.168.10.65", "localhost", "127.0.0.1"]

ADMINS = (
    ('Kevin Jay', 'kevin@kjay.net'),
)
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["192.168.10.65", "localhost", "127.0.0.1"]


try:
    from .local import *
except ImportError:
    pass
