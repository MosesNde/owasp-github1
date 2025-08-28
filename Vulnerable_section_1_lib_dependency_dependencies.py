     allow_urls = []
 
     if (url
             and not url.startswith("/")
             and not url.startswith(str(request.base_url))
             and url not in allow_urls):