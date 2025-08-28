 
 
 class ContrailHttp(object):
    def __init__(self, auth_info, logger):
         self._logger = logger
        # default don't verify client cert
        self._ssl_verify = False
         # auth info: must contain auth_url and auth_dict
         self.auth_url = auth_info["auth_url"]
         self.auth_dict = auth_info["auth_dict"]
         return requests.get(url, headers=headers, params=query_params)
 
     def _http_post_headers(self, url, headers, json_data=None):
        return requests.head(url, json=json_data, headers=headers, verify=False)
 
     def _http_post(self, url, headers, json_data=None):
        return requests.post(url, json=json_data, headers=headers, verify=False)
 
     def _http_delete(self, url, headers, json_data=None):
         return requests.delete(url, json=json_data, headers=headers)