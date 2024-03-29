"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import environ
env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'
# DEBUG = True
ENV = os.environ.get('URL')
if DEBUG:
    ALLOWED_HOSTS = [ENV, 'localhost', '127.0.0.1',]
else:
    ALLOWED_HOSTS = []
    ALLOWED_HOSTS.append(ENV)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "apps.home",
    "apps.paciente",
    'apps.obra_sociales',

]

if DEBUG:
    INSTALLED_APPS += ["django_browser_reload"]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if DEBUG:
    MIDDLEWARE.append(
        "django_browser_reload.middleware.BrowserReloadMiddleware")

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


if  DEBUG:
# if not DEBUG:
    # if DEBUG:
    # DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': os.getenv('DB_NAME'),
        #     'USER': os.getenv('DB_USER'),
        #     'PASSWORD': os.getenv('DB_PASSWORD'),
        #     'HOST': os.getenv('DB_HOST'),
        #     'PORT': os.getenv('DB_PORT'),
        # }
        DATABASES = {
            'default': {
                'ENGINE': 'djongo',
                'NAME': 'consultorio',
                'ENFORCE_SCHEMA': False,
                'CLIENT': {
                    'host': 'mongodb+srv://carlos8788:0hM7ULTC83zJ01AN@consultorio.2qliuug.mongodb.net/consultorioBIOMED?retryWrites=true&w=majority',  # Reemplaza esto con tu URI de MongoDB Atlas.
                }
            }
        }
else:

    # DATABASES = {
    #         'default': {
    #             'ENGINE': 'django.db.backends.sqlite3',
    #             'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #         }
    #     }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'consultorio',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Salta'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ORIGIN = os.environ.get('ORIGIN')
CSRF_TRUSTED_ORIGINS = [ORIGIN]

SESSION_COOKIE_AGE = 1800  # duración de la sesión en segundos
# la sesión se cierra cuando el usuario cierra el navegador
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Para cuando alguien quiera entrar y no está logueado utilizamos
LOGIN_URL = 'login'
if DEBUG:
    print('http://localhost:8000')
X_FRAME_OPTIONS = 'SAMEORIGIN'
