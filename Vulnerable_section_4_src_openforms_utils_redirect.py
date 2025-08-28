 from urllib.parse import urlparse, urlunparse
 
 from corsheaders.conf import conf as cors_conf
 from corsheaders.middleware import CorsMiddleware
 
     are allowed to access Open Forms. We leverage this configuration to block or allow
     redirects to external hosts.
     """
     cors = CorsMiddleware()
     origin = origin_from_url(url)
     parts = urlparse(url)