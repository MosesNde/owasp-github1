 DEBUG = config('DEBUG', default=False, cast=bool)
 
 ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="127.0.0.1,localhost").split(",")
# CSRF_TRUSTED_ORIGINS=['https://carehub.up.railway.app']
 
 # Application definition
 