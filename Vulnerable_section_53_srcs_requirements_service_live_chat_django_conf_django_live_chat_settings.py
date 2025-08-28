     'whitenoise.middleware.WhiteNoiseMiddleware',
     'django.contrib.sessions.middleware.SessionMiddleware',
     'django.middleware.common.CommonMiddleware',
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     'django.contrib.messages.middleware.MessageMiddleware',
     'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'https://transcendence.fr:443',
 ]
 
 # Autoriser les en-têtes spécifiques (nécessaire pour les tokens JWT et WebSocket)
 CORS_ALLOW_HEADERS = [
     'accept',