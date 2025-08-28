         data = self.encode_session(scope["session"])
         data = self.signer.sign(data)
         # we need to update the message
        headers = Header.from_scope(scope=message)
         header_value = "{session_cookie}={data}; path={path}; {max_age}{security_flags}".format(
             session_cookie=self.session_cookie,
             data=data.decode("utf-8"),
             security_flags=self.security_flags,
         )
         headers.add("Set-Cookie", header_value)
        message["headers"] = headers.encoded_multi_items()
         return message
 
     async def clear_session_cookie(self, scope: Scope, message: Message) -> Message:
             scope (Scope): ASGI scope.
         """
         # we need to update the message
        headers = Header.from_scope(scope=message)
         header_value = "{session_cookie}={data}; path={path}; {expires}{security_flags}".format(
             session_cookie=self.session_cookie,
             data="null",
             security_flags=self.security_flags,
         )
         headers.add("Set-Cookie", header_value)
        message["headers"] = headers.encoded_multi_items()
         return message