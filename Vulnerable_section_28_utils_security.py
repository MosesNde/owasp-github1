 from flask_limiter.util import get_remote_address
 from werkzeug.security import generate_password_hash, check_password_hash
 from functools import wraps
from flask import request, abort
 import os
 
 def init_security(app):
     # Initialize CSRF protection
     csrf = CSRFProtect(app)
     
    # Initialize rate limiter
     limiter = Limiter(
         app,
         key_func=get_remote_address,
        default_limits=["200 per day", "50 per hour"],
        storage_uri="memory://"
     )
     
    # Add rate limit decorators
     def limit_requests(f):
         @wraps(f)
        @limiter.limit("5 per minute")
         def decorated_function(*args, **kwargs):
             return f(*args, **kwargs)
         return decorated_function