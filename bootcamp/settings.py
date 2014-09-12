


from unipath import Path
PROJECT_DIR = Path(__file__).parent

from decouple import config

import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config(
      default = config('DATABASE_URL'))
}

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
)

 
 
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'south',
    'django.contrib.admin',
    'bootcamp.activities',
    'bootcamp.articles',
    'bootcamp.auth',
    'bootcamp.core',
    'bootcamp.feeds',
    'bootcamp.messages',
    'bootcamp.questions',
    'bootcamp.search',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)


ROOT_URLCONF = 'bootcamp.urls'

WSGI_APPLICATION = 'bootcamp.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

TIME_ZONE = 'America/Guatemala'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('es', 'Spanish'),
    ('pt-br', 'Portuguese'),
    ('en', 'English')
)

LOCALE_PATHS = (PROJECT_DIR.child('locale'), )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child('static'),
)

MEDIA_ROOT = PROJECT_DIR.parent.child('media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/feeds/'

ALLOWED_SIGNUP_DOMAINS = ['@hotmail.com'] 
# nos permite indicar que dominios permite registrarse en la direccion de correo electronico

FILE_UPLOAD_TEMP_DIR = '/tmp/'
FILE_UPLOAD_PERMISSIONS = 0644
