             self.domain = config.get("domain")
             self.asn = config.get("asn")
             self.fabric = config.get("fabric")
 
         # Init http headers for all requests
         self.http_header = {"Content-Type": "application/json"}
 
         # Init http lib
         auth_info = {"auth_url": self.auth_url, "auth_dict": auth_dict}
        self.http = ContrailHttp(auth_info, self.logger)
 
     def check_auth(self):
         response = self.http.get_cmd(url=self.auth_url, headers=self.http_header)