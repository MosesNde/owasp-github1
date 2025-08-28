 import time
 import traceback
 from urllib.parse import urlparse
 LOG_BEFORE_REQUESTS = app.config["LOG_BEFORE_REQUESTS"]
 
 
 @app.before_request
 def preprocess_request():
     session.permanent = True
         p = request.path
         if "//" in p or (p.endswith("/") and p != "/"):
             query_str = request.query_string.decode()
            fixed_url = p.rstrip("/").replace("//", "/")
             if query_str:
                 fixed_url = f"{fixed_url}?{query_str}"
             return redirect(fixed_url)