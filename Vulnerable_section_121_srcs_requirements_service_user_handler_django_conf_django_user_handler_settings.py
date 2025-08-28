     'django.middleware.security.SecurityMiddleware',
     'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.common.CommonMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     'django.contrib.messages.middleware.MessageMiddleware',
     'django.middleware.clickjacking.XFrameOptionsMiddleware',
 WSGI_APPLICATION = 'django_user_handler.wsgi.application'
 
 CORS_ALLOWED_ORIGINS = [
    'https://transcendence.fr:443',  # Adresse de ton frontend
 ]
 
 ALLOWED_HOSTS = ['transcendence.fr']