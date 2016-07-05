"""
Django settings for djangoapp project.

Generated by 'django-admin startproject' using Django 1.10b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import importlib
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from trello import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

try:
    settings_local = importlib.import_module('djangotrellostats.settings_local')
except ImportError:
    print("Please, create a local_settings.py in project directory with SECRET_KEY, DEBUG, DOMAIN, ALLOWED_HOSTS and DATABASES settings")
    exit(-1)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings_local.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = settings_local.DEBUG

DOMAIN = settings_local.DOMAIN
ALLOWED_HOSTS = settings_local.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'djangotrellostats.apps.members',
    'djangotrellostats.apps.public',
    'djangotrellostats.apps.boards',
]

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'djangotrellostats.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/djangotrellostats/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangotrellostats.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = settings_local.DATABASES


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.member.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.member.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.member.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.member.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Europe/Madrid"
Configuration.TIMEZONE = "Europe/Madrid"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
