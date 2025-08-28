 
 class TrailingSlashHandler(web.RequestHandler):
     """Simple redirect handler that strips trailing slashes
    
     This should be the first, highest priority handler.
     """
    
     def get(self):
        self.redirect(self.request.uri.rstrip('/'))
    
     post = put = get
 
 
         url = sep.join([self._url, self.request.query])
         self.redirect(url, permanent=self._permanent)
 
 class PrometheusMetricsHandler(IPythonHandler):
     """
     Return prometheus metrics for this notebook server