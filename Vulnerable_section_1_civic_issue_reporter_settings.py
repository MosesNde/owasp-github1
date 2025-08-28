 SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-development-key-only')  # Always use environment variable in production
 DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
 ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')
 
 # Security headers (enable these in production)
 if not DEBUG: