import os
from django.conf import global_settings

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
USE_SAML2 = False

# Django settings for cowcloud project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cowcloud.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '61_t+5-ve5_#@izw7+g$qp93*1@5v@ubt-xrfk%e1&amp;hl%2k)=+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	#'downtime.middleware.DowntimeMiddleware',
	'readonly.middleware.DatabaseReadOnlyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'anafero.middleware.SessionJumpingMiddleware',
    'pybb.middleware.PybbMiddleware',
)

ROOT_URLCONF = 'cowcloud.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'cowcloud.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates')
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    'files.context_processors.auth_urls',
    'files.context_processors.storage',
    'pybb.context_processors.processor',
    'readonly.context_processors.readonly',
    'plans.context_processors.account_status',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    # Uncomment the next line to enable the admin:
    #'django_admin_bootstrapped',
    'suit',
    #'bootstrap_admin',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    #'files',
    'fileupload',
    'registration',
    #'moneybookers',
    'plans',
    'anafero',
    'contact_form',
    'pybb',
    #'pytils',
    #'sorl.thumbnail',
    #'pure_pagination',
    'south',
    #'webmaster_verification',
    #'static_sitemaps',
    #'downtime',
    #'readonly',
    'debug_toolbar',
 )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

if USE_SAML2:
    INSTALLED_APPS.append('djangosaml2')
    LOGIN_URL = '/saml2/login/'
    AUTHENTICATION_BACKENDS = (
        'djangosaml2.backends.Saml2Backend',
        'django.contrib.auth.backends.ModelBackend',
    )

SAML_CONFIG = {
    'xmlsec_binary': '/usr/local/bin/xmlsec1',
    "sp":
        {
        "name": "Gijs SP",
        "url": "http://localhost:8087/",
        "idp": {
            "urn:mace:localhost:saml:gijs:idp": {
                "single_signon_service": "http://localhost:8000/idp/"
                },
            },
        },

    "entityid": "urn:mace:localhost:saml:gijs:sp",
    "service": {
        "sp": {
            "name": "Gijs SP",
            "url": "http://localhost:8002/simplesaml",
            "idp": {
                "urn:mace:localhost:saml:gijs:idp": {
                    "single_signon_service": "http://localhost:8000/sp/"},
            },
            "endpoints": "",
        }
    },
    "key_file": os.path.join('/keys/private-key.pem'),
    "cert_file": os.path.join('/keys/certificate.pem'),
    "attribute_map_dir": "./attributemaps",
    "organization": {
        "display_name": ["Panjianom identities"]
    },
    "contact_person": [
        {
        "givenname": "Panjianom",
        "surname": "Panji",
        "phone": "+62 83877053343",
        "mail": "panjul76@homail.com",
        "type": "technical",
        }
    ]
}

SAML_USERNAME_ATTRIBUTE = 'uid'

# where to store large upload
FILE_UPLOAD_TEMP_DIR = '/tmp'

# length of file secret. Don't change this after database creation
FILE_SECRET_LENGTH = 50

# Where to store the large files
STORAGE_ROOT = os.path.join('storage')

# How are the files accessed from outside
STORAGE_URL = '/storage/'

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLE_STACKTRACES': True,
}

ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST = 'localhost'
EMAIL_PORT = '1025'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'admin@cowcloud.com'
LOGIN_REDIRECT_URL = '/accounts/'
LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout/'

#MONEYBOOKERS_MERCHANT_ID = "123456"
#MONEYBOOKERS_SECRET_WORD = "YourSecretWord"
#MONEYBOOKERS_PAY_TO_EMAIL = "panjul76@hotmail.com"
#MONEYBOOKERS_STATUS_URL = "https://www.cowcloud.com/moneybookers/status_url/"
#MONEYBOOKERS_CURRENCY_CODE = "EUR"

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'panjul76@gmail.com'
EMAIL_HOST_PASSWORD = 'tratap60'
EMAIL_USE_TLS = True

AUTH_PROFILE_MODULE = 'pybb.Profile'
PYBB_SMILES = {
	'&gt;_&lt;': 'angry.png',
	':.(': 'cry.png',
	'o_O': 'eyes.png',
	'[]_[]': 'geek.png',
	'8)': 'glasses.png',
	':D': 'lol.png',
	':(': 'sad.png',
	':O': 'shok.png',
	'-_-': 'shy.png',
	':)': 'smile.png',
	':P': 'tongue.png',
	';)': 'wink.png'
}

PAYPAL_RECEIVER_EMAIL = "panjul76@hotmail.com"

WEBMASTER_VERIFICATION = {
#    'bing': '<bing verification code>',
    'google': 'google722faf1b2e594e5e',
#    'majestic': '<majestic verification code>',
#    'yandex': '<yandex verification code>',
#    'alexa': '<alexa verification code>',
}

CURRENCY = 'USD'

#STATICSITEMAPS_ROOT_SITEMAP = 'cowcloud.sitemaps.sitemaps'

#DOWNTIME_EXEMPT_PATHS = (
#    '/admin',
#)

# Set to False to allow writes
SITE_READ_ONLY = False

# Enable
#DB_READ_ONLY_MIDDLEWARE_MESSAGE = True

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

