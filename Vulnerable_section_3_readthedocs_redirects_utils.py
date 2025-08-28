     if not project:
         return None
 
     language = None
     version_slug = None
     schema, netloc, path, params, query, fragments = urlparse(full_path)
 
     # Re-use the domain and protocol used in the current request.
     # Redirects shouldn't change the domain, version or language.
     new_path = request.build_absolute_uri(new_path)
 
     if http_status and http_status == 301: