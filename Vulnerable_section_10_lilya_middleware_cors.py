             return
 
         method = scope["method"]
        headers = Header.from_scope(scope=scope)
         origin = headers.get("origin")
 
         if origin is None:
             await send(message)
             return
 
        message.setdefault("headers", [])
         # we need to update the message
        headers = Header.from_scope(scope=message)
         headers.update(self.simple_headers)
         origin = request_headers["Origin"]
         has_cookie = "cookie" in request_headers
         elif not self.allow_all_origins and self.validate_origin(origin=origin):
             self.set_explicit_origin(headers, origin)
 
        message["headers"] = headers.encoded_multi_items()
         await send(message)
 
     @staticmethod