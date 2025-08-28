 DATABASES['default']['OPTIONS'] = {
     'sslmode': 'require',
 }
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(",")
 # إعدادات AliExpress API
 ALIEXPRESS_API_URL = "https://api-sandbox.aliexpress.com"
 ALIEXPRESS_APP_KEY = "ضع_المفتاح_هنا"