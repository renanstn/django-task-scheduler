from pathlib import Path

import dj_database_url
from decouple import config
from django.core.management.utils import get_random_secret_key
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key())

DEBUG = config("DEBUG", cast=bool, default=False)

DOCKERENV = config("DOCKERENV", cast=bool, default=False)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", default="127.0.0.1,localhost"
).split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'task_scheduler.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'task_scheduler.wsgi.application'


# Database

DATABASE_URL = config(
    "DATABASE_URL",
    default="postgres://postgres:postgres@database:5432/postgres"
)

if DOCKERENV:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL),
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'


# Django admin user

ADMIN_USERNAME = config("ADMIN_USERNAME", default=None)
ADMIN_PASSWORD = config("ADMIN_PASSWORD", default=None)
