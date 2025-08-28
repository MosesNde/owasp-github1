             await self.app(scope, receive, send)
             return
 
        headers = Header.from_scope(scope=scope)
         host = headers.get("host", "").split(":")[0]
         is_valid_host, found_www_redirect = self.validate_host(host)
 