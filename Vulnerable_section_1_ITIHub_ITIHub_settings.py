 
 CSRF_TRUSTED_ORIGINS = [
     "https://itisocialmediawebsitebackend-production.up.railway.app",
    "https://iti-social-media-websi-git-2fec63-nada-ahmeds-projects-9fb624b0.vercel.app"
 ]
 CSRF_COOKIE_SECURE = True  # Ensures CSRF cookie only sent over HTTPS
 SESSION_COOKIE_SECURE = True  # Ensures session cookie only sent over HTTPS
 
 # OpenAI API configuration
 OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY") 
 
# Ensure CORS settings allow frontend to communicate with backend
 CORS_ALLOWED_ORIGINS = [
     origin.strip() for origin in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if origin.strip()
 ]
print(f"CORS_ALLOWED_ORIGINS: {CORS_ALLOWED_ORIGINS}")
 
CORS_ALLOW_CREDENTIALS = False
 CORS_ALLOW_HEADERS = [
    'content-type',
     'authorization',
     'x-csrftoken',
     'x-requested-with',
    'accept',
    'withcredentials',
    'origin',  # Add origin header which is important for CORS
    'access-control-allow-origin'  # Allow this header to be processed
 ]
# In production, this should be False and specific origins should be set
CORS_ALLOW_ALL_ORIGINS = os.environ.get('CORS_ALLOW_ALL_ORIGINS', 'True').lower() == 'true'
 
 # Add to ensure JWT works properly in production
 REST_FRAMEWORK = {