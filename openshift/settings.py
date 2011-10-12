# -*- coding: utf-8 -*-
# Django settings for openshift project.
import os
gettext = lambda s: s
ugettext = lambda s: s

# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG
LOGIN_URL="/administration/login_user/"

ADMINS = (
     ('Michel VOULA', 'michel@akoden.com'),
)
MANAGERS = ADMINS

if ON_OPENSHIFT:
    # os.environ['OPENSHIFT_DB_*'] variables can be used with databases created
    # with rhc-ctl-app (see /README in this git repo)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': os.path.join(PROJECT_DIR, 'sqlite3.db'),  # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'fixy_db',  # Or path to database file if using sqlite3.
            'USER': 'sample',                      # Not used with sqlite3.
            'PASSWORD': 'welcome1',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

EMAIL_HOST="gmail-smtp-msa.l.google.com"
EMAIL_HOST_USER="michel@akoden.com"
EMAIL_PORT=587
EMAIL_HOST_PASSWORD="cmvn1987"
EMAIL_USE_TLS=True

LANGUAGES = (
    ('en', ugettext('English')),
    #('fr', ugettext('French')),
   
    
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT =os.path.join(PROJECT_DIR, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, '..', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX= '/media/'

TEMPLATE_DIR=os.path.join(MEDIA_ROOT, 'posts')

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vm4rl5*ymb@2&d_(gc$gb-^twq9w(u69hi--%$5xrh!xk(t%hw'


TEMPLATE_DIRS = (

    os.path.join(PROJECT_DIR, 'templates'),
)




# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
   
    'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware' ,
         'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    
)

if ON_OPENSHIFT:
	ROOT_URLCONF = 'openshift.urls'
else:
	ROOT_URLCONF = 'urls'



STATICFILES_DIRS = (
    # ...
    ("downloads",os.path.join(PROJECT_DIR, 'downloads')),
)


if ON_OPENSHIFT:
	INSTALLED_APPS = (
    		'django.contrib.auth',
		'django.contrib.contenttypes',
	        'django.contrib.sessions',
    		'django.contrib.sites',
    		'django.contrib.messages',
   		# 'django.contrib.staticfiles',
    		#'grappelli',
    		#'filebrowser',
    		# Uncomment the next line to enable the admin:
     		'django.contrib.admin',
     		'openshift.salon',
     		'openshift.fixy_cms',
     		'openshift.medias',
      		'openshift.tekextensions',
         # Uncomment the next line to enable admin documentation:
     		'django.contrib.admindocs',
	)
else:

	PROJECT_APPS=(
    		'salon',
     		'fixy_cms',
     		'medias',
      		'tekextensions',
      		'django_jenkins',
	)

	INSTALLED_APPS = (
    		'django.contrib.auth',
    		'django.contrib.contenttypes',
    		'django.contrib.sessions',
    		'django.contrib.sites',
    		'django.contrib.messages',
   # 'django.contrib.staticfiles',
    #'grappelli',
    #'filebrowser',
    # Uncomment the next line to enable the admin:
     		'django.contrib.admin',
     		'salon',
     		'fixy_cms',
     		'medias',
      		'tekextensions',
      		'django_jenkins',
         # Uncomment the next line to enable admin documentation:
     		'django.contrib.admindocs',
	)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
    'django.core.context_processors.i18n',
     'tekextensions.context_processors.admin_media_prefix',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
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
