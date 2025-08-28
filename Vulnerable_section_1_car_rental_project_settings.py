     'https://*.repl.co',
     'https://07e67146-564e-4c35-aefd-537ca316147c-00-qud2bpdkzhko.pike.replit.dev:8000',
     'https://07e67146-564e-4c35-aefd-537ca316147c-00-qud2bpdkzhko.pike.replit.dev',
 ]
 
 # Additional CSRF Settings
CSRF_COOKIE_SECURE = False  # Set to True in production
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_USE_SESSIONS = True

CSRF_COOKIE_SECURE = False  # Set to True in production
CSRF_COOKIE_HTTPONLY = False
CSRF_COOKIE_SAMESITE = 'Lax'  # Changed from None to 'Lax'
CSRF_USE_SESSIONS = True  # Changed to True to use sessions
 CSRF_COOKIE_NAME = 'csrftoken'
 CSRF_HEADER_NAME = 'HTTP_X_CSRFTOKEN'
 CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
 
 
 # Session cookie settings
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'  # Changed from None to 'Lax' for better security and compatibility
 
 ROOT_URLCONF = 'car_rental_project.urls'
 
 LANGUAGE_COOKIE_AGE = 60 * 60 * 24 * 365    # مدة صلاحية الكوكي (سنة واحدة بالثواني)
 LANGUAGE_COOKIE_DOMAIN = None               # نطاق الكوكي (لا تعيين قيمة يعني النطاق الحالي فقط)
 LANGUAGE_COOKIE_PATH = '/'                  # مسار الكوكي (متاح لجميع الصفحات)
LANGUAGE_COOKIE_SECURE = False              # لا تطلب HTTPS (مهم للتطوير المحلي)
 LANGUAGE_COOKIE_HTTPONLY = False            # السماح لـ JavaScript بالوصول
LANGUAGE_COOKIE_SAMESITE = 'Lax'            # تم التغيير من None إلى 'Lax' للتوافق مع إعدادات الكوكيز الأخرى
 
 # Use SessionMiddleware for storing language preference in the session as well
 SESSION_COOKIE_AGE = 60 * 60 * 24 * 30      # مدة جلسة المستخدم (30 يوم)