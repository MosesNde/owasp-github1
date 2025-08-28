 class RunTest(CSRFExemptMixin, View):
     """ Proxy-view between clients and servers """
     error_codes = [(400, 599)]  # boundaries considered as errors
    exclude_request_header = ['Authorization']
 
     def get_exposed_url(self):
         exposed_url = '{}/{}'.format(self.kwargs['exposed_url'], self.kwargs['name'])
             request_headers['Content-Crs'] = request_headers.pop('HTTP_CONTENT_CRS')
         if 'CONTENT_TYPE' in request_headers:
             request_headers['Content-Type'] = request_headers.pop('CONTENT_TYPE')
        if not settings.DEBUG:
            for rh in self.exclude_request_header:
                if rh in request_headers:
                    del request_headers[rh]
 
         return request_headers
 