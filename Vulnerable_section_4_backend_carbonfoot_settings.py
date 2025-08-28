 
 CORS_ALLOWED_ORIGINS = [
     "http://localhost:3000",
     "http://127.0.0.1:3000",
     "http://134.209.19.90:3000",
 ]
 
 CSRF_TRUSTED_ORIGINS = [
     "http://localhost:3000",
     "http://127.0.0.1:3000",
     "http://134.209.19.90:3000",
 ]
 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
 
 SESSION_EXPIRE_AT_BROWSER_CLOSE = False
 SESSION_COOKIE_AGE = 60 * 60