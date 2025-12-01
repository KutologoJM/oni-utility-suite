# settings/local.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
INTERNAL_IPS = [
    "127.0.0.1",
]


INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(2, "debug_toolbar.middleware.DebugToolbarMiddleware")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"