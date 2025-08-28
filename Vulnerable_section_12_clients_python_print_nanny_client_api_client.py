             self.default_headers[header_name] = header_value
         self.cookie = cookie
         # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/0.6.0-rc5/python'
         self.client_side_validation = configuration.client_side_validation
 
     async def __aenter__(self):