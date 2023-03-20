"""
Django base settings file for dev and prod.
"""
from pathlib import Path

import environ

env = environ.Env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

########################################
# APPS
########################################
INSTALLED_APPS = [
    # django apps
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
    "django",
    "users",
    "jupus",
]

########################################
# MIDDLEWARE
########################################
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

########################################
# SECURITY
########################################
SECRET_KEY = env("SECRET_KEY")
DEBUG = False
ALLOWED_HOSTS = []

########################################
# OTHER
########################################
WSGI_APPLICATION = "wsgi.application"
SITE_ID = 1

########################################
# TEMPLATES
########################################
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

########################################
# DATABASE
########################################
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("POSTGRES_DATABASE"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": "5432",
    }
}

########################################
# CACHE
########################################
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f"redis://{env('REDIS_HOST')}:6379/{env('REDIS_DATABASE')}",
    },
}

########################################
# URLS
########################################
ROOT_URLCONF = "urls"
APPEND_SLASH = False

########################################
# PASSWORD VALIDATION
########################################
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

########################################
# INTERNATIONALISATION
########################################
LANGUAGE_CODE = "de-de"
TIME_ZONE = env("TIMEZONE")
USE_I18N = True
USE_TZ = True

########################################
# TIME_FORMATS
########################################
TIME_INPUT_FORMATS = [
    "%I:%M:%S %p",  # 6:22:44 PM
    "%I:%M %p",  # 6:22 PM
    "%I %p",  # 6 PM
    "%H:%M:%S",  # '14:30:59'
    "%H:%M:%S.%f",  # '14:30:59.000200'
    "%H:%M",  # '14:30'
]

########################################
# STATIC SETTINGS
########################################
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

########################################
# AUTHENTICATION
########################################
AUTH_USER_MODEL = "users.User"
