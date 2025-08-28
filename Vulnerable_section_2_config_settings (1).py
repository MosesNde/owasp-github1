 # SECURITY WARNING: don't run with debug turned on in production!
 DEBUG = False
 
 ALLOWED_HOSTS = ['*']
 
 # Application definition
 
     # installed
     'rest_framework',
     'rest_framework_simplejwt',
     'drf_yasg',
     'django_celery_beat',
 MIDDLEWARE = [
     'django.middleware.security.SecurityMiddleware',
     'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.common.CommonMiddleware',
     'django.middleware.csrf.CsrfViewMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
 }
 
 
 try:
     from .local import *
 except ImportError: