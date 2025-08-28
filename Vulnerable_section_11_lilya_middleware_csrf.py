             message: An ASGI 'Message'
         """
         # we need to update the message
        headers = Header.from_scope(scope=message)
         if "set-cookie" not in headers:
             cookie = Cookie(
                 key=self.cookie_name,
                 domain=self.cookie_domain,
             )
             headers.add("set-cookie", cookie.to_header(header=""))
            message["headers"] = headers.encoded_multi_items()
         return message
 
     def _generate_csrf_hash(self, token: str) -> str: