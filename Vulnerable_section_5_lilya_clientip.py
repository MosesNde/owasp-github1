         client_ip = "unix"
 
     if client_ip in get_trusted_proxies(trusted_proxies):
        headers = Header.from_scope(scope)
         try:
             ip_matches = _forwarded_regex.search(headers["forwarded"])
             client_ip = ip_matches[1]