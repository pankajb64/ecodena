# Django settings for Ecodena project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Pankaj Bhambhani', 'pankajb64@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '200901047',                      # Or path to database file if using sqlite3.
        'USER': '200901047',                      # Not used with sqlite3.
        'PASSWORD': 'admin',                  # Not used with sqlite3.
        'HOST': '10.100.71.21',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Calcutta'

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

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/home/ecodena/src/Ecodena/Main/static',
    'static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'k!*n&!9$t9sp61=vq(%t^(k@yz7o^=*y=i2kmxtpi!4+88gyhl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.middleware.csrf.CsrfResponseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'Ecodena.urls'

'''EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ecodenacommit@gmail.com'
EMAIL_HOST_PASSWORD = 'senteam3'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
'''
#EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ecodenacommit@gmail.com'
EMAIL_HOST_PASSWORD = 'senteam3'
EMAIL_PORT = 687

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'Main/Template/registration',
	'Main/Template',	
	'Question/Template',
	'Query/Template',
	'Attempt/Template',
)

#TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.csrf')
TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.static",
	"django.core.context_processors.request",
	'django.core.context_processors.csrf')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.markup',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Ecodena.User',
    'Ecodena.Question',
    'Ecodena.Attempt',
    'Ecodena.Comment',
#    'Ecodena.Query',
    'Ecodena.Compiler',	
    #'Ecodena.Contest',
    'Ecodena.ProblemSetter',
    'Ecodena.Recommendation',	 	
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.admindocs',
#     'Compiler.Judge',
    'kombu.transport.django',  
    'djcelery',
    'forum' ,
    'registration',
    'simplewiki',
    'pagination',
#    'notification', 
)  

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
  
BROKER_URL = "django://" # tell kombu to use the Django database as the message queue  
  
import djcelery  
djcelery.setup_loader()      


AUTH_PROFILE_MODULE = 'Ecodena.User.Profile'

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"

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
