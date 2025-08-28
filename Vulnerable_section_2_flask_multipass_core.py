         If you override this and want to allow more hosts, make sure to use
         a whitelist of trusted hosts to avoid creating an open redirector.
         """
        url_info = urlsplit(url)
         if url_info.scheme and url_info.scheme not in {'http', 'https'}:
             return False
         return not url_info.netloc or url_info.netloc == request.host
 
     def process_login(self, provider=None):