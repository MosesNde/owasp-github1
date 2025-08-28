 print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
 
 CSRF_TRUSTED_ORIGINS = [
    "https://itisocialmediawebsitebackend-production.up.railway.app"
 ]
 CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie only sent over HTTPS
 SESSION_COOKIE_SECURE = True  # Ensures session cookie only sent over HTTPS